import os
import colorama
import time
import random
import sys
import math
from colorama import init, Fore, Back, Style
import itertools
import string
import re
import getpass

def clear():
    print('\033[H\033[J', end='')
clear()

def b(s, color=Fore.BLUE, brightness=Style.BRIGHT, **kwargs):
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)

def r(s, color=Fore.RED, brightness=Style.BRIGHT, **kwargs):
  print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)

def space():
    print (" ")

def sleep():
    time.sleep(0.1)
FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
BRIGHTNESS = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]
init()
clear()

def convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time taken = {0} Hours: {1} Minutes: {2} Seconds".format(int(hours),int(mins),sec))

def restart():      
    clear()
    logo = '''\u001b[34m
 /$$$$$$$                        /$$                     /$$$$$$$$                                     
| $$__  $$                      | $$                    | $$_____/                                     
| $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$       | $$     /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$ 
| $$$$$$$  /$$__  $$| $$  | $$|_  $$_/   /$$__  $$      | $$$$$ /$$__  $$ /$$__  $$ /$$_____/ /$$__  $$
| $$__  $$| $$  \__/| $$  | $$  | $$    | $$$$$$$$      | $$__/| $$  \ $$| $$  \__/| $$      | $$$$$$$$
| $$  \ $$| $$      | $$  | $$  | $$ /$$| $$_____/      | $$   | $$  | $$| $$      | $$      | $$_____/
| $$$$$$$/| $$      |  $$$$$$/  |  $$$$/|  $$$$$$$      | $$   |  $$$$$$/| $$      |  $$$$$$$|  $$$$$$$
|_______/ |__/       \______/    \___/   \_______/      |__/    \______/ |__/       \_______/ \_______/
                                                                                                   
'''
    print(logo)
    b("Welcome to the Brute Force Password Cracker, by derpydrag0nite")
    sleep()
    space()
    b("(1) - Start Cracking")
    sleep()
    space()
    b("(2) - Help")
    sleep()
    space()
    b("(3) - Information")
    sleep()
    space()
    b("(4) - Credits")
    space()
    cho = input()
    
    if cho == "1":
      clear()
      print("(1) - Any Password")
      space()
      print("(2) - Custom Cracking")
      space()
      pas = input()
      if pas == "1":
          clear()
          print("Would you like to print the guess each time? (This will make the process slower) [Y/N]")
          prp = input()
          prpc = prp.capitalize()
          if prpc == "Y":
              s = 1
              clear()
          else:
              s = 0
              clear()
          clear()

          print ("Would you like to know how many tries were taken? (This will make the process slower) [Y/N]")
          twt = input()
          twtc = twt.capitalize()
          if twtc == "Y":
              tw = "1"
          else:
              tw = "0"
          clear()
          password = input("Type your password: ")
          clear()
          if password == " ":
              print("No password entered")
              time.sleep(1)
              restart()
          print ("Cracking" ,(password), ". . .")
          print("Feel free to leave this tab/window open, as this may take a while.")
          def crack(password):
              clear()
              all = ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghigjklmnopqrstuvwxyz~`!@#$%^&*()-_=+[]'""{}\|,<>./?;:1234567890")
              tries = 0
              guess = (" ")
              import time
              start = time.time()
              while guess != password:
                  for password_length in range(1,9999999999999999999999999999999999999):
                      for guess in itertools.product(all, repeat=password_length):
                          if tw == "1":
                              tries += 1
                          guess = ''.join(guess)
                          if s == 1:
                              print (guess)
                          if guess == password:
                              clear()
                              if tries == 0:
                                  tries = ("---")
                              end = time.time()
                              time = end - start
                              if tw == "1":
                                  psec = tries/time
                                  ipsec = int(psec) 
                                  pps = (round(ipsec))
                              else:
                                  pps = ("---")
                              convert(time)
                              
                              print('Password:',guess,"/","Found in",tries,'tries')
                              print("Passwords per second:",pps) 
                              space()
                              res = input("Restart? [Y/N] ")
                              rest = res.capitalize()
                              if rest == "Y":
                                  restart()  
                              else:
                                  exit()
          crack(password)
      if pas == "2":  
          def custom():
              nomatch = 0
              uppercase = False
              lowercase = False
              numbers = False
              symbols = False
              customl = (" ")
              upperl = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
              lowerl = ("abcdefghigjklmnopqrstuvwxyz")
              numl = ("1234567890")
              syml = ("~`!@#$%^&*()-_=+[]'""{}\|,<>./?;:")
            
              clear()
              print("Does it contain uppercase letters? [Y/N]")
              uc = input()
              uc = uc.capitalize()
              if uc == "Y":
                  uppercase = True
              clear()
              print("Does it contain lowercase letters? [Y/N]")
              lc = input()
              lc = lc.capitalize()
              if lc == "Y":
                  lowercase = True
              clear()
              print("Does it contain numbers? [Y/N]")
              nc = input()
              nc = nc.capitalize()
              if nc == "Y":
                  numbers = True
              clear()
              print("Does it contain symbols? [Y/N]")
              sc = input()
              sc = sc.capitalize()
              if sc == "Y":
                  symbols = True
              clear()
              
              print("Type your password: ")
              password = input()
                    
              if uppercase == True and ("A" in password or "B" in password or "C" in password or "D" in password or "E" in password or "F" in password or "G" in password or "H" in password or "I" in password or "J" in password or "K" in password or "L" in password or "M" in password or "N" in password or "O" in password or "P" in password or "Q"  in password or "R" in password or "S" in password or "T" in password or "U" in password or "V" in password or "W" in password or "X" in password or "Y" in password or "Z" in password) == False:
                  nomatch = 1
                
              if lowercase == True and ("a" in password or "b" in password or "c" in password or "d" in password or "e" in password or "f" in password or "g" in password or "h" in password or "i" in password or "j" in password or "k" in password or "l" in password or "m" in password or "n" in password or "o" in password or "p" in password or "q"  in password or "r" in password or "s" in password or "t" in password or "u" in password or "v" in password or "w" in password or "x" in password or "y" in password or "z" in password) == False:
                  nomatch = 1
                
              if numbers == True and ("1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password or "0" in password) == False:
                  nomatch = 1
                
              if symbols == True and ("~" in password or "`" in password or"!" in password or "@" in password or "#" in password or "$" in password or "%" in password or "^" in password or "&" in password or "*" in password or "(" in password or ")" in password or "-" in password or "_" in password or "=" in password or "+" in password or "[" in password or "]" in password or "'" in password or '"' in password or "{" in password or "}" in password or "/" in password or "|" in password or "," in password or "<" in password or ">" in password or "." in password or "?" in password or ";" in password or ":" in password) == False: 
                  nomatch = 1
                
              if uppercase == False and ("A" in password or "B" in password or "C" in password or "D" in password or "E" in password or "F" in password or "G" in password or "H" in password or "I" in password or "J" in password or "K" in password or "L" in password or "M" in password or "N" in password or "O" in password or "P" in password or "Q" in password or "R" in password or "S" in password or "T" in password or "U" in password or "V" in password or "W" in password or "X" in password or "Y" in password or "Z" in password) == True:
                  nomatch = 1
                
              if lowercase == False and ("a" in password or "b" in password or "c" in password or "d" in password or "e" in password or "f" in password or "g" in password or "h" in password or "i" in password or "j" in password or "k" in password or "l" in password or "m" in password or "n" in password or "o" in password or "p" in password or "q" in password or "r" in password or "s" in password or "t" in password or "u" in password or "v" in password or "w" in password or "x" in password or "y" in password or "z" in password) == True:
                  nomatch = 1
              if numbers == False and ("1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password or "0" in password) == True:
                  nomatch = 1
                
              if symbols == False and ("~" in password or "`" in password or"!" in password or "@" in password or "#" in password or "$" in password or "%" in password or "^" in password or "&" in password or "*" in password or "(" in password or ")" in password or "-" in password or "_" in password or "=" in password or "+" in password or "[" in password or "]" in password or "'" in password or '"' in password or "{" in password or "}" in password or "/" in password or "|" in password or "," in password or "<" in password or ">" in password or "." in password or "?" in password or ";" in password or ":" in password) == True: 
                  nomatch = 1
                
              if nomatch == 1:
                  print("Password does not match custom settings.")
                  time.sleep(2)
                  custom()
              if uppercase == True:
                  customl = (customl+upperl)
                  customl = ''.join(customl)
              if lowercase == True:
                  customl = (customl+lowerl)
                  customl = ''.join(customl)
              if symbols == True:
                  customl = (customl+syml)
                  customl = ''.join(customl)
              if numbers == True:
                  customl = (customl+numl)
                  customl = ''.join(customl)
              
              print (customl)
              clear()
              print("Would you like to print the guess each time? (This will make the process slower) [Y/N]")
              prp = input()
              prpc = prp.capitalize()
              if prpc == "Y":
                  s = 1
                  clear()
              else:
                  s = 0
                  clear()
              clear()
    
              print ("Would you like to know how many tries were taken? (This will make the process slower) [Y/N]")
              twt = input()
              twtc = twt.capitalize()
              if twtc == "Y":
                  tw = "1"
              else:
                  tw = "0"
              clear()
              print("Cracking",'(',password,')',". . .")
              print("Feel free to leave this tab/window open, as this may take a while.")
              def crack(password):
                  clear()
                  all = customl
                  tries = 0
                  guess = (" ")
                  import time
                  start = time.time()
                  while guess != password:
                      for password_length in range(1,9999999999999999999999999999999999999):
                          for guess in itertools.product(all, repeat=password_length):
                              if tw == "1":
                                  tries += 1
                              guess = ''.join(guess)
                              if s == 1:
                                  print (guess)
                              if guess == password:
                                  clear()
                                  if tries == 0:
                                      tries = ("---")
                                  end = time.time()
                                  time = end - start
                                  if tw == "1":
                                      psec = tries/time
                                      ipsec = int(psec) 
                                      pps = (round(ipsec))
                                  else:
                                      pps = ("---")
                                  convert(time)
                                  print('Password:',guess,"/","Found in",tries,'tries')
                                  print("Passwords per second:",pps) 
                                  space()
                                  res = input("Restart? [Y/N] ")
                                  rest = res.capitalize()
                                  if rest == "Y":
                                      restart()  
                                  else:
                                      exit()
              crack(password)
          custom()

    if cho == "2":
        clear()
        r("This is a Brute Force Password Cracker which tries every possible combination until the password is found. You can choose [Any password] which will crack any password. [Custom Cracking] let's you choose what characters are used in the password to maximize efficiency.")
        r("There are also settings that let you choose from good experience or max efficiency")
        space()
        print ("Back? [Y/N]")
        back = input()
        backc = back.capitalize()
        if backc == "Y":
            restart()
        else:
            exit()
    if cho == "3":
        clear()
        r("Cracking speed increases with the Hacker Plan.")
        r("If you don't activate the [Tries] counter, you will not get passwords per second.")
        r("A password with space cannot be cracked.")
        r("A password with \ can also for whatever reason not be cracked.")
        r("If something shows (---), it means you may have turned off a setting that requires those values.")
        r("I did not add a checker that looks for easy password such as ABC, as the whole program breaks.")
        r("Thank you for using this program.")
        space()
        print ("Back? [Y/N]")
        back = input()
        backc = back.capitalize()
        if backc == "Y":
            restart()
        else:
            exit()
    if cho == "4":
        clear()
        r("All code is by the one and only derpydrag0nite.")
        space()
        print ("Back? [Y/N]")
        back = input()
        backc = back.capitalize()
        if backc == "Y":
            restart()
        else:
            exit()
restart()
