from get_music_list import get_music_list
import dasda as music_player
import os

music_list = get_music_list()
music_player.initMixer()

while True:
    os.system('cls')
    for i, ml in enumerate(music_list):
        print(str(i) + '.' + ml)

    user_input = input()

    if 0 <= int(user_input) < len(music_list):
        music_player.playmusic(music_list[int(user_input)])
    elif user_input == 'stop':
        music_player.stopmusic()
    else:
        exit()
