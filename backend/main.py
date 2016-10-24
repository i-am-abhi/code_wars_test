import os
import sys
import json

def main():
	choice = showMenu()
	while choice!=4:
		if choice==1:
			print("Call function to create user\n")
		elif choice==2:
			print("Call function to edit user\n")
		elif choice==3:
			print("Call function to show leaderboard\n")
		else:
			print("Invalid option\n")
		choice = showMenu()


def showMenu():
	print("Menu :")
	print("1) Create user")
	print("2) Edit user")
	print("3) Show leaderboard")
	print("4) Exit")
	print("Enter your choice (1-4) :")
	choice = int(input())
	return choice


def printDataFile():
	file_name = 'data.json'
	with open(file_name) as f:
		data = json.load(f)
	print(json.dumps(data, indent=2, sort_keys=True))


main()