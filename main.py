# Main file for the test UI

import wx, time
from MainFrame import MainFrame
from Serial import SerialComms
from threading import Thread


def serial_poll_thread(serial):
    while True:
        serial.serial_check()
        time.sleep(0.1)


def main():
    serial = SerialComms()

    app = wx.App()
    frame = MainFrame(serial)
    frame.Show()

    new_thread = Thread(target=serial_poll_thread, args=(serial,))
    new_thread.start()

    app.MainLoop()


if __name__ == '__main__':
    main()
