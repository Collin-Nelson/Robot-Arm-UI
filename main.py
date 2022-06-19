import wx, time
from main_frame import main_frame
from serial import serial_comms
from threading import Thread

def serial_poll_thread(serial):
    while True:
        try:
            serial.serial_check()
        except:
            print("Tried reading a line")
            time.sleep(2)

        time.sleep(0.1)

def main():
    serial = serial_comms()

    app = wx.App()
    frame = main_frame(serial)
    frame.Show()

    new_thread = Thread(target=serial_poll_thread, args=(serial,))
    new_thread.start()

    app.MainLoop()

if __name__ == '__main__':
    main()
