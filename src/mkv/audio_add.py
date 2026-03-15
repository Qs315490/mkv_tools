"""
合并mkv mka，参数1为 文件夹
"""

from argparse import ArgumentParser
from os import chdir, path
from sys import argv, exit

from pymkv import MKVFile, MKVTrack
from rich.progress import track as rich_track

from utils import dir_scan_va

arg = ArgumentParser()
arg.add_argument("dir_path", help="mkv and mka dir")


def file_work(work_file: str):
    mkv = MKVFile(work_file)
    add_track = False
    name = path.splitext(work_file)[0]  # 获取文件名，无扩展名
    mka_list: list[str] = []  # 匹配文件
    for mka in audios[:]:
        if name.lower() in mka.lower():
            mka_list.append(mka)
            audios.remove(mka)
    # 开始添加文件
    for mka in mka_list:
        mkvtrack = MKVTrack(mka)
        mkv.add_track(mkvtrack)
        add_track = True

    if add_track:
        # 在文件目录新建output文件夹
        mkv.mux(f"./output/{work_file}", silent=True)


def main(arg_list: list = argv):
    args = arg.parse_args(arg_list[1:])
    work_path: str = args.dir_path
    if not path.isdir(work_path):
        exit(f"Path {work_path} is not a directory")

    chdir(work_path)
    global audios
    videos, audios = dir_scan_va()
    for mkv in rich_track(videos, description="正在添加音频"):
        file_work(mkv)


if __name__ == "__main__":
    main()
