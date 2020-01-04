import random
import re

ask = input("What are you rolling? ")

#num_dice = int(re.sub(r'(\d*)d(\d+)([+-]\d+)*', r'\1', ask, flags = 0))
#dice_size = int(re.sub(r'(\d*)d(\d+)([+-]\d+)*', r'\2', ask, flags = 0))
#roll_mod = re.sub(r'(\d*)d(\d+)([+-]\d+)*', r'\3', ask, flags = 0)

num_dice = int(re.sub(r'(\d*)d.*', r'\1', ask, flags = 0))
dice_size = int(re.sub(r'.*d(\d+).*', r'\1', ask, flags = 0))
roll_mod_sign = re.sub(r'.*d\d+([+-]).*', r'\1', ask, flags = 0)
roll_mod = re.sub(r'(\d*)d(\d+)([+-])(\d+)*', r'\4', ask, flags = 0)

if roll_mod is None:
    roll_mod = 0

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

standard_roll(dice_size, roll_mod_sign, roll_mod, num_dice)




