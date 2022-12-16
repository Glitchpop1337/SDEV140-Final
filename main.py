#This is the main script for the main function of the application
from tkinter import * #tkiner import all

root = Tk() # creating the window
root.title("D&D 5E Character creator.") # assigning the title
root.geometry("1920x1080") # assigning the window default size
bg = PhotoImage(file="background2.png") # assigning a background image
imgLabel = Label(root, image=bg) # creating a label for image
imgLabel.place(x=0, y=0, relwidth=1, relheight=1) # placing label
#################################################################
# Creating dictionaries with relevant text to be inserted into the output
traits = {'darkvision': '\nDarkvision: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light.',
          'keen senses': '\nKeen Senses: You have proficiency in the Perception skill.',
          'fey ancestry': '\nFey Ancestry: You have advantage on saving throws against being charmed, and magic can’t put you to sleep.',
          'trance': '\nTrance: Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day.\n'
                    ' (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion;\n'
                    ' such dreams are actually mental exercises that have become reflexive through years of practice.\n'
                    ' After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.',
          'ability increase': '\nAbility Scores Up: Your ability scores each increase by 1.',
          'int increase': '\nIntelligence up: +1 intelligence',
          'str increase': '\nStrength up: +1 strength',
          'dex increase': '\nDexterity up: +1 dexterity',
          'wis increase': '\nWisdom up: +1 wisdom',
          'cha increase': '\nCharisma up: +1 charisma',
          'con increase': '\nConstitution up: +1 constitution',
          'elf weapon training': '\nElf Weapon Training: You have proficiency with the longsword, shortsword, shortbow, and longbow.',
          'fleet of foot': '\nFleet of Foot: Your base walking speed increases to 35 feet.',
          'mask of the wild': '\nMask of the Wild: You can attempt to hide even when you are only lightly obscured by\n'
                              'foliage, heavy rain, falling snow, mist, and other natural phenomena.',
          'dwarven resilience': '\nDwarven Resilience: You have advantage on saving throws against poison, and you have resistance against poison damage.',
          'dwarven combat training': '\nDwarven Combat Training: You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.',
          'tool proficiency': '\nTool Proficiency: You gain proficiency with the artisan’s tools of your choice:\n smith’s tools, brewer’s supplies, or mason’s tools.',
          'stonecutting': '\nStonecutting: Whenever you make an Intelligence (History) check related to the origin of stonework,\n'
                          ' you are considered proficient in the History skill and add double your proficiency bonus to the check,\n'
                          ' instead of your normal proficiency bonus.',
          'dwarven toughness': '\nDwarven Toughness: Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.',
          'dwarven armor training': '\nDwarven Armor Training: You have proficiency with light and medium armor.'}
classes = {'rogue': '\nRogue Class'
                    '\nHit Dice: 1d8 per rogue level'
                    '\nHit Points at 1st level: 8 + Con modifier'
                    '\nHit points at Higher Levels: 1d8 (or 5) + Con modifier'
                    '\n'
                    '\nProficiencies:'
                    '\nArmor: Light armor'
                    '\nWeapons: Simple weapons, hand crossbows, longswords, rapiers, shortswords'
                    '\nTools: Thieves’ tools'
                    '\nSaving Throws: Dexterity, Intelligence'
                    '\nSkills: Choose four from Acrobatics, Athletics, Deception, Insight,'
                    '\nIntimidation, Investigation, Perception, Performance, Persuasion, Sleight of Hand, and Stealth'
                    '\n'
                    '\nExpertise:'
                    '\nAt 1st level, choose two of your skill proficiencies,'
                    '\nor one of your skill proficiencies and your proficiency with thieves’ tools.'
                    'Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies.'
                    '\nAt 6th level, you can choose two more of your proficiencies (in skills or with thieves’ tools) to gain this benefit.'
                    '\n'
                    '\nSneak Attack:'
                    '\nBeginning at 1st level, you know how to strike subtly and exploit a foe’s distraction.'
                    '\nOnce per turn, you can deal an extra 1d6 damage to one creature you hit with an attack if you have advantage on the attack roll.'
                    'The attack must use a finesse or a ranged weapon.'
                    '\nYou don’t need advantage on the attack roll if another enemy of the target is within 5 feet of it,'
                    'that enemy isn’t incapacitated, and you don’t have disadvantage on the attack roll.'
                    '\n'
                    '\nThieves Cant:'
                    '\nDuring your rogue training you learned thieves’ cant, a secret mix of dialect,'
                    'jargon, and code that allows you to hide messages in seemingly normal conversation.'
                    '\nOnly another creature that knows thieves’ cant understands such messages.'
                    'It takes four times longer to convey such a message than it does to speak the same idea plainly.'
                    '\n'
                    '\nCunning Action:'
                    '\nStarting at 2nd level, your quick thinking and agility allow you to move and act quickly.'
                    '\nYou can take a bonus action on each of your turns in combat.'
                    'This action can be used only to take the Dash, Disengage, or Hide action.'
                    '\n'
                    '\nUncanny Dodge:'
                    '\nStarting at 5th level, when an attacker that you can see hits you with an attack,'
                    'you can use your reaction to halve the attack’s damage against you.'
                    '\n'
                    '\nEvasion:'
                    '\nBeginning at 7th level, you can nimbly dodge out of the way of certain area effects,'
                    'such as an ancient red dragon’s fiery breath or an ice storm spell.'
                    '\nWhen you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage,'
                    '\nyou instead take no damage if you succeed on the saving throw, and only half damage if you fail.'
                    '\n'
                    '\nReliable Talent:'
                    '\nBy 11th level, you have refined your chosen skills until they approach perfection.'
                    '\nWhenever you make an ability check that lets you add your proficiency bonus,'
                    'you can treat a d20 roll of 9 or lower as a 10'
                    '\n'
                    '\nBlindsense:'
                    '\nStarting at 14th level, if you are able to hear,'
                    'you are aware of the location of any hidden or invisible creature within 10 feet of you.'
                    '\n'
                    '\nSlippery Mind:'
                    '\nBy 15th level, you have acquired greater mental strength. You gain proficiency in Wisdom saving throws.'
                    '\n'
                    '\nElusive:'
                    '\nBeginning at 18th level, you are so evasive that attackers rarely gain the upper hand against you.'
                    'No attack roll has advantage against you while you aren’t incapacitated'
                    '\n'
                    '\nStroke of Luck:'
                    '\nAt 20th level, you have an uncanny knack for succeeding when you need to.'
                    'If your attack misses a target within range, you can turn the miss into a hit.'
                    '\nAlternatively, if you fail an ability check, you can treat the d20 roll as a 20.'
                    'Once you use this feature, you can’t use it again until you finish a short or long rest.'
                    '\n'
                    '\nAbility Score Increases at levels: 4, 8, 10, 12, 16, 19.'}
