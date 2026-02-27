# 10MBy

Easily compress videos and audio to fit under just 10MB from the context menu in Windows.

## Download

Get the installer from [Releases](https://github.com/bluevacation/10MBy/releases)

## Install
1. Install ffmpeg if you don't have it already:
```bash
winget install --id=Gyan.FFmpeg -e
winget install --id=Gyan.FFmpeg.Essentials -e
```
2. Run `10MBy_Setup.exe`

Alternatively, you can build it from source:
```bash
pip install pyinstaller pillow tkinterdnd2
pyinstaller --onefile --windowed --icon=10mby.ico 10mbizer.py
```
Executable will be in: `dist/10MBy.exe`

## Usage

- **Quick compress**: Right-click any video/audio file → "Compress to 10 MB"

## Supported Formats

Video: MP4, MKV, AVI, MOV, WEBM, WMV, FLV, M4V  
Audio: MP3, WAV, FLAC, AAC, OGG, M4A, WMA

## Requirements

- Windows 10/11
- [FFmpeg](https://ffmpeg.org/) in PATH (app warns if not found)

