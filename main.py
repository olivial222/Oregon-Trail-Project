## Oregon Trail
# Author: Abhay B. Joshi
# Unit 3 Project starter code

import random

### Global constants
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]

### Global variables
userHealth = 5
healthCounter = 2
availableFood = 500
currentDay = 1
currentMonth = 3
milesToGo = 2000
gameOver = False

# The main program loop
def main():
    global currentDay, currentMonth, userHealth, availableFood, milesToGo, healthCounter, gameOver

    print( "Welcome to the game of Oregon Trail." )
    print( "You are expected to reach Oregon City, Oregon from Independence, Missouri before 31st December." )
    while (gameOver == False):
        # Get user command and call appropriate function
      command = input( "What do you want to do next? " )
      if (command == 'travel'): 
        commandTravel()
        endCondition()
      elif (command == 'rest'): 
        commandRest()
        endCondition()
      elif (command == 'hunt'): 
        commandHunt()
        endCondition()
      elif (command == 'quit'): 
        commandQuit()
      elif (command == 'help'): 
        commandHelp()
      elif (command == 'status'): 
        commandStatus()
      else: print("please enter a valid command, type help for commands.")


# Purpose: Spend a few days. The player eats 5lbs of food a day. The players health
# will decrease twice each month.
# Input: # of days spent
# Output: None
def addDays():
    global currentDay, currentMonth, userHealth, availableFood, milesToGo, healthCounter
    currentDay = currentDay + 1
    availableFood = availableFood - 5
    if currentDay > 31 and currentMonth in MONTHS_WITH_31_DAYS:
      currentMonth = currentMonth + 1
      currentDay = 1
      if healthCounter > 0:
        print(f"Month has changed. Reducing health by {healthCounter}")
        userHealth = userHealth - healthCounter
      healthCounter = 2
    if currentDay > 30 and currentMonth not in MONTHS_WITH_31_DAYS:
      currentMonth = currentMonth +1
      currentDay = 1
      if healthCounter > 0:
        print(f"Month has changed. Reducing health by {healthCounter}")
        userHealth = userHealth - healthCounter
      healthCounter = 2
    changeHealth = random.randint(0,1)
    if changeHealth == 0 and healthCounter > 0:
      userHealth = userHealth - 1
      healthCounter = healthCounter - 1
      print("reducing health by 1")


#### Functions for each game command
def commandTravel():
    global currentDay, currentMonth, userHealth, availableFood, milesToGo, healthCounter
    miles = random.randint(30,60)
    daysTaken = random.randint(3,7)
    print(f"you are travelling {miles} miles. This will take {daysTaken} days.")
    milesToGo = milesToGo - miles
    for x in range(daysTaken): addDays()
#end commandTravel


## NEED CONTRACT
# Purpose:  increases health 1 level (up to 5 maximum) and takes 2-5 days (random)
def commandRest():
    global currentDay, currentMonth, userHealth, availableFood, milesToGo, healthCounter
    if userHealth > 4:
      print("you are already at full health.")
    else:
      daysTaken = random.randint(2,5)
      print(f'you have rested and gained 1 health point. this took {daysTaken} days.')
      userHealth = userHealth + 1
      for x in range(daysTaken): addDays()
#end commandRest


## NEED CONTRACT
# Purpose: adds 100lbs of food and takes 2-5 days (random)
def commandHunt():
    global currentDay, currentMonth, userHealth, availableFood, milesToGo, healthCounter
    daysTaken = random.randint(2,5)
    print(f'added 100lbs of food, this will take {daysTaken} days.')
    availableFood = availableFood + 100
    for x in range(daysTaken): addDays()
#end commandHunt


## NEED CONTRACT
# Purpose: Display status of the trip
def commandStatus():
    global currentDay, currentMonth, userHealth, availableFood, milesToGo, healthCounter
    print(f"The date is {currentMonth}/{currentDay}. Your health is {userHealth}/5. You have {availableFood}lbs of food left and {milesToGo} miles to go.")
#end commandStatus

## NEED CONTRACT
# Purpose: Display instructions
def commandHelp():
    global currentDay, currentMonth, userHealth, availableFood, milesToGo, healthCounter
    print("Valid commands")
    print("travel - Travel 30 to 60 Miles, takes 3-7 days")
    print("rest - Heals you one health point, takes 2-5 days")
    print("hunt - Adds 100lbs of food, takes 2-5 days")
    print("status - Displays your current stats")
    print("help - Displays valid commands")
    print("quit - Quits the game")
#end commandHelp

## NEED CONTRACT
# Purpose: Quit the game
def commandQuit():
    global currentDay, currentMonth, userHealth, availableFood, milesToGo, healthCounter, gameOver
    print("Thanks for playing, see you next time!")
    gameOver = True
#end commandQuit
def endCondition():
    global currentDay, currentMonth, userHealth, availableFood, milesToGo, healthCounter, gameOver
    if currentMonth > 12:
      print("It's past december, you have lost.")
      gameOver = True
    elif availableFood < 1:
      print("You have no more food left, you have lost.")
      gameOver = True
    elif userHealth < 1:
      print("Your health is bad, you have lost")
      gameOver = True
    elif milesToGo < 1:
      print("You have reached the destination, you have won!")
      gameOver = True
main()