subclasses = {'rogue(assassin)': '\nAssassin Archetype'
                                 '\n'
                                 '\nBonus Proficiencies:'
                                 '\nWhen you choose this archetype at 3rd level, you gain proficiency with the disguise kit and the poisoner’s kit'
                                 '\n'
                                 '\nAssassinate:'
                                 '\nStarting at 3rd level, you are at your deadliest when you get the drop on your enemies.'
                                 '\nYou have advantage on attack rolls against any creature that hasn’t taken a turn in the combat yet.'
                                 '\nIn addition, any hit you score against a creature that is surprised is a critical hit'
                                 '\n'
                                 '\nInfiltration Expertise:'
                                 '\nStarting at 9th level, you can unfailingly create false identities for yourself.'
                                 '\nYou must spend seven days and 25 gp to establish the history, profession, and affiliations for an identity.'
                                 '\nYou can’t establish an identity that belongs to someone else.'
                                 '\nFor example, you might acquire appropriate clothing, letters of introduction,'
                                 '\nand official-looking certification to establish yourself as a member of a trading house'
                                 '\nfrom a remote city so you can insinuate yourself into the company of other wealthy merchants.'
                                 '\n'
                                 '\nImpostor:'
                                 '\nAt 13th level, you gain the ability to unerringly mimic another person’s speech, writing, and behavior.'
                                 '\nYou must spend at least three hours studying these three components of the person’s behavior,'
                                 '\nlistening to speech, examining handwriting, and observing mannerisms'
                                 '\n'
                                 '\nDeath Strike:'
                                 '\nStarting at 17th level, you become a master of instant death.'
                                 '\nWhen you attack and hit a creature that is surprised, it must make a Constitution saving throw (DC 8 + your Dexterity modifier + your proficiency bonus).'
                                 '\nOn a failed save, double the damage of your attack against the creature.',
              'rogue(thief)': '\nThief Archetype'
                              '\n'
                              '\nFast Hands:'
                              '\nStarting at 3rd level, you can use the bonus action granted by your Cunning Action to make a Dexterity (Sleight of Hand)'
                              '\ncheck, use your thieves’ tools to disarm a trap or open a lock, or take the Use an Object action.'
                              '\n'
                              '\nSecond-Story Work'
                              '\nWhen you choose this archetype at 3rd level, you gain the ability to climb faster than normal;'
                              '\nclimbing no longer costs you extra movement.'
                              '\nIn addition, when you make a running jump, the distance you cover increases by a number of feet'
                              '\nequal to your Dexterity modifier.'
                              '\n'
                              '\nSupreme Sneak:'
                              '\nStarting at 9th level, you have advantage on a Dexterity (Stealth) check if you move no more than half your speed on the same turn.'
                              '\n'
                              '\nUse Magic Device:'
                              '\nBy 13th level, you have learned enough about the workings of magic that you can improvise the use of items even when they are not intended for you.'
                              '\nYou ignore all class, race, and level requirements on the use of magic items'
                              '\n'
                              '\nThiefs Reflexes:'
                              '\nWhen you reach 17th level, you have become adept at laying ambushes and quickly escaping danger.'
                              '\nYou can take two turns during the first round of any combat.'
                              '\nYou take your first turn at your normal initiative and your second turn at your initiative minus 10.'
                              '\nYou can’t use this feature when you are surprised.'}
