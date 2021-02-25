# ROCK PAPER SCISSOR GAME
import random


def gamewin(you, computer):
    # all possibilities when computer choose r
    if you == computer:
        return None
    elif computer == 'r':
        if you == 'p':
            return False
        elif you == 's':
            return True

# all possibilities when computer choose p
        elif you == 'r':
            if computer == 'p':
                return False
            if you == 's':
                return True

    # all properties computer choose s
    elif you == 'r':
        if computer == 's':
            return False
        if you == 'p':
            return True


print("computer's turn : rock(r),paper(p),scissor(s)")
randNo = random.randint(1, 3)
if randNo == 1:
    computer = 'r'
if randNo == 2:
    computer = 'p'
elif randNo == 3:
    computer = 's'

you = input("your turn : rock(r),paper(p),scissor(s)  : ")
a = gamewin(you, computer)
print("you choose : {you}")
print("computer choose : {computer}")
if a == None:
    print("game is tie...!")
elif a:
    print("you win.......!")
elif a:
    print("computer win")
