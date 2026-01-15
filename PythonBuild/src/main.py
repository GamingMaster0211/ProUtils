import tkinter
import pymsgbox
import traceback
import UtilSource
import ReCoreLib

BUILD_VERSION = "1.9.8 Release"

def __init__():
    def check_version():
        if BUILD_VERSION:
            print(f"ProUtils | Python Edition | Build {BUILD_VERSION} Loaded Successfully.")

    check_version()

    pymsgbox.alert(ReCoreLib.START_MESSAGE_BOX_TEXT, title="ProUtils | Loading Edition | Build 1.3.0", button="OK")
    
__init__()

UtilEorBoolean = False
BUTTON_TEXT_EOR_OFF = "Execute On Run: Off"
BUTTON_TEXT_EOR_ON = "Execute On Run: On"

def eor_toggle():
    global UtilEorBoolean
    current_text = UtilEor.cget("text")
    new_text = BUTTON_TEXT_EOR_ON if current_text == BUTTON_TEXT_EOR_OFF else BUTTON_TEXT_EOR_OFF
    UtilEor.config(text=new_text)

    if new_text == BUTTON_TEXT_EOR_ON: 
        UtilEorBoolean = True
    if new_text == BUTTON_TEXT_EOR_OFF: 
        UtilEorBoolean = False

def create_util():
    try:
        global UtilEorBoolean
        NewUtilName = UtilName.get("1.0", tkinter.END).strip()
        NewUtilFactor = UtilFactor.get("1.0", tkinter.END).strip()
        NewUtilEor = UtilEorBoolean

        NewUtil = UtilSource.__polishutil__(NewUtilName, NewUtilFactor, "uc", NewUtilEor)
        NewUtilResult = NewUtil()
        print({NewUtilResult})
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()

def help_menu():
    pymsgbox.alert(ReCoreLib.WINDOW_HELP_MENU_TEXT, title="ProUtils | Help Edition | Build 1.1.9", button="OK")

Window = tkinter.Tk()
UtilName = tkinter.Text(Window)
UtilFactor = tkinter.Text(Window)
UtilEor = tkinter.Button(Window, text="Execute On Run: Off", command=eor_toggle)
UtilCreate = tkinter.Button(Window, text="Create Utility", command=create_util)
Help = tkinter.Button(Window, text="Help Menu", command=help_menu)

UtilName.place(x=10, y=10, width=200, height=30)
UtilFactor.place(x=10, y=50, width=200, height=30)
UtilEor.place(x=10, y=90, width=200, height=30)
UtilCreate.place(x=10, y=130, width=200, height=30)
Help.place(x=10, y=170, width=200, height=30)

Window.title(f"ProUtils | Python Edition | Build {BUILD_VERSION}")
Window.resizable(False, False)
Window.geometry("225x212")

Window.mainloop()

ReCoreLib.LOADER()
