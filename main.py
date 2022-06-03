import os
import subprocess
from os.path import exists

pathName: str

if __name__ == '__main__':
    import sys

    if len(sys.argv) <= 1:
        print("No path file found.")
        input()
        quit()

    pathName = sys.argv[1]

    if not exists(pathName):
        file = open(pathName, 'r')
        file.close()

    DETACHED_PROCESS = 0x00000008
    file = open(pathName, 'r')

    print("Opening files")

    length = file.readlines()
    if length == 0:
        print("No links found.")
        input()
        quit()

    file.seek(0, 0)
    for link in file.readlines():
        try:
            finalLink = link.replace('\n', '')
            print(finalLink)
            os.startfile(finalLink)
        except:
            print("Failed to open link.")

    input()
