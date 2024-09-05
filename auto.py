import time
import pyautogui
import pydirectinput
import keyboard

user_input = input("What key to press? ")
loop_length = input("How many times? ")
user_sleep = input("How long between each key press (in seconds)? ")

running = True
x = 0

def countdown(user_input, loop_length, user_sleep):
    count = range(5, 0, -1)
    for num in count:
        print(f"{num}")
        time.sleep(1)
    print(f"Pressing '{user_input}' {loop_length} times with {user_sleep} seconds in between, starting in 5 seconds!")
    time.sleep(5)
    
countdown(user_input,loop_length,user_sleep)

def press_user_defined_key(user_input,loop_length,user_sleep):
    pydirectinput.press(user_input)
    print(user_input)
    time.sleep(int(user_sleep))
    
def quit():
    pydirectinput.press("f8")
    pydirectinput.write("quit")
    pydirectinput.press("enter")
start = time.perf_counter()
while running == True:
    press_user_defined_key(user_input,loop_length,user_sleep)
    x += 1
    if x == int(loop_length):
        print("Loop finished!")
        break
    else:
        continue
stop = time.perf_counter()

print(f"This ran for {stop-start} seconds")
