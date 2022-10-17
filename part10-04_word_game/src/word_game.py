# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")
    
class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word)>len(player2_word):
            return 1
        elif len(player1_word)==len(player2_word):
            pass
        else: return 2



class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)


    def round_winner(self, player1_word: str, player2_word: str):
        vowels = "aeiou"
        counter1 = 0
        counter2 = 0
        for letter in player1_word:
            if letter in vowels:
                counter1+=1
        
        for letter in player2_word:
            if letter in vowels:
                counter2+=1
        
        if counter1>counter2:
            return 1
        elif counter1==counter2:
            pass
        else:
            return 2

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        allowed_words = ["rock", "paper", "scissors"]

        if player1_word not in allowed_words and player2_word not in allowed_words:
            pass
        elif player1_word not in allowed_words:
            return 2
        elif player2_word not in allowed_words:
            return 1
        
        if player1_word == "rock":
            if player2_word == "scissors":
                return 1
            elif player2_word == "paper":
                return 2
            else: 
                pass
        elif player1_word == "scissors":
            if player2_word == "rock":
                return 2
            elif player2_word == "paper":
                return 1
            else: 
                pass
        else: 
            if player2_word == "scissors":
                return 2
            elif player2_word == "rock":
                return 1
            else: 
                pass
        

if __name__=="__main__":
    p = RockPaperScissors(4)
    p.play()

