'''
The purpose of this program is to show how honey encryption
works. Given any password, the program should be able to
give the user a selection of manipulated passwords (sweet
words). If the sweet word is entered, then the program will
trigger an alarm. Of course, the correct password will
not trigger the alarm.

Current issues:
-certain false passwords are not displaying false data when
 they should
-more modularized code is needed
-debugging at line 133 is needed

Created by:    Victor Nguyen
Updated on:    12/12/2016
'''
import random
from pprint import pprint

# Function prototyping
def validate(char):
    # Input validation
	while char != 'Y' and char != 'y' and char != 'N' and char != 'n':
            char = input("Would you like to enter another inquiry? (Y/N) ")

# Prompts user and defines variables
while True:
    userPass = input("Please enter a password: ")
    message = input("Please enter a secret message to store (one word): ")
    passwordsToSeeds = {}   # dictionary
    seedsToMessages = {}    # dictionary
    trueSeed = random.randint(10, 27)    # Random seed value
    states = {  # U.S States as secret messages
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    ' Verify input with the user '
    print("Your password is " + userPass
          + ", your seed value is " + str(trueSeed)
          + ", and your secret message is " + message
          + "\n=====================================")

    # Seed generator + Sweetwords generator
    # Manipulate the password input by the user
    #   Add a string to that password
    #   Seeds should remain as integers that
    #   be converted into binary digits
    passwordsToSeeds[userPass] = trueSeed
    seedsToMessages[trueSeed] = message

    passwordsToSeeds[userPass + str(trueSeed - 1)] = trueSeed + 1
    seedsToMessages[trueSeed + 1] = states['AL']

    passwordsToSeeds[userPass + str(trueSeed - 2) + "1"] = trueSeed + 2
    seedsToMessages[trueSeed + 2] = states['CA']

    passwordsToSeeds[userPass.lower()] = trueSeed + 3
    seedsToMessages[trueSeed + 3] = states['FL']

    passwordsToSeeds[userPass.lower() + str(trueSeed + 1) + "3"] = trueSeed + 4
    seedsToMessages[trueSeed + 4] = states['TX']

    passwordsToSeeds[userPass.upper()] = trueSeed + 5
    seedsToMessages[trueSeed + 5] = states['TN']

    passwordsToSeeds[userPass.upper() + str(trueSeed + 2) + "5"] = trueSeed + 6
    seedsToMessages[trueSeed + 6] = states['WA']

    # ENCRYPTION: c = sk XOR sm
    cipher = int(passwordsToSeeds[userPass]) ^ trueSeed

    # Shuffle the passwords and display them on the screen to begin the game
    passwords = list(passwordsToSeeds.keys())
    random.shuffle(passwords)                   # Shuffle the passwords
    pprint(passwords)                           # Display results

    # Prompt the user to crack this password
    try:
        query = input("Enter a password to crack: ")
        keySeed = passwordsToSeeds[query]
        # DECRYPTION: m = sk XOR c
        m = keySeed ^ cipher                        # ^ == XOR

        if m != trueSeed:                       # Honey checker
            print("Intruder! SOUNDING ALARM!")  # If seeds don’t match, this is an intruder

        # Check seeds
        pprint(seedsToMessages[m])
    except KeyError:
        print("Password not found. ")

    # Prompt the user to try another password
    retry = input("Would you like to enter another inquiry (Y/N):  ")
    validate(retry)  # Validates input

    # Ends program by breaking out of the loop
    if retry == 'N' or retry == 'n':
        break

# Goodbye message
print("\nThank you for testing Honey Encryption")

'''
    DEBUGGING

    print(str(cipher) + "\n" +
          str(int(passwordsToSeeds[userPass])) + "\n" +
          str(trueSeed))
    print("\n" + str(m) + "\n" +
          str(keySeed) + "\n" +
          str(cipher))

    for x in seedsToMessages.keys():           # Display results
        print(str(x) + "\t" + str(seedsToMessages[x]))
'''
