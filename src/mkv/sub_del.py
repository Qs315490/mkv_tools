"""
剔除mkv文件字幕，参数1为 文件 或 文件夹
"""

from argparse import ArgumentParser
from os import chdir, path
from sys import argv

from pymkv import MKVFile, MKVTrack
from rich.progress import track as rich_track

from utils import dir_scan

arg = ArgumentParser()
arg.add_argument("input", help="input.mkv or mkv_dir")


def file_work(work_file: str):
    mkv = MKVFile(work_file)
    removed_track = False
    tracks: list[MKVTrack] = mkv.tracks
    if type(tracks[0]) is not MKVTrack:
        return
    for file_track in tracks[:]:
        if file_track.track_type == "subtitles":
            mkv.tracks.remove(file_track)
            removed_track = True
    if removed_track:
        mkv.no_attachments()
        # 在文件目录新建output文件夹
        mkv.mux(f"./output/{path.basename(work_file)}", silent=True)


def main(arg_list: list = argv):
    args = arg.parse_args(arg_list[1:])
    input_file = args.input

    if path.isfile(input_file):
        work_path = path.dirname(input_file)
        chdir(work_path)
        file_work(path.basename(input_file))
    else:  # Directory
        work_path = input_file
        chdir(work_path)
        for file in rich_track(dir_scan(), description="正在剔除字幕"):
            file_work(file)


if __name__ == "__main__":
    main()
