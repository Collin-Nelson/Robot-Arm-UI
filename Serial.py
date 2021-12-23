# File to handle all of the serial communication with the robot arm

import serial, queue
from AngleDisplayPanel import AngleDisplayPanel

queue = queue.Queue()
waiting = False


class SerialComms:
    # Start serial connection - uncomment lines below when hardware connected
    # serial = serial.Serial('COM3', 9600, timeout=1)
    # serial.open()

    # Function periodically called to check if there is anything waiting to be read from the serial connection and read it in if so
    def SerialCheck():
        if serial.in_waiting > 0:
            self = SerialComms
            self.SerialRead()


    # Function to write lines to the serial com
    def SerialWrite(string):
        global waiting

        if waiting:  # If the arm is waiting for a command, send the command, if not, add it to the queue
            serial.write(string)
            waiting = False
            print("Command '", string, "' sent")
        else:
            queue.put(string)
            print("Command '", string, "' added to queue \n")

    # Function to read lines from the serial com
    def SerialRead(self):
        global waiting

        line = serial.readline()

        # if move is received, send the next command from the queue. If there is no command,
        # set the bool waiting to true to indicate the next command should be sent immediately
        head, sep, tail = line.partition(': ')
        if line == "Move?":
            if queue.empty():
                waiting = True
            else:
                string = queue.get()
                serial.write(string)
                print("Command '", string, "' sent from queue")

        # if position reports are received (After sending "print pos" to the robot arm), update the positions in the UI
        elif head == "Stepper 1":
            # Set position field for J1 in the UI to be tail
            AngleDisplayPanel.tc1.SetValue(tail)
        elif head == "Stepper 2":
            # Set position field for J2 in the UI to be tail
            AngleDisplayPanel.tc2.SetValue(tail)
        elif head == "Stepper 3":
            # Set position field for J3 in the UI to be tail
            AngleDisplayPanel.tc3.SetValue(tail)
        elif head == "Stepper 4":
            # Set position field for J4 in the UI to be tail
            AngleDisplayPanel.tc4.SetValue(tail)
        elif head == "Stepper 5":
            # Set position field for J5 in the UI to be tail
            AngleDisplayPanel.tc5.SetValue(tail)
        elif head == "Stepper 6":
            # Set position field for J6 in the UI to be tail
            AngleDisplayPanel.tc6.SetValue(tail)

        # if limit switch reports are received, update the UI to show which are triggered and which are not
        elif head == "LS1":
            # Set LS status for J1 in the UI
            if tail == 0:
                AngleDisplayPanel.statusLight1.SetBackgroundColour('white')
            elif tail == 1:
                AngleDisplayPanel.statusLight1.SetBackgroundColour('green')
        elif head == "LS2":
            # Set LS status for J2 in the UI
            if tail == 0:
                AngleDisplayPanel.statusLight2.SetBackgroundColour('white')
            elif tail == 1:
                AngleDisplayPanel.statusLight2.SetBackgroundColour('green')
        elif head == "LS3":
            # Set LS status for J3 in the UI
            if tail == 0:
                AngleDisplayPanel.statusLight3.SetBackgroundColour('white')
            elif tail == 1:
                AngleDisplayPanel.statusLight3.SetBackgroundColour('green')
        elif head == "LS4":
            # Set LS status for J4 in the UI
            if tail == 0:
                AngleDisplayPanel.statusLight4.SetBackgroundColour('white')
            elif tail == 1:
                AngleDisplayPanel.statusLight4.SetBackgroundColour('green')
        elif head == "LS5":
            # Set LS status for J5 in the UI
            if tail == 0:
                AngleDisplayPanel.statusLight5.SetBackgroundColour('white')
            elif tail == 1:
                AngleDisplayPanel.statusLight5.SetBackgroundColour('green')
        elif head == "LS6":
            # Set LS status for J6 in the UI
            if tail == 0:
                AngleDisplayPanel.statusLight6.SetBackgroundColour('white')
            elif tail == 1:
                AngleDisplayPanel.statusLight6.SetBackgroundColour('green')

        # Add other possibly returned text from the arm firmware here, such as when limit switches are pressed and
        # the current angle of the joints

    # Should move the event functions from the panel files to this file and include the Serial file in the panel files?
    # ^ Doesn't work, need to find a different method
