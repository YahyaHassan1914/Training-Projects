import random
import collections

class DiceRollingSimulator:
    def __init__(self):
        self.dice_types = {
            'D4': 4,
            'D6': 6,
            'D8': 8,
            'D10': 10,
            'D12': 12,
            'D20': 20,
            'D100': 100
        }
        self.results = collections.defaultdict(list)

    def roll_dice(self, dice, rolls):
        if dice not in self.dice_types:
            raise ValueError("Invalid dice type")
        sides = self.dice_types[dice]
        self.results[dice] = [random.randint(1, sides) for _ in range(rolls)]

    def display_results(self):
        for dice, rolls in self.results.items():
            print(f"Results for {dice}:")
            print(f"{self.results[dice]}")
            counter = collections.Counter(rolls)
            for side in range(1, self.dice_types[dice] + 1):
                print(f"Side {side}: {counter.get(side, 0)} times")
            print(f"Total rolls: {len(rolls)}")
            print(f"Average roll: {sum(rolls)/len(rolls):.2f}")
            print("-" * 20)

    # def reset_results(self):
    #     self.results.clear()

def main():
    simulator = DiceRollingSimulator()
    print("Welcome to the Dice Rolling Simulator!")
    print("You can roll various types of dice (D4, D6, D8, D10, D12, D20, D100) and see detailed statistical results.")
    print("To start, enter the type of dice you want to roll and the number of rolls.")
    print("Enter 'q' at any time to quit.")
    
    while True:
        print("\nAvailable dice types:", ", ".join(simulator.dice_types.keys()))
        dice = input("Enter the type of dice to roll (or 'q' to quit): ").strip().upper()
        if dice == 'Q':
            break
        if dice not in simulator.dice_types:
            print("Invalid dice type. Please try again.")
            continue
        try:
            rolls = int(input(f"Enter the number of rolls for {dice}: "))
            if rolls <= 0:
                raise ValueError
        except ValueError:
            print("Invalid number of rolls. Please enter a positive integer.")
            continue

        simulator.roll_dice(dice, rolls)
        simulator.display_results()

        # reset = input("Do you want to reset results? (y/n): ").strip().lower()
        # if reset == 'y':
        #     simulator.reset_results()

if __name__ == "__main__":
    main()