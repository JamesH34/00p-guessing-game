import random
class GuessingGame():

    def __init__(self, answer):
        self.answer = answer
        print("Guess the number I am thinking of, or else: ")

    def guess(self):
        user_guess = int(input("Enter your guess: "))
        return user_guess
    
    def compare_answer(self, player_guess):
        if player_guess == self.answer:
            print(f"Congrats brother/sister! {player_guess} was the number! You win absolutely nothing.")
            return True
        elif player_guess > self.answer:
            print(f"Oof, {player_guess} is a little too large there big dog. Try again: ")
        else:
            print(f"You gotta go bigger than {player_guess} gamer. Guess again: ")


random_answer = random.randint(1, 100)

game = GuessingGame(random_answer)

user_guess = game.guess()

game.compare_answer(user_guess)

while True:
    user_guess = game.guess()
    if game.compare_answer(user_guess):
        break