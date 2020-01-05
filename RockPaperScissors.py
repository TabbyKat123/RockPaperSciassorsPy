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
print("Print a hand")

player_name="Lilly"
player_hand=0

if validate(player_hand):
	computer_hand=1

print_hand(player_hand,player_name)
print_hand(computer_hand,"computer")

#Assign the return value of judge to the result variable

result=judge(player_hand,computer_hand)

#Print the result variable

print("result:"+result)

else:
	print("Please enter a valid number")