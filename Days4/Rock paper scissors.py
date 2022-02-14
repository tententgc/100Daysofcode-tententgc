import random
randomNumber = random.randint(1,3)
print("rock = [1] paper = [2] scissors = [3]") 
Number = int(input("Enter a number between 1 and 3: "))    
if randomNumber == Number: 
    print("draw")
elif randomNumber == 1 and Number == 2: 
    print("player wins") 
elif randomNumber == 1 and Number == 3:
    print("computer wins")
elif randomNumber == 2 and Number == 1:
    print("computer wins")
elif randomNumber == 2 and Number == 3:
    print("player wins") 
elif randomNumber == 3 and Number == 1:
    print("player wins") 
elif randomNumber == 3 and Number == 2:
    print("computer wins") 
print(randomNumber)