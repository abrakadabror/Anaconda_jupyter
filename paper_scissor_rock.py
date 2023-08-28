player1_score = 0
player2_score = 0
options = ['kamien', 'papier', 'nozyce']


def download_choice(gracz):
    while True:
        user_choice = input(f' {gracz} podaj swoj wybor: ')
        if user_choice in options:
            return user_choice


def check_result(user_choice_1, user_choice_2):
    if user_choice_1 == 'papier' and user_choice_2 == 'kamien' or \
            user_choice_1 == 'kamien' and user_choice_2 == 'nozyce' or  \
            user_choice_1 == 'nozyce' and user_choice_2 == 'papier':
        print('Gracz1 wygral')
        return 1
    elif user_choice_1 == user_choice_2:
        return 0
    else:
        print('Gracz dwa wygral')
        return -1


while player1_score != 3 and player2_score != 3:
    user_choice_1 = download_choice('Gracz1')
    user_choice_2 = download_choice('Gracz2')
    score = check_result(user_choice_1, user_choice_2)

    if score == 1:
        player1_score += 1
    elif score == - 1:
        player2_score += 1

if player1_score > player2_score:
    print('gre wygrywa gracz 1')
elif player1_score < player2_score:
    print('gre wygrywa gracz 2')
