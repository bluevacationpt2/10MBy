import sys
import os
import subprocess
import threading
import time
import tkinter as tk
from tkinter import ttk, filedialog
from pathlib import Path

TARGET_SIZE_BYTES = int(9.99 * 1024 * 1024)
AUDIO_EXTENSIONS = {'.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma'}
VIDEO_EXTENSIONS = {'.mp4', '.mkv', '.avi', '.mov', '.webm', '.wmv', '.flv', '.m4v'}

BG_COLOR = "#1e1e1e"
FG_COLOR = "#e0e0e0"
BTN_BG = "#333333"
BTN_FG = "#e0e0e0"

DND_FILES = None

def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True,
                      creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0)
        return True
    except:
        return False

class App:
    def __init__(self):
        self.auto_close = len(sys.argv) > 1 and os.path.isfile(sys.argv[-1])
        
        try:
            from tkinterdnd2 import TkinterDnD, DND_FILES
            global DND_FILES
            self.root = TkinterDnD.Tk()
            self.has_dnd = True
        except:
            self.root = tk.Tk()
            self.has_dnd = False
        
        self.root.title("10MBy")
        self.root.geometry("380x200")
        self.root.resizable(False, False)
        self.root.configure(bg=BG_COLOR)
        
        self._set_icon()
        
        if self.auto_close:
            self.root.wm_attributes("-topmost", True)
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background=BG_COLOR)
        style.configure("TLabel", background=BG_COLOR, foreground=FG_COLOR)
        
        main_frame = ttk.Frame(self.root, padding="25")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.status_label = tk.Label(main_frame, text="10MBy", 
                                    font=("Inter", 16, "bold"), bg=BG_COLOR, fg=FG_COLOR)
        self.status_label.pack(pady=(0, 5))
        
        self.instruction_label = tk.Label(main_frame, 
                                       text="Drag file here or click to browse",
                                       font=("Inter", 9), bg=BG_COLOR, fg="#888888")
        self.instruction_label.pack(pady=(0, 10))
        
        self.open_btn = tk.Button(main_frame, text="Open File", font=("Inter", 10),
                                 bg=BTN_BG, fg=BTN_FG, relief="flat", padx=25, pady=8,
                                 command=self._open_file, cursor="hand2")
        self.open_btn.pack()
        
        formats_text = "MP4, MKV, AVI, MOV, WEBM, MP3, WAV, FLAC"
        self.formats_label = tk.Label(main_frame, text=f"Formats: {formats_text}",
                                     font=("Inter", 7), bg=BG_COLOR, fg="#555555")
        self.formats_label.pack(side=tk.BOTTOM, pady=(10, 0))
        
        if self.has_dnd:
            try:
                from tkinterdnd2 import DND_FILES
                self.root.drop_target_register(DND_FILES)
                self.root.dnd_bind('<<Drop>>', self._on_drop)
            except:
                pass
        
        self.progress_frame = None
        self.progress = None
        self.detail_label = None
        self.compressor = None
        self.scrolling = False
        self.scroll_job = None
        
        if not check_ffmpeg():
            self.status_label.config(text="FFmpeg not found!", fg="#ff5555")
            return
        
        input_file = get_input_file()
        if input_file:
            self.start_compression(input_file)
    
    def _on_drop(self, event):
        files = self.root.tk.splitlist(event.data)
        for f in files:
            if os.path.isfile(f):
                self.start_compression(f)
                break
    
    def _set_icon(self):
        try:
            paths = [
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "10mby.png"),
                os.path.join(os.path.dirname(sys.executable), "10mby.png"),
            ]
            for p in paths:
                if os.path.exists(p):
                    from PIL import Image, ImageTk
                    img = Image.open(p).resize((64, 64), Image.Resampling.LANCZOS)
                    self.root.iconphoto(False, ImageTk.PhotoImage(img))
                    break
        except:
            pass
    
    def _open_file(self):
        path = filedialog.askopenfilename(
            title="Select video or audio file",
            filetypes=[
                ("Video files", "*.mp4 *.mkv *.avi *.mov *.webm *.wmv *.flv *.m4v"),
                ("Audio files", "*.mp3 *.wav *.flac *.aac *.ogg *.m4a *.wma"),
                ("All files", "*.*")
            ]
        )
        if path:
            self.start_compression(path)
    
    def _show_progress(self):
        if self.progress_frame:
            return
        
        self.instruction_label.pack_forget()
        self.formats_label.pack_forget()
        self.open_btn.pack_forget()
        self.status_label.pack_forget()
        
        self.progress_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.progress_frame.pack(fill=tk.BOTH, expand=True)
        
        container = tk.Frame(self.progress_frame, bg=BG_COLOR)
        container.pack(expand=True)
        
        self.filename_label = tk.Label(container, text="",
                                     font=("Inter", 11), bg=BG_COLOR, fg=FG_COLOR)
        self.filename_label.pack(pady=(15, 8))
        
        self.progress = ttk.Progressbar(container, mode="indeterminate", length=340)
        self.progress.start(15)
        self.progress.pack(pady=(0, 8))
        
        self.detail_label = tk.Label(container, text="Starting...", 
                                    font=("Inter", 8), bg=BG_COLOR, fg="#666666")
        self.detail_label.pack(pady=(0, 15))
    
    def start_compression(self, input_path):
        self._show_progress()
        
        filename = os.path.basename(input_path)
        self.filename_label.config(text=filename)
        
        self.compressor = Compressor(input_path, self.on_progress, self.on_done)
        self.compressor.start()
    
    def on_progress(self, detail):
        if self.detail_label:
            self.detail_label.config(text=detail)
        self.root.update()
    
    def on_done(self, success, message):
        if self.progress:
            self.progress.stop()
        
        if success:
            self.filename_label.config(text=f"Done! {os.path.basename(message)}", fg="#4CAF50")
            copy_to_clipboard(message)
            if self.auto_close:
                self.root.after(500, self.root.destroy)
        else:
            self.filename_label.config(text=f"Error: {message}", fg="#ff5555")

