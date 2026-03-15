"""
添加mkv文件字幕，参数1为 文件夹
"""

from argparse import ArgumentParser
from os import chdir, path
from sys import argv, exit

from pymkv import MKVFile, MKVTrack
from rich.progress import track as rich_track

from utils import dir_scan_vs, subtitle_get_lang_code

arg = ArgumentParser()
arg.add_argument("dir_path", type=str, help="mkv and ass dir")


def file_work(work_file: str):
    mkv = MKVFile(work_file)
    add_track = False
    name = path.splitext(work_file)[0]  # 获取文件名，无扩展名
    subs_list: list[str] = []  # 匹配的字幕文件
    for sub in subs[:]:
        if name.lower() in sub.lower():
            subs_list.append(sub)
            subs.remove(sub)
    # 开始添加字幕文件
    for sub in subs_list:
        mkvtrack = MKVTrack(sub)
        try:
            mkvtrack.track_name, mkvtrack.language = subtitle_get_lang_code(
                sub.replace(name, "", 1)
            )  # 获取文件尾部名称
        except Exception:  # 不符合格式
            print(f"文件 {sub} 无匹配格式，跳过")
            continue
        if "简" in mkvtrack.track_name:  # 如果是简体就设置为默认
            mkvtrack.default_track = True
        mkv.add_track(mkvtrack)
        add_track = True

    if add_track:
        # 在文件目录新建output文件夹
        mkv.mux(f"./output/{work_file}")


def main(arg_list: list = argv):
    args = arg.parse_args(arg_list[1:])
    work_path = args.dir_path

    if not path.isdir(work_path):
        exit(f"Path {work_path} is not a directory")

    chdir(work_path)
    global subs
    mkvs, subs = dir_scan_vs()
    for mkv in rich_track(mkvs, description="正在添加字幕"):
        file_work(mkv)


if __name__ == "__main__":
    main()
