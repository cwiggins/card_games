import random
import math
import array

def create_deck():
	deck = array.array('i',[int(math.floor(random.random()*52+1))])
	index = 1
	while index < 52:
		card = int(math.floor(random.random()*52+1))
		if check_deck(card,deck, index) == False:
			deck.append(card);
			index += 1;
		else:
			index = index;
	return deck;

def check_deck(card, deck, pindex):
	index = 0
	ce = False
	while index <= pindex-1 and ce == False:
		if card != deck[index]:
			ce = False
			index += 1;
		else:
			ce = True
	return ce;


def deal_hand(deck):
	index = 0
	dealt_card = 0
	if deck[0] == 0:
		while index < 52:
			if deck[index] != 0:
				dealt_card = deck[index]
				deck[index] = 0
				break;
			else:
				index += 1
	else:
		dealt_card = deck[0];
		deck[0] = 0
	return dealt_card;

def hand_score(card):
	return get_value(card);

def get_value(card):
	real_value = card % 13
	value = 0
	if real_value == 0 or real_value == 10 or real_value == 11 or real_value == 12:
		if real_value == 0:
			value = 1;
		else:
			value = 10;
	else:
		value = real_value+1;
	return value;



def determine_suit(card):
	suit = ""
	if card >= 1 and card <= 13:
		suit = "Hearts"
	elif card >= 14 and card <=26:
		suit = "Spades"
	elif card >= 27 and card <= 39:
		suit = "Clubs"
	else:
		suit = "Diamonds"
	return suit;

def determine_face(card):
	face = card % 13
	if face == 0 or face == 10 or face == 11 or face == 12:
		if face == 0:
			return "Ace";
		elif face == 10:
			return "Jack";
		elif face == 11:
			return "Queen";
		else:
			return "King";
	else:
		return face + 1;

deck = create_deck()
print deck
index = 'y'
while index != 'n':
	card_1 = deal_hand(deck)
	card_2 = deal_hand(deck)
	print card_1, card_2
	card_1_score = hand_score(card_1)
	card_2_score = hand_score(card_2)
	card_1_suit = determine_suit(card_1)
	card_2_suit = determine_suit(card_2)
	card_1_face = determine_face(card_1)
	card_2_face = determine_face(card_2)
	print card_1_face, card_2_face
	print "score is:",card_1_score + card_2_score
	print "With a:", card_1_face, "of", card_1_suit
	print "And", card_2_face, "of", card_2_suit

	print "do you want to play again"
	choice = raw_input("> ")
	if choice == 'y' or choice == "yes":
		index = 'y';
	else:
		index = 'n';
