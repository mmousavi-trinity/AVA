import AVA
import main
import colors

## reminders is a dictionary of tuples containing a string mapping to a list of reminders
reminders = {"":[]}

class Reminder:

    def __init__(self,note):
        self.note = note




def reminder():

    command =input(colors.OKGREEN+ "Would you like to make, get, update, or delete a reminder? " + colors.OKEND)

    if 'make' in command:
            setReminder()
    elif 'delete' in command:
            deleteReminder()
    elif 'get' in command:
            getReminder()
    elif 'update' in command:
            updateReminder()
    else:
        leave = input("Would you like to go back to general use?(y/n)\n")
        if leave is 'n':
            command
        elif 'y':
             return
        else: "y or n response only"



def setReminder():
    date = input("Please enter date in the following format: mm/dd/yyyy")

    if verify_date(date) is False:
        print("I am sorry please try again" + date)
    else:
        reminder = input("Please type the reminder. Time is preferable")

        if reminders.__contains__(date) is True:

             reminders[date] +  [reminder]
             return
        else:
            reminders[date] = reminder
            return


def getReminder():
    date = input("Please enter date in the following format: mm/dd/yyyy")

    if verify_date(date) is False:
        print("I am sorry please try again" + date)
    else:
        reminder_list = reminders[date]

        for rem in reminder_list:

            print("Here are your reminders for today: ")
            print(rem + "\n")
        return


def updateReminder():
    date = input("Please enter date in the following format: mm/dd/yyyy")

    return


def deleteReminder():

    return


def setBirthday():
    return

def birthdays():
    return

def verify_date(input_str):

        if len(input_str) != 10:
            return False
        if input_str[2] != "/" or input_str[5] != "/":
            return False
        checks = 0
        for i in range(1, 32):
            if i >= 10:
                if str(i) == input_str[:2]:
                    checks = 1
                    break
            else:
                if ('0' + str(i)) == input_str[:2]:
                    checks = 1
                    break

        if checks == 0:
            return False

        for i in range(1, 13):
            if i >= 10:
                if str(i) == input_str[3:5]:
                    checks = 2
                    break
            else:
                if ('0' + str(i)) == input_str[3:5]:
                    checks = 2
                    break

        if checks == 1:
            return False

        for i in range(2016, 3000):
            if str(i) == input_str[-4:]:
                checks = 3
                break
        if checks == 2:
            return False
