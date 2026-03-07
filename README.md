# 10MBy

Easily compress videos and audio to fit under just 10MB from the context menu in Windows.

> ⚠️ This project is currently in alpha. Please report any issues.

## Install
Download the latest setup file from [releases](https://github.com/bluevacation/10MBy/releases).
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
- The compressed file will be automatically copied to your clipboard. The compressed file will be in the same directory as the original file.

## Supported Formats

Video: MP4, MKV, AVI, MOV, WEBM, WMV, FLV, M4V  
Audio: MP3, WAV, FLAC, AAC, OGG, M4A, WMA

## Requirements

- Windows 10/11
- [FFmpeg](https://ffmpeg.org/) in PATH (app warns if not found)

