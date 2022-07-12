import random

from data import CHOOSE_OPTION, RULES, score_board, test_decorator


def valid_user_input():
    choose = input("please choose (r,p,s) \n")
    if choose not in CHOOSE_OPTION:
        print("please choose valid ")
        valid_user_input()
    return choose


def find_winner(user, system):
    main = {user, system}

    if user == system:
        return "draw"

    return RULES[tuple(sorted(main))]


def update_score_board(result):
    if result['user'] == 3:
        score_board["user"] += 1

    elif result['system'] == 3:
        score_board["system"] += 1

    print("#" * 30)
    print("##", f'user: {score_board["user"]}'.ljust(24), "##")
    print("##", f'system: {score_board["system"]}'.ljust(24), "##")
    print("#" * 30)


def play():
    result = {"user": 0, "system": 0}

    while result['user'] < 3 and result['system'] < 3:
        user_input = valid_user_input()
        system_choose = random.choice(CHOOSE_OPTION)
        winner = find_winner(user_input, system_choose)

        #  print(user_input + "" + system_choose + "" + winner)

        if winner == user_input:
            result['user'] += 1
            print("you win")
        elif winner == system_choose:
            result['system'] += 1
            print("you lose")
        else:
            print("draw")
    update_score_board(result)
    end = input("you want to still play (y/n) ")
    if end == "y":
        play()


@test_decorator
def play_update():
    play()


if __name__ == '__main__':
    play_update()

#end
