import random
character_data = {
    "name": "Bob",
    "dead": False,
    "base_health": 30,
    "base_attack": 30,
    "base_defence": 30,
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
    "current_health": 30,
    "current_attack": 30,
    "current_defence": 30
}
scene_1 = {
    "scene_title":"Prison Cell",
    "scene_description": "You awaken in a dark cell, head throbbing and body aching from the battle earlier that day. \n You hear soft footsteps outside, a short silence before a click as the lock is turned. The door opens to reveal your mother, the queen in a dark robe. She stealthily moves towards you and whispers, Bob Thank god you are OK! Come with me quickly, we don't have much time.",
    "option_1_text": "Immediately exit the cell with her",
    "option_1_outcome_text": "You leave and travel down a tunnel to the exit",
    "option_1_display": True,
    "option_2_text": "Ask, 'We lost? Is Jennifer safe?",
    "option_2_outcome_text": "We did... I'm sorry Bob... That tyrant, Archibald took her'. Footsteps then the door flings open! Guards enter and the captain gives the orders, 'Take that slag to a cell, we\'ll have fun with her later... And slit that pricks throat!",
    "option_2_display": True,
    "option_3_text": "Do Nothing",
    "option_3_outcome_text":"Not so clever... The guards come in and run you and your mother through with swords. You definitely deserved that...",
    "option_3_display": True,
    "option_4_text": "",
    "option_4_outcome_text": "",
    "option_4_display": False,
}
scene_2 = {
    "scene_title":"The Tunnel",
    "scene_description": "You're mother, Queen Xenia, leads you quietly to a secret passage in the basement of the castle. You pass through and come across 2 dead guards at the feet of Queen Xenia's bodyguard. Their weapons lay loose in their death grip: \n Do you:",
    "option_1_text": "Exclaim loudly, 'Godwin, you old rascal. You could have left some for me?'",
    "option_1_display": True,
    "option_1_outcome_text": "Your excessively loud greeting results in an army of guards being alerted. You put up a decent fight but they outnumber you 10 - 1. You watch as your mother and friend are cut to pieces and then you lose your head...",
    "option_2_text": "Quickly take a sword and head along the forest path to the cross-roads",
    "option_2_display": True,
    "option_2_outcome_text": "You reach down and take one of the guard's sword then move - it's standard issue but it is well balanced and feels good in your hand. (att increased by 2).",
    "option_3_text": "Head along the forest path immediately",
    "option_3_display": True,
    "option_3_outcome_text": "You flee down the forest path with your mother and Godric close by",
    "option_4_text": "Take armour and sword from the dead men",
    "option_4_display": True,
    "option_4_outcome_text": "You start to remove a dead guards armour... Just as you pull it over your head, 2 guards come through the passage. Unarmed and outnumbered, your life flashes before your eyes as your head is cleaved from your neck.",
    }
scene_3 = {
    "scene_title":"Forest Path",
    "scene_description": "As you travel further in to the woods, your mother asks you to halt. 'Bob, I strongly advise we stop at the inn to speak to the bar keep. He is a valuable source of information and can help you understand the adventure that awaits you.'",
    "option_1_text": "Ignore your mother and head straight to the cross-roads (don't receive game overview)",
    "option_1_display": True,
    "option_1_outcome_text": "You rush towards the crossroads",
    "option_2_text": "Go to the inn with your mother (receive game overview)",
    "option_2_display": True,
    "option_2_outcome_text": "'You're right, mother, a helping hand is always welcome",
    "option_3_text": "",
    "option_3_display": False,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": "",
    }
scene_4 = {
    "scene_title":"The Inn",
    "scene_description": "You enter the inn. Amazingly, despite recent events, it appears completely in tact with the inn keep entertaining customers. The inn keep spies you, shepherds you in to a quiet side room and gives you the following information: \n \n 'You must travel to Archibald's Castle in the deep south, to avenge your father and rescue your princess.' \n \n 'I'm not certain that you are strong enough right now and you are ill equipped.' \n \n 'You're direct route to Archibald is South but I would encourage you to consider paths to the west or east as well to speak to your allies and gain some equipment and experience along the way.'",
    "option_1_text": "",
    "option_1_display": False,
    "option_1_outcome_text": "",
    "option_2_text": "",
    "option_2_display": False,
    "option_2_outcome_text": "",
    "option_3_text": "",
    "option_3_display": False,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": "",
    }
scene_5 = {
    "scene_title":"ambush_Cross-roads",
    "scene_description": "A small band of guards ambush you as you reach the Cross-Roads. You face your first test in battle. Godric and the Queen act fast and you follow them into the fray:",
    "option_1_text": "",
    "option_1_display": False,
    "option_1_outcome_text": "",
    "option_2_text": "",
    "option_2_display": False,
    "option_2_outcome_text": "",
    "option_3_text": "",
    "option_3_display": False,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": False,
    "option_4_outcome_text": "",
    }


scene_7 = {
    "scene_title":"Mountains",
    "scene_description": "The snowy ice cold mountains, where few dare to go block the majority of your view to the North and East. \n \nYou've heard tell of mystical creatures in the mountains to your South East where you spy a mountain pass. \n \nThere is a road South West to Riverside, where your ally Queen Cassandra calls home.",
    "option_1_text": "",
    "option_1_display": True,
    "option_1_outcome_text": "",
    "option_2_text": "",
    "option_2_display": True,
    "option_2_outcome_text": "",
    "option_3_text": "",
    "option_3_display": True,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": True,
    "option_4_outcome_text": "",
    }

