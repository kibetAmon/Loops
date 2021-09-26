def searchname():
    infile = open("names.txt", "r")
    first_letter = input("Enter the search letter: ")
    for s in infile:
        if s[0].lower() == first_letter.lower():
            print(s)

def search_age():
    infile = open("names.txt", "r")
    age = input("Enter the search age: ")
    for s in infile:
        name_age = s.split()
        if int(name_age[1]) == int(age):
            print(s)


searchname()
search_age()