import os


def ping()->bool:
    hostname = "google.com"
    response = os.system('ping -c 1' + hostname)

    if response is 1: return True




