# I want to create a Number guessing game in which a random number will come between 1 to 100 but we have to guess that number
import random 
try:
    Consent = input("Want to play big brain number Guessing Game ? (y/n)").lower()
    shuffle = random.randint(1,100)

    while True:
        if Consent == 'y':
            print('lets choose your Number')
            guess = int(input("Guess a number : "))

            while True :
                if guess>1 and guess<100:
                    
                    if guess == shuffle :
                        print("Hurray !!! you won....")
                        print(f"You guess the exact Number : {shuffle}")
                        Consent = input("Want to try Again ? (y/n) : ").lower()

                    elif guess > shuffle:
                        print("Number you Enter is a bit too high than the number you Entered")
                        
                        try :
                            Continue = input("Want to continue trying (y/n) : ").lower()
                            if Continue == 'y':
                                guess = int(input("Guess again : "))

                            elif Continue == 'n':
                                print("Are you sure you want to Exit")
                                try:
                                    want_to_quit = input("I want to Quit :  (y/n)").lower()
                                    if want_to_quit == 'y':
                                        Consent = 'n'
                                        break 
                                    elif want_to_quit == 'n':
                                        Continue = input("Want to continue trying (y/n) : ").lower()
                                    else:
                                        print("Enter valid input")
                                        want_to_quit = input("I want to Quit :  (y/n)").lower()

                                except ValueError:
                                    print("Enter Valid Input")           
                                

                            else :
                                print("Only Enter (y/n)")
                                Continue = input("Want to continue trying (y/n) : ").lower()

                        except ValueError:
                            print("Only Enter (y/n)")



                    else :
                        print("Number you Enter is a bit too low  than the number you Entered")

                        try :
                            Continue = input("Want to continue trying (y/n) : ").lower()
                            if Continue == 'y':
                                guess = int(input("Guess again : "))

                            elif Continue == 'n':
                                print("Are you sure you want to Exit")
                                try:
                                    want_to_quit = input("I want to Quit :  (y/n)").lower()
                                    if want_to_quit == 'y':                                 
                                        Consent = 'n'
                                        break 
                                    elif want_to_quit == 'n':
                                        Continue = input("Want to continue trying (y/n) : ").lower()
                                    else:
                                        print("Enter valid input")
                                        want_to_quit = input("I want to Quit :  (y/n)").lower()

                                except ValueError:
                                    print("Enter Valid Input")
                                

                            else :
                                print("Only Enter (y/n)")
                                Continue = input("Want to continue trying (y/n) : ").lower()

                        except ValueError:
                            print("Only Enter = (y/n)")

                        

                else:
                    print("pls Enter between 1 to 100")
                    guess = int(input("Guess a number : ")) 
                    

        elif Consent == 'n':
            print("Thanks for Visiting")
            break
        else:
            print("Enter Valid input")
            Consent = input("Want to play a game ? (y/n)").lower()

except ValueError:
    print("Enter a valid input")
    

