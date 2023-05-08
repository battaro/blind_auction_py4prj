import os #importing os library to clear the console when i want
from art import logo 

def clear(): #the console cleaner function
    #idk what this line of code exactly does but i think he looking for the system if its window he will write
    #cls else he will write clear
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo) #printing the logo of the program

bidders_char = [] #new list will contain the characteristics of the bidder 
isAuctionEnds = False #is the auction ends ? :()
def auction(name,bid,others): #main function on the program contain three parameters 
    global isAuctionEnds #amazing thing made the isAuctionEnds as a global var
    
    max_bid = 0 #new variable i will use it later to get the max bid
    winner = "" #new variable will contain the winner on the bid
    
    bidders_char.append({name : bid})  #appending the name and the bid as key and value like a dictionary on list

    merged_dict = {} #new dict will contain all dicts on it 
    for dictionary in bidders_char: #looping through the main list to get all other dicts
        merged_dict.update(dictionary) #making the new list as i said by using update method
    
    for bidder in merged_dict: #looping through the new list to know who is the winner
        money = merged_dict[bidder] #new variable equal to the value of first bidder
        #if this money greater than the max_bid that mean max_bid equal to this money and this bidder is the winner
        if money > max_bid: 
            max_bid = money
            winner = bidder
            
    if others == "yes": #if the user wrote yes the program will continue after cleaning the console
        clear()
    else:
        #otherwise finish the program
        isAuctionEnds = True 
        print(f"The winner is {winner} with a bid of ${max_bid}") 
        
while not isAuctionEnds: #The Auction loop
    
    name = input("What is your name?: ") #name of the bidder
    bid = int(input("What is your bid?: $")) #bid of the bidder
    others = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower() #is there any one else this bidder ?
    
    auction(name,bid,others) #finally calling the function with the three arguments

    
