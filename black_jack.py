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


def deal_card(deck):
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

def deal_hand(deck):
	index = 1
	hand = array.array('i', [deal_card(deck)])
	while index < 2:
		hand.append(deal_card(deck))
		index += 1
	return hand;

def hand_score(hand):
	score = array.array('i', [get_value(hand[0])])
	index = 1
	while index < 2:
		score.append(get_value(hand[index]))
		index += 1
	return score;

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



def determine_suit(hand):
	suit = []
	index = 0
	while index < 2:
		if hand[index] >= 1 and hand[index] <= 13:
			suit.append("Hearts")
			index += 1
		elif hand[index] >= 14 and hand[index] <= 26:
			suit.append("Clubs")
			index += 1
		elif hand[index] >= 27 and hand[index] <= 39:
			suit.append("Spades")
			index += 1
		else:
			suit.append("Diamonds")
			index += 1
	return suit;

def determine_face(hand):
	face = []
	index = 0
	while index < 2:
		card = hand[index] % 13
		if card == 0 or card == 10 or card == 11 or card == 12:
			if card == 0:
				face.append("Ace")
				index += 1
			elif card == 10:
				face.append("Jack")
				index += 1
			elif card == 11:
				face.append("Queen")
				index += 1
			else:
				face.append("King")
				index += 1
		else:
			face.append(card + 1)
			index += 1
	return face;

