import random



print("Hi, welcome to Escape from Europe!")
print("The black plague has consumed most of europe, and you need to escape.")
print("With a horse and a canteen, you need to escape the continent.")
print("Survive your journey and outrun the plague.")
print()

# Variables
fatigue = 0
onfoot = 0
milesTraveled = 0
thirst = 0
horseFatigue = 0
plagueTraveled = -20
canteen = 2
merchant = 0
done = False

# Start main loop
while not done:
    plagueBehind = milesTraveled - plagueTraveled
    fullSpeed = random.randrange(12,17)
    moderateSpeed = random.randrange(5, 10)
    walkFullSpeed = random.randrange(4,9)
    walkModerateSpeed = random.randrange(2,6)

    print("A. Drink from your canteen.")
    print("B. Ahead at moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Stop at a nearby town for resources.")
    print("F. Status check")
    print("Q. Quit.")
    print()

    userInput = raw_input("Your choice? ")

    if userInput.lower() == "q":
        done = True

    # Status
    elif userInput.lower() == "f":
        print("Miles traveled:", milesTraveled)
        print("Drinks in canteen:", canteen)
        print("Your camel has", horseFatigue, "amount of fatigue.")
        print("The plague is", plagueBehind, "miles behind you.")
    
    # Horse actions
    if not onfoot:
        if userInput.lower() == "d":
            horseFatigue = horseFatigue - 6
            print("Your horse feels refreshed and happy. His fatigue is now", horseFatigue)
            plagueTraveled += random.randrange(6, 14)
    
        elif userInput.lower() == "c":
            print("You traveled ", fullSpeed, "miles!")
            milesTraveled += fullSpeed
            thirst += 1
            horseFatigue += random.randrange(2, 4)
            plagueTraveled += random.randrange(7, 14)
            merchant = random.randrange(5, 10)

         # Move moderate speed
        elif userInput.lower() == "b":
            print("You traveled" , moderateSpeed, "miles!")
            milesTraveled += moderateSpeed
            thirst += 1
            horseFatigue += 1
            plagueTraveled += random.randrange(7, 15)
            merchant = random.randrange(3, 10)
        elif userInput.lower() == "e":
            horseFatigue = horseFatigue - 3
            canteen = canteen + 1
            print "You stop at a town on the way to Asia. You partially refill your canteen and your horse gets some rest."
            print "Your canteen is now", canteen,
            print "and your horses fatigue is", horseFatigue,
            plagueTraveled += random.randrange(4,11)    
            
    if onfoot:
        if userInput.lower() == "d":
            fatigue = fatigue - 3
            print("You stayed at an in and got some rest. Your fatigue is now", fatigue)
            plagueTraveled += random.randrange (5,13)
        if userInput.lower() == "c":
            print("You traveled" , walkFullSpeed, "miles!")
            plagueTraveled += random.randrange(7,15)
            milesTraveled += walkFullSpeed
            fatigue += 2
        if userInput.lower() == "b":
            print("You traveled" ) , walkModerateSpeed, "miles!"
            fatigue += 1
        if userInput.lower() == "e":
            horseFatigue = horseFatigue - 3
            canteen = canteen + 1
            print "You stop at a town on the way to Asia. You partially refill your canteen and you get some rest"
            print "Your canteen is now", canteen,
            print "and your fatigue is", fatigue,
            plagueTraveled += random.randrange(4,11)
            
    # Drink canteen
    if userInput.lower() == "a":
        if canteen == 0:
            print("You're out of water.")
        else:
            canteen -= 1
            thirst *= 0
            print("You have" , canteen, "drinks left and you are no longer thirsty.")

    # Not done check
    if merchant == 10:
        horseFatigue *= horseFatigue - 2
        thirst *= 0
        canteen = 3
        print("You found a traveling merchant! He sells you some food and water, you filled your canteen and the horse is partially refreshed.")

    if plagueBehind <= 15:
        print("The plague is drawing near!")

    if milesTraveled >= 250 and not done:
        print("Asia welcomes you with open arms. You win!")
        done = True

    if plagueTraveled >= milesTraveled:
        print("You were infected by the plague.")
        print("You're dead!")
        done = True

    if thirst > 4 and thirst <= 6 and not done:
        print("You are thirsty")

    if thirst > 6:
        print("You died of dehydration!")
        done = True
        
    if horseFatigue < 0:
        horseFatigue = horseFatigue - horseFatigue * 2

    if horseFatigue > 5 and horseFatigue <= 8 and not done:
        print("Your horse is getting tired.")

    if horseFatigue > 8:
        print("Your horse is dead. You are now on foot.")
        onfoot = 1
    if fatigue < 5 and fatigue > 3:
        print"You are getting tired"
        
    if fatigue > 5:
        print("You died of exhaustion.")
        done = 1