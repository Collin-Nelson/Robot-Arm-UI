# File to handle all of the serial communication with the robot arm

import wx, serial, queue, time
from AngleDisplayPanel import AngleDisplayPanel





class SerialComms:
    def __init__(self):

        print("init SerialComms")

        self.queue = queue.Queue()
        self.waiting = False
        # Start serial connection - uncomment lines below when hardware connected
        self.ser = serial.Serial('COM3', 9600, timeout=1)

    def pass_angle_display_panel(self, angle_disp_panel):
        global angle_display_panel
        angle_display_panel = angle_disp_panel

    def on_timer(self):
        self.serial_check()
        self.serial_write("print pos")
        self.serial_write("LS status")

        # wx.CallLater(self, 1000, self.on_timer(), self)

    # Function periodically called to check if there is anything waiting to be read from the serial connection and
    # read it in if so
    def serial_check(self):
        print("Serial Check")
        if self.ser.in_waiting > 0:
            self.serial_read()

    # Function to write lines to the serial com
    def serial_write(self, string):
        if self.waiting:  # If the arm is waiting for a command, send the command, if not, add it to the queue
            my_str = string.encode('utf-8')
            self.ser.write(my_str)
            self.waiting = False
            print("Command '", string, "' sent \n")
        else:
            self.queue.put(string)
            print("Command '", string, "' added to queue \n")

    # Function to force send the next command in the serial command queue
    def serial_force_send(self):
        if self.queue.empty():
            print("Queue is empty")
        else:
            string = self.queue.get()
            my_str = string.encode('utf-8')
            self.ser.write(my_str)
            print("Command '", string, "' forcibly sent \n")

    # Function to read lines from the serial com
    def serial_read(self):
        self.waiting

        print("Reading from serial")

        line = self.ser.readline()
        print(line)

        # if move is received, send the next command from the queue. If there is no command,
        # set the bool waiting to true to indicate the next command should be sent immediately
        head, sep, tail = line.partition(bytes(': ', 'utf-8'))
        if line == "Move?":
            if self.queue.empty():
                self.waiting = True
            else:
                string = self.queue.get()
                self.ser.write(string)
                print("Command '", string, "' sent from queue")

        # if position reports are received (After sending "print pos" to the robot arm), update the positions in the UI
        elif head == "Stepper 1":
            # Set position field for J1 in the UI to be tail
            AngleDisplayPanel.set_joint_angle(angle_display_panel, 1, tail)
        elif head == "Stepper 2":
            # Set position field for J2 in the UI to be tail
            AngleDisplayPanel.set_joint_angle(angle_display_panel, 2, tail)
        elif head == "Stepper 3":
            # Set position field for J3 in the UI to be tail
            AngleDisplayPanel.set_joint_angle(angle_display_panel, 3, tail)
        elif head == "Stepper 4":
            # Set position field for J4 in the UI to be tail
            AngleDisplayPanel.set_joint_angle(angle_display_panel, 4, tail)
        elif head == "Stepper 5":
            # Set position field for J5 in the UI to be tail
            AngleDisplayPanel.set_joint_angle(angle_display_panel, 5, tail)
        elif head == "Stepper 6":
            # Set position field for J6 in the UI to be tail
            AngleDisplayPanel.set_joint_angle(angle_display_panel, 6, tail)

        # if limit switch reports are received, update the UI to show which are triggered and which are not
        elif head == "LS1":
            # Set LS status for J1 in the UI
            AngleDisplayPanel.set_ls_status_light(angle_display_panel, 1, tail)
        elif head == "LS2":
            # Set LS status for J2 in the UI
            AngleDisplayPanel.set_ls_status_light(angle_display_panel, 2, tail)
        elif head == "LS3":
            # Set LS status for J3 in the UI
            AngleDisplayPanel.set_ls_status_light(angle_display_panel, 3, tail)
        elif head == "LS4":
            # Set LS status for J4 in the UI
            AngleDisplayPanel.set_ls_status_light(angle_display_panel, 4, tail)
        elif head == "LS5":
            # Set LS status for J5 in the UI
            AngleDisplayPanel.set_ls_status_light(angle_display_panel, 5, tail)
        elif head == "LS6":
            # Set LS status for J6 in the UI
            AngleDisplayPanel.set_ls_status_light(angle_display_panel, 6, tail)
