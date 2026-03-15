# 介绍

# 使用
安装 `MKVToolNix`，并添加环境变量。使终端能够执行 `mkvmerge` 相关命令。
推荐使用 `uv` 安装依赖。
```bash
git clone --depth=1 此项目仓库地址
cd mkv_tools
uv sync
uv run mkv-tools -h
```

# 功能
## ass-zhconvert.py
```
python ass-zhconvert.py <input.ass>|<mkv_dir>
```
将繁体的字幕文件翻译为简体

## mkv.attachments_del.py
```
python -m src.mkv.attachments_del.py <input.mkv>|<mkv_dir>
```
剔除mkv附加文件

## mkv.audio_add.py
```
python -m src.mkv.audio_add.py <mkv_and_audio_dir>
```
将 `input.flac` 音频文件添加到 `input.mkv` 视频中，音频文件前名称应与视频匹配，后缀前字符应为语言代码。

## mkv.audio2_del.py
将 `input.mkv` 视频中的第二音频轨道删除。
```
python -m src.mkv.audio2_del.py <input.mkv>
```

## mkv.title_del.py
删除 mkv 视频的 `标题`
```
python -m src.mkv.title_del.py <input.mkv>|<mkv_dir>
```

## mkv.sub_add.py
```
python -m src.mkv.sub_add.py <mkv_and_ass_dir>
```
将 `input.ass` 字幕文件添加到 `input.mkv` 视频中，字幕文件前名称应与视频匹配，后缀前字符应为语言代码。
语言|代码
-|- 
简体中文 | 'chs'、'sc'、'zh'、'zh-cn'、'zh-Hans'
繁体中文 | 'cht'、'tc'、'zh-tw'、'zh-Hant'

## mkv.sub_del.py
```
python -m src.mkv.sub_del.py <input.mkv>|<mkv_dir>
```
删除 mkv 视频的 `字幕` 和 `附加文件`

## mkv.sub_edit.bat
将第一字幕轨道名称设置为 `简体中文`，并设置为默认轨道。将第二字幕（如果存在）轨道名称设置为 `繁体中文`，并取消默认轨道。  
```
python -m src.mkv.sub_edit.py <input.mkv>|<mkv_dir>
```

## mkv.sub_ext.py
获取轨道为2的字幕文件，并保存为 `input.ass`。
```
python -m src.mkv.sub_ext.py <input.mkv>|<mkv_dir>
```
