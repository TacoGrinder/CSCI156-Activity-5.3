__author__ = 'ortus'


def menu():
    print("A. Input employee name."+"\n"+"B. Input a salary"+"\n"+"C.Input Date of Birth"+"\n"+"D. Exit")
    return input("What do you want to do?").upper()


def name():

    input("First Name:")
    input("Last Name:")


def salary():
    input("Enter Salary:")


def dob():
    input("Enter DOB:")


def ext():
    exit()


def empcomp():
    i = 1
    while i != 0:
        choice = menu()
        if choice == "A":
            name()
        if choice == "B":
            salary()
        if choice == "C":
            dob()
        if choice == "D":
            ext()

empcomp()