#################################################################
mainFrame = LabelFrame(root, text="Choose your race and gender.") # Frame for housing all main functions (drop down menus and buttons)
mainFrame.grid(row=0, column=0) # Setting it on a grid

raceLabel = Label(mainFrame, text="Click and select race") # Label for the race drop down
raceLabel.pack() # Packing
defRace = StringVar() # Setting the default var type
defRace.set("None") # Default variable to be displayed when nothing is chosen by user
race_box = OptionMenu(mainFrame, defRace,"High Elf", "Wood Elf", "Hill Dwarf", "Mountain Dwarf", "Human") # Drop down box with race choices for user
race_box.pack()# Packing

genderLabel = Label(mainFrame, text="Select gender") # Label for the gender drop down
genderLabel.pack() # Packing
defGender = StringVar() # Setting the default var type
defGender.set("None") # Default variable to be displayed when nothing is chosen by user
gender_box = OptionMenu(mainFrame, defGender,"Male", "Female", "Other") # Drop down with gender choices for user
gender_box.pack() # Packing

classLabel = Label(mainFrame, text="Select Class") # Label for class drop down
classLabel.pack() # Packing
defClass = StringVar() # Setting the default var type
defClass.set("None") # Default variable to be displayed when nothing is chosen by user
class_box = OptionMenu(mainFrame, defClass, "Rogue (Assassin)", "Rogue (Thief)") # Drop down with class choices for user
class_box.pack() # Packing
#################################################################
resultFrame1 = LabelFrame(root, text="Your character is a...") # Setting a frame to house the race and subclass details
resultFrame1.grid(row=0, column=0) # Placing it on a grid
resultFrame2 = LabelFrame(root, text="Class is...") # Setting a frame to house the class details
resultFrame2.grid(row=0, column=1) # Placing it on a grid

def characterGet(): # Making a function
    if defRace.get() == "High Elf": # Checks the relevant selection by user
        myLabel = Label(resultFrame1, text="High elf - As a high elf," # Applies relevant text (THIS APPLIES TO EVERYTHING IN THIS FUNCTION)
                                          " you have a keen mind and a mastery of at least the basics of magic.\n"
                                          "Traits:\n " + traits['darkvision'] + traits['keen senses'] + traits['fey ancestry']
                         + traits['trance'] + traits['int increase'] + traits['elf weapon training']).pack()
    if defRace.get() == "Wood Elf":
        myLabel = Label(resultFrame1, text="Wood elf - As a wood elf, you have keen senses and intuition,\n"
                                          " and your fleet feet carry you quickly and stealthily through your native forests."
                                          "Traits: " + traits['darkvision'] + traits['keen senses'] + traits['fey ancestry']
                         + traits['trance'] + traits['wis increase'] + traits['fleet of foot'] + traits['mask of the wild']).pack()
    if defRace.get() == "Hill Dwarf":
        myLabel = Label(resultFrame1, text="Hill Dwarf - As a hill dwarf, you have keen senses,"
                                          " deep intuition, and remarkable resilience.\nTraits: " + traits['darkvision'] +
                        traits['dwarven resilience'] + traits['dwarven combat training'] + traits['tool proficiency'] +
                        traits['stonecutting'] + traits['dwarven toughness']).pack()
    if defRace.get() == "Mountain Dwarf":
        myLabel = Label(resultFrame1, text="Mountain Dwarf - As a mountain dwarf, you’re strong and hardy,"
                                          " accustomed to a difficult life in rugged terrain.\nTraits:" + traits['darkvision'] +
                        traits['dwarven resilience'] + traits['dwarven combat training'] + traits['tool proficiency'] +
                        traits['stonecutting'] + traits['dwarven armor training']).pack()
    if defRace.get() == "Human":
        myLabel = Label(resultFrame1, text="Human - Humans are the most adaptable and ambitious people among the common races.\nTraits:"
                         + traits['ability increase'] ).pack()
    if defGender.get() == "Male":
        myLabel = Label(resultFrame1, text="Gender: Male").pack()
    if defGender.get() == "Female":
        myLabel = Label(resultFrame1, text="Gender: Female").pack()
    if defGender.get() == "Other":
        myLabel = Label(resultFrame1, text="Gender: Other").pack()
    if defClass.get() == "Rogue (Assassin)":
        myLabel = Label(resultFrame2, text=classes['rogue']).pack()
    if defClass.get() == "Rogue (Assassin)":
        myLabel = Label(resultFrame1, text=subclasses['rogue(assassin)']).pack()
    if defClass.get() == "Rogue (Thief)":
        myLabel = Label(resultFrame2, text=classes['rogue']).pack()
    if defClass.get() == "Rogue (Thief)":
        myLabel = Label(resultFrame1, text=subclasses['rogue(thief)']).pack()

# Making a button that calls to the character get function for user to press when done with selection
resultButton = Button(mainFrame, text="Show character", command=characterGet)
resultButton.pack() # Packing

root.mainloop() # tkinter loop