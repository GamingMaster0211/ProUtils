###########################################
#                                         #
#   ReCoreLib made by GamingMaster0211.   #
#                                         #
#   Made using ProUtils Python Edition    ###########################
#                                                                   #
#   ReCoreLib is a library made on January 14, 2026.                #
#   ReCoreLib is a DETICATED library to ProUtils Python Edition.    #
#                                                                   #
#   License is in the README.md file.   #############################
#                                       #
#########################################

#####################################################################
#                                                                   #
#   This library is a core component of ProUtils Python Edition     #
#   text handling. Please do not tamper with this file unless you   #
#   have EXPLICIT permission given by me. So please; No modding.    #
#                                                                   #
#####################################################################

RECORE_LOAD_MESSAGE = "ReCoreLib Loaded successfully."
RECORE___INIT___LOAD_MESSAGE = "ReCoreLib __init__ Loaded successfully."

print(RECORE_LOAD_MESSAGE)

class __ReCoreLib__:
    def __init__(self):
        print(RECORE___INIT___LOAD_MESSAGE)
        
    def __call__(self):
        print(f"ReCoreLib got called. Doing whatever utilsource.py, or main.py told ReCoreLib to do. Of course that is, with ReCoreLib's supported parameters or functions.")

LOADER = __ReCoreLib__()

PHC = "print('Utility Created. Writing this code to it to ensure proper compatability with project.')\n"
UPHC = "IPHDS = '[[[ I N S E R T E D   P L A C E H O L D E R   C O D E   S U C C E S S F U L L Y ]]]'\n"

UEOR = [
    PHC + "\n",
    UPHC + "\n",
    """import sys

# Execute On Run (EOR) | Auto-run when main.py or entry point is executed.

if __name__ == "__main__" or any(script.endswith(("main.py", "__main__.py", "run.py")) for script in sys.argv):
    print("Utility auto executed on run...")

    # Add auto run utility logic here.

# Add non auto run utility logic here.
"""
]

WINDOW_HELP_MENU_TEXT = "Instructions for ProUtils Python Edition use. \n\n Top text input box is for the utility name. \n\n Second text input box is for the utility factor. \n\n Execute On Run (EOR) runs the util whenever a entry point \n .py file is run within the same directory. \n\n The first button creates the utility file. \n\n The second button brings up this menu."
START_MESSAGE_BOX_TEXT = "I just want to say one thing before you launch. \nI HIGHLY advise you to run ProUtils from 'Visual Studio Code.' \nNot doing so can either lead to the program not working, or just \nstraight up not launching. If it still works for you, maybe it's okay. \n\n                                                           .   .\n                                                            U"
