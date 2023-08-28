player1_score = 0
player2_score = 0
options = ['kamien', 'papier', 'nozyce']


def download_choice(gracz):
    users_choices_is_correct = True
    while users_choices_is_correct:
        user_choice = input(f' {gracz} podaj swoj wybor: ')
        if user_choice in options:
            users_choices_is_correct = False
    return user_choice


while player1_score != 3 and player2_score != 3:
    user_choice_1 = download_choice('Gracz1')
    user_choice_2 = download_choice('Gracz2')

    if user_choice_1 == 'papier' and user_choice_2 == 'kamien' or \
            user_choice_1 == 'kamien' and user_choice_2 == 'nozyce' or  \
            user_choice_1 == 'nozyce' and user_choice_2 == 'papier':
        print('Gracz1 wygral')
        player1_score += 1
    elif user_choice_1 == user_choice_2:
        print('remis')
    else:
        print('Gracz dwa wygral')
        player2_score += 1
if player1_score > player2_score:
    print('gre wygrywa gracz 1')
elif player1_score < player2_score:
    print('gre wygrywa gracz 2')
