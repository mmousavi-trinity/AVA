

class bcolors:

    ENDC = '\033[0m'

    def __init__(self, color):
          self.color = color


    def printColor(self, string):
        ##applies color and ending to string
        string = self.color + string + bcolors.ENDC
        print (string)

purple = bcolors('\033[95m')
purple.printColor("Testing")

blue = bcolors('\033[94m')

blue.printColor("Testing")

green = bcolors('\033[92m')
yellow = bcolors('\033[93m')
red = bcolors('\033[91m')
bold = bcolors('\033[1m')
underline = ('\033[4m')