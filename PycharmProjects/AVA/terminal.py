import os

def terminal():
    """
    Opens the terminal.
    """
    print("You are into the terminal now."
        "Type 'exit' when you want to quit.")
    while True:
        command = input('User: ')   #modify
        if command.lower() == "exit":
            print("Quit terminal.")
            return
        else:
            os.system(command)
def speak(string):
    "the spaces make the pause longer before speaking"
    os.system("say     " + string)



