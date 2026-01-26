def make_hangman(secret_word):
    guesses=[]

    def hangman_closure(letter):
        if len(letter) == 1:
            guesses.append (letter.lower())
        else:
            print("You can enter only one letter. ")
            return False
        
        guess=""
        for ch in secret_word:
            if ch.lower() in guesses:
                guess+=ch
            else:
                guess+="_"
        print(guess)
        if "_" in guess:
            return False
        else:
            print("You win!")
            return True
    return hangman_closure

def game():
    stop = False
    print("Set a secret: ")
    play_game = make_hangman(input())
    while not stop:
        print("Make a guess or enter 'exit_game': ")
        letter = input()
        if letter == 'exit_game':
            stop = True
        else:
            stop = play_game(letter)
        
game()