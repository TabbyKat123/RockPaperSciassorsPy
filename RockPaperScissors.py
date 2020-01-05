def validate(hand):
	if hand<0 or hand>2:
		return False
	return True

def print_hand(hand,name):
	hands=["Rock"+"Paper"+"Scissors"]
	print(name+"picked:"+hands[hand])

#define the judge function
def judge(player,computer):
#Add control flow based on the comparison player aand computer

if player==computer:
	return "Draw"
elif player==0 and computer==1:
	return "Lose"
elif player==1 and computer==2:
	return"Lose"
elif player==2 and computer==0:
	return"Lose"
else:
	return"Win"

print("Starting the rock Paper Scissors game!")