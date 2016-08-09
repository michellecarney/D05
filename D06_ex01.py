import os


def change_directory():
    current_directory = os.getcwd()
    change_desired = input(
        "Your current directory is {}. Do you want to change it?".format(current_directory))
    if change_desired == "yes":
        display_list()
        new_directory = input("Here is a list of subfolders. Please type the folder you want to change to: \n")
        os.chdir(current_directory + "/" + new_directory)
        new_directory = os.getcwd()
        print (new_directory)


def display_list():
    print(os.listdir())

change_directory()

def main():
    pass  # Call your functions here.

if __name__ == '__main__':
    main()