from art import logo
from art import vs
from replit import clear
from game_data import data
import random

def choseData():
  return data.pop(random.randrange(len(data)))

score = 0

dataa = choseData()

clear()
print(logo)

while len(data) > 0:
  aname = dataa["name"]
  adescription = dataa["description"]
  acountry = dataa["country"]
  ascore = dataa["follower_count"]

  datab = choseData()
  bname = datab["name"]
  bdescription = datab["description"]
  bcountry = datab["country"]
  bscore = datab["follower_count"]
  
  print(f"Compare A: {aname}, {adescription} from {acountry} ")
  print(vs)
  print(f"Against B: {bname}, {bdescription} from {bcountry} ")

  yourchoice = ""  
  while True:
    yourchoice = input().upper()
    if yourchoice.upper() == "A" or yourchoice.upper() == "B":
      break
    print("Please type A or B only")

  #print(yourchoice)
  if ( yourchoice == "A" and ascore < bscore ) or ( yourchoice == "B" and ascore > bscore ):
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    break
  else:
    score += 1
    clear()
    print(logo)
    print(f"You're right! Current score: {score}")
    if bscore > ascore:
      dataa = datab

