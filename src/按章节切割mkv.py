import json
from argparse import ArgumentParser
from os import path, popen, system
from sys import argv

from rich.progress import track as rich_track

arg = ArgumentParser()
arg.add_argument("video_path", type=str, nargs="+", help="视频文件路径")


def file_work(file: str):
    ffprobe_cmd = [
        "ffprobe",
        "-v",
        "warning",
        "-show_chapters",
        "-of",
        "json",
        "-i",
        f'"{argv[1]}"',
    ]
    # 获取视频章节信息
    video_chapters = popen(" ".join(ffprobe_cmd)).read()
    chapters = json.loads(video_chapters)["chapters"]

    ffmpeg_cmd_temp = ["ffmpeg", "-v", "info", "-i", f'"{argv[1]}"', "-c", "copy"]
    for chapter in rich_track(chapters, description=f"正在处理{file}"):
        chapter_start = chapter["start_time"]
        chapter_end = chapter["end_time"]

        # 开始分割视频
        ffmpeg_cmd: list[str] = ffmpeg_cmd_temp.copy()
        ffmpeg_cmd.extend(
            [
                "-ss",
                str(chapter_start),
                "-to",
                str(chapter_end),
                f'"{path.splitext(argv[1])[0]}_{chapter["tags"]["title"]}.mkv"',
            ]
        )
        system(" ".join(ffmpeg_cmd))


def main():
    args = arg.parse_args()
    for video_path in args.video_path:
        if not path.isfile(argv[1]):
            print("请输入正确的视频文件路径")
            continue
        file_work(video_path)


if __name__ == "__main__":
    main()
