VOWELS = 'aeiou'
VOWEL_MESSAGE = 'vowel'
CONSONANT_MESSAGE = 'consonant'

user_input = input()
for char in user_input:
    if not char.isalpha():
        break
    if char in VOWELS:
        print(VOWEL_MESSAGE)
    else:
        print(CONSONANT_MESSAGE)
