from black_jack import *

index = 'y'
while index != 'n':
	deck = create_deck()
	hand = deal_hand(deck)
	score = hand_score(hand)
	suit = determine_suit(hand)
	face = determine_face(hand)
	print hand
	print suit
	print face
	print_results(hand, face, suit, score)

	print "do you want to play again"
	choice = raw_input("> ")
	if choice == 'y' or choice == "yes":
		index = 'y';
	else:
		index = 'n';
