import os
import re


def get_music_list():
    music_regex = re.compile(r'[^\.]+\.mp3')
    files = os.listdir('.')
    wave_files = [i for i in files if music_regex.match(i) != None]
    return wave_files
