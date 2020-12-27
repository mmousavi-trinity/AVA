from skpy import Skype


user, pswd = "marcusmousavi@outlook.com", "automatedavaaccount2019"
switch = False
sk = Skype(user, pswd)
ch = sk.contacts["live:fe9ecd3affa68bdd"].chat

command = ch.getMsgs()
stringCommand = str(command)
toList = stringCommand.split(",")
content = str([x for x in toList if x in "content"])

print (content)