def copy_to_clipboard(path):
    try:
        subprocess.run(['powershell', '-Command', f'Set-Clipboard -Path "{path}"'], 
                     capture_output=True, creationflags=0x08000000)
    except:
        pass

class Compressor:
    def __init__(self, input_path, progress_callback, done_callback):
        self.input_path = input_path
        self.is_audio = Path(input_path).suffix.lower() in AUDIO_EXTENSIONS
        self.output_path = self._get_output_path()
        self.progress_callback = progress_callback
        self.done_callback = done_callback
        self.running = True
    
    def _get_output_path(self):
        p = Path(self.input_path)
        stem = p.stem
        if self.is_audio:
            return str(p.parent / f"{stem}_10mb.mp3")
        return str(p.parent / f"{stem}_10mb{p.suffix}")
    
    def start(self):
        thread = threading.Thread(target=self.run)
        thread.start()
    
    def run(self):
        try:
            original_size = os.path.getsize(self.input_path)
            
            if original_size <= TARGET_SIZE_BYTES:
                self.done_callback(False, f"File is already under 10MB ({original_size//1024}KB)")
                return
            
            self.progress_callback("Starting compression...")
            
            if self._try_compress():
                return
            
            if not os.path.exists(self.output_path):
                self.done_callback(False, "Compression failed")
                return
            
            final_size = os.path.getsize(self.output_path)
            if final_size <= TARGET_SIZE_BYTES:
                self.done_callback(True, self.output_path)
            else:
                self.done_callback(False, f"Could not compress below 10MB ({final_size//1024}KB)")
                
        except Exception as e:
            self.done_callback(False, str(e))
    
    def _try_compress(self):
        if self.is_audio:
            tests = [
                ["ffmpeg", "-y", "-i", self.input_path, "-b:a", "320k", "-codec:a", "libmp3lame", self.output_path],
                ["ffmpeg", "-y", "-i", self.input_path, "-b:a", "256k", "-codec:a", "libmp3lame", self.output_path],
                ["ffmpeg", "-y", "-i", self.input_path, "-b:a", "192k", "-codec:a", "libmp3lame", self.output_path],
                ["ffmpeg", "-y", "-i", self.input_path, "-b:a", "160k", "-codec:a", "libmp3lame", self.output_path],
                ["ffmpeg", "-y", "-i", self.input_path, "-b:a", "128k", "-codec:a", "libmp3lame", self.output_path],
                ["ffmpeg", "-y", "-i", self.input_path, "-b:a", "96k", "-codec:a", "libmp3lame", self.output_path],
            ]
        else:
            tests = [
                ["ffmpeg", "-y", "-i", self.input_path, "-c:v", "libx264", 
                 "-preset", "fast", "-crf", "23", "-c:a", "copy", self.output_path],
                ["ffmpeg", "-y", "-i", self.input_path, "-vf", "scale=1280:-2", "-c:v", "libx264", 
                 "-preset", "fast", "-crf", "23", "-c:a", "copy", self.output_path],
                ["ffmpeg", "-y", "-i", self.input_path, "-vf", "scale=854:-2", "-c:v", "libx264", 
                 "-preset", "fast", "-crf", "24", "-c:a", "copy", self.output_path],
                ["ffmpeg", "-y", "-i", self.input_path, "-vf", "scale=640:-2", "-c:v", "libx264", 
                 "-preset", "fast", "-crf", "26", "-c:a", "copy", self.output_path],
                ["ffmpeg", "-y", "-i", self.input_path, "-vf", "scale=640:-2", "-c:v", "libx264", 
                 "-preset", "fast", "-crf", "28", "-c:a", "copy", self.output_path],
                ["ffmpeg", "-y", "-i", self.input_path, "-vf", "scale=480:-2", "-c:v", "libx264", 
                 "-preset", "fast", "-crf", "30", "-c:a", "aac", "-b:a", "96k", self.output_path],
                ["ffmpeg", "-y", "-i", self.input_path, "-vf", "scale=480:-2", "-c:v", "libx264", 
                 "-preset", "ultrafast", "-crf", "32", "-c:a", "aac", "-b:a", "64k", self.output_path],
                ["ffmpeg", "-y", "-i", self.input_path, "-vf", "scale=320:-2", "-c:v", "libx264", 
                 "-preset", "ultrafast", "-crf", "35", "-c:a", "aac", "-b:a", "48k", self.output_path],
            ]
        
        best_path = None
        best_size = float('inf')
        
        for i, cmd in enumerate(tests):
            if not self.running:
                return False
            
            self.progress_callback(f"Compressing ({i+1}/{len(tests)})...")
            
            if os.path.exists(self.output_path):
                try:
                    os.remove(self.output_path)
                except:
                    pass
            
            try:
                result = subprocess.run(cmd, capture_output=True, timeout=300,
                              creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0)
            except:
                continue
            
            if os.path.exists(self.output_path):
                size = os.path.getsize(self.output_path)
                if size <= TARGET_SIZE_BYTES:
                    self.done_callback(True, self.output_path)
                    return True
                if size < best_size:
                    best_size = size
                    best_path = self.output_path
        
        if best_path and best_size < 15 * 1024 * 1024:
            self.done_callback(True, best_path)
            return True
        
        return False

