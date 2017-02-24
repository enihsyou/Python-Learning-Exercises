# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score_p = 0
score_d = 0


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []	# create Hand object

    def __str__(self):
        strs = ""
        for i in self.cards:
            strs += str(i)
            strs += " "
 
        return "Hand contains " + strs.strip()	# return a string representation of a hand

    def add_card(self, card):
        self.cards.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        As = 0
        for i in self.cards:
            if 'A' in i.get_rank():
                As += 1
        
        if As == 1:
            sum = 0
            for i in self.cards:
                sum += VALUES[i.get_rank()]
            if sum + 10 <= 21:
                return sum + 10
            else:
                return sum
        else:
            sum = 0
            for i in self.cards:
                sum += VALUES[i.get_rank()]
            return sum
        
   
    def draw(self, canvas, pos, r = 1):
        for inde,item in enumerate(self.cards):
            item.draw(canvas, (pos[0] + 80 * inde * r, pos[1]))
        
# define deck class 
class Deck:
    def __init__(self):
        self.decks = [Card(suit,rank) for suit in SUITS for rank in RANKS]# create a Deck object

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.decks)    # use random.shuffle()

    def deal_card(self):
        return random.choice(self.decks)	# deal a card object from the deck
    
    def __str__(self):
        strs = ""
        for i in self.decks:
            strs += str(i)
            if i != self.decks[-1]:
                strs += " "
        return "Deck contains " + strs	# return a string representing the deck

player = Hand()
dealer = Hand()
deck = Deck()

#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, score_d
    if not in_play:
        newdeal.stop()
        changeback.stop()
        outcome = "Hit or stand?".center(20)

        player = Hand()
        dealer = Hand()
        deck = Deck()
        deck.shuffle()
        in_play = True
        for i in range(2):
            player.add_card(deck.deal_card())
            dealer.add_card(deck.deal_card())
    else:
        outcome = "Dealer Win".center(20)
        score_d += 1
        in_play = False
        

def hit():
    global in_play, outcome, score_p
    
    while in_play:
        outcome = "Hit or stand?".center(20)
        
        player.add_card(deck.deal_card())
        if player.get_value() <= 21:
            break
        else:
            outcome = "Player BUSTED".center(20)
            in_play = False
            score_p += 1
            newdeal.start()
            changeback.start()
            break
            
def stand():
    global outcome, in_play, score_p, score_d
    
    if in_play:
        outcome = "STAND".center(20)    
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
            if dealer.get_value() > 21:
                outcome = "Dealer BUSTED".center(20)
                in_play = False
                score_p += 1
                newdeal.start()
                changeback.start()
                break
        in_play = False
        if player.get_value() <= 21 and dealer.get_value() <= 21:
            if player.get_value() <= dealer.get_value():
                outcome =  "Dealer wins".center(20)
                score_d += 1
                #print player.get_value(), dealer.get_value()
            else:
                outcome =  "Player wins".center(20)
                score_p += 1
                #print player.get_value(), dealer.get_value()
            newdeal.start()
            changeback.start()

# draw handler
outcome_ori = outcome

def change_back():
    global outcome
    outcome = outcome_ori
    newdeal.start()
    changeback.stop()
    
def NewDeal():
    global outcome, outcome_ori
    outcome_ori = outcome
    outcome = "New deal?".center(20)
    newdeal.stop()
    changeback.start()
    
newdeal = simplegui.create_timer(1500, NewDeal)
changeback = simplegui.create_timer(1500, change_back)


#draw
def draw(canvas):
    player.draw(canvas, (40, 60))
    dealer.draw(canvas, (460, 440), -1)
    canvas.draw_text(outcome, (120, 300), 46, "White")
    canvas.draw_text("Blackjack", (520, 30), 16, "White") 
    canvas.draw_text("Player", (30, 50) , 20, "White")
    canvas.draw_text("Dealer", (430, 560), 20, "White")
    if in_play:
        canvas.draw_image(card_back, CARD_CENTER , CARD_SIZE, (496,488), CARD_SIZE)

    canvas.draw_text(str(score_p).center(3), (90, 50), 30, "White")
    canvas.draw_text(str(score_d).center(3), (490, 560), 30, "White")    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric