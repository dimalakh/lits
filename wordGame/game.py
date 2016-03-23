from dictionary import *
from sys import exit
import os

wordUsed = ["lam"]
scoreStorage = [0]
wordBot = dictionary
originalDict = dictionary

os.system('clear')

print('Hello it is word game. \nType word-exit to close the game. \n\nRules: \n  1.Your word must start from letter which is the last letter of previous word.\n  2.If you type used word you will lose.')


def wordSelector():
  i = -1
  while wordBot[i].startswith(inpt[-1]) == False:
    i = i -1
    if wordBot[i].startswith(inpt[-1]) == True:
      wordUsed.append(wordBot[i])
      print(wordBot[i])
      wordBot.pop(i)
      break
  
def score(wordScore):
     scoreStorage.append(len(wordScore)*10)
     return (sum(scoreStorage))



for index in range(len(wordBot)): 
  inpt = raw_input()
  
  if inpt in wordUsed:
    print('\n\n  You lose!\n  Youre score:' + str(globalScore) + '\n  This word is already used!Do you want to start new game?Y/N')
    controlInpt = raw_input()
    
    if controlInpt == 'Y':
      print('I dont know how to do it')
    else:
      exit()  


  elif inpt =='word-exit':
    exit()


  else:
    wordStorage = wordUsed[-1]

    if inpt in originalDict:
      if wordStorage.endswith(inpt[0]):
        wordUsed.append(inpt)
        wordSelector()
        globalScore = score(inpt)
      else:
        print('First letter must be '+wordStorage[-1])


    elif len(wordBot) == 0:
      print('You win!') 
      

    else:
      print('it isnt word') 
      
print('You win!') 