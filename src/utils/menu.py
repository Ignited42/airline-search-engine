# Authors: Mark, Steven, Yuuki
# Description:
#   Basic text menu to run functionality

def run_main_menu():
    stopMenu = False

    while stopMenu != True:
        print("""
1.
2.
3.
"""
        )

        userInput = input()


        # Break
        if userInput == str(0):
            break