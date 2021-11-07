#Python Blackjack Program

import random, sys, time

uservalue = 0
bankvalue = 0
cardcount = 0
bankcardcount = 0
cash = 0

def banner():
    print("************************************** ")
    time.sleep(1)
    print("Welcome to the Ollies Blackjack Game ")
    time.sleep(1)
    print("************************************** ")
    time.sleep(1)
    print("                                        ")
    print("The aim of the game is to score 21 ")
    time.sleep(1.5)
    print("Another way to win is by out scoring the banker (Below 21) ")
    time.sleep(1.5)
    print("Also if you can get a total of 5 cards without exceeding 21 you can win, unless the banker gets 21 ")
    time.sleep(1)
    print("                                                  ")
    choice = input("Press any key to continue... ")
    play()

def play():
    print(" ")
    choice = input("Press P to play or C to quit ")
    if choice == "p" or choice == "P":
        user()
    else:
        print(" ")
        print("Your current balance is %s" % cash)
        sys.exit()


def user():
    global uservalue
    global cardcount
    clubs = [2,3,4,5,6,7,8,9,"Jack ","Queen ","King ","Ace "]
    hearts = [2,3,4,5,6,7,8,9,"Jack ","Queen ","King ","Ace "]
    spades = [2,3,4,5,6,7,8,9,"Jack ","Queen ","King ","Ace "]
    diamonds = [2,3,4,5,6,7,8,9,"Jack ","Queen ","King ","Ace "]
    deck1 = clubs+hearts+spades+diamonds
    random.shuffle(deck1)
    userhand = (deck1[0],deck1[1])
    uservalue1 = deck1[0]
    if uservalue == "Jack " or uservalue1 == "Queen " or uservalue1 == "King ":
        uservalue1 = 10
    elif uservalue1 == "Ace ":
        uservalue1 = 11
    else:
        uservalue1 = uservalue1

    uservalue2 = deck1[1]
    if uservalue2 == "Jack " or uservalue2 == "Queen " or uservalue2 == "King ":
        uservalue2 = 10
    elif uservalue2 == "Ace ":
        uservalue2 = 11
    else:
        uservalue1 = uservalue1

    uservalue = uservalue1 + uservalue2
    if uservalue == 22:
        uservale = 12
    else:
        uservalue = uservalue

        print("Your cards are.... ")
        print(userhand)
        print("The value of your hand is .... ")
        print(uservalue)
        choice = input("Press T to twist or any other key to stick... ")
    if choice == "T" or choice == "t":
        print("You have chosen to twist ")
        uservalue3 = deck1[2]
        print("Your next card is... ")
        print(deck1[2])
        if uservalue3 == "Jack " or uservalue3 == "Queen " or uservalue3 == "King ":
            uservalue3 = 10
        elif uservalue3 == "Ace ":
            if uservalue <=10:
                uservalue3 = 11
            else:
                uservalue3 = 1
        else:
            uservalue3 = uservalue3
            uservalue = uservalue + uservalue3
            userhand = (deck1[0],deck1[1],deck1[2])
            print("Your cards are.... ")
            print(userhand)
            print("The value of your hand is %s.. " %uservalue)
            if uservalue > 21:
                    print("Bust... You Lose ")
            elif uservalue == 21:
                print("21, You Win! ")
            else:
                choice = input("Press T to twist or any other key to stick... ")
                if choice == "T":
                        print("You have chosen to twist ")
                        uservalue4 = deck1[3]
                        print("Your next card is... ")
                        print(deck1[3])
                        if uservalue4 == "Jack " or uservalue4 == "Queen " or uservalue4 == "King ":
                            uservalue4 = 10
                        elif uservalue4 == "Ace ":
                            if uservalue4 <= 10:
                                uservalue4 = 11
                            else:
                                uservalue4 = 1

                        else:
                            uservalue4 = uservalue4
                        uservalue = uservalue + uservalue4
                        userhand = (deck1[0],deck1[1],deck1[2],deck1[3])
                        print("Your cards are.... ")
                        print(userhand)
                        print("The value of your hand is %s.. " % uservalue)
                        if uservalue > 21:
                            print("Bust... You Lose ")
                        elif uservalue == 21:
                                print("21... You Win!")
                        else:
                            choice = input("Press T to twist or any other key to stick.... ")
                            if choice == "T":
                                print("You have chosen to twist ")
                                uservalue5 = deck1[4]
                                print("Your next card is... ")
                                print(deck1[4])
                                if uservalue5 == "Jack " or uservalue5 == "Queen " or uservalue5 == "King ":
                                    uservalue5 = 10
                                elif uservalue5 == "Ace ":
                                    if uservalue <= 10:
                                        uservalue5 = 11
                                    else:
                                        uservalue5 = 1

                                else:
                                    uservalue5 =  uservalue5
                                uservalue = uservalue + uservalue5
                                userhand = (deck1[0],deck1[1],deck1[2],deck[3],deck1[4])
                                print("Your cards are.... ")
                                print(userhand)
                                print("The value of your hand is %s.." % uservalue)
                                if uservalue > 21:
                                    print("Bust.. You Lose ")
                                elif uservalue == 21:
                                    print("21... You Win! ")
                                else:
                                    print("5 card trick... You Win! ")
                                    cardcount = 5

                            else:
                                print("You have chosen to stick ")
                                print("The value of your hand is... ")
                                print(uservalue)

                else:
                    print("You have chosen to stick ")
                    print("The value of your hand is... ")
                    print(uservalue)

    else:
        print("You have chosen to stick ")
        print("The value of your hand is %s..." % uservalue)
    print(" ")
    bank()
    return uservalue, cardcount

