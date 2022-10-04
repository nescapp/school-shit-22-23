import random


def main():
    deck = []
    for suit in ['H', 'D', 'S', 'C']:  # Hearts, Diamonds, Spades, Clubs
        for value in range(1, 14):
            deck.append((suit, value))
    random.shuffle(deck)  # shuffle the deck
    player = []
    dealer = []
    for i in range(2):  # deal two cards to each player
        player.append(deck.pop())
        dealer.append(deck.pop())
    print("Player: ", player)
    print("Dealer: ", dealer)
    while True:
        # sum the values of the cards
        total = sum([card[1] for card in player])
        if total > 21:  # if the total is over 21, the player has busted
            print("Bust!")
            break
        print("Total: ", total)  # print the total

        # ask the player if they want to hit or stay
        choice = input("Hit or stay? ")
        if choice == "hit":  # if they want to hit, deal them another card
            player.append(deck.pop())
        else:  # if they want to stay, break out of the loop
            break
    while True:
        total = sum([card[1] for card in dealer])
        if total > 21:
            print("Bust!")
            break
        if total >= 17:  # if the dealer has 17 or more, they must stay
            break
        dealer.append(deck.pop())
    print("Player: ", player)
    print("Dealer: ", dealer)
    # sum the values of the cards
    player_total = sum([card[1] for card in player])
    dealer_total = sum([card[1] for card in dealer])
    if player_total > 21:  # if the player has busted, the dealer wins
        print("Dealer wins!")
    elif dealer_total > 21:  # if the dealer has busted, the player wins
        print("Player wins!")
    elif player_total > dealer_total:  # if the player has a higher total, the player wins
        print("Player wins!")
    elif dealer_total > player_total:  # if the dealer has a higher total, the dealer wins
        print("Dealer wins!")
    else:
        print("Tie!")  # if the totals are the same, it's a tie


# call the main function if the program is run directly (not imported)
if __name__ == "__main__":
    main()
