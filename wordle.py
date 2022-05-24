import urllib.request
import random
import sys
from colorama import Fore, Back, Style
import re

l1 = []
z = 0
answer  = ""
sol = ""
flag = False
c = 0

def rules():
	print("\n\033[1mHOW TO PLAY\033[0m\n\n")
	print("Each guess must be a valid five-letter word. Hit the enter button to submit.")

	print("After each guess, the color of the tiles will change to show how close your guess was to the word.\n\n")

	print("\033[1mExamples\033[0m\n")
	for k in "weary":
		if k=="w":
			print(Fore.WHITE + Back.GREEN + " " +k.upper()+ " ", end = " ")
			print(Style.RESET_ALL, end = " ")
		else:
			print(Fore.WHITE + Back.BLACK + " " +k.upper()+ " ", end = " ")
			print(Style.RESET_ALL, end = " ")
	print("\n")
	print("The letter \033[1mW\033[0m is in the word and in the correct spot.")
	print("\n")
	for k in "pills":
		if k=="i":
			print(Fore.WHITE + Back.YELLOW + " " +k.upper()+ " ", end = " ")
			print(Style.RESET_ALL, end = " ")
		else:
			print(Fore.WHITE + Back.BLACK + " " +k.upper()+ " ", end = " ")
			print(Style.RESET_ALL, end = " ")
	print("\n")
	print("The letter \033[1mI\033[0m is in the word but in the wrong spot.")
	print("\n")
	for k in "vague":
		if k=="u":
			print(Fore.WHITE + " " +k.upper()+ " ", end = " ")
			print(Style.RESET_ALL, end = " ")
		else:
			print(Fore.WHITE + Back.BLACK + " " +k.upper()+ " ", end = " ")
			print(Style.RESET_ALL, end = " ")
	print("\n")
	print("The letter \033[1mU\033[0m is not in the word in any spot.")
	print("\n")

def words():
	url = "https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt"
	file = urllib.request.urlopen(url)
	global l1
	for line in file:
		decoded_line = line.decode("utf-8")
		l1.append(decoded_line.strip())
	global z
	z = random.randint(0, len(l1)-1)

def count(wordcheck):
	let_freq = {}
	for i in wordcheck:
	    if i in let_freq:
	        let_freq[i] += 1
	    else:
	        let_freq[i] = 1
	return let_freq

def check_input(i):
	global answer
	answer = " " 
	print("\033[1mGUESS ", i+1, "\033[0m")	
	answer = input("GUESS THE WORD OR TYPE \033[1mHELP\033[0m TO SEE THE RULES ").lower()
	if answer == "help":
		rules()
		check_input(i)
	elif len(answer)!=5:
		print("\n\033[1mLength should be equal to 5\033[0m\n")
		check_input(i)
	elif re.search("[0-9]", answer):
		print("\n\033[1mNo numbers allowed\033[0m\n")
		check_input(i)
	elif re.search("[^a-zA-Z0-9]", answer):
		print("\n\033[1mNo special characters allowed\033[0m\n")
		check_input(i)	
	elif answer not in l1:
		print("\n\033[1mNOT IN WORD LIST\033[0m\n")
		check_input(i)

def guess():
	global answer
	global sol
	global c
	for i in range(6):
		check_input(i)
		val = sol
		sol_dic = count(sol)
		green = {}
		for k in range(5):
			if answer[k] == sol[k]:
				green[k] = sol[k]
				sol_dic[answer[k]] = sol_dic[answer[k]]-1
		for k in range(5):
			if answer[k] == sol[k]:

				print(Fore.WHITE + Back.GREEN + " " +answer[k].upper()+ " ", end = " ")
				print(Style.RESET_ALL, end = " ")
			elif answer[k] in sol and sol_dic[answer[k]] > 0:
				print(Fore.WHITE + Back.YELLOW + " " +answer[k].upper()+ " ", end = " ")
				print(Style.RESET_ALL, end = " ")
				sol_dic[answer[k]] = sol_dic[answer[k]]-1
			elif answer[k] not in sol or(answer[k] in sol and sol_dic[answer[k]] ==0):
				print(Fore.WHITE + " " +answer[k].upper()+ " ", end = " ")
				print(Style.RESET_ALL, end = " ")
		print(Style.RESET_ALL)		
		sol = val
		print("\n")
		c+=1
		if answer == sol:
			global flag
			flag = True
			if c ==1 :
				compliment("Genius")
			elif c ==2 :
				compliment("Magnificient")
			elif c ==3 :
				compliment("Impressive")
			elif c ==4 :
				compliment("Splendid")
			elif c ==5 :
				compliment("Great")
			elif c ==6 :
				compliment("Phew")
			else:
				compliment(sol)
			sys.exit(0)
		answer = ""

def compliment(text):
	print(Style.BRIGHT)
	print(Fore.GREEN + text, end = " ")
	print(Style.RESET_ALL, end =" ")
	print("\n")

def final():
	print("The correct word is ", end=" ")
	compliment(sol)
	print("\n")

def main():
	rules()
	words()
	global sol
	sol =l1[z]
	guess()
	if not flag:
		final()

if __name__=="__main__":
	main()
