#Blackjack is a game thats goals to add up the card without going above 21. once its gone over 21, its a bust

#ace counts as 11
#One can decide the count of ace
#there are two players , 1. Dealer , 2.Player

#===============++=================#

#the deck is unlimited in size 
#there is no joker
##jack queen king counts 10
import random
import math


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

                                      
     

cards = [11, 2 ,3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10 , 10]
blackjack = 11 + 10
user_cards = random.sample(cards , 2)
dealers_cards = random.sample(cards , 2)
# sum of cards
user_sum = sum(user_cards[:2])
dealers_sum = sum(dealers_cards[:2])
game_over = False



while not game_over :
    print(logo)
    print(f'Your cards: {user_cards} , current score: {user_sum}')
    print(f'Computers first card: {dealers_cards[0]}')
    if dealers_cards == blackjack:
        print("Computer wins as he has Blackjack cards")
        game_over = True
    elif user_sum == blackjack:
        print("Player wins as he has Blackjack cards")
        game_over = True
    else:
        
        withdraw = input("Type 'y' to get another card, type 'n' to pass: ")
        if withdraw == 'y':
            user_cards.append(random.choice(cards))
            user_sum = sum(user_cards[:3])
        else:
            game_over = True
print(f"Your final hand : {user_cards}, finl score: {user_sum}")
print(f"Conputers final hand : {dealers_cards}, finl score: {dealers_sum}")

if dealers_sum > user_sum:
    print("Computer wins :)")
elif dealers_sum < user_sum:
    print("You win :)")
else:
    print("Draw")
