#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        while True:
            choice = input("Rock, paper, scissors? \n")
            if choice.lower() in["rock", "paper", "scissors"]:
                return choice

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class ultimate_strategy:
    def move(self):
        return "rock"

    def learn(self, mo_move, their_move):
        pass

class cpu:
    def move(self):
        choice = random.choice(moves)
        return choice

    def learn(self, mo_move, their_move):
        pass


class reflectplayer:

    def learn(self, my_move, their_move):
        self.pmove = their_move

    def move(self):
        choice = random.choice(moves)
        try:
            return self.pmove
        except AttributeError:
            return choice


class cycleplayer:

    def learn(self, my_move, their_move):
        self.pmove = my_move

    def move(self):
        choice = random.choice(moves)
        return choice


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print("** PLAYER ONE WINS **")
            return "one"
        else:
            if move1 == move2:
                print("** TIE **")
            else:
                print("** PLAYER TWO WINS **")
                return "two"

    def play_game(self):
        self.p1_score = 0
        self.p2_score = 0
        print("Game start!")
        round = 1
        while True:
            print(f"Round {round}:")
            result = self.play_round()
            if result == "one":
                self.p1_score += 1
            elif result == "two":
                self.p2_score += 1
            print(f"Score: Player One {self.p1_score}, Player Two {self.p2_score}")
            if self.p1_score == 3 or self.p2_score == 3:
                print("We have a winner!")
                if self.p1_score > self.p2_score:
                    print("Player One is the Champion!")
                    break
                else:
                    print("Player Two is the Champion!")
                    break
            round += 1
        print("Game over!")


def rematch():
    print("Rematch?")
    option = input("y / n \n")
    if option == "n":
        print("Thank you For Playing!")
        exit()
    elif option == "y":
        return
    else:
        rematch()


if __name__ == '__main__':
    print("Rock Paper Scissors, Go")
    while True:
        p1 = Player()
        p2 = reflectplayer()
        option = random.randint(0, 4)
        if option == 0:
            p2 = cpu()
        elif option == 1:
            p2 = reflectplayer()
        elif option == 2:
            p2 = cycleplayer()
        else:
            p2 = ultimate_strategy()

        game = Game(p1, p2)
        game.play_game()
        rematch()
