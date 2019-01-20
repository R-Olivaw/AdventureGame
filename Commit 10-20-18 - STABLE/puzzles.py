class simple_puzzle():
    def __init__(self):
        self.solved = False
        
    def quit_puzzle(self):
        print("DIDNDOITHERE5555!")
        return
        print("DIDNDOITHERE!")
        
    def activate(self):
        ans = input("What is brown and sticky? (Q to quit): ")
        if ans in ['q', 'Q']:
            self.quit_puzzle()
            print("DIDNDOIT")
        elif ans != "stick":
            print("\nNope!")
            return
        #When player enters correct phrase, this puts an item in their inventory and gives them gold.
        ##Then we set the puzzle to 'solved' so that it does not trigger again.
        else:
            print("\nYeah it is!")
            self.solved = True
            self.quit_puzzle()