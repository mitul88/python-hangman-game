import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list

stages = hangman_art.stages

logo = hangman_art.logo

display = []

lives = 6

end_of_game = False

chosen_word = random.choice(word_list)

print(logo)
print(f"This is to give a break. Your word is {chosen_word}")

word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"

print(display)

while not end_of_game:
    guess = input("Guess a letter").lower()
    if guess in display:
        print(f'you have already guessed "{guess}" before')

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives = lives - 1
        print(f'your guessed letter "{guess}" is not in the word!!!!')
        if lives == 0:
            print(stages[lives])
            print("You lose")
            end_of_game = True

    print(display)
    print(f"You have {lives} chances")
    print(stages[lives])
    if '_' not in display:
        end_of_game = True
        print("You win")
