#Sort of completed, but design can always be improved
import random 

def main():
    print("Welcome to a game of Rock, Paper, Scissors!\n")
    print("Type 'r' for rock, 'p' for paper, 's' for scissors\n")
    
    playing = True
    
    while playing:
        while True:
            x = input("Rock, Paper or Scissors? ")
            if x in ['r', 'p', 's']:
                break
            else:
                print("Please type in r, p or s")
                continue

        #Tie
        n = computer_play()
        if x == n:
            print(f"Computer chose: {n}")
            print("It's a tie!")
            break
        #You win
        if x == 'r' and n == 's':
            print(f"Computer chose: {n}")
            print("You win!")
            break
        if x == 's' and n == 'p':
            print(f"Computer chose: {n}")
            print("You win!")
            break
        if x == 'p' and n == 'r':
            print(f"Computer chose: {n}")
            print("You win!")
            break
        #You lose
        if x == 'r' and n == 'p':
            print(f"Computer chose: {n}")
            print("You lose!")
            break
        if x == 'p' and n == 's':
            print(f"Computer chose: {n}")
            print("You lose!")
            break
        if x == 's' and n == 'r':
            print(f"Computer chose: {n}")
            print("You lose!")
            break

def computer_play():
    string = "rps"
    n = random.choice(string)
    return n

main()

# hello
