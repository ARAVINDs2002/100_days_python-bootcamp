import random as rn

hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\  |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      /    |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      / \  |
           |
    """,
]

word_list = ["apple", "mango"]
lives = 6
chosen_word = rn.choice(word_list)
blankspace = ["_" for _ in chosen_word]

print(" ".join(blankspace))
game_over = False

while not game_over:
    guess = input("Enter a letter guess: ").lower()

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                blankspace[i] = guess
    else:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")
        print(hangman_stages[6 - lives])

    print(" ".join(blankspace))

    if "_" not in blankspace:
        game_over = True
        print("Congratulations! You win.")
    elif lives == 0:
        game_over = True
        print(f"You lose! The word was '{chosen_word}'.")
