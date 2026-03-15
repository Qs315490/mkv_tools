from os import getcwd, listdir
from os.path import isfile
from os.path import join as path_join

VIDEO_EXT = [".mkv", ".mp4"]
AUDIO_EXT = [".mka", ".mp3", ".flac"]
SUBTITLE_EXT = [".ass", ".srt"]


def dir_scan(dir_path: str | None = None, file_ext: list[str] = VIDEO_EXT):
    """扫描目录，返回视频文件列表，不包含子目录
    @param dir_path: 目录路径
    @return: 视频文件列表
    """
    if dir_path is None:
        dir_path = getcwd()

    videos: list[str] = []
    for file in listdir(dir_path):
        if not isfile(path_join(dir_path, file)):
            continue
        if any([file.endswith(ext) for ext in file_ext]):
            videos.append(file)

    return videos


def dir_scan_vs(dir_path: str | None = None):
    """扫描目录，返回视频文件和字幕文件列表，不包含子目录
    @param dir_path: 目录路径
    @return: (视频文件列表, 字幕文件列表)
    """
    if dir_path is None:
        dir_path = getcwd()

    videos: list[str] = []
    subtitles: list[str] = []
    for file in listdir(dir_path):
        if not isfile(path_join(dir_path, file)):
            continue
        if any([file.endswith(ext) for ext in VIDEO_EXT]):
            videos.append(file)
        if any([file.endswith(ext) for ext in SUBTITLE_EXT]):
            subtitles.append(file)

    return videos, subtitles


def dir_scan_va(dir_path: str | None = None):
    """扫描目录，返回视频文件和音频文件列表，不包含子目录
    @param dir_path: 目录路径
    @return: (视频文件列表, 音频文件列表)
    """
    if dir_path is None:
        dir_path = getcwd()

    videos: list[str] = []
    audios: list[str] = []
    for file in listdir(dir_path):
        if not isfile(path_join(dir_path, file)):
            continue
        if any([file.endswith(ext) for ext in VIDEO_EXT]):
            videos.append(file)
        if any([file.endswith(ext) for ext in AUDIO_EXT]):
            audios.append(file)

    return videos, audios

def lang_code_convert(code: str = "und", name: str = "") -> tuple[str, str]:
    """
    @param code: 语言代码
    @param name: 语言名称
    @return: (语言名称, ISO639名称)
    """
    if code == "":
        return name, "und"
    lang_zh_cn = ["chs", "sc", "zh", "zh-cn", "zh-hans", "jpsc", "gb"]
    lang_zh_tw = ["cht", "tc", "zh-tw", "zh-hant", "jptc", "big5"]
    lang_jp = ["ja", "jp"]
    if code.lower() in lang_zh_cn:
        return "简体中文", "chi"
    if code.lower() in lang_zh_tw:
        return "繁体中文", "chi"
    if code.lower() in lang_jp:
        return "日语", "jpn"
    return name, code


def subtitle_get_lang_code(filename: str):
    """从字幕文件名获取语言代码
    @param filename: 文件名
    @return: (语言名称, ISO639名称)
    """
    info = filename.split(".")[1:-1]  # 获取文件尾部名称
    count = len(info)

    if count == 2:  # 符合jellyfin标注的格式 “语言名称.ISO639名称”
        tmp = lang_code_convert(info[1], info[0])
    elif count == 1:  # 常见格式
        tmp = lang_code_convert(info[0])
    elif count == 0:
        # 无语言代码，默认为简体中文
        tmp = lang_code_convert("chs")
    else:
        raise Exception("无法从文件名获取语言代码")
    return tmp
