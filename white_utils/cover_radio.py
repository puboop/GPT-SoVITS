# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2024-05-16
# @Author  : white
# @FileName: cover_radio.py
# @Software: PyCharm
# **************************************
from pydub import AudioSegment
import wave


# pip install pydub
# conda install ffmpeg

class CoverRadio:
    def __init__(self, source_radio: str):
        self.source_radio = source_radio
        self.out_file = self.source_radio.rsplit('.', maxsplit=1)[0]

    def to_wav(self, out_file: str = None):
        """mp3转为wav格式"""
        sound = AudioSegment.from_file(self.source_radio)

        out_file = out_file or self.out_file + ".wav"
        sound.export(out_file, format="wav")
        print(f"转换完成！转换路径：{out_file}")

    def to_mp3(self, out_file: str = None):
        """wav转换为mp3格式"""
        audio = AudioSegment.from_wav(self.source_radio)

        out_file = out_file or self.out_file + ".mp3"
        audio.export(out_file, format="mp3")
        print(f"转换完成！转换路径：{out_file}")


if __name__ == '__main__':
    c = CoverRadio("../data/zxp.m4a")
    c.to_wav()
