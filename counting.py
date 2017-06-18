#Jim Vargas counting
import string

def LetterTable(phrase):
    compare = (string.ascii_uppercase + string.ascii_lowercase + 
    " " + string.digits + string.punctuation)
    table = ""
    for letter in range(len(compare)):
        if phrase.count(compare[letter]) > 0:
            table = ("'"+compare[letter]+"'") + '\t' + str(phrase.count(compare[letter]))
            print(table)


def check():
    print("Do you want to continue?")
    thing = input("Y or N?"+'\n'+">>> ")
    if (thing == "Y") or (thing == "y"):
        main()
    elif (thing == "N") or (thing == "n"):
        print("Quitting...")
        exit()
    elif len(thing) == 0:
        print("You didn't enter anything.")
        print("Quitting...")
        exit()
    elif len(thing) > 1:
        print("The program needs a one letter anser.", '\n')
        check()
    else:
        print("You entered something invalid.")
        print("Quitting...")
        exit()

def main():
    TheString = input("Input your string:"+'\n'+">>> ")
    if len(TheString) == 0:
        print("You didn't input anything.", '\n')
        check()
    else:
        LetterTable(TheString)


if __name__ == '__main__':
    main()