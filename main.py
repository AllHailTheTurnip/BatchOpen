# Written by @MightyTurnip.
# To use...
# Step 1: Package with pyinstaller as an .exe
# Step 2: Create a shortcut to the .exe
# Step 3: In target, add in-between double-quotes a link for the programs you want connected.
# Note: Each connected program needs a to be within its own double-quotes.

import os

if __name__ == '__main__':
    import sys

    # Check if list is empty or not.
    if len(sys.argv) <= 1:
        print("No links were provided.")
    else:
        DETACHED_PROCESS = 0x00000008
        for x in range(1, len(sys.argv)):
            # Open all links.
            try:
                os.startfile(sys.argv[x])
            except:
                print("Not a link.")
