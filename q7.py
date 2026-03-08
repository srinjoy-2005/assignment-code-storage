import os

filepath = input("Enter base address");

def findfiles(filepath):
    try:
        for item in os.listdir(filepath):
            address = os.path.join(filepath, item)
            print(os.path.abspath(address))

            if os.path.isdir(address):
                print(os.path.abspath(address))
                findfiles(address)
    except PermissionError:
        pass

findfiles(filepath)