import random 
machinethrow = ["rock", "paper", "scissors"]
response =""
dictionary = {
             'rock': 'scissors',
             'paper': 'rock',
             'scissors': 'paper',
}


while True:

    choice = random.choice(machinethrow)
    response = input ("Rock, Paper, Scissors or q to quit.")
   
    if response.lower() in ['q', 'quit']:
        break


    if choice == response:
        print ("Tie!")
    elif choice == dictionary[response]:
        print ('User Wins!')
    else:
        print ( 'Loser!')
    print (choice)
    print (response)
