import random
#########################################
"""FUNCTIONS"""
#########################################

"""1. SET UP CAVE STRUCTURE"""

#make a list of 20nr empty lists to store caves and their links in
def setup_caves(cave_numbers):
    caves = []
    for i in cave_numbers:
        caves.append([])
    return caves

#pass in caves list of lists and add links
def cave_structure(caves):
    caves[0] = [1,4,7]
    caves[1] = [0,2,9]
    caves[2] = [1,3,11]
    caves[3] = [2,4,13]
    caves[4] = [0,3,5]
    caves[5] = [4,6,14]
    caves[6] = [5,7,16]
    caves[7] = [0,6,8]
    caves[8] = [7,9,17]
    caves[9] = [1,8,10]
    caves[10] = [9,11,18]
    caves[11] = [2,10,12]
    caves[12] = [11,13,19]
    caves[13] = [3,12,14]
    caves[14] = [5,13,15]
    caves[15] = [14,16,19]
    caves[16] = [6,15,17]
    caves[17] = [8,16,18]
    caves[18] = [10,17,19]
    caves[19] = [12,15,18]
    return caves

#check to see if 3 caves are connected -- this allows you to shoot around corners
def is_connected(cave1, cave2, cave3, cave4):
    if cave1 in caves[cave2] and cave2 in caves[cave3] and cave3 in caves[cave4]:
        return True
    else:
        return False

#turn outer pentagon clockwise and re-do links
def turn_outer_pent(caves):
    #swaps points 0-4 on outer pent.
    #c = place holder for 1st point to change
    c = caves[0][2]
    for i in range(0,4):
        caves[i][2] = caves[i+1][2]
    caves[4][2] = c
    #swaps points 5,7,9,11,13 on centre pentagon
    d = caves[13][0]
    for i in range(13,5,-2):
        caves[i][0] = caves[i -2][0]
    caves[5][0] = d    
    return caves

#turn inner pentagon clockwise and re do links
def turn_inner_pent(caves):
    
    #swaps points 15,16,17,18,19 on inner pentagon
    copy = caves[15][0]
    for i in range(15,19):
        caves[i][0]=caves[i+1][0]
    caves[19][0] = copy
    
    #swaps points 6,8,10,12,14 of center pentagon
    copy2 = caves[14][2]
    for i in range(14,6,-2):
        cave[i][2] = cave[i-2][2]
    caves[6][2] = copy2
  
    return caves

#rotate the two pentagons
def rotate_pentagons(caves, turns):
    for i in range(0, turns):
        turn1 = turn_outer_pent(caves)
        caves = turn_inner_pent(turn1)
    return caves

#reset cave struture back to its origional form
def reset_caves(caves):
    caves = cave_structure(caves)
    return caves


"""2. INTRODUCE ITEMS TO GAME"""
#create a list to store wumpii locations => adds random numbers to list while at the same time removes these
#nums from the setup_num list therefore no random number is repeated twice. The setup_nums list is then passed to
#setup_bats and setup_pits so they are operating from a list with wumpii location taken out of it and therefore
#wumpii, bats and pits all end up in seperate caves.
def setup_wumpii(setup_nums,levels):
    wumpus = []
    for i in levels:
        number = random.choice(setup_nums)
        wumpus.append(number)
        setup_nums.remove(number)
    return wumpus
    
# create a list of bat locations takes in levels as a parameter : this is how I set difficulty of the game
def setup_bats(setup_nums, levels):
    bats = []
    for i in levels:
        number = random.choice(setup_nums)
        bats.append(number)
        setup_nums.remove(number)
    return bats

#creates a list of pit locations
def setup_pits(setup_nums, levels):
    pits = []
    for i in levels:
        number = random.choice(setup_nums)
        pits.append(number)
        setup_nums.remove(number)
    return pits


#print all the links between caves for testing
def print_caves(caves):
    for i in cave_numbers:
        print i, ":", caves[i]
    print '------'


"""3. GAME LOGIC"""