def get_input_file():
    all_exts = VIDEO_EXTENSIONS | AUDIO_EXTENSIONS
    for arg in sys.argv[1:]:
        if os.path.isfile(arg) and Path(arg).suffix.lower() in all_exts:
            return arg
    if len(sys.argv) > 1:
        potential = sys.argv[-1]
        if os.path.isfile(potential):
            return potential
    return None

def install():
    import winreg
    exe_path = os.path.abspath(sys.executable)
    exe_dir = os.path.dirname(exe_path)
    try:
        path_var = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment"), "Path")[0]
        if exe_dir not in path_var:
            winreg.SetValueEx(winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_WRITE), "Path", 0, path_var + ";" + exe_dir)
    except:
        pass
    
    ALL_EXT = [".mp4", ".mkv", ".avi", ".mov", ".webm", ".wmv", ".flv", ".m4v", ".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"]
    for ext in ALL_EXT:
        key_path = f"Software\\Classes\\SystemFileAssociations\\{ext}\\shell\\10MBy"
        try:
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "Compress to 10 MB")
            winreg.SetValueEx(key, "Icon", 0, winreg.REG_SZ, exe_path)
            winreg.CloseKey(key)
            cmd_key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path + "\\command")
            winreg.SetValueEx(cmd_key, "", 0, winreg.REG_SZ, f'"{exe_path}" "%1"')
            winreg.CloseKey(cmd_key)
        except:
            pass
    print("Installed!")

def uninstall():
    import winreg
    exe_dir = os.path.dirname(os.path.abspath(sys.executable))
    
    try:
        path_var = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment"), "Path")[0]
        paths = [p.strip() for p in path_var.split(";") if p.strip()]
        if exe_dir in paths:
            paths.remove(exe_dir)
            winreg.SetValueEx(winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_WRITE), "Path", 0, ";".join(paths))
    except:
        pass
    
    ALL_EXT = [".mp4", ".mkv", ".avi", ".mov", ".webm", ".wmv", ".flv", ".m4v", ".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"]
    for ext in ALL_EXT:
        try:
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, f"Software\\Classes\\SystemFileAssociations\\{ext}\\shell\\10MBy")
        except:
            pass
    print("Uninstalled!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--install":
            install()
        elif sys.argv[1] == "--uninstall":
            uninstall()
        else:
            app = App()
            app.root.mainloop()
    else:
        app = App()
        app.root.mainloop()
