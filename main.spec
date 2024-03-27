# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('toxic_comment_classifier.joblib', '.'), 
        ('tfidf_vectorizer.joblib', '.'),
        ('PieChart1.png', '.'),  # Pie chart image
        ('Barchart1.png', '.'),  # Bar chart image
        ('LineGraph.png', '.')  # Line chart image
    ],
    hiddenimports=[
        'sklearn',
        'sklearn.tree._criterion',
        'sklearn.tree._splitter',
        'sklearn.tree._tree',
        'sklearn.ensemble._forest',
        'sklearn.neighbors.typedefs',
        'sklearn.neighbors.quad_tree',
        'sklearn.tree._utils',
        'sklearn.utils._cython_blas',
        'sklearn.utils._weight_vector',
        'sklearn.neighbors._partition_nodes',
        'sklearn.multioutput',
        'sklearn.feature_extraction',
        'sklearn.feature_extraction.text',
        # Add any other hidden imports your application requires
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,  # Make sure `a.datas` is included here
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Use `console=True` if you want a console window, useful for debugging
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
