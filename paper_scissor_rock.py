import getpass
player1_score = 0
player2_score = 0

options = ['kamien', 'papier', 'nozyce']
while player1_score != 3 and player2_score != 3:
    users_choices = True
    while users_choices:
        user_choice_1 = getpass.getpass(
            'Graczu numer 1 wybierz jedna z opcji: kamien/papier/nozyce: ')
        if user_choice_1 in options:
            users_choices = False
    users_choices = True
    while users_choices:
        user_choice_2 = getpass.getpass(
            'Graczu numer 2 wybierz jedna z opcji: kamien/papier/nozyce: ')
        if user_choice_2 in options:
            users_choices = False

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
