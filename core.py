from pathlib import Path

import bpy


def print_size(*args):
    """保存時に実行され、ファイルサイズを出力"""
    pth = Path(bpy.data.filepath)
    st = pth.stat()
    print(f"# {pth.name} {st.st_size / 1000_000:.2f} MB")


def register():
    """追加登録用（クラス登録は、register_class内で実行）"""
    bpy.app.handlers.save_post.append(print_size)


def unregister():
    """追加削除用（クラス削除は、register_class内で実行）"""
    bpy.app.handlers.save_post.remove(print_size)
