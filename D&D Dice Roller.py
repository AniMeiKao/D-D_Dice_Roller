import random
import re

#num_dice = int(re.sub(r'(\d*)d(\d+)([+-]\d+)*', r'\1', ask, flags = 0))
#dice_size = int(re.sub(r'(\d*)d(\d+)([+-]\d+)*', r'\2', ask, flags = 0))
#roll_mod = re.sub(r'(\d*)d(\d+)([+-]\d+)*', r'\3', ask, flags = 0)

'''
ask = input("What are you rolling? (Use format such as 1d20) ")

num_dice = int(re.sub(r'(\d*)d.*', r'\1', ask, flags = 0))
dice_size = int(re.sub(r'.*d(\d+).*', r'\1', ask, flags = 0))
roll_mod_sign = re.sub(r'.*d\d+([+-]).*', r'\1', ask, flags = 0)
roll_mod = re.sub(r'(\d*)d(\d+)([+-])(\d+)*', r'\4', ask, flags = 0)


if roll_mod is None:
    roll_mod = 0



def pick_game_type():
    print("What edition of D&D are you using?")
    print("5E for 5th edition")
    print("3E for 3rd and 3.5 edition (including Pathfinder)")
    game = input(  )
    supported_games = ['3E','5E']
    while game not in supported_games:
        print(game + " is an invalid option. Please try again. Valid options are:", *supported_games, sep='\n  ')
        game = input("What rules are we rolling with?\n  ")

'''

# all purpose rolls allowing modifiers
def standard_roll(die_size, sign, mod = 0, die_qty = 1):
    results = []
    total = 0
    for i in range(0,die_qty):
        results.append(random.randint(1, int(die_size)))
    sub_total = sum(results)
    if sign is '-' and mod != 0:
        total = sub_total - int(mod)
        print("Rolls: " + str(results), "Sum of rolls: " + str(sub_total), "With the -" + mod + " penalty: " + str(total), sep='\n')
    elif sign is '+' and mod != 0:
        total = sub_total + int(mod)
        print("Rolls: " + str(results), "Sum of rolls: " + str(sub_total), "With the +" + mod + " bonus: " + str(total), sep='\n')
    else:
        print("Rolls: " + str(results), "Sum of rolls: " + str(sub_total), sep='\n')
    
    #print('totals', str(total), 'results', str(results), sep='', end='\n')

def d20_basic(qty): # basic skill or attack roll
    for i in range(qty):
        roll = random.randint(1, 20)
        if roll <10 and not 8:
            print("", "**************", sep='\n')
        elif roll in (11, 18):
            print("", "****************", sep='\n')
        else:
            print("", "***************", sep='\n')
        if roll is 1:
            print("  Critical") 
            print("     Failure!")
        elif roll is 20:                 
            print("  Critical") 
            print("     Success!")
        elif roll in (8, 11, 18):
            print("You rolled an " + str(roll))
        else:
            print("You rolled a " + str(roll))
        if roll <10 and not 8:
            print("", "**************", sep='\n')
        elif roll in (11, 18):
            print("", "****************", sep='\n')
        else:
            print("", "***************", sep='\n')

def d20_5E(advantage): # 
    group_roll = []
    group_roll.append(random.randint(1, 20))
    print("", "***************", sep='\n')
    if advantage is "dis":
        group_roll.append(random.randint(1, 20))
        group_roll.sort()
        print("Disadvantage")
        print(group_roll)
        print(" " + str(group_roll[0]))
    if advantage is "adv":
        group_roll.append(random.randint(1, 20))
        group_roll.sort(reverse=True)
        print("Advantage")
        print(group_roll)
        print(" " + str(group_roll[0]))
    if group_roll[0] is 1:
        print("  Critical") 
        print("     Failure!")
    elif group_roll[0] is 20:
        print("  Critical") 
        print("     Success!")
    print("", "***************", sep='\n')




d20_basic(3)
d20_5E("dis")
d20_5E("adv")

#standard_roll(dice_size, roll_mod_sign, roll_mod, num_dice)




