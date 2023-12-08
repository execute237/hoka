# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['/home/yan/wagyu-key-gen/src/scripts/stakingdeposit_proxy.py'],
    pathex=['/home/yan/wagyu-key-gen/src/scripts/../../dist/packages', '/home/yan/wagyu-key-gen/src/scripts/../vendors/staking-deposit-cli-2.7.0', '', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', '/home/yan/.local/lib/python3.10/site-packages', '/usr/local/lib/python3.10/dist-packages', '/usr/lib/python3/dist-packages'],
    binaries=[],
    datas=[('/home/yan/wagyu-key-gen/src/scripts/../vendors/staking-deposit-cli-2.7.0/staking_deposit/intl', 'staking_deposit/intl')],
    hiddenimports=[],
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
    a.binaries,
    a.datas,
    [],
    name='stakingdeposit_proxy',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
