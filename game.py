from random import choice
from constants import PLAYER_OPTION, RESULT_BANNER, CONTROL_OPTIONS
from core import check_one_hand, modify_scores, check_total
from datetime import datetime


scores = {'user': 0, 'system': 0, 'total_user': 0, 'total_system': 0}
play = True
started_time = datetime.now()
while play:
    user_input = input('Enter your choice please (options are r,p,s): ')
    system_choice = choice(list(PLAYER_OPTION.keys()))

    if user_input in PLAYER_OPTION.keys():
        result = check_one_hand(user_input, system_choice)
        scores = modify_scores(result, scores)
        print('your choice : {}, system choice : {}, result : {} \tscores : {} - {}'.format(
            PLAYER_OPTION[user_input], PLAYER_OPTION[system_choice], RESULT_BANNER[result],
            scores['user'], scores['system'])
        )
        scores = check_total(scores)
    elif user_input in CONTROL_OPTIONS.keys():
        play = False
        ended_time = datetime.now()
        duration = ended_time-started_time 
    
        print('duration: {}:{}'.format(duration.seconds//60, duration.seconds % 60), ' Bye!!!!!!!!')
    else:
        print('Invalid input, try again please...')
