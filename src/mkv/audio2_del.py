"""
剔除mkv文件轨道id为2的音频，参数1为 文件 或 文件夹
"""

from argparse import ArgumentParser
from os import chdir, path
from sys import argv

from pymkv import MKVFile, MKVTrack
from rich.progress import track as rich_track

from utils import dir_scan

arg = ArgumentParser()
arg.add_argument("input", help="input file or directory")


def file_work(work_file: str):
    mkv = MKVFile(work_file)
    removed_track = False
    tracks: list[MKVTrack] = mkv.tracks
    if type(tracks[0]) is not MKVTrack:
        return
    for track in tracks[:]:
        if track.track_id == 2 and track.track_type == "audio":
            mkv.tracks.remove(track)
            removed_track = True
    if removed_track:
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
        for file in rich_track(dir_scan(), description="正在删除音频"):
            file_work(file)


if __name__ == "__main__":
    main()
