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
        file_name_no_ext: str = file_name.rsplit(".", 1)[0]
        print(f"Extracting {file_name_no_ext}.ass")
        system(f"mkvextract '{file}' tracks '2:{file_name_no_ext}.ass'")


if __name__ == "__main__":
    main()
