# Main file for the test UI

import wx
from MainFrame import MainFrame
from Serial import SerialComms


def main():
    app = wx.App()
    frame = MainFrame()
    frame.Show()

    serial = SerialComms()
    # serial.on_timer()

    app.MainLoop()


if __name__ == '__main__':
    main()
