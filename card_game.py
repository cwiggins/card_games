from black_jack import *

index = 'y'
while index != 'n':
	deck = create_deck()
	#print deck
	card_1 = deal_hand(deck)
	card_2 = deal_hand(deck)
	#print card_1, card_2
	card_1_score = hand_score(card_1)
	card_2_score = hand_score(card_2)
	card_1_suit = determine_suit(card_1)
	card_2_suit = determine_suit(card_2)
	card_1_face = determine_face(card_1)
	card_2_face = determine_face(card_2)
	#print card_1_face, card_2_face
	print "score is:",card_1_score + card_2_score
	print "With a:", card_1_face, "of", card_1_suit
	print "And", card_2_face, "of", card_2_suit

	print "do you want to play again"
	choice = raw_input("> ")
	if choice == 'y' or choice == "yes":
		index = 'y';
	else:
		index = 'n';
