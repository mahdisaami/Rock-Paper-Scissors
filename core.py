from constants import PLAYER_RULE


def check_one_hand(user_choice, system_choice):
    return PLAYER_RULE[user_choice][system_choice]


def modify_scores(current_result, current_scores):
    if current_result == 1:
        current_scores['user'] = current_scores['user'] + 1
    elif current_result == -1:
        current_scores['system'] = current_scores['system'] + 1
    return current_scores


def check_total(current_scores):
    if current_scores["user"] == 3:
        current_scores["total_user"] = current_scores["total_user"] + 1
        current_scores['user'] = 0
        current_scores['system'] = 0

        print('#' * 30, '\tyou win the hand \t', "#" * 30)
        print("total scores : {} - {}".format(
            current_scores["total_user"], current_scores["total_system"]))
        print('#' * 80)

    elif current_scores["system"] == 3:
        current_scores["total_system"] = current_scores["total_system"] + 1
        current_scores['user'] = 0
        current_scores['system'] = 0

        print('#' * 30, '\tyou lose the hand \t', "#" * 30)
        print("total scores : {} - {}".format(
            current_scores["total_user"], current_scores["total_system"]))
        print('#' * 80)

    return current_scores
