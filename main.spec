# -*- mode: python ; coding: utf-8 -*-
pillow_path = '/Users/pier/.virtualenvs/fancyfolders/lib/python3.11/site-packages/PIL'


a = Analysis(
    ['fancyfolders/main.py'],
    pathex=[],
    binaries=[],
    #datas=[("assets", "assets")],
    datas=[
        ("assets", "assets"),
        ("fancyfolders", "fancyfolders"), # Aggiungi questa riga
        (pillow_path, "PIL") # <-- QUESTA RIGA COPIERÀ LA CARTELLA PIL AL SUO POSTO
    ],
    #hiddenimports=[],
    hiddenimports=['uuid', 'colorsys', 'Cocoa'], # Aggiungi 'Cocoa' qui
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
app = BUNDLE(
    coll,
    name='Fancy Folders.app',
    version='2.0',
    icon="assets/app_icon.icns",
    bundle_identifier="ca.kfreitag.fancyfolders",
)

# note, need to do: .venv/bin/pyinstaller main.spec
