from pathlib import Path

import bpy
from bpy.app.handlers import persistent

bl_info = {
    "name": "PrintSize",
    "author": "tsutomu",
    "version": (0, 1),
    "blender": (3, 1, 0),
    "support": "TESTING",
    "category": "Object",
    "description": "",
    "location": "View3D > Object",
    "warning": "",
    "doc_url": "https://github.com/SaitoTsutomu/PrintSize",
}


@persistent
def print_size(*args):
    """保存時に実行され、ファイルサイズを出力"""
    pth = Path(bpy.data.filepath)
    st = pth.stat()
    print(f"# {st.st_size / 1000_000:.2f} MB {pth.name}")


def register():
    bpy.app.handlers.save_post.append(print_size)


def unregister():
    bpy.app.handlers.save_post.remove(print_size)
