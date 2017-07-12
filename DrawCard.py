def DrawCard(deckCards):
    ''' This function draws a card, prints the value'''
    import random as rand
    import numpy as np
    # generate and report  card then ask for action
    index = rand.randint(0, len(deckCards)-1)
    card_value = deckCards[index]
    deckCards = np.delete(deckCards, index)
    # print('Cards after removal: \n {}'.format(deckCards))
    print("card value is: {}".format(card_value))

    return card_value, deckCards

def intro(money):
    print("\n")
    print("welcome to the amazing blackjack experience")
    print("thanks to our infinite kindness you can bet more money than you have. Cause F it, why not")
    print("try to earn as much money as possible and unlock the cool rewards")
    print("remember, bank holds at 16")
    print("You are starting with {} euros".format(money))
    print("\n")

def update(money, money_betted, type):
    if type == 'win':
        money_betted = money_betted * 1.5
        print("you win and you {} $".format(money_betted))
        money += money_betted
    elif type == 'lose':
        money_betted = money_betted * -1
        print("the bank wins and you lose {} $".format(money_betted))
        money += money_betted

    return  money