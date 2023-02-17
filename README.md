# Rock-Paper-Scissors-Game-Python-
A simple game of Rock Paper Scissors in Python (User vs AI). Python libraries used: random

## Thoughts on starting this project
My very first programming project, in Python! Gotta start somewhere, right?

As a coder just starting out, I thought that making the first program that seems fun is important, hence I thought that my first project would be a simple game.

<br>

Computer program used for coding: VS Code

## Code description
Let's start with:
1. Imported Libraries
2. Self-defined functions
3. Main code

<br>

<br>

**1. Imported Libraries**
```python
import random
```
Importing the 'random' library.

<br>

<br>

**2. Self-defined functions**
```python
def computer_play():
    string = "rps"
    n = random.choice(string)
    return n
```
The 'computer_play()' function is to get a random, computer-generated input, either the letter 'r', 'p' or 's' that would be defined as rock, paper and scissors respectively in the program.

<br>

Returns the generated input back to the main code.

<br>

<br>

**3. Main code**
```python
def main():
    print("Welcome to a game of Rock, Paper, Scissors!\n")
    print("Type 'r' for rock, 'p' for paper, 's' for scissors\n")
```
Mainly to print out aesthetics and instructions on what the user should be typing in to play the game.

<br>
    
```python
    playing = True
    
    while playing:
        while True:
            x = input("Rock, Paper or Scissors? ")
            if x in ['r', 'p', 's']:
                break
            else:
                print("Please type in r, p or s")
                continue
```
The main while loop that will keep running to get input from user, as well as checking if that input is the desired input. Otherwise, the code will keep looping until the user gives the desired input, 'r', 'p' and 's'.

<br>

```python
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
```
Depending on the user input and computer input, 1 of these if loops will run as they are guided by the conditions. Tie, Win and Lose has 3 possible scenarios of them occuring as displayed above, and will tell the user which of the 3 scenarios has occured.

## Output
```
Welcome to a game of Rock, Paper, Scissors!

Type 'r' for rock, 'p' for paper, 's' for scissors

Rock, Paper or Scissors? s
Computer chose: p
You win!
```
(Tie and Lose has a different output)

## Thoughts after the project
The aim was for this project is to firstly to make things work, try my best to make it well designed and concise, and bug proof as well.

<br>

To be improved:
* Too many if loops to check for Win, Lose and Tie, should be possible to shorten them
* Like all code, more features can definitely be added to make the game more interactive such as making it with GUI, with a score counter

<br>

Side note: I have yet to figure out why typing out this description of my code require coding and abit of HTML :weary: , took me  while to type this out.

Documentations to type out README.mds: 
* https://about.gitlab.com/handbook/markdown-guide/#:~:text=To%20insert%20images%20to%20your,ALT%5D(%2Fpath%2Fimage.
* https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md#table-of-contents (emoji documentation)

Have a gif:

![Semantic description of image](https://media.tenor.com/fTTVgygGDh8AAAAM/kitty-cat-sandwich.gif "Image Title")
