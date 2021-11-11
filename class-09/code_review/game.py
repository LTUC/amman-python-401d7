import collections

class Game:


    def __init__(self, roller=None):
        self.still_playing = True

    def play(self):
        print("Welcome message")
        res = input("Wanna play? ")
        if res == 'y' or 'yes':
            self.start_game()
        elif res == 'n' or 'no':
            print("Ok. Maybe another time")
        else:
            raise ValueError("You can only choose yes or no")

    def start_game(self):
        # Initialize Rounds
        # Set total
        self.round = 1
        while(self.still_playing):

            self.start_round(self.round)

            # When the user enters q, 
            # 1. Call quit game
            # 2. Set still_playing to False
            # 3. Break the current loop

    def check_if_ziltch(self, tuple_of_dice): # THIS CODE SHOULD BE IN game_logic
        """
        Optimal Solution: send dice to calculate score and if it's 0, it's a zilch
        """
        # if no 1,5 or any number that has 3 values and bove it's a ziltch
        ctr = collections.Counter(tuple_of_dice)
        if ctr[1] or ctr[5]:
            return False
        if ctr.most_common(1)[1] > 2:
            return False

        # if no 3 pairs 
        if ctr.most_common(1)[1] == 2 and len(ctr.most_common()) == 3: #  [(2,2),(4,2),(3,1), (6,1)]
            return False
        
        return True
            

    def start_round(self, round, num_of_dice=6):
        pass

    def quit_game(self):
        """
        This method will be called when the player type q
        """
        print("Total score")
        print("Thank you message")
