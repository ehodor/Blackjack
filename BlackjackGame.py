# Created by Emma Hodor on 12/30/2022
# ASCII art generated using patorjk.com
import random

logo = """

 ______     __         ______     ______     __  __       __     ______     ______     __  __    
/\  == \   /\ \       /\  __ \   /\  ___\   /\ \/ /      /\ \   /\  __ \   /\  ___\   /\ \/ /    
\ \  __<   \ \ \____  \ \  __ \  \ \ \____  \ \  _"-.   _\_\ \  \ \  __ \  \ \ \____  \ \  _"-.  
 \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ /\_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
  \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_/\/_/ \/_____/   \/_/\/_/   \/_____/   \/_/\/_/ 
                                                                                                 

"""

print(logo)
print('Welcome to Blackjack in Python!')
print('Your goal here is to beat the dealer by getting your total card'
      'value as close as possible to 21, but be careful to not go over!'
      'If you win, your bet is doubled. Otherwise, you lose your bet.'
      'Have fun!')

card = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'jack': 10,
    'queen': 10,
    'king': 10,
    'ace': [1, 11]
}


def blackjack(total=1000):
    def rerun():
        while True:
            replay = input("Would you like to replay? Type 'y' if yes and 'n' if no. ")
            if replay == 'y' or replay == 'n':
                break
            else:
                print('Please enter valid input.\n')
        if replay == 'y':
            blackjack(total)

    print(f'Your total cash: ${total}')
    while True:
        bet = input('First of all, how much would you like to bet? ')
        if bet.isdigit() and int(bet) <= total:
            bet = int(bet)
            break
        elif bet.isdigit() and int(bet) > total:
            print('Please enter bet less than total money.\n')
        else:
            print('Please enter valid amount.\n')
    print('The dealer is giving out cards...\n')

    player_cards = random.choices(list(card.keys()), k=2)
    dealer_cards = random.choices(list(card.keys()), k=2)

    def find_value(player):
        hand_value = 0
        if player == 'player':
            for i in player_cards:
                if i == 'ace':
                    if hand_value + card['ace'][1] > 21:
                        hand_value += card['ace'][0]
                    else:
                        hand_value += card['ace'][1]
                else:
                    hand_value += card[i]
        else:
            for i in dealer_cards:
                if i == 'ace':
                    if hand_value + card['ace'][1] > 21:
                        hand_value += card['ace'][0]
                    else:
                        hand_value += card['ace'][1]
                else:
                    hand_value += card[i]
        return hand_value

    player_value = find_value('player')
    dealer_value = find_value('dealer')
    print(f'Your hand: {player_cards}. Total hand value of {player_value}.')

    print(f"Your dealer has a '{random.choice(dealer_cards)}' and another card.")

    if player_value > 21 >= dealer_value:
        if total - bet > 0:
            new_total = total - bet
            print(f'Oops! You lose! Bet of ${bet} take from total of ${total}. You now have ${new_total}.')
            rerun()
        else:
            print('Oops! You ran out of money to bet :(')
            exit()
    elif player_value > 21 and dealer_value > 21:
        print('You guys both lost! This counts as a draw.')
        rerun()
    if dealer_value < 17:
        print('Dealer must draw another card since his hand is worth under 17 points.')
        dealer_cards.append(random.choice(list(card.keys())))
        dealer_value = find_value('dealer')
        if dealer_value > 21:
            total += bet
            print(
                f"Congrats! You won since the dealer's score is now {dealer_value} and your total cash is now ${total}.")
            rerun()

    while True:
        choice = input("Input 's' to stand (not choose another card) or 'h' to hit (choose another card). ")
        if choice == 's' or choice == 'h':
            break
        else:
            print('Please enter valid choice.\n')

    if choice == 's':
        if player_value > dealer_value:
            total += bet
            print(
                f"Congrats! You beat the dealer with a score of {player_value} to the dealer's score of {dealer_value}.")
            rerun()
        elif player_value == dealer_value:
            print(f"Tie! You and the dealer both had a score of {player_value}.")
            rerun()
        else:
            print(f"Sorry, you lost! You had a score of {player_value} while the dealer had a score of {dealer_value}.")
            if total - bet > 0:
                new_total = total - bet
                print(f'Oops! You lose! Bet of ${bet} take from total of ${total}. You now have ${new_total}.')
                rerun()
            else:
                print('Oops! You ran out of money to bet :(')
                exit()
            rerun()
    elif choice == 'h':
        player_cards.append(random.choice(list(card.keys())))
        player_value = find_value('player')
        if player_value > 21:
            if total - bet > 0:
                new_total = total - bet
                print(f'Oops! You lose! Bet of ${bet} take from total of ${total}. You now have ${new_total}.')
                rerun()
            else:
                print('Oops! You ran out of money to bet :(')
                exit()
        else:
            if player_value > dealer_value:
                total += bet
                print(
                    f"Congrats! You beat the dealer with a score of {player_value} to the dealer's score of {dealer_value}.")
                rerun()
            elif player_value == dealer_value:
                print(f"Tie! You and the dealer both had a score of {player_value}.")
                rerun()
            else:
                if total - bet > 0:
                    total = total - bet
                    print(
                        f"Sorry, you lost! You had a score of {player_value} while the dealer had a score of {dealer_value}.")
                    rerun()
                else:
                    print('Oops! You ran out of money to bet :(')
                    exit()




blackjack()
