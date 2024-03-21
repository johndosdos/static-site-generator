from process_nodes import *
import os
import shutil


def copy_directory(src_path, dst_path):
    paths = os.listdir(src_path)

    for path in paths:
        new_src = os.path.join(src_path, path)
        new_dst = os.path.join(dst_path, path)

        if os.path.isdir(new_src):
            os.makedirs(new_dst, exist_ok=True)
            copy_directory(new_src, new_dst)

        elif os.path.isfile(new_src):
            shutil.copy2(new_src, new_dst)


def main():
    copy_directory("static", "public")


main()
