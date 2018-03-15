__author__ = 'burak'
import random #random function imported to select pokemons randomly from pokemon_list.txt
def print_win_or_lose(winner,loser): #take winner and loser as a parameter and print them
    print winner, " YOU HAVE BECOME A POKEMON MASTER!!!" #print winner
    print loser,"YOU HAVE TO TRAIN YOUR POKEMON HARDER..." #print loser
def random_select_3_pokemons(): #this function take infos from file and select 3 pokemon randomly from 'pokemon_list.txt'
    pokemon_list=open('pokemon_list.txt','r') #list open to read
    list=[] #empty list defined to add pokemons
    for line in pokemon_list:
        temporarily_list=[]
        for token in line.split(): #this loop for added file to list and and split another things
            try: #if thing in file int add to list
                int_token=int(token)
                temporarily_list.append(int_token)
            except: #if thimh in file not int add to list
                temporarily_list.append(token)
        list.append(temporarily_list) #pokemon_list.txt added to list
    pokemon_list.close() # pokemon_list closed
    random_select_list=[] #empty list defined to add random pokemons
    i=True
    while i==True:
        random_select=random.choice(list) #select random from list
        if random_select not in random_select_list: #check if random_select in random_select_list or not to avoid same pokemons in same list
            random_select_list.append(random_select)
            if len(random_select_list)==3:
                i=False
    return random_select_list #random selected list returned to use after
def modification(attacker,defencer): # this function modifying each player's Pokemon stats during a fight and if defencer pokemon has a weakness attackers hit's +10
    if attacker[3]=="Grass" and defencer[4]=="Grass": #these statements controls weaknesses
        attacker[2]=attacker[2]+10
    elif attacker[3]=="Fire" and defencer[4]=="Fire":
        attacker[2]=attacker[2]+10
    elif attacker[3]=="Water" and defencer[4]=="Water":
        attacker[2]=attacker[2]+10
    elif attacker[3]=="Normal" and defencer[4]=="Normal":
        attacker[2]=attacker[2]+10
    elif attacker[3]=="Electric" and defencer[4]=="Electric":
        attacker[2]=attacker[2]+10
    elif attacker[3]=="Fighting" and defencer[4]=="Fighting":
        attacker[2]=attacker[2]+10
    elif attacker[3]=="Rock" and defencer[4]=="Rock":
        attacker[2]=attacker[2]+10
    defencer[1]= defencer[1]-attacker[2] #modify stats
def remove_pokemon(player_list): # this function remove the dead Pokemon from the list.
   i=0
   while i<len(player_list):
        if player_list[i][1]<=0: # if player's pokemons health<0
            print player_list[i],"was dead" #print was dead
            player_list.remove(player_list[i]) # and remove this pokemon from the player's list
        i=i+1



def decide_winner(player1_list,player2_list): # this function decide the winner and loser
    if player1_list==[]: # if player1_list empty
        first_player="first player"
        second_player="second player"
        loser=first_player #first player = loser
        winner=second_player # second player = winner
        return loser,winner
    elif player2_list==[]: # if player2_list empty
        first_player="first player"
        second_player="second player"
        loser=second_player # second player = loser
        winner=first_player #first player = winner
        return loser,winner
    else:
        return -1 # if anyone has one return -1

Heads_or_Tails=[1,2] #program decide which player starts first
result=random.choice(Heads_or_Tails) #random choice 1 or 2
player1_list=random_select_3_pokemons() #random select function run and this return equal to player1_list
player2_list=random_select_3_pokemons() #random select function run and this return equal to player2_list
print "player 1's pokemons are",player1_list #print pokemons
print "player 2's pokemons are",player2_list
if result==1:
    print "player 1 start firts"
    first_player=player1_list #if first player start first player = player1_list
    second_player=player2_list # and second player = player2_list
else:
    print "player 2 start first" # or reverse
    first_player=player2_list
    second_player=player1_list
win=True
while win==True: # while win = True loop
    if first_player==player1_list: # if player1 start first
        print  player1_list
        first_player_choice=input("Player1 which pokemon do you choice (0)(1)(2)") # choose pokemon
        i=0
        while i < len(player1_list): # pokemon choosed from player1_list
            if first_player_choice==i:
                first_player_pokemon=player1_list[i]
            i=i+1
        print "you choose ",first_player_pokemon #print choosed pokemon

        print  player2_list # after player 2 choose pokemon and codes are the same
        second_player_choice=input("Player2 which pokemon do you choice (0)(1)(2)")
        j=0
        while j < len(player2_list):
            if second_player_choice==j:
                second_player_pokemon=player2_list[j]
            j=j+1
        print "you choose ",second_player_pokemon
    elif first_player==player2_list: # if player 2 start first codes are the same with which player1 start codes
        print player2_list
        first_player_choice=input("player 2 which pokemon do you want (0)(1)(2)")
        k=0
        while k < len(player2_list):
            if first_player_choice==k:
                first_player_pokemon=player2_list[k]
            k=k+1
        print "you choose ",first_player_pokemon
        print  player1_list
        second_player_choice=input("Player1 which pokemon do you choice (0)(1)(2)")
        l=0
        while l < len(player1_list):
            if second_player_choice==l:
                second_player_pokemon=player1_list[l]
            l=l+1
        print "you choose ",second_player_pokemon


    modification(first_player_pokemon,second_player_pokemon) #modificate with atacker is first_player and defender is second_player
    modification(second_player_pokemon,first_player_pokemon) #modificate with atacker is second_player and defender is first_player
    remove_pokemon(player1_list) # run remove pokemon function with player1_list
    remove_pokemon(player2_list) #run remove pokemon function with player2_list

    print  "player 1 list after fight = ",player1_list # print player's lists after fight
    print  "player 2 list after fight= ",player2_list

    if decide_winner(player1_list,player2_list)== -1: # if decide winner return -1 loop is continue
        print "game is running"
    else:
        loser,winner=decide_winner(player1_list,player2_list) # else decide winner function returns loser and winner
        print_win_or_lose(winner,loser) # wir_or_lose function run and print
        win=False # win = false and loop ended