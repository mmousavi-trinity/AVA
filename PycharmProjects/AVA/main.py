# MAIN FILE

import os
import datetime
import random
import colors
import terminal
import AVA

input_string = ""


def main():
    greetings_path = os.getcwd() + "/Text_Files/greetings.txt"
    f_greetings = open(greetings_path, "r")
    greetings_list = f_greetings.read().strip().split("\n")
    f_greetings.close()
    random_greeting = random.randrange(0, len(greetings_list))

    #terminal.speak(greetings_list[random_greeting])


    farewell_path = os.getcwd() + "/Text_Files/farewell.txt"
    f_farewell = open(farewell_path, "r")
    farewell_list = f_farewell.read().strip().split("\n")
    f_farewell.close()
    farewell_list2 = [''.join(farewell_list[i]) + " ava" for i in range(0, len(farewell_list))]
    farewell_list3 = [''.join(farewell_list[i]) + " then" for i in range(0, len(farewell_list))]
    while 1:
        input_string = input('User: ')  # modify
        if input_string:
            input_string = input_string.lower()
            if input_string in greetings_list: print(random_greeting)

            elif input_string in farewell_list or \
                            input_string in farewell_list2 or \
                            input_string in farewell_list3:
                time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                if int(time_now[11:13]) > 20 or int(time_now[11:13]) < 4:
                    print(colors.bcolors.OKGREEN + "Goodnight." + colors.bcolors.ENDC)
                else:
                    print('See you later then! Have a good day!')
                return
            AVA.ava(input_string)


if __name__ == "__main__":
    main()