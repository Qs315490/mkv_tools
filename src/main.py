import importlib
from argparse import ArgumentParser
from functools import partial
from sys import argv

arg = ArgumentParser()
subparsers = arg.add_subparsers(required=True, dest="command")
add_subparser = partial(subparsers.add_parser, add_help=False)
add_subparser("attachments_del", help="删除 mkv 的附件", )
add_subparser("audio_add", help="添加 音频 文件到 mkv ")
add_subparser("audio2_del", help="删除 mkv 的第二音频轨道")
add_subparser("sub_add", help="添加 字幕文件到 mkv 中")
add_subparser("sub_del", help="删除 mkv 的字幕轨道")
add_subparser("sub_ext", help="提取 mkv 的字幕轨道")
add_subparser("sub_rename", help="重命名 mkv 的字幕轨道")
add_subparser("title_del", help="删除 mkv 的标题")


def main():
    ns, args = arg.parse_known_args()
    command = ns.command
    # print(command, args)
    argv[0] = f"mkv_tools {command}"
    importlib.import_module(f"mkv.{command}").main(args)


if __name__ == "__main__":
    main()
