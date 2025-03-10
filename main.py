# Kerolos Amgad
import random

# List of cards :
card_categories=['Hearts','Diamonds','Clubs','Spades']
card_list=['Ace','2','3','4','5','6','7','8','9','10','King','Queen','Jack']

#------------------------------------------------------------------------------------------------------

#the function of card value :
def card_value (card):
    """
    the function card_value, i used to return the values
    of the Cards ,like King, Queen , jack & Ace

    """
    if card[0] in ['King','Queen','Jack']:
        return 10
    elif card[0] =='Ace':
        return 11
    else:
        return int(card[0])
#--------------------------------------------------------------------------------------------------------

# the outer loop
while True :

    deck=[(card,category) for card in card_list for category in card_categories] #form the deck of cards

    random.shuffle(deck) #Shuffle the deck
    player_cards=[deck.pop(),deck.pop()]    # Deal 2 cards to player
    dealer_cards=[deck.pop(),deck.pop()]    # Deal 2 cards to dealer

    # the inner loop
    while True:
        player_score=sum(card_value(card) for card in player_cards)     # summing the total score of player
        dealer_score=sum(card_value(card) for card in dealer_cards)     # summing the total score of dealer
        print("Cards player has : ",player_cards)
        print("Score of  the player : ",player_score)
        print("\n")
        choice = input('What do you want? ["play" to request another card, "stop" to stop]: ').lower()  # the decision of player

        if choice=="play":
            new_card=deck.pop()
            player_cards.append(new_card)
            player_score+=card_value(new_card)

        elif choice=="stop":
            break

        else:
            print("Invalid input , please try again :) ")
            continue

        # the first possibitiy
        if player_score>21 :
            print("Cards dealer has : ",dealer_cards)
            print("Score of the dealer has : ",dealer_score)
            print("Cards player has : ",player_cards)
            print("Score of the player has : ",player_score)
            print("Dealer wins (Player Loss Because Player Score is exceeding 21)")
            break

    # the loop control the decision of dealer
    while dealer_score<17 :
        new_card =deck.pop()
        dealer_cards.append(new_card)
        dealer_score+=card_value(new_card)



    print("Cards dealer has : ",dealer_cards)
    print("Score of the dealer has : ",dealer_score)
    print("\n")



    # the Second possibility
    if player_score>dealer_score:
        print("Cards dealer has : ", dealer_cards)
        print("Score of the dealer has : ", dealer_score)
        print("Cards player has : ", player_cards)
        print("Score of the player has : ", player_score)
        print("Player wins (Player Has High Score than Dealer)")
    # the Third possibility
    elif dealer_score>player_score:
        print("Cards dealer has : ", dealer_cards)
        print("Score of the dealer has : ", dealer_score)
        print("Cards player has : ", player_cards)
        print("Score of the player has : ", player_score)
        print("Dealer wins (Dealer Has High Score than Player )")
    # the Fourth possibility
    else :
        print("Cards dealer has : ", dealer_cards)
        print("Score of the dealer has : ", dealer_score)
        print("Cards player has : ", player_cards)
        print("Score of the player has : ", player_score)
        print("It's a draw.")

    print("\n")
    choice_player=input('Do you want to play again? ["yes" to continue, "no" to quit]: ').lower() #the decision of player

    if choice_player=="no":
        print("Thanks for playing! Goodbye!")
        break
    elif choice_player=="yes":
        print('\n'*20 )


