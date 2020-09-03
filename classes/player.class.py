
#from hand.class.py import *
#from pair.class.py import *
#from pool.class.py import *


cardMapping = {

	1: "ACE",
	2: "TWO", 
	3: "THREE",
	4: "FOUR",
	5: "FIVE",
	6: "SIX",
	7: "SEVEN",
	8: "EIGHT",
	9: "NINE",
	10: "TEN",
	11: "JACK",
	12: "QUEEN",
	13: "KING"
}


class Player:
	
	
	
	#constructor for player object
	def __init__(self):
		#hand = Hand();
		return

	#console get players choice of card to Fish
	def RequestPickFromPlayer(self):
		print "Ask the computer for a card..."
		print " 1. {:15s} 8. {:15s}".format(cardMapping[1], cardMapping[8])
		print " 2. {:15s} 9. {:15s}".format(cardMapping[2], cardMapping[9])
		print " 3. {:15s}10. {:15s}".format(cardMapping[3], cardMapping[10])
		print " 4. {:15s}11. {:15s}".format(cardMapping[4], cardMapping[11])
		print " 5. {:15s}12. {:15s}".format(cardMapping[5], cardMapping[12])
		print " 6. {:15s}13. {:15s}".format(cardMapping[6], cardMapping[13])
		print " 7. {:15s}".format(cardMapping[7])
		card = 0;
		
		while card > 13 or card < 1:
			print "chose a number within [1-13]"
			#TODO: handle bad string input (anything alphebetic) frorm raw_input()
			inStr = raw_input(">> ")
			if inStr.isnumeric():
				card = int(inStr)
			
		
		print ("you ask the computer if it has any {}s".format(cardMapping[card]))
		
		
	#take any pairs from the hand and 
	def updateHand(self):
		return
	
	
	def replyToFish(self, request):
		#for request in hand:
			#self.hand.remove(self)
		return
	
	

john = Player()

john.RequestPickFromPlayer()
	
		