def bank():
    global bankvalue
    global bankcardaccount
    clubs = [2,3,4,5,6,7,8,9,"Jack ","Queen ","King ","Ace "]
    hearts = [2,3,4,5,6,7,8,9,"Jack ","Queen ","King ","Ace "]
    spades = [2,3,4,5,6,7,8,9,"Jack ","Queen ","King ","Ace "]
    diamonds = [2,3,4,5,6,7,8,9,"Jack ","Queen ","King ","Ace "]
    deck1 = clubs+hearts+spades+diamonds
    random.shuffle(deck1)
    userhand = (deck1[0],deck1[1])
    uservalue1 = deck1[0]
    if uservalue1 == "Jack " or uservalue1 == "Queen " or uservalue1 == "King ":
        uservalue1 = 10
    elif uservalue1 == "Ace ":
        uservalue1 = 11
    else:
        uservalue1 = uservalue1

    uservalue2 = deck1[1]
    if uservalue2 == "Jack " or uservalue2 == "Queen " or uservalue2 == "King ":
        uservalue2 = 10
    elif uservalue2 == "Ace ":
        uservalue2 = 11
    else:
        uservalue1 = uservalue1

    uservalue = uservalue1 + uservalue2
    if uservalue == 22:
        uservalue = 12
    else:
        uservalue = uservalue

    bankvalue = uservalue

    if bankvalue < 15:
        uservalue3 = deck1[2]
        bankvalue = bankvalue + uservalue3
        userhand = (deck1[0],deck1[1],deck1[2])
        print(userhand)
        if bankvalue < 15:
            uservalue4 = deck1[3]
            bankvalue = bankvalue + uservalue5
            userhand = (deck1[0],deck1[1],deck1[2],deck1[3],deck1[4])
            bankcardcount = 5
            print(userhand)
            if bankvalue < 15:
                uservalue5 = deck[4]
                bankvalue = bankvalue + uservalue5
                userhand = (deck1[0],deck1[1],deck1[2],deck1[3],deck1[4])
                bankcardcount = 5
                print(userhand)
                print("5 card trick... Bank Wins ")
            else:
                bankvalue = bankvalue
        else:
            bankvalue = bankvalue

    else:
        bankvalue = bankvalue

    print("The Bank's cards are... ")
    print(userhand)
    print("The value of the Bank's hand is %s" % bankvalue)
    compare()
    return bankvalue, bankcardcount

def compare():
    print(" ")
    global bankvalue
    global uservalue
    global cash
    global bankcardcount
    if bankcardcount == 5:
        print("Banks Wins - You lose £50 ")
        cash = cash - 50
    elif cardcount == 5:
        print("You win £225 ")
        cash = cash + 225
    elif uservalue > 21:
        print("Bank wins - You lose £25 ")
        cash = cash - 25
    elif uservalue == 21:
        print("You win £300 ")
        cash = cash + 300
    elif uservalue > bankvalue:
        print("You win £50 ")
        cash = cash + 50
    elif uservalue == bankvalue:
        print("Draw - You get your money back ")
        cash = cash
    else:
        print("Bank wins - You lose £100 ")
        cash = cash - 100
    print(" ")
    print("You have %s cash in your account " % cash)
    print("         ")
    choice = input("Would you like to play again, it will cost £50? Press Y for yes and N for no ")
    if choice == "Y" or choice == "y":
        print("    ")
        print(" -£50 cash")
        cash = cash - 50
        banner()
    else:
        sys.exit()
        


banner()
        

    



    
            

        
    

    

                                
                                
                
                        
        
        
