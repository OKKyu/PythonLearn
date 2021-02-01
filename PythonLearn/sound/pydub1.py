#!python3
# -*- coding:utf-8 -*-
import sys
import os
from pydub import AudioSegment
from pydub.playback import play

# シェル引数からファイル名を受け取る
if len(sys.argv) != 2 or os.path.exists(sys.argv[1]) == False:
    print("Please input target audio file(mp3)")
    sys.exit(1)

# 音声ファイルの読み込み
sound = AudioSegment.from_file(sys.argv[1], "mp3")

# 再生
play(sound)

# 情報の取得
time = sound.duration_seconds # 再生時間(秒)
rate = sound.frame_rate  # サンプリングレート(Hz)
channel = sound.channels  # チャンネル数(1:mono, 2:stereo)

# 情報の表示
print('チャンネル数：', channel)
print('サンプリングレート：', rate)
print('再生時間：', time)

# 指定したフォーマットとビットレートで保存
sound.export("output.mp3", format="wav", bitrate="192k")