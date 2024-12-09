print("Welcome to the Hangman Guessing Game")
print("Can you guess the following characters from the Bible?")
import random

words = ("hezekiah","isaiah","daniel","zerubabel","david","hosea","jeremiah","balaam")

#dictionary of key:()
hangamn_art = {0:("   ",
                  "    ",
                  "     "),
               1:(" o  ",
                  "    ",
                  "     "), 
               2:(" o  ",
                  " |  ",
                  "     "),
               3:(" o  ",
                  "/|  ",
                  "     "),
               4:(" o  ",
                  "/|\\  ",
                  "     "),
               5:(" o  ",
                  "/|\\  ",
                  "/     "),
               6:(" o  ",
                  "/|\\  ",
                  "/  \\  ")}

def display_hangman(wrong_guess):
    for line in hangamn_art[wrong_guess]:
        print(line)


def display_hint(hint):
    print(" ".join(hint))

def display_ans(ans):
    print(" ".join(ans))

def main():
    ans = random.choice(words)
    hint = ["_"] * len(ans)
    wrong_guess = 0
    guessed_letters = set()
    is_running = True


    while is_running:
        display_hangman(wrong_guess)
        display_hint(hint)
        guess = input("Enter a letter:").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Null Input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed..")
            continue

            guessed_letters.add(guess)

        if guess in ans:
             for i in range(len(ans)):
                 if ans[i] == guess:
                      hint[i] = guess

        else:
            wrong_guess += 1

        if "_" not in hint:
            display_hangman(wrong_guess)
            display_ans(ans)
            print("Congraa o!!, You Win")
            is_running = False
        elif wrong_guess >= len(hangamn_art) - 1:
            display_hangman(wrong_guess)
            display_ans(ans)
            print("sorry, you lose!")
            is_running = False
        
               
    

if __name__ == "__main__":
    main()
    