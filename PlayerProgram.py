from get_music_list import get_music_list
import dasda as music_player
import os

music_list = get_music_list()
music_player.initMixer()

while True:
    for i,ml in enumerate(music_list):
        print(str(i) + '.' + ml)    

    user_input = input()

    if user_input.isdigit():
        music_player.playmusic(music_list[int(user_input)])
        os.system('cls')
    elif user_input == 'stop':
        music_player.stopmusic()
        os.system('cls')
    
    









