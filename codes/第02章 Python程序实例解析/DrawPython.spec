# -*- mode: python -*-

block_cipher = None


a = Analysis(['DrawPython.py'],
             pathex=['E:\\02 �����ݿ�������-Python\\01 �μ�\\�����ݿ�������(Python���Գ������)-�μ�\\Codes\\��02�� Python����ʵ������'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='DrawPython',
          debug=False,
          strip=False,
          upx=True,
          console=True )
