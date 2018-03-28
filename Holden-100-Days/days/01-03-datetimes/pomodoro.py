""" Pomodoro Timer
    By: Holden Daugherty
    This is my pomodoro timer program I made for the #100 Days of Code Challenge by Talk Python and Pybites.
    This program uses the datetime and time packages and I also used the os package to speak to the user. Currently
    the os.system lines will only work on a Mac. I'm not sure how to do that in windows or linux but found that
    seen that there are various different ways to accomplish this. For now you will have to comment those out. """

import time
from datetime import datetime
from datetime import timedelta
import os


print("This is the pomodoro timer. The goal is to dedicate a complete pomodoro(in this case 25 minutes) "
      "to your task and then take a short break(3 minutes). After the fourth cycle of this then you can "
      "take an extended break (15 minutes)")
marks = 0


def pomodoro():
    print("Begin your task.")
    os.system('say "Begin your task"')  # Comment these lines out unless your using a Mac
    current = datetime.now()  # Gets the current local time
    stopping_time = timedelta(seconds=3)  # Determines how long the timer will last, can be changed as needed
    ending_time = current + stopping_time
    while datetime.now() < ending_time:
        time.sleep(1)


def short_break():
    print("Take a short break")
    os.system('say "Take a short break"')
    current = datetime.now()
    stopping_time = timedelta(seconds=1)
    ending_time = current + stopping_time
    while datetime.now() < ending_time:
        time.sleep(1)


def long_break():
    print("Take a long break and decide if you need to continue")
    os.system('say "Take a long break, and decide if you shall continue!"')
    current = datetime.now()
    stopping_time = timedelta(seconds=2)
    ending_time = current + stopping_time
    while datetime.now() < ending_time:
        time.sleep(1)


def end():
    exit()

    # I wanted the user to be able to start the timer each time so I used input
    # Also be sure to enter the correct numbers or it will throw an error

start = input("Decide on a task to complete.\nPress 1 and Enter to start the timer!\n"  
              "Press 2 and Enter to exit the program!")
if int(start) == 1:
    while marks < 4:
        marks += 1
        pomodoro()
        short_break()
        next_cycle = input("Press 1 and then Enter to restart your timer\n"
                           "Press 2 and Enter to exit the program")
        if int(next_cycle) == 1:
            print("Continue!")
        else:
            end()
    long_break()
    print("Nice session! Goodbye!")


elif int(start) == 2:
    end()
else:
    print("Next time read the instructions!!!")
    end()
