"""
Cards.json generator based on images on 'Cards' folder

"""

import os
import json

# base = os.path.join(os.getcwd(), "Cards")
base = './Cards/'
cards_list = []
cards_json = None


def check_value(card):
    # Return a value to the card dictionary based on card values
    value = 0
    splitted = card.split('.') 
    # Split the values of card by '.' which returns the name of card image in the first position (0) and the extension in the second position (1)
    # If the name which it is in the first position of the list ends with below cases return the value with that value
    if splitted[0].endswith("A"):
        return 1
    if splitted[0].endswith("J"):
        return 11
    if splitted[0].endswith("Q"):
        return 12
    if splitted[0].endswith("K"):
        return 13
    if splitted[0].endswith("10"):
        return 10
    if "cardJoker" in splitted[0]:
        return 1
    else:
        # Return the as value the number of the card if not of cases above do not match
        return splitted[0][-1]


if __name__ == '__main__':
    for root, folder, files in os.walk("./Cards"): # return a list of files inside the 'cards' folder
        files.sort() #shuffle the files before append in card_list
        value = 0
        for card in files:
            if not "cardBack" in card: # if card back in the list the value will be set to 0
                value = check_value(card)
            # append inside the card_list the values of card name, card img path and the value the was set in the check_value function
            cards_list.append(
                {'card':card.split(".")[0], 'img':f'{os.path.join(base, card)}','value':int(value)}
            )
            value = 0 #return value to 0 in case of any card back appear in the list

    cards_json = json.dumps(cards_list, indent=4) # transform the dictionary in JSON

    with open('cards.json', 'w') as f:
        # transform the JSON variable in a JSON file
        f.write(cards_json)