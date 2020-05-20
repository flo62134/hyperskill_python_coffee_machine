CORRECT_LETTER = 'C'
INCORRECT_LETTER = 'I'
MAX_MISTAKES = 3
GAME_OVER_MESSAGE = 'Game over'
VICTORY_MESSAGE = 'You won'

scores = input().split()
# put your python code here

mistakes = 0
score = 0


def end_game(is_victory):
    if is_victory:
        print(VICTORY_MESSAGE)
        print(score)
    else:
        print(GAME_OVER_MESSAGE)
        print(score)


for char in scores:
    if char == CORRECT_LETTER:
        score += 1
    elif char == INCORRECT_LETTER:
        mistakes += 1

    if mistakes == MAX_MISTAKES:
        end_game(is_victory=False)
        break

if mistakes < MAX_MISTAKES:
    end_game(is_victory=True)
