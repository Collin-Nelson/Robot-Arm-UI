import wx


class motion_panel(wx.Panel):
    def __init__(self, parent, serial):
        wx.Panel.__init__(self, parent=parent, size=(600, 800))

        self.serial = serial
        self.SetBackgroundColour('white')

        title_font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)

        move_to_angle_title = wx.StaticText(self, label="Move to Angle", pos=(5,5), size=(200, 18), style=wx.ALIGN_LEFT)
        move_to_angle_title.SetFont(title_font)

        # Text input boxes for the angle for each joint
        self.j1_angle_tc = wx.TextCtrl(self, pos=(100, 30), size=(100, 25))
        self.j2_angle_tc = wx.TextCtrl(self, pos=(100, 60), size=(100, 25))
        self.j3_angle_tc = wx.TextCtrl(self, pos=(100, 90), size=(100, 25))
        self.j4_angle_tc = wx.TextCtrl(self, pos=(100, 120), size=(100, 25))
        self.j5_angle_tc = wx.TextCtrl(self, pos=(100, 150), size=(100, 25))
        self.j6_angle_tc = wx.TextCtrl(self, pos=(100, 180), size=(100, 25))

        # Buttons to trigger moving to the specified angle
        j1_move_btn = wx.Button(self, label='Move J1', pos=(5, 30))
        j2_move_btn = wx.Button(self, label='Move J2', pos=(5, 60))
        j3_move_btn = wx.Button(self, label='Move J3', pos=(5, 90))
        j4_move_btn = wx.Button(self, label='Move J4', pos=(5, 120))
        j5_move_btn = wx.Button(self, label='Move J5', pos=(5, 150))
        j6_move_btn = wx.Button(self, label='Move J6', pos=(5, 180))
        move_all_btn = wx.Button(self, label='Move All', pos=(5, 210), size=(195, 30))

        # Bind each button to its action
        j1_move_btn.Bind(wx.EVT_BUTTON, self.j1_move_btn_press)
        j2_move_btn.Bind(wx.EVT_BUTTON, self.j2_move_btn_press)
        j3_move_btn.Bind(wx.EVT_BUTTON, self.j3_move_btn_press)
        j4_move_btn.Bind(wx.EVT_BUTTON, self.j4_move_btn_press)
        j5_move_btn.Bind(wx.EVT_BUTTON, self.j5_move_btn_press)
        j6_move_btn.Bind(wx.EVT_BUTTON, self.j6_move_btn_press)
        move_all_btn.Bind(wx.EVT_BUTTON, self.move_all_btn_press)


        jog_title = wx.StaticText(self, label="Jog Axes", pos=(200,5), size=(25, 18), style=wx.ALIGN_LEFT)
        jog_title.SetFont(title_font)

        # Buttons to jog axes
        j1_jog_pos_btn = wx.Button(self, label='+', pos=(210, 30), size=(25, 25))
        j2_jog_pos_btn = wx.Button(self, label='+', pos=(210, 60), size=(25, 25))
        j3_jog_pos_btn = wx.Button(self, label='+', pos=(210, 90), size=(25, 25))
        j4_jog_pos_btn = wx.Button(self, label='+', pos=(210, 120), size=(25, 25))
        j5_jog_pos_btn = wx.Button(self, label='+', pos=(210, 150), size=(25, 25))
        j6_jog_pos_btn = wx.Button(self, label='+', pos=(210, 180), size=(25, 25))
        j1_jog_neg_btn = wx.Button(self, label='-', pos=(240, 30), size=(25, 25))
        j2_jog_neg_btn = wx.Button(self, label='-', pos=(240, 60), size=(25, 25))
        j3_jog_neg_btn = wx.Button(self, label='-', pos=(240, 90), size=(25, 25))
        j4_jog_neg_btn = wx.Button(self, label='-', pos=(240, 120), size=(25, 25))
        j5_jog_neg_btn = wx.Button(self, label='-', pos=(240, 150), size=(25, 25))
        j6_jog_neg_btn = wx.Button(self, label='-', pos=(240, 180), size=(25, 25))

        # Bind each button to its action
        j1_jog_pos_btn.Bind(wx.EVT_BUTTON, self.j1_jog_pos_btn_press)
        j2_jog_pos_btn.Bind(wx.EVT_BUTTON, self.j1_jog_pos_btn_press)
        j3_jog_pos_btn.Bind(wx.EVT_BUTTON, self.j1_jog_pos_btn_press)
        j4_jog_pos_btn.Bind(wx.EVT_BUTTON, self.j1_jog_pos_btn_press)
        j5_jog_pos_btn.Bind(wx.EVT_BUTTON, self.j1_jog_pos_btn_press)
        j6_jog_pos_btn.Bind(wx.EVT_BUTTON, self.j1_jog_pos_btn_press)
        j1_jog_neg_btn.Bind(wx.EVT_BUTTON, self.j1_jog_neg_btn_press)
        j2_jog_neg_btn.Bind(wx.EVT_BUTTON, self.j1_jog_neg_btn_press)
        j3_jog_neg_btn.Bind(wx.EVT_BUTTON, self.j1_jog_neg_btn_press)
        j4_jog_neg_btn.Bind(wx.EVT_BUTTON, self.j1_jog_neg_btn_press)
        j5_jog_neg_btn.Bind(wx.EVT_BUTTON, self.j1_jog_neg_btn_press)
        j6_jog_neg_btn.Bind(wx.EVT_BUTTON, self.j1_jog_neg_btn_press)

        end_effector_title = wx.StaticText(self, label="End Effector Command", size=(200, 18), pos=(5,250), style=wx.ALIGN_LEFT)
        end_effector_title.SetFont(title_font)

        # Buttons to open and close end effector
        open_btn = wx.Button(self, label='Open', pos=(5, 280))
        close_btn = wx.Button(self, label='Close', pos=(5, 310))

        # Bind buttons to actions
        open_btn.Bind(wx.EVT_BUTTON, self.open_btn_press)
        close_btn.Bind(wx.EVT_BUTTON, self.close_btn_press)

        # Homing section
        home_title = wx.StaticText(self, label="Homing", size=(200, 18), pos=(5,350), style=wx.ALIGN_LEFT)
        home_title.SetFont(title_font)

        # Checkbox for each axis to home
        self.home_chk1 = wx.CheckBox(self, label="Joint 1", pos=(10, 410))
        self.home_chk2 = wx.CheckBox(self, label="Joint 2", pos=(10, 430))
        self.home_chk3 = wx.CheckBox(self, label="Joint 3", pos=(10, 450))
        self.home_chk4 = wx.CheckBox(self, label="Joint 4", pos=(10, 470))
        self.home_chk5 = wx.CheckBox(self, label="Joint 5", pos=(10, 490))
        self.home_chk6 = wx.CheckBox(self, label="Joint 6", pos=(10, 510))

        # Sets checkboxes to default to checked
        self.home_chk1.SetValue(1)
        self.home_chk2.SetValue(1)
        self.home_chk3.SetValue(1)
        self.home_chk4.SetValue(1)
        self.home_chk5.SetValue(1)
        self.home_chk6.SetValue(1)

        # Button to home selected axes
        home_btn = wx.Button(self, label='Home Selected Axes', pos=(5, 380))

        # Bind home button to its action
        home_btn.Bind(wx.EVT_BUTTON, self.home_btn_press)

        # Zero section
        zero_title = wx.StaticText(self, label="Zeroing", size=(200, 18), pos=(200,350), style=wx.ALIGN_LEFT)
        zero_title.SetFont(title_font)

        # Checkbox for each axis to zero
        self.zero_chk1 = wx.CheckBox(self, label="Joint 1", pos=(200, 410))
        self.zero_chk2 = wx.CheckBox(self, label="Joint 2", pos=(200, 430))
        self.zero_chk3 = wx.CheckBox(self, label="Joint 3", pos=(200, 450))
        self.zero_chk4 = wx.CheckBox(self, label="Joint 4", pos=(200, 470))
        self.zero_chk5 = wx.CheckBox(self, label="Joint 5", pos=(200, 490))
        self.zero_chk6 = wx.CheckBox(self, label="Joint 6", pos=(200, 510))

        # Sets checkboxes to default to checked
        self.zero_chk1.SetValue(1)
        self.zero_chk2.SetValue(1)
        self.zero_chk3.SetValue(1)
        self.zero_chk4.SetValue(1)
        self.zero_chk5.SetValue(1)
        self.zero_chk6.SetValue(1)

        # Button to zero selected axes
        zero_btn = wx.Button(self, label='Zero Selected Axes', pos=(200, 380))

        # Bind zero button to its action
        zero_btn.Bind(wx.EVT_BUTTON, self.zero_btn_press)

    # Deals with zero button press
    def zero_btn_press(self, event):
        print("Zero Button Pressed")
        if self.zero_chk1.GetValue() and self.zero_chk2.GetValue() and self.zero_chk3.GetValue() and self.zero_chk4.GetValue() and \
                self.zero_chk5.GetValue() and self.zero_chk6.GetValue():

            print("Zeroing all joints")
            self.serial.serial_write("zero")
        else:
            if self.zero_chk1.GetValue():
                print("Zeroing joint 1")
                self.serial.serial_write(self, "zero 1")
            if self.zero_chk2.GetValue():
                print("Zeroing joint 2")
                self.serial.serial_write(self, "zero 2")
            if self.zero_chk3.GetValue():
                print("Zeroing joint 3")
                self.serial.serial_write(self, "zero 3")
            if self.zero_chk4.GetValue():
                print("Zeroing joint 4")
                self.serial.serial_write(self, "zero 4")
            if self.zero_chk5.GetValue():
                print("Zeroing joint 5")
                self.serial.serial_write(self, "zero 5")
            if self.zero_chk6.GetValue():
                print("Zeroing joint 6")
                self.serial.serial_write(self, "zero 6")

    # Deals with homing button press
    def home_btn_press(self, event):
        print("Home Button Pressed")
        if self.home_chk1.GetValue() and self.home_chk2.GetValue() and self.home_chk3.GetValue() and self.home_chk4.GetValue() and \
                self.home_chk5.GetValue() and self.home_chk6.GetValue():
            print("Homing all joints")
            self.serial.serial_write("home")
        else:
            if self.home_chk1.GetValue():
                print("Homing joint 1")
                self.serial.serial_write("home 1")
            if self.home_chk2.GetValue():
                print("Homing joint 2")
                self.serial.serial_write("home 2")
            if self.home_chk3.GetValue():
                print("Homing joint 3")
                self.serial.serial_write("home 3")
            if self.home_chk4.GetValue():
                print("Homing joint 4")
                self.serial.serial_write("home 4")
            if self.home_chk5.GetValue():
                print("Homing joint 5")
                self.serial.serial_write("home 5")
            if self.home_chk6.GetValue():
                print("Homing joint 6")
                self.serial.serial_write("home 6")



    # Deals with button presses
    def open_btn_press(self, event):
        print("Opening Gripper")
        self.serial.serial_write('7:180')

    def close_btn_press(self, event):
        print("Closing Gripper")
        self.serial.serial_write('7:0')

    # Actions for move to angle buttons
    def j1_move_btn_press(self, event):
        value = self.j1_angle_tc.GetValue()
        if not value:
            print("You didn't enter anything!")

        else:
            print(f'You typed: "{value}"')
            self.serial.serial_write("1:" + value)

    def j2_move_btn_press(self, event):
        value = self.j2_angle_tc.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            self.serial.serial_write("2:" + value)

    def j3_move_btn_press(self, event):
        value = self.j3_angle_tc.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            self.serial.serial_write("3:" + value)

    def j4_move_btn_press(self, event):
        value = self.j4_angle_tc.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            self.serial.serial_write("4:" + value)

    def j5_move_btn_press(self, event):
        value = self.j5_angle_tc.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            self.serial.serial_write("5:" + value)

    def j6_move_btn_press(self, event):
        value = self.j6_angle_tc.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            self.serial.serial_write("6:" + value)

    def move_all_btn_press(self, event):
        value1 = self.j1_angle_tc.GetValue()
        value2 = self.j2_angle_tc.GetValue()
        value3 = self.j3_angle_tc.GetValue()
        value4 = self.j4_angle_tc.GetValue()
        value5 = self.j5_angle_tc.GetValue()
        value6 = self.j6_angle_tc.GetValue()

        # set null values to zero
        if value1 == "": value1 = "0"
        if value2 == "": value2 = "0"
        if value3 == "": value3 = "0"
        if value4 == "": value4 = "0"
        if value5 == "": value5 = "0"
        if value6 == "": value6 = "0"
        
        self.serial.serial_write("1:" + value1 + ".2:" + value2 + ".3:" + value3 + ".4:" + value4 + ".5:" + value5 + ".6:" + value6)

    # Actions for jog buttons
    def j1_jog_pos_btn_press(self, event):
        self.serial.serial_write("relJ1:10")

    def j2_jog_pos_btn_press(self, event):
        self.serial.serial_write("relJ2:10")

    def j3_jog_pos_btn_press(self, event):
        self.serial.serial_write("relJ3:10")

    def j4_jog_pos_btn_press(self, event):
        self.serial.serial_write("relJ4:10")

    def j5_jog_pos_btn_press(self, event):
        self.serial.serial_write("relJ5:10")

    def j6_jog_pos_btn_press(self, event):
        self.serial.serial_write("relJ6:10")

    def j1_jog_neg_btn_press(self, event):
        self.serial.serial_write("relJ1:-10")

    def j2_jog_neg_btn_press(self, event):
        self.serial.serial_write("relJ2:-10")

    def j3_jog_neg_btn_press(self, event):
        self.serial.serial_write("relJ3:-10")

    def j4_jog_neg_btn_press(self, event):
        self.serial.serial_write("relJ4:-10")

    def j5_jog_neg_btn_press(self, event):
        self.serial.serial_write("relJ5:-10")

    def j6_jog_neg_btn_press(self, event):
        self.serial.serial_write("relJ6:-10")
    
    
    