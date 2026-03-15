# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "opencc>=1.2.0",
# ]
# ///
"""
转换mkv文件字幕，参数1为 文件 或 文件夹
"""

from os import chdir, mkdir, path
from sys import argv

from opencc import OpenCC

from utils import SUBTITLE_EXT, dir_scan

OUTPUT_PATH = "./output"


def file_convert(work_file: str):
    with open(work_file, encoding="utf-8") as f:
        content = f.read()
    content = OpenCC("t2s.json").convert(content)
    if not path.isdir(OUTPUT_PATH):
        mkdir(OUTPUT_PATH)
    with open(f"{OUTPUT_PATH}/{work_file}", "x", encoding="utf-8") as f:
        f.write(content)
    print(f"{work_file} 转换完成")


def dir_convert():
    file_list = dir_scan(file_ext=SUBTITLE_EXT)

    for file in file_list:
        file_convert(file)


def main():
    argc = len(argv)
    if argc < 2:
        print(f"Usage: python {argv[0]} <input.ass>|<mkv_dir>")
        return

    if path.isfile(argv[1]):
        work_path = path.dirname(argv[1])
        chdir(work_path)
        file_convert(path.basename(argv[1]))
    else:
        work_path = argv[1]
        chdir(work_path)
        dir_convert()


if __name__ == "__main__":
    main()
