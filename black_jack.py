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

