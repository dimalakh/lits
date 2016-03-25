from dictionary import *
from sys import exit
import time
import random
import os

def wordSelector():
  i = -1
  while wordBot[i].startswith(inpt[-1]) == False:
    i = i -1
    if wordBot[i].startswith(inpt[-1]) == True:
      wordUsed.append(wordBot[i])
      print(wordBot[i])
      wordBot.pop(i)
      break

def countrySelector():
  selectedCountry = random.choice(wordBot)  
  if selectedCountry in wordUsed:
    countrySelector()
  else:
      wordUsed.append(selectedCountry)
      print(selectedCountry)
  
def score(wordScore):
  scoreStorage.append(len(wordScore)*10)
  return (sum(scoreStorage))

def header():
  os.system('clear') 
  print(gameName.upper()+'''             Type Q to close the game.\n___________________________________________________________________________''')



def endGame():
  print('''\n  ____________________________________
    \n   You lose!                         
    \n   Youre score:''' + str(globalScore) + '''         
    \n   Do you want to start new game?Y/N 
    \n  ____________________________________''')
  controlInpt = raw_input()
  if controlInpt == 'Y' or controlInpt == 'y':
    execfile('game.py')
  else:
    exit()     

os.system('clear')

print('''Hello it is word game.
 \n\nChoose game type:
 \n Press 1 - to play simple words game\n ______________________________
 \n Press 2 - to play countries game\n ______________________________
 \n Press 3 - to play cities game\n ______________________________
 \n Press 4 - to play rivers game\n ______________________________''')

endCounter = 0
menuInpt = raw_input()

if menuInpt == '2':
  wordUsed = ["a"]
  gameName = 'Countries'
  scoreStorage = [0]
  wordBot = countriesDict
  originalDict = countriesDict

  os.system('clear')
  print('''Rules: \n1.Type random name of country.\n2.If you type used country name  you will lose.\n\nWait 10 seconds.''')
  time.sleep(10)
  os.system('clear')
  header()

  for index in range(len(wordBot)): 
      inpt = raw_input()
      
      if inpt in wordUsed:
        endGame()
      elif inpt =='q' or inpt =='Q':
        exit()
      elif inpt == 'a' or inpt =='A':
        countryAdvice()  
      else:
        if inpt in originalDict:
            wordUsed.append(inpt)
            countrySelector()
            globalScore = score(inpt)
        elif len(wordBot) == 0:
          print('You win!') 
        else:
          print('it isnt word')    
          endCounter = endCounter + 1
          if endCounter > 5:
            endGame()

  print('You win!') 


elif menuInpt == '3':
  gameName = 'Cities'
  wordUsed = ["a"]
  scoreStorage = [0]
  wordBot = dictionary
  originalDict = dictionary 
elif menuInpt == '4':
  gameName = 'Rivers'
  wordUsed = ["a"]
  scoreStorage = [0]
  wordBot = dictionary
  originalDict = dictionary 
else:
  wordUsed = ["a"]
  gameName = 'Words'
  scoreStorage = [0]
  wordBot = dictionary
  originalDict = dictionary 

  os.system('clear')
  print('''Rules: \n1.Your word must start from letter which is the last letter of previous word.\n2.If you type used word you will lose.\n\nWait 10 seconds.''')
  time.sleep(10)
  os.system('clear')
  header()

  for index in range(len(wordBot)): 
    inpt = raw_input()
    
    if inpt in wordUsed:
      endGame()  
    elif inpt =='q' or inpt =='Q':
      exit()
    else:
      wordStorage = wordUsed[-1]
      if inpt in originalDict:
        if wordStorage.endswith(inpt[0]) and len(wordUsed)>1:
          wordUsed.append(inpt)
          wordSelector()
          globalScore = score(inpt)
        elif len(wordUsed)==1:
          wordUsed.append(inpt)
          wordSelector()
          globalScore = score(inpt)
        else:
          print('First letter must be '+wordStorage[-1])
      elif len(wordBot) == 0:
        print('You win!') 
      else:
        print('it isnt word') 
        endCounter = endCounter + 1
        if endCounter > 5:
          endGame()

  print('You win!') 








