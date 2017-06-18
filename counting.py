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


def main():
    TheString = input("Input your string:"+'\n'+">>> ")
    #test = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."
    #LetterTable(test)
    if len(TheString) == 0:
        print("You didn't input anything.")
    else:
        LetterTable(TheString)


if __name__ == '__main__':
    main()