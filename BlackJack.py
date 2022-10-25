### Not complete

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game=input('Do you wanna play a blackjack game? select y or n')
if (game=='y'):
    sum_player=0
    sum_dealer = 0
    player_1=random.choice(cards)
    player_2=random.choice(cards)
    dealer_1=random.choice(cards)
    dealer_2 = random.choice(cards)
    sum_player=player_1+player_2
    sum_dealer=dealer_1+dealer_2
    if sum_dealer==21:
        print('dealer wins')
        exit()
    elif sum_player==21:
        print('Player wins')
        print(f'player first two cards are {player_1} & {player_2}')
        exit()
    print(f'player first two cards are {player_1} & {player_2}')
    print(f'dealer first card is {dealer_1}')
    while True:
        another_card=input('If the user wants to take another card? select y or n')
        if another_card=='y':
            card=random.choice(cards)
            sum_player+=card
            print(f'player 3rd card {card}')
            if sum_player>21:
                print('dealer won')
                exit()
        else:
            com_card=random.choice(cards)
    if dealer_1==11:
        sum_dealer+=1


else:
    print('you did not choose to play the game')