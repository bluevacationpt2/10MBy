#define MyAppName "10MBy"
#define MyAppVersion "1.0"
#define MyAppPublisher "10MBy"
#define MyAppURL "https://github.com/bluevacation/10MBy"
#define MyAppExeName "10MBy.exe"

[Setup]
AppId={{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
OutputDir=output
OutputBaseFilename=10MBy_Setup
SetupIconFile=10mby.ico
UninstallDisplayIcon={app}\{#MyAppExeName}
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "dist\10MBy.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\10mby.png"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Registry]
; Add right-click context menu for all supported file types
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.mp4\shell\{#MyAppName}"; ValueType: string; ValueName: ""; ValueData: "Compress to 10 MB"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.mp4\shell\{#MyAppName}"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\{#MyAppExeName},0"
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.mp4\shell\{#MyAppName}\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.mkv\shell\{#MyAppName}"; ValueType: string; ValueName: ""; ValueData: "Compress to 10 MB"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.mkv\shell\{#MyAppName}"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\{#MyAppExeName},0"
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.mkv\shell\{#MyAppName}\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.avi\shell\{#MyAppName}"; ValueType: string; ValueName: ""; ValueData: "Compress to 10 MB"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.avi\shell\{#MyAppName}"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\{#MyAppExeName},0"
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.avi\shell\{#MyAppName}\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.mov\shell\{#MyAppName}"; ValueType: string; ValueName: ""; ValueData: "Compress to 10 MB"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.mov\shell\{#MyAppName}"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\{#MyAppExeName},0"
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.mov\shell\{#MyAppName}\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.webm\shell\{#MyAppName}"; ValueType: string; ValueName: ""; ValueData: "Compress to 10 MB"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.webm\shell\{#MyAppName}"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\{#MyAppExeName},0"
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.webm\shell\{#MyAppName}\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.wmv\shell\{#MyAppName}"; ValueType: string; ValueName: ""; ValueData: "Compress to 10 MB"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.wmv\shell\{#MyAppName}"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\{#MyAppExeName},0"
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.wmv\shell\{#MyAppName}\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.flv\shell\{#MyAppName}"; ValueType: string; ValueName: ""; ValueData: "Compress to 10 MB"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.flv\shell\{#MyAppName}"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\{#MyAppExeName},0"
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.flv\shell\{#MyAppName}\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.m4v\shell\{#MyAppName}"; ValueType: string; ValueName: ""; ValueData: "Compress to 10 MB"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.m4v\shell\{#MyAppName}"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\{#MyAppExeName},0"
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.m4v\shell\{#MyAppName}\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.mp3\shell\{#MyAppName}"; ValueType: string; ValueName: ""; ValueData: "Compress to 10 MB"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.mp3\shell\{#MyAppName}"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\{#MyAppExeName},0"
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.mp3\shell\{#MyAppName}\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.wav\shell\{#MyAppName}"; ValueType: string; ValueName: ""; ValueData: "Compress to 10 MB"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.wav\shell\{#MyAppName}"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\{#MyAppExeName},0"
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.wav\shell\{#MyAppName}\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.flac\shell\{#MyAppName}"; ValueType: string; ValueName: ""; ValueData: "Compress to 10 MB"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.flac\shell\{#MyAppName}"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\{#MyAppExeName},0"
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.flac\shell\{#MyAppName}\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.aac\shell\{#MyAppName}"; ValueType: string; ValueName: ""; ValueData: "Compress to 10 MB"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.aac\shell\{#MyAppName}"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\{#MyAppExeName},0"
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.aac\shell\{#MyAppName}\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.ogg\shell\{#MyAppName}"; ValueType: string; ValueName: ""; ValueData: "Compress to 10 MB"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.ogg\shell\{#MyAppName}"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\{#MyAppExeName},0"
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.ogg\shell\{#MyAppName}\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.m4a\shell\{#MyAppName}"; ValueType: string; ValueName: ""; ValueData: "Compress to 10 MB"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.m4a\shell\{#MyAppName}"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\{#MyAppExeName},0"
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.m4a\shell\{#MyAppName}\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.wma\shell\{#MyAppName}"; ValueType: string; ValueName: ""; ValueData: "Compress to 10 MB"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.wma\shell\{#MyAppName}"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\{#MyAppExeName},0"
Root: HKCU; Subkey: "Software\Classes\SystemFileAssociations\.wma\shell\{#MyAppName}\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""
