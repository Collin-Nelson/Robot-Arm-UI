# Main file for the test UI

import wx
from MainFrame import MainFrame
from Serial import SerialComms


def main():
    serial = SerialComms()

    app = wx.App()
    frame = MainFrame(serial)
    frame.Show()

    app.MainLoop()


if __name__ == '__main__':
    main()
