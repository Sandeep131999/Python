import random
import art

def chose_card():
    """
    Randomly selects and returns a card value from a standard Blackjack deck.

    Returns:
        int: A card value, where Ace is treated as 11 and face cards as 10.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def adjust_ace(hand):
    """
    Adjusts Aces in the hand so that the total does not exceed 21.
    Converts Ace values from 11 to 1 only if needed.

    Args:
        hand (list[int]): The list of card values in the player's or dealer's hand.

    Returns:
        list[int]: The modified hand with adjusted Ace values.
    """
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
    return hand


def chose_winner(player, dealer):
    """
    Determines the outcome of the Blackjack round based on totals.

    Args:
        player (list[int]): The player's card values.
        dealer (list[int]): The dealer's card values.

    Returns:
        str: A message indicating the result (win, lose, draw).
    """
    player_total = sum(player)
    dealer_total = sum(dealer)

    if player_total > 21:
        return "You went over. You lose."

    elif dealer_total > 21:
        return "Dealer went over. You win!"

    elif player_total > dealer_total:
        return "Player wins."

    elif dealer_total > player_total:
        return "Dealer wins."

    else:
        return "Draw."


# ------------------ GAME START ------------------ #
def play_game ():
    userCards = []
    compCards = []
    print(art.logo)

    for _ in range(2):
        userCards.append(chose_card())
        compCards.append(chose_card())

    adjust_ace(userCards)
    adjust_ace(compCards)

    print(f"Your cards: {userCards}, current score: {sum(userCards)}")
    print(f"Computer's first card: {compCards[0]}")

    game_on = True

    while game_on:

        if sum(userCards) < 21:
            choice = input("Type 'y' to get another card, type 'n' to pass: ")

            if choice.lower() == 'y':
                userCards.append(chose_card())
                adjust_ace(userCards)
                print(f"Your cards: {userCards}, current score: {sum(userCards)}")
            else:
                game_on = False
        else:
            game_on = False

    # Dealer plays
    while sum(compCards) < 17:
        compCards.append(chose_card())
        adjust_ace(compCards)

    # Results
    print(f"\nYour final hand: {userCards}, final score: {sum(userCards)}")
    print(f"Computer's final hand: {compCards}, final score: {sum(compCards)}")
    print(chose_winner(userCards, compCards))

game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if game_start == "y" :
    play_game()



