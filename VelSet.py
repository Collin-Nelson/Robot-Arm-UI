import wx


class VelSet(wx.Panel):
    def __init__(self, parent, serial):
        wx.Panel.__init__(self, parent=parent, size=(200, 500), style=wx.SUNKEN_BORDER)

        self.serial = serial

        serial.pass_vel_set_panel(self)

        title = wx.StaticText(self, label="Set Velocities", size=(200, 18), style=wx.ALIGN_CENTER_HORIZONTAL)
        self.SetBackgroundColour('white')
        font = title.GetFont()
        font.PointSize = 12
        font = font.Bold()
        title.SetFont(font)

        # Labels for the joint angle text boxes
        lbl1 = wx.StaticText(self, label="J1 Vel", pos=(40, 30))
        lbl2 = wx.StaticText(self, label="J2 Vel", pos=(40, 90 + 10))
        lbl3 = wx.StaticText(self, label="J3 Vel", pos=(40, 150 + 20))
        lbl4 = wx.StaticText(self, label="J4 Vel", pos=(40, 210 + 30))
        lbl5 = wx.StaticText(self, label="J5 Vel", pos=(40, 270 + 40))
        lbl6 = wx.StaticText(self, label="J6 Vel", pos=(40, 330 + 50))

        # Set the font of the labels on the joint angle display textctrl boxes
        lblfont = lbl1.GetFont()
        lblfont.PointSize = 10
        lblfont = lblfont.Bold()
        lbl1.SetFont(lblfont)
        lbl2.SetFont(lblfont)
        lbl3.SetFont(lblfont)
        lbl4.SetFont(lblfont)
        lbl5.SetFont(lblfont)
        lbl6.SetFont(lblfont)

        # Text boxes to display the current angle of each joint
        self.tc1 = wx.TextCtrl(self, pos=(90, 30), style=wx.TE_READONLY, size=(100, 22))
        self.tc2 = wx.TextCtrl(self, pos=(90, 90 + 10), style=wx.TE_READONLY, size=(100, 22))
        self.tc3 = wx.TextCtrl(self, pos=(90, 150 + 20), style=wx.TE_READONLY, size=(100, 22))
        self.tc4 = wx.TextCtrl(self, pos=(90, 210 + 30), style=wx.TE_READONLY, size=(100, 22))
        self.tc5 = wx.TextCtrl(self, pos=(90, 270 + 40), style=wx.TE_READONLY, size=(100, 22))
        self.tc6 = wx.TextCtrl(self, pos=(90, 330 + 50), style=wx.TE_READONLY, size=(100, 22))

        # set the angle value in the text control box
        self.tc1.SetValue('0')
        self.tc2.SetValue('0')
        self.tc3.SetValue('0')
        self.tc4.SetValue('0')
        self.tc5.SetValue('0')
        self.tc6.SetValue('0')

        font = title.GetFont()
        font.PointSize = 12
        font = font.Bold()
        title.SetFont(font)

        # Text input boxes for the angle for each joint
        self.tc11 = wx.TextCtrl(self, pos=(90, 60), size=(100, 22))
        self.tc12 = wx.TextCtrl(self, pos=(90, 120 + 10), size=(100, 22))
        self.tc13 = wx.TextCtrl(self, pos=(90, 180 + 20), size=(100, 22))
        self.tc14 = wx.TextCtrl(self, pos=(90, 240 + 30), size=(100, 22))
        self.tc15 = wx.TextCtrl(self, pos=(90, 300 + 40), size=(100, 22))
        self.tc16 = wx.TextCtrl(self, pos=(90, 360 + 50), size=(100, 22))

        # Buttons to trigger moving to the specified number of degrees
        btn1 = wx.Button(self, label='Set J1', pos=(5, 60))
        btn2 = wx.Button(self, label='Set J2', pos=(5, 120 + 10))
        btn3 = wx.Button(self, label='Set J3', pos=(5, 180 + 20))
        btn4 = wx.Button(self, label='Set J4', pos=(5, 240 + 30))
        btn5 = wx.Button(self, label='Set J5', pos=(5, 300 + 40))
        btn6 = wx.Button(self, label='Set J6', pos=(5, 360 + 50))
        btn7 = wx.Button(self, label='Set All', pos=(5, 400 + 60), size=(175, 30))

        # Bind each button to its action
        btn1.Bind(wx.EVT_BUTTON, self.btn1_press)
        btn2.Bind(wx.EVT_BUTTON, self.btn2_press)
        btn3.Bind(wx.EVT_BUTTON, self.btn3_press)
        btn4.Bind(wx.EVT_BUTTON, self.btn4_press)
        btn5.Bind(wx.EVT_BUTTON, self.btn5_press)
        btn6.Bind(wx.EVT_BUTTON, self.btn6_press)
        btn7.Bind(wx.EVT_BUTTON, self.btn7_press)

    def set_vel(self, joint_id, vel):
        if joint_id == 1:
            self.tc1.SetValue(vel)
        if joint_id == 2:
            self.tc2.SetValue(vel)
        if joint_id == 3:
            self.tc3.SetValue(vel)
        if joint_id == 4:
            self.tc4.SetValue(vel)
        if joint_id == 5:
            self.tc5.SetValue(vel)
        if joint_id == 6:
            self.tc6.SetValue(vel)

    # Actions for each button
    def btn1_press(self, event):
        value = self.tc11.GetValue()
        if not value:
            print("You didn't enter anything!")

        else:
            print(f'You typed: "{value}"')
            self.serial.serial_write("V1:" + value)

    def btn2_press(self, event):
        value = self.tc12.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            self.serial.serial_write("V2:" + value)

    def btn3_press(self, event):
        value = self.tc13.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            self.serial.serial_write("V3:" + value)

    def btn4_press(self, event):
        value = self.tc14.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            self.serial.serial_write("V4:" + value)

    def btn5_press(self, event):
        value = self.tc15.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            self.serial.serial_write("V5:" + value)

    def btn6_press(self, event):
        value = self.tc16.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            self.serial.serial_write("V6:" + value)

    def btn7_press(self, event):
        value1 = self.tc11.GetValue()
        value2 = self.tc12.GetValue()
        value3 = self.tc13.GetValue()
        value4 = self.tc14.GetValue()
        value5 = self.tc15.GetValue()
        value6 = self.tc16.GetValue()

        # set null values to zero
        if value1 == "":
            value1 = "0"
        if value2 == "":
            value2 = "0"
        if value3 == "":
            value3 = "0"
        if value4 == "":
            value4 = "0"
        if value5 == "":
            value5 = "0"
        if value6 == "":
            value6 = "0"

        self.serial.serial_write("V1:" + value1 + ".V2:" + value2 + ".V3:" + value3 +
                                 ".V4:" + value4 + ".V5:" + value5 + ".V6:" + value6)
