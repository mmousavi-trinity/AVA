import nltk

# from Speech import speak
# from files import open_folder
# import firefox
# from pdf import fn_open_pdf, fn_close_pdf
import os
import time, datetime
# import reminder
import terminal
from terminal import speak
import sys
import colors
import ping
import wikipedia
import datetime
from search import googleSearch, goToSite
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.tokenize import TreebankWordTokenizer



tokenizer = TreebankWordTokenizer()
questions = ["who","what","where","why","how","when"]

def ava(string):
    command = tokenizer.tokenize(string)
    stop_words = set(stopwords.words('english'))

    filtered_command = [w for w in command if w not in stop_words]
    print(filtered_command)

    if 'terminal' in filtered_command:
        if filtered_command.index('open') < filtered_command.index('terminal'):
            terminal.terminal()
        elif filtered_command.index('close') < filtered_command.index('terminal'):
            sys.exit
        else: terminal.speak("Do you want to open a terminal window? Enter 'open terminal' ")

    elif 'shutdown' in filtered_command:
        terminal.speak('Would you like me to shutdown the system?')
        confirm = input(
            colors.bcolors.YELLOW + " Would you like me to shutdown the system? \n(y/n)?: " + colors.bcolors.ENDC)
        if confirm == 'y':
            os.system("sudo shutdown -h now")
        else:
            return

    elif 'restart' in filtered_command:
        terminal.speak('Would you like me to restart the system?')
        confirm = input(
            colors.bcolors.YELLOW + " Would you like me to restart the system? \n(y/n): " + colors.bcolors.ENDC)
        if confirm == 'y':
            os.system("sudo reboot")
        else:
            return

    elif (set(questions) & set(filtered_command)) in set(questions):
          if ping() is True:
            confirm = input("Would you like me to provide a wikipedia summary for your question? \n (y/n): ")
            if confirm is "y":
                page = wikipedia.page(filtered_command)
                return page.content    #prints a summary of wiki article
            else:
                pass
            ##or say
          else: print("The internet does not seem to be working")

    elif 'update' in filtered_command:
          if('libraries' in filtered_command):
              ans = input("Would you like me to check and update your python libraries?\n(y/n): ")
              ###run through txt or csv and see if any libraries need to be updated
              if ans is 'y':
                    return
              else: return

          elif('system' in filtered_command):
              ans = input("Would you like me to check and update your system?\n(y/n):")
              if (ans is 'y'):
                  speak("Ok, updating operating system")
                  os.system('sudo softwareupdate -i -a')
              else: speak("okay")
    elif('reminder' in filtered_command):
              ##
              return
    elif 'time' in filtered_command:
              now = datetime.datetime.now()
              speak(" Current time is d% hours d% minutes" % (now.hour, now.minute))
              print(" Current time is d% hours d% minutes" % (now.hour, now.minute))
    elif('search' in filtered_command):
              filtered_command = [x for x in filtered_command if x is not 'search']
              newCommand = " ".join(filtered_command)
              googleSearch(newCommand)
    else:
        pass
