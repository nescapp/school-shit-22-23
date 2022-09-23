import random

def main():
    deck = []
    for suit in ['H', 'D', 'S', 'C']:
        for value in range(1, 14):
            deck.append((suit, value))
    random.shuffle(deck)
    player = []
    dealer = []
    for _ in range(2):
        player.append(deck.pop())
        dealer.append(deck.pop())
    print("Player: ", player)
    print("Dealer: ", dealer)
    while True:
        total = sum([card[1] for card in player])
        if total > 21:
            print("Bust!")
            break
        print("Total: ", total)
        choice = input("Hit or stay? ")
        if choice == "hit":
            player.append(deck.pop())
        else:
            break
    while True:
        total = sum([card[1] for card in dealer])
        if total > 21:
            print("Bust!")
            break
        if total >= 17:
            break
        dealer.append(deck.pop())
    print("Player: ", player)
    print("Dealer: ", dealer)
    player_total = sum([card[1] for card in player])
    dealer_total = sum([card[1] for card in dealer])
    if player_total > 21:
        print("Dealer wins!")
    elif dealer_total > 21:
        print("Player wins!")
    elif player_total > dealer_total:
        print("Player wins!")
    elif dealer_total > player_total:
        print("Dealer wins!")
    else:
        print("Tie!")

if __name__ == "__main__":
    main()
