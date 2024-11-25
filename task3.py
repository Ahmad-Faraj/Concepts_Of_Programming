import random

def scramble(word) :
    n = len(word)
    visited = [False] * n
    scrambled_word = [""] * n
    remain = n
    while remain > 0 :
        random_index = random.randint(0,n-1)
        if not visited[random_index] :
            scrambled_word[random_index] = word[n - remain]
            visited[random_index] = True
            remain -= 1
    return "".join(scrambled_word)

def word_scramble_game() :
    word = ["DP" , "Trees" , "range" , "graph"]
    original_word = random.choice(word)
    scrambled_word = scramble(original_word)
    print(f"your scrabmled word is {scrambled_word} \n")
    attempts = 5

    while attempts > 0 :
        guess = input("type your guess ")

        if not guess :
            print("invalid guess try again \n")
            continue

        if guess == original_word :
            print("congrate you won")
            return
        else :
            attempts -= 1;
            print(f"wrong guess {attempts} left\n")

        if(attempts == 0) :
            print(f"you lost the correct answer was {original_word}")
            return

word_scramble_game()