## maak een spelletje o.i.d.
## blackjack voor 1 speler tegen het huis

# laad benodigde modules
import numpy as np
import random as rand
import DrawCard as DC

# intialize values
score_player = 0
money = 100
stop = True

#introduction
DC.intro(money)

# TODO: remove cards from deck during a round, in DrawCard
# TODO: place more repetitive code into different files
# TODO, check for redundancy by reading through the entire doc.

#play until there is no money, or the stop command is given
while stop:
    # bet money per round
    money_betted = float(input("How much do you want to bet? "))
    print("A new round is starting, good luck and have fun!")
    print("\n")

    # a new deck of cards is shuffled
    vecCards_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    vecCards_deck = np.repeat(vecCards_set, 4)

    stop_round = True

    # play a round untill the score goes equal or above 21, or the stop command is given
    while stop_round:

        # a card is drawn, which is removed from the deck
        player_firstcard, vecCards_deck = DC.DrawCard(vecCards_deck)
        action = int(input("What do you want to do? bet=1, check=2 "))

        # execute betting action
        if action ==1:
            raising = float(input("How much do you want to bet? "))
            money_betted += raising

        player_secondcard, vecCards_deck = DC.DrawCard(vecCards_deck)

        score_player = player_firstcard + player_secondcard
        print("you have: {}".format(score_player))
        print('\n')

        print("Bank's cards are: ")
        bank_firstcard, vecCards_deck = DC.DrawCard(vecCards_deck)
        bank_secondcard, vecCards_deck = DC.DrawCard(vecCards_deck)
        score_bank = bank_firstcard + bank_secondcard
        print("Bank has: {}".format(score_bank))

        if score_player == 21:
            print("You have 21, you win")
            money = DC.update(money, money_betted, 'win')
            break
        elif score_bank == 21:
            print("bank has 21, you LOSE!")
            money = DC.update(money, money_betted, 'lose')
            break

        action = int(input("What do you want to do? bet=1, check=2 "))
        # if the player bets, she gets another card.
        while action==1:
            raising = float(input("How much do you want to bet? "))
            money_betted += raising
            player_thirdcard, vecCards_deck = DC.DrawCard(vecCards_deck)
            score_player += player_thirdcard
            print("you have: " + str(score_player))
            print("\n")

            if score_player > 21:
                print("You are bust")
                print('Your score is {}, the bank has {}'.format(score_player, score_bank))
                money = DC.update(money, money_betted, 'lose')
                break
            else:
                action = int(input("What do you want to do? bet=1, check=2 "))
        if action==2:
            while score_bank < 16:
                print("\n")
                print("Bank has lower than 16, so a new card is drawn")
                bank_newcard, vecCards_deck = DC.DrawCard(vecCards_deck)
                score_bank += bank_newcard
                print("Bank has: {}".format(score_bank))
                if score_bank > 21:
                    print("\n")
                    print("the bank has gone bust")
                    print('Your score is {}, the bank has {}'.format(score_player, score_bank))
                    money = DC.update(money, money_betted, 'win')
                    break

            if score_player == 21:
                print("You have 21, you win")
                print('Your score is {}, the bank has {}'.format(score_player, score_bank))
                money = DC.update(money, money_betted, 'win')
                stop_round = False
            elif score_player > 21:
                print("You KOMEN WE HIER OOIT?")
            else:
                if score_bank >= score_player and score_bank < 21:
                    print('Your score is {}, the bank has {}'.format(score_player, score_bank))
                    money = DC.update(money, money_betted, 'lose')
                    stop_round = False
                elif score_player > score_bank and score_player < 21:
                    print('Your score is {}, the bank has {}'.format(score_player, score_bank))
                    money = DC.update(money, money_betted, 'win')
                    stop_round = False


        print("your current balance is {} $".format((money)))
        if money <= 0:
            break
        stop_choice = int(input("Do you want to continue? 1=yes, 2=no"))
        if stop_choice ==2:
            stop=False
