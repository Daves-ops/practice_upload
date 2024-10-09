import random

# Player Info
level = 0
playerStats = {'vigor': 100, 'mind': 50, 'endurance': 30, 'strength': 50}
inventory = ['map']

# Simplified Areas
areas = {
    'north': ('Limgrave', 'A temperate land of green plains and golden trees.'),
    'south': ('Weeping Peninsula', 'A land of unceasing rain, giving the impression of constant lament. It is connected to Limgrave proper by the Bridge of Sacrifice.'),
    'east': ('Caelid', 'A corrupt land with red soil and many undead roaming the open fields.'),
    'west': ('Stormhill', 'A windy and stormy region west of Limgrave, filled with ruins and dangerous enemies.')
}

# Story-driven events
events = [
    {'Encounter White Mask Varre': 'Standing before you is White Mask Varre. He calls you maidenless.', 'type': 'chance', 'continue quest': 'check map', 'fight': 'die'},
    {'Encounter Renna': 'Appears before you in Church of Elleh in Limgrave. Gives you a Spirit Summon: Comet', 'type': 'chance', 'continue quest': 'check map'},
    {'Murkwater Cave': 'Fight through enemies and get to the final room where you find Patches who initiates a boss fight.', 'type': 'chance', 'fight Patches': 'Fight until Patches apologizes and presents you with armor', 'Die': 'You Died'}
]

# Main Game Loop
while playerStats['vigor'] > 0:
    print('\n-- Main Menu --')
    print('Your current stats: ', playerStats)
    print('Your inventory: ', inventory)
    
    # Display available directions to explore
    print('\nWhere would you like to go?')
    for direction, area_info in areas.items():
        print(f'{direction.capitalize()}: Travel to {area_info[0]} - {area_info[1]}')
    
    # Get player choice for direction
    choice = input('\nChoose a direction (north, south, east, west) to travel or type \'quit\' to exit: ').lower()
    
    if choice == 'quit':
        print('Thanks for playing!')
        break
    
    if choice in areas:
        selected_area = areas[choice][0]
        print(f'\nYou travel to {selected_area}.\n')
        
        # Randomly trigger an event
        current_event = random.choice(events)
        print(f'You encounter: {list(current_event.keys())[0]}')
        print(current_event[list(current_event.keys())[0]])
        
        # Special handling for Murkwater Cave
        if 'Murkwater Cave' in current_event:
            print('\nYou enter the Murkwater Cave and fight through enemies.')
            action = input('Do you want to fight Patches? (yes/no): ').lower()
            
            if action == 'yes':
                outcome = random.choice(['success', 'failure'])
                if outcome == 'success':
                    print('You fight Patches, and he apologizes. You gain new armor!')
                    inventory.append('armor')  # Add armor to inventory
                    playerStats['vigor'] -= random.randint(10, 20)
                    level += 1  # Increase level after fighting successfully
                elif outcome == 'failure':
                    print('You fight Patches but fail. You died.')
                    playerStats['vigor'] = 0  # Player dies
                    break
            elif action == 'no':
                print('You chose to leave Murkwater Cave without fighting.')
                playerStats['vigor'] -= random.randint(5, 10)  # Slight vigor loss for traveling
        # Handle other chance events
        elif current_event['type'] == 'chance':
            # Handle chance events (50/50 chance)
            action = input(f'\nWhat do you want to do? (continue quest / fight): ').lower()
            if action == 'continue quest':
                print(current_event['continue quest'])
                print('You check your map and continue.')
                playerStats['vigor'] -= random.randint(5, 15)  # Lose vigor while traveling
            elif action == 'fight':
                outcome = random.choice(['success', 'failure'])
                if outcome == 'success':
                    print('You fight and win!')
                    playerStats['vigor'] -= random.randint(10, 20)
                    level += 1  # Increase player level after winning a fight
                else:
                    print('You fight and lose!')
                    playerStats['vigor'] = 0  # Player dies
                    print('You died.')
                    break
        else:
            print('No event occurs.')
        
    else:
        print('Invalid direction. Please choose a valid direction.')

# End of game
if playerStats['vigor'] <= 0:
    print('\nGame Over! You died.')
elif level > 0:
    print(f'\nCongratulations! You reached level {level}.')
