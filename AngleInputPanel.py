import wx


class AngleInputPanel(wx.Panel):
    def __init__(self, parent, serial):
        wx.Panel.__init__(self, parent=parent, pos=(415, 5), size=(200, 230), style=wx.SUNKEN_BORDER)

        title = wx.StaticText(self, label="Joint Angle Inputs", size=(200, 18), style=wx.ALIGN_CENTER_HORIZONTAL)
        self.SetBackgroundColour('white')

        font = title.GetFont()
        font.PointSize = 12
        font = font.Bold()
        title.SetFont(font)

        # Text input boxes for the angle for each joint
        self.tc1 = wx.TextCtrl(self, pos=(90, 20))
        self.tc2 = wx.TextCtrl(self, pos=(90, 50))
        self.tc3 = wx.TextCtrl(self, pos=(90, 80))
        self.tc4 = wx.TextCtrl(self, pos=(90, 110))
        self.tc5 = wx.TextCtrl(self, pos=(90, 140))
        self.tc6 = wx.TextCtrl(self, pos=(90, 170))

        # Buttons to trigger moving to the specified number of degrees
        btn7 = wx.Button(self, label='Move All', pos=(5, 200), size=(175, 30))
        btn1 = wx.Button(self, label='Move J1', pos=(5, 20))
        btn2 = wx.Button(self, label='Move J2', pos=(5, 50))
        btn3 = wx.Button(self, label='Move J3', pos=(5, 80))
        btn4 = wx.Button(self, label='Move J4', pos=(5, 110))
        btn5 = wx.Button(self, label='Move J5', pos=(5, 140))
        btn6 = wx.Button(self, label='Move J6', pos=(5, 170))

        # Bind each button to its action
        btn1.Bind(wx.EVT_BUTTON, self.btn1_press(self, serial))
        btn2.Bind(wx.EVT_BUTTON, self.btn2_press(self, serial))
        btn3.Bind(wx.EVT_BUTTON, self.btn3_press(self, serial))
        btn4.Bind(wx.EVT_BUTTON, self.btn4_press(self, serial))
        btn5.Bind(wx.EVT_BUTTON, self.btn5_press(self, serial))
        btn6.Bind(wx.EVT_BUTTON, self.btn6_press(self, serial))
        btn7.Bind(wx.EVT_BUTTON, self.btn7_press(self, serial))

    # Actions for each button
    def btn1_press(self, event, serial):
        value = self.tc1.GetValue()
        if not value:
            print("You didn't enter anything!")

        else:
            print(f'You typed: "{value}"')
            serial.serial_write(self, "1:" + value)

    def btn2_press(self, event, serial):
        value = self.tc2.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            serial.serial_write(self, "2:" + value)

    def btn3_press(self, event, serial):
        value = self.tc3.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            serial.serial_write(self, "3:" + value)

    def btn4_press(self, event, serial):
        value = self.tc4.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            serial.serial_write(self, "4:" + value)

    def btn5_press(self, event, serial):
        value = self.tc5.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            serial.serial_write(self, "5:" + value)

    def btn6_press(self, event, serial):
        value = self.tc6.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            serial.serial_write(self, "6:" + value)

    def btn7_press(self, event, serial):
        value1 = self.tc1.GetValue()
        value2 = self.tc2.GetValue()
        value3 = self.tc3.GetValue()
        value4 = self.tc4.GetValue()
        value5 = self.tc5.GetValue()
        value6 = self.tc6.GetValue()

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

        serial.serial_write("1:" + value1 + ".2:" + value2 + ".3:" + value3 +
                            ".4:" + value4 + ".5:" + value5 + ".6:" + value6)
