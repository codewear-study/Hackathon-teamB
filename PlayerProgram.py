from get_music_list import get_music_list
import dasda as music_player

music_list = get_music_list()

for i in music_list:
    print(i + '.' + music_list[i])    

while True:
    user_input = input()

    if user_input.isdigit:
        music_player.playmusic(music_list[user_input])
    elif user_input == 'stop':
        music_player.stopmusic()
    
    









