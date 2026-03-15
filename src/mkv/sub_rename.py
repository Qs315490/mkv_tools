from argparse import ArgumentParser
from os import system
from os.path import basename, isfile
from sys import argv

from rich.progress import track as rich_track

arg = ArgumentParser()
arg.add_argument("video_file", nargs="+", help="video file")


def main(arg_list: list = argv):
    args = arg.parse_args(arg_list[1:])

    for file in rich_track(args.video_file):
        if not isfile(file):
            print(f"{file} is not a file")
            continue
        file_name: str = basename(file)
        print(f"Rename {file_name}")
        # 编辑第一个字幕名称 第二个字幕名称，设置默认标志关闭
        system(
            f'mkvpropedit --edit track:3 -s name="简体中文" -s flag-default=1 '
            f'--edit track:4 -s name="繁体中文" -s flag-default=0 "{file}"'
        )


if __name__ == "__main__":
    main()