The snowy, ice cold mountains, where few dare to go block the majority of your view to the North and East. You've heard tell of mystical creatures in the mountains to your South East where you spy a mountain pass and there is a road South West to Riverside, where your ally Queen Cassandra calls home.

Do you:
a) Head to Riverside
b) Begin the trek up the mountain pass
c) Try to scale the sheer rock face to the North
d) Head back to the cross-roads

Outcome:
a) River crossing
b) Mountain Pass
c) For some reason you choose to do a bit of mountain climbing instead of continuing your adventure. You're pretty good at it but sadly, as you reach halfway up the mountain you realise you have no equipment and in the panic, lose your grip and fall to your death... Splat!

scene_7 = {
    "scene_title":"",
    "scene_description": "",
    "option_1_text": "",
    "option_1_display": True,
    "option_1_outcome_text": "",
    "option_2_text": "",
    "option_2_display": True,
    "option_2_outcome_text": "",
    "option_3_text": "",
    "option_3_display": True,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": True,
    "option_4_outcome_text": "",
    }

scene_7 = {
    "scene_title":"",
    "scene_description": "",
    "option_1_text": "",
    "option_1_display": True,
    "option_1_outcome_text": "",
    "option_2_text": "",
    "option_2_display": True,
    "option_2_outcome_text": "",
    "option_3_text": "",
    "option_3_display": True,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": True,
    "option_4_outcome_text": "",
    }

scene_7 = {
    "scene_title":"",
    "scene_description": "",
    "option_1_text": "",
    "option_1_display": True,
    "option_1_outcome_text": "",
    "option_2_text": "",
    "option_2_display": True,
    "option_2_outcome_text": "",
    "option_3_text": "",
    "option_3_display": True,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": True,
    "option_4_outcome_text": "",
    }

scene_7 = {
    "scene_title":"",
    "scene_description": "",
    "option_1_text": "",
    "option_1_display": True,
    "option_1_outcome_text": "",
    "option_2_text": "",
    "option_2_display": True,
    "option_2_outcome_text": "",
    "option_3_text": "",
    "option_3_display": True,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": True,
    "option_4_outcome_text": "",
    }

scene_7 = {
    "scene_title":"",
    "scene_description": "",
    "option_1_text": "",
    "option_1_display": True,
    "option_1_outcome_text": "",
    "option_2_text": "",
    "option_2_display": True,
    "option_2_outcome_text": "",
    "option_3_text": "",
    "option_3_display": True,
    "option_3_outcome_text": "",
    "option_4_text": "",
    "option_4_display": True,
    "option_4_outcome_text": "",
    }


# functions
def display_message(message):
    print('')
    print(message)
    print('')
def calc_damage(attack, defence):
    return (attack + random.randint(1,10) - defence)
def calc_opponent_health (health, attack, defence):
    return (health - calc_damage(attack, defence))
def calc_hero_health (health, attack, defence):
    return (health - calc_damage(attack, defence))
def fight(hero_health, hero_attack, hero_defence, opponent_health, opponent_attack, opponent_defence):
    both_alive = True
    while both_alive:
        new_opponent_health = calc_opponent_health(opponent_health,hero_attack,opponent_defence)
        if new_opponent_health <= 0:
            print('enemy defeated')
            both_alive = False
        else:
            print(new_opponent_health)
            opponent_health = new_opponent_health
        new_hero_health = calc_hero_health(hero_health, opponent_attack, hero_defence)
        if new_hero_health <= 0:
            print('You are dead')
            both_alive = False
        else:
            print('health  ')
            print(new_hero_health)
            hero_health = new_hero_health
def option_display():
    # print('')
    print('Your Options are')
    option_string = ''
    if current_scene["option_1_display"]:
        print ('a: ' + current_scene["option_1_text"])
        option_string +='a'
    if current_scene["option_2_display"]:
        print ('b: '+ current_scene["option_2_text"])
        option_string +='b'
    if current_scene["option_3_display"]:
        print ('c: '+ current_scene["option_3_text"])
        option_string +='c'
    if current_scene["option_4_display"]:
        print ('d: '+ current_scene["option_4_text"])
        option_string +='d'
    option_chosen = False
    while option_chosen != True:
        option_choice = input('Choose an option:')
        if option_choice.lower() in option_string:
            option_chosen = True
            return option_choice.lower()
        else:
            print('try again')
def you_are_dead():
    character_data['dead'] = True
    print('')
    print('Oh No...')
    print('Death comes to us all eventually')
    print('Unfortunately for you, it is happened to you now ')
    print('')
# main game
while character_data['dead'] == False:
    current_scene = scene_1
    display_message(current_scene['scene_description'])
    option = option_display() # get selected option a b c d
    if option == 'a':
        display_message(current_scene['option_1_outcome_text'])
        current_scene = scene_2
    if option == 'b':
        display_message(current_scene['option_2_outcome_text'])
        you_are_dead()
        break
    if option == 'c':
        display_message(current_scene['option_3_outcome_text'])
        you_are_dead()
        break
    display_message(current_scene['scene_description'])
    option = option_display() # get selected option a b c d
    if option == 'a':
            display_message(current_scene['option_1_outcome_text'])
            # current_scene = scene_2
    if option == 'b':
        display_message(current_scene['option_2_outcome_text'])
        # you_are_dead()
        # break
    if option == 'c':
            display_message(current_scene['option_3_outcome_text'])
            # you_are_dead()
            # break
print('Game Over!')