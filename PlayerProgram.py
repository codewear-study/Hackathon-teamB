from get_music_list import get_music_list
import dasda as music_player

music_list = get_music_list()
music_player.initMixer()

for i,ml in enumerate(music_list):
    print(str(i) + '.' + ml)    

while True:
    user_input = input()

    if user_input.isdigit():
        music_player.playmusic(music_list[int(user_input)])
    elif user_input == 'stop':
        music_player.stopmusic()
    
    









