# File to handle all of the serial communication with the robot arm

import serial, queue


class serial_comms:
    def __init__(self):

        self.queue = queue.Queue()
        self.waiting = True

        # Start serial connection
        self.com_port = 'COM1'
        self.baudrate = 57600
        self.set_com_port(self.com_port)

    # Function to set com port for serial coommunication
    def set_com_port(self, com_port):
        self.com_port = com_port
        print("Initializing serial communication on", self.com_port)
        try:
            self.ser = serial.Serial(self.com_port, self.baudrate, timeout=1)
        except:
            print("Serial communication could not be initialized on", self.com_port)

    # Pass the AngleDisplayPanel to serial so it can be updated
    def pass_angle_display_panel(self, angle_disp_panel):
        global angle_display_panel
        angle_display_panel = angle_disp_panel

    # Pass the AccelSet panel to serial so it can be updated
    def pass_accel_set_panel(self, acceleration_set_panel):
        global accel_set_panel
        accel_set_panel = acceleration_set_panel

    # Pass the VelSet panel to serial so it can be updated
    def pass_vel_set_panel(self, velocity_set_panel):
        global vel_set_panel
        vel_set_panel = velocity_set_panel

    # Pass the MinAngleSet panel to serial so it can be updated
    def pass_min_angle_set_panel(self, min_angle_set_panel):
        global minangle_set_panel
        minangle_set_panel = min_angle_set_panel

    # Pass the MaxAngleSet panel to serial so it can be updated
    def pass_max_angle_set_panel(self, max_angle_set_panel):
        global maxangle_set_panel
        maxangle_set_panel = max_angle_set_panel

    # Function periodically called to check if there is anything waiting to be read from the serial connection and
    # read it in if so
    def serial_check(self):
        while self.waiting > 0:
            # self.serial_write_no_print("print pos")
            # self.serial_write_no_print("LS status")
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

    # Same function as serial_write, but without print statements
    def serial_write_no_print(self, string):
        if self.waiting:  # If the arm is waiting for a command, send the command, if not, add it to the queue
            my_str = string.encode('utf-8')
            self.ser.write(my_str)
            self.waiting = False
        else:
            self.queue.put(string)

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
        line = self.ser.readline()
        line = line.decode("utf-8")
        line = line.strip()
        # print(line)

        # if move is received, send the next command from the queue. If there is no command,
        # set the bool waiting to true to indicate the next command should be sent immediately
        head, sep, tail = line.partition(': ')
        # tail = tail.strip()

        if line == "Move?":
            if self.queue.empty():
                self.waiting = True
            else:
                string = self.queue.get()
                my_str = string.encode('utf-8')
                self.ser.write(my_str)
                print("Command '", string, "' sent from queue")

        # if position reports are received (After sending "print pos" to the robot arm), update the positions in the UI
        elif head == "Stepper 1":
            angle_display_panel.set_joint_angle(1, tail)
        elif head == "Stepper 2":
            angle_display_panel.set_joint_angle(2, tail)
        elif head == "Stepper 3":
            angle_display_panel.set_joint_angle(3, tail)
        elif head == "Stepper 4":
            angle_display_panel.set_joint_angle(4, tail)
        elif head == "Stepper 5":
            angle_display_panel.set_joint_angle(5, tail)
        elif head == "Stepper 6":
            angle_display_panel.set_joint_angle(6, tail)
        elif head == "Gripper 7":
            angle_display_panel.set_joint_angle(7, tail)

        # if limit switch reports are received, update the UI to show which are triggered and which are not
        elif head == "LS1":
            angle_display_panel.set_ls_status_light(1, tail)
        elif head == "LS2":
            angle_display_panel.set_ls_status_light(2, tail)
        elif head == "LS3":
            angle_display_panel.set_ls_status_light(3, tail)
        elif head == "LS4":
            angle_display_panel.set_ls_status_light(4, tail)
        elif head == "LS5":
            angle_display_panel.set_ls_status_light(5, tail)
        elif head == "LS6":
            angle_display_panel.set_ls_status_light(6, tail)

        # If accelerations are recieved, update AccelSet to display the current acceleration parameters
        elif head == "Accel 1":
            accel_set_panel.set_accel(1, tail)
        elif head == "Accel 2":
            accel_set_panel.set_accel(2, tail)
        elif head == "Accel 3":
            accel_set_panel.set_accel(3, tail)
        elif head == "Accel 4":
            accel_set_panel.set_accel(4, tail)
        elif head == "Accel 5":
            accel_set_panel.set_accel(5, tail)
        elif head == "Accel 6":
            accel_set_panel.set_accel(6, tail)

        # If velocities are recieved, update VelSet to display the current velocity parameters
        elif head == "Vel 1":
            vel_set_panel.set_vel(1, tail)
        elif head == "Vel 2":
            vel_set_panel.set_vel(2, tail)
        elif head == "Vel 3":
            vel_set_panel.set_vel(3, tail)
        elif head == "Vel 4":
            vel_set_panel.set_vel(4, tail)
        elif head == "Vel 5":
            vel_set_panel.set_vel(5, tail)
        elif head == "Vel 6":
            vel_set_panel.set_vel(6, tail)

        # If min angles are recieved, update minAngleSet to display the current velocity parameters
        elif head == "Min 1":
            minangle_set_panel.set_min_angle(1, tail)
        elif head == "Min 2":
            minangle_set_panel.set_min_angle(2, tail)
        elif head == "Min 3":
            minangle_set_panel.set_min_angle(3, tail)
        elif head == "Min 4":
            minangle_set_panel.set_min_angle(4, tail)
        elif head == "Min 5":
            minangle_set_panel.set_min_angle(5, tail)
        elif head == "Min 6":
            minangle_set_panel.set_min_angle(6, tail)

        # If max angles are recieved, update MaxAngleSet to display the current velocity parameters
        elif head == "Max 1":
            maxangle_set_panel.set_max_angle(1, tail)
        elif head == "Max 2":
            maxangle_set_panel.set_max_angle(2, tail)
        elif head == "Max 3":
            maxangle_set_panel.set_max_angle(3, tail)
        elif head == "Max 4":
            maxangle_set_panel.set_max_angle(4, tail)
        elif head == "Max 5":
            maxangle_set_panel.set_max_angle(5, tail)
        elif head == "Max 6":
            maxangle_set_panel.set_max_angle(6, tail)
