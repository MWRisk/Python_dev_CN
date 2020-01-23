import random
import time 
from time import sleep

character_data = {
"name": "Errenwulf",
"base_health": 20,
"base_attack": 20,
"base_defence": 20,
"has_ring": False,
"ring_health": 1,
"has_necklace": False,
"necklace_health": 0,
"has_shield": False,
"shield_health": 0,
"has_sword1": False,
"sword_1_attack": 0,
"has_sword2": False,
"sword_2_attack": 0,
"has_sword3": False,
"sword_3_attack": 0,
"max_sword_attack": 0,
"has_key": False,
"current_health": 80,
"current_attack": 20,
"current_defence": 20,
"opponent_health": 80,
"opponent_attack": 20,
"opponent_defence": 20
}


def calc_damage(attack, defence, text1, text2, text3, text4, text5, text6):
    attack_value = (attack + random.randint(1,10) - defence)
    time.sleep(.5)
    if attack_value < 0:
        attack_value = 0
        sleep(1)
        print("OOOOOPS!! " + text1 + " comically fumble" + text2 + text6 + " weapon!!")
    elif attack_value > 0 and attack_value < 4:
        print(text1 + " gain" + text2 + " a glancing blow") 
    elif attack_value > 3 and attack_value < 8:
        print("A clinical attack. " + text1 + "manage" + text2 + " a clean strike through " + text6 + " guard.")
    elif attack_value > 10:
        print("What a strike!! A critical hit" + text1 + text5 + " tempted to take a bow!" )
    else:
        print("OUCH!! That was swift and strong!!" + text1 + "land" + text2 + " an extremely powerful blow!")
    print(" ")
    time.sleep(1.3)
    print(text1 + "deal" + text2 + " " + str( attack_value) + text4)
    print(" ")
    return attack_value

def calc_opponent_health (health, attack, defence):
    return (health - calc_damage(attack, defence, "You ", "", "Your attack deals ", " damage to the opponent", "are", "their"))

def calc_hero_health (health, attack, defence):
    return (health - calc_damage(attack, defence, "The enemy ", "s", "The enemy attack deals ", " damage to you.", "is", "your"))

def fight(hero_health, hero_attack, hero_defence, opponent_health, opponent_attack, opponent_defence):
    both_alive = True
    while both_alive == True:
        new_opponent_health = calc_opponent_health(opponent_health,hero_attack,opponent_defence)
        if both_alive == True:
            if new_opponent_health <= 0:
                time.sleep(3)
                print(" ")
                print('YOU VANQUISHED YOUR FOE!')
                both_alive = False
            else:
                time.sleep(1.8)
                opponent_health = new_opponent_health
                print("Your enemy has " + str(opponent_health) + " health left.")
                print(" ") 
                print(" ")
        if both_alive != True:
            break

        new_hero_health = calc_hero_health(hero_health, opponent_attack, hero_defence)
        if both_alive == True:
            if new_hero_health <= 0:
                time.sleep(3)
                print(" ")
                print('Your enemy bested you...')
                print(" ")
                both_alive = False
            else:
                time.sleep(1.5)
                hero_health = new_hero_health
                sleep(1)
                print("Errenwulf, you now have " + str(new_hero_health) + " health remaining")
                print(" ")
                print(" ")
        

# print(current_scene["option_2_display"])
# current_scene["enemy_health"]
# current_scene["enemy_attack"]
# current_scene["enemy_defence"]
# character_data["current_health"]
# character_data["current_attack"]
# character_data["current_defence"]
fight(character_data["current_health"], character_data["current_attack"], character_data["current_defence"], character_data["opponent_health"], character_data["opponent_attack"], character_data["opponent_defence"])

