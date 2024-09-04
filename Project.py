
import json


fin=open("dictionary.json","r")

cont = json.load(fin)


def dispwords():
    letter=input('Enter The Letter To Display That Word With which It Begins With: ')
    for i in cont:
        if i.startswith(letter):
            print(i)



def findword():
    word = input('Enter The word to Check in the Dictionary: ').lower()
    found = False
    for i in cont:
        if i == word:
            found = True
    if found == False:
        print("There Exist No such Word In The Dictionary!")
    else:
        print("It Is There In the Dictionary!")


def dispm():
    word=input("Enter the Word to Check the Meaning of: ").lower()
    found = False
    for key,value in cont.items():
        if key == word:
            found = True
            print("{} Word has Meaning {}".format(key,value))
    if found == False:
        print("No Such Word Exist")


while True:
    
    
          print('''
               I N T E R A C T I V E    D I C T I O N A R Y
              =================================================
              1. Display The Words That Begin With a Specific Letter
              2. Find a Specific Word
              3. Display The Meaning Of The Specific Word
              4. Exit
              ''')

          choice=int(input('Enter your Choice of Operation: '))
          if choice == 1:
                 dispwords()
          elif choice == 2:
                   findword()
          elif choice == 3:
                  dispm()
          elif choice == 4:
                exit
else:
    print("Invalid Number! Enter your Choice of Operation: ")