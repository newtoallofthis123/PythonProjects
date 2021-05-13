print("Guess")
secret_word = "Apple"
user_guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while user_guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
            user_guess = input("Enter your guess")
            guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses")
else:
    print("You won")