#lets player know where he is in cave struture and warns him of any dangers
#uses the check_for_intersection function that returns true if there same numbers in each set
#as in if pits locations are contained in players link caves set then give a warning
def print_location(player_location):
    print "\nYou are in cave", player_location

    player_caves = caves[player_location]

    if check_for_intersection(wumpus_location, player_caves):
        print "I smell trouble!"

    if check_for_intersection(bat_location, player_caves):
        print "I hear bats!"
        
    if check_for_intersection(pit_location, player_caves):
        print "I feel a breeze!"

#takes in two lists and compares them for any equalities. As in if pits location in links to players location
def check_for_intersection(list1, list2):
    answer = set(list1)
    if answer.intersection(list2):
        return True

#gets the next cave player is going to move to or shoot into
def get_next_cave():
    player_input = raw_input("Which cave?")
    if (not player_input.isdigit() or int(player_input)
        not in caves[player_location]):
        print player_input + "?"
        print "Can't move there"
        return None
    else:
        return int(player_input)

#handles player input
def get_player_input():
    print "What do you want to do?"
    print " m) move"
    print " s) shoot an arrow"
    print " x) magic arrow"

    response = raw_input("> ")

    if response == "m" or response == "s" or response == "x":
        return response
    else:
        print response + "?"
        print "Thats not a command That I recognise"
        return None

#take input for magic arrow shot
def get_caves():
    global caves_list
    cave1 = raw_input("1st cave?")
    if (not cave1.isdigit()):
        return None
    else:
        caves_list.append(int(cave1))

    cave2 = raw_input("2nd cave?")
    if (not cave2.isdigit()):
        return None
    else:
        caves_list.append(int(cave2))

    cave3 = raw_input("3rd cave?")
    if (not cave3.isdigit()):
        return None
    else:
         caves_list.append(int(cave3))

    return caves_list



#takes input from the player to set the level of difficulty
def choose_levels(lev_num):
    print"Which level do you want to play at"
    print " 1) Easy: 1nr wumpus, 1nr Bat, 1nr Pit"
    print " 2) Medium: 2nr wumpus, 2nr Bat, 2nr Pit"
    print " 3) Hard: 3nr wumpus, 3nr Bat, 3nr Pit"

    response = raw_input("> ")

    if response == "1":
        print "You have chosen level 1"
        return set_level(1)
    if response == "2":
        print "You have chosen level 2"
        return set_level(2)
    if response == "3":
        print "You have chosen level 3"
        return set_level(3)
    else:
        print response + "?"
        print "Thats not a command that I recognise"
        return None
        

#move changes players location and also checks for bats if there is one you get
#sent to another random cave

def move():
    print "Caves", caves[player_location], "are around you"
    next_cave = get_next_cave()
    if check_for_bats(next_cave):
        next_cave = bat_drop()
    if next_cave is None:
        return player_location
    else:
        return next_cave
    
#handles shooting arrows
def shoot():
    global arrows
    global wumpus_location
    global setup_nums
    print "Firing..."
    #print "Caves", caves[player_location], "are around you"
    shoot_at = get_next_cave()
    #if player shoots into a cave that is linked to wumpus it changes wumpus postion
    #by removing item from wumpus list and appending a new random number to list
    for wumpus in wumpus_location:
        if shoot_at in caves[wumpus]:
            print "You spooked the wumpus and he has flown to a different cave!"
            new_loc = random.choice(setup_nums)
            wumpus_location.remove(wumpus)
            wumpus_location.append(new_loc)
            print "new wumpus locations: ",wumpus_location
            
    if shoot_at in wumpus_location:
        print "Well Done! You shot a wumpus!"
        set_wumpus_lives(1)
        #remove killed wumpus from wumpus list
        wumpus_location.remove(shoot_at)
        return wumpus_location

    
    elif shoot_at not in wumpus_location:
        print "You missed!"
        

    arrows = arrows - 1
    print "You have",arrows, "arrows left"
        
def magic_arrow():
    global arrows
    global wumpus_location
    print "select the 3 nr caves to shoot into. All caves must be linked!!"
    shot =get_caves()


    if is_connected(player_location, shot[0], shot[1], shot[2]) and check_for_intersection(shot, wumpus_location):
        print "you killed some wumpus"
        
        set_wumpus_lives(1)
        answer = set(shot)
        kill_shot = answer.intersection(wumpus_location)
        for shot in kill_shot:
            wumpus_location.remove(shot)
            print "you have", wumpus , "left to kill!"
        return wumpus_location
  
    else:
        print "you missed!"
        

    arrows = arrows - 1
    print "You have",arrows, "arrows left"

   

#checks for the presence of bats by comparing players location to bat location list
def check_for_bats(player_location):

    if player_location in bat_location:
        print "bats in this cave!"
        return True
    
#drops player to new random location as long as its not another bat cave or wumpus cave
#that just wouldn't be fair
def bat_drop():
    player_location = random.choice(cave_numbers)
    while player_location in bat_location or player_location in wumpus_location:
        player_location = random.choice(cave_numbers)
    print "A giant bat got you and left you in cave ", player_location
    return player_location

#keeps track of arrows
def out_of_arrows(arrows):
    if arrows < 1:
        return True
    
#keeps track of number of wumpus   
def kill_all_wumpus(wumpus):
    if wumpus < 1:
        return True
    
#sets level at start of the game
def set_level(level):
    global lev_num
    lev_num = level
    return lev_num

#keeps track of wumpus lives
def set_wumpus_lives(kill):
    global wumpus
    wumpus = wumpus - kill
    return wumpus

    
#prints instructions
def print_instructions():
    print "                 WELCOME TO HUNT THE WUMPUS!"
    print "You are in one of 20nr caves some of which have wumpii, bats or pits within them"
    print "to win the game you must first"
    print "find the wumpus and then kill him with one of your arrows "
    print "you get twice as many arrows as there are wumpii at the start of the game"
    print "if you run out of arrows thens its game over"
    print "if you go into a cave where there are wumpii then you are eaten"
    print "if you fall into a pit well thens its game over"
    print "if you gon into a cave where there are bats the bats pick you up and drop you into a new cave"
    print ""
    print "First choose your level of difficulty: " 
    print ""
    
###############################
""" START OF GAME SET-UP """
###############################


"""globals """
print_instructions()
lev_num = 1
choose_levels(lev_num)

cave_numbers = range(0,20)
setup_nums = range(0,20)
arrows = lev_num * 2
wumpus = lev_num
levels = range(0,lev_num)
caves_list = []


wumpus_location = setup_wumpii(setup_nums, levels)
player_location = random.choice(cave_numbers)
bat_location = setup_bats(setup_nums, levels)
pit_location = setup_pits(setup_nums, levels)

while player_location in wumpus_location or player_location in pit_location or player_location in bat_location:
    player_location = random.choice(cave_numbers)

cave = setup_caves(cave_numbers)
c = cave_structure(cave)
turns = random.randint(0,5)
caves = rotate_pentagons(c, turns)

####################################################
"""GAME LOOP"""
####################################################
while True:
    print_location(player_location)
    
    player_input = get_player_input()

    if player_input is None:
        continue
    if player_input == "m":
        player_location = move()
        if player_location in wumpus_location:
            print "GAME OVER! You Lose! You were eaten by the wumpus!"
            break
        elif player_location in pit_location:
            print "GAME OVER! You Lose! You fell into the pit!"
            break
    

    if player_input =="s":
        shoot()
        if wumpus < 1:
            print "You win! You Killed all the wumpus"
            break
        quiver_empty = out_of_arrows(arrows)
        if quiver_empty:
            print "Game Over! You Lose! Your out of arrows"
            break
        

    if player_input == "x":
        magic_arrow()
        if wumpus < 1:
            print "You win! You Killed all the wumpus"
            break
        quiver_empty = out_of_arrows(arrows)
        if quiver_empty:
            print "Game Over! You Lose! Your out of arrows"
            break
