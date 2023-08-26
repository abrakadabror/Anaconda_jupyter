player1_score = 0
player2_score = 0
while player1_score != 3 and player2_score != 3:
    user_choice_1 = input(
        str('Graczu numer 1 wybierz jedna z opcji: kamien/papier/nozyce '))
    user_choice_2 = input(
        str('Graczu numer 2 wybierz jedna z opcji: kamien/papier/nozyce '))

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
