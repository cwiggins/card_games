from black_jack import *

index = 'y'
while index != 'n':
	deck = create_deck()
	print deck
	hand = deal_hand(deck)
	print hand
	score = hand_score(hand)
	suit = determine_suit(hand)
	print score
	print suit
	face = determine_face(hand)
	print face
	#print_results(hand, score, suit, face)

	print "do you want to play again"
	choice = raw_input("> ")
	if choice == 'y' or choice == "yes":
		index = 'y';
	else:
		index = 'n';
