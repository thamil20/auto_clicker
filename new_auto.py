import time
import pydirectinput
import argparse

class AutoClicker:
    def __init__(self, user_input, loop_length, user_sleep):
        try:
            loop_length = int(loop_length)
            user_sleep = int(user_sleep)
        except ValueError:
            raise ValueError("Loop length and user sleep must be integers.")
        self.user_input = user_input
        self.loop_length = loop_length
        self.user_sleep = user_sleep
        self.x = 0
        print(f"Initialized AutoClicker with key: {user_input}, loops: {loop_length}, sleep: {user_sleep}")

    def press_user_defined_key(self):
        pydirectinput.press(self.user_input)
        print(self.user_input)
        time.sleep(self.user_sleep)
    
    def run(self):
        start = time.perf_counter()
        print("Starting in 5 seconds...")
        time.sleep(5)
        try:
            for _ in range(self.loop_length):
                self.press_user_defined_key()
                self.x += 1
        except ValueError as e:
            print(f"An error occurred during execution: {e}")
        
        stop = time.perf_counter()
        print(f"This ran for {stop-start} seconds")

parser = argparse.ArgumentParser(description="Automated Key Presser")
parser.add_argument("key", type=str, help="The key to press")
parser.add_argument("loops", type=int, help="Number of times to press the key")
parser.add_argument("sleep", type=int, help="Seconds to wait between key presses")
args = parser.parse_args()

if __name__ == "__main__":
    try:
        if not args.key or not args.loops or not args.sleep:
            user_input = input("What key to press? ")
            loop_length = input("How many times? ")
            user_sleep = input("How long between each key press (in seconds)? ")
            auto_clicker = AutoClicker(user_input, loop_length, user_sleep)
        else:
            auto_clicker = AutoClicker(args.key, args.loops, args.sleep)
            auto_clicker.run()
    except ValueError as e:
        print(f"\nAn error occurred: {e}")
        
    