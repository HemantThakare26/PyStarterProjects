import random

choice = input("Want to Try Your luck ? (y/n)").lower()

while True:
    if choice == 'y':
        die1 = random.randint(1,10)
        luck = int(input("Enter the number you think will come Between 1 to 10 : ")) 
        while luck < 1 or luck >10:
            print("Incorrect input....\npls...Choose number Between 1 to 10")
            luck = int(input("Enter the number you think will come :")) 
        if luck == die1 :
            print("You won jackpot ! Hurray......")
            print(f'Number you Got = {die1},  Number you Choose = {luck}')
        else:
            print("Ohh Bad Luck Try Again ....")
            print(f'Number you Got = {die1}, Number you Choose = {luck}')
        choice = input("Want to play again ?(y/n)").lower()
    elif choice == 'n':
        print("Thanks for playing")
        break
    else:
        print("Invalid Input")
        choice = input("Want to try your luck ? (y/n)").lower()
