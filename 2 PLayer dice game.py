#welcome guys to my first python programmed game for two players.hope you guys enjoy it.
import random
num=0
dice1=0
dice2=0
def gameplay():
  global num
  global dice1
  global dice2
  dice1 = dice1+random.randint(1,6)
  dice2 = dice2+random.randint(1,6)
  
  print(

  )
  print("*************")
  print("The value are:")
  print("Dice 1=",dice1,"\ndice 2=",dice2)
  
  print(

  )
  print(name1,dice1 )
  print(name2,dice2)
  
  print(
      
  )

  if dice1 == dice2:
    print("you rolled a double!")
  if dice1>dice2:
    print(name1 +' is the WINNER')
  if dice2>dice1:
    print(name2 +'is the WINNER')
  else:
    print("keep trying!")
  num=num+1
  if num<5:
    gameplay()

question= input('Are there two people to play a dice game? ')
bPlayerWantsToPlay=0
if question==('yes'):
  print('okay')
  bPlayerWantsToPlay=True
else:
  print('see you later')
  bPlayerWantsToPlay=False

if bPlayerWantsToPlay:
  question=input('Are are you ready? ')
  if question == ('no'):
    SystemExit
  else:
    print('let\'s start.. ')
  name1 =input('what is your name player1?')
  age1 =input('how old are you player1? ')
  name2 =input('what is your name player2? ')
  age2 =input('how old are you player2? ')
print()





rules =input ('THE RULES ARE: This is a 2 player dice game and there are 5 rounds the computer does it automatic for you,The score cannot go below zero, The person with the highest score wins, if each  player rolls the same score at the end of the game each person  can rool one dice. ENTER yes to continue..... ')
if question==('yes'):
 print('Here we go...')
 

roll_again ="question"

while roll_again == 'yes' or roll_again =='Y' or roll_again=='yes'or roll_again =="Y":
 print("\nRolling the dice...")

gameplay()
gameplay()
gameplay()
gameplay()
gameplay()