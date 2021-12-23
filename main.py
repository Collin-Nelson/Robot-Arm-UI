# Main file for the test UI

import wx
from MainFrame import MainFrame
from Serial import SerialComms

def main():
    app = wx.App()
    frame = MainFrame()
    frame.Show()

    app.MainLoop()  # These two loops might interfere with each other and other processes and might need to be their own threads
    while True:
        SerialComms.SerialCheck()
        SerialComms.SerialWrite("print pos")
        SerialComms.SerialWrite("LS status")


if __name__ == '__main__':
    main()
