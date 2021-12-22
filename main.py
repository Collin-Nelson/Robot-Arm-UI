# Main file for the test UI

import wx
from MainFrame import MainFrame


def main():
    app = wx.App()
    frame = MainFrame()
    frame.Show()

    app.MainLoop()


if __name__ == '__main__':
    main()
