import string
import random

def main():
	print('\033[1;32;40m c'.center(300, random.choice(string.ascii_letters)))
while True:
	main()	
