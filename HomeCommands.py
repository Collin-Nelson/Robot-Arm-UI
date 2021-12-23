import wx

from Serial import SerialComms


class HomeCommands(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, pos=(415, 240), size=(200, 230), style=wx.SUNKEN_BORDER)

        title = wx.StaticText(self, label="Homing", size=(200, 18), style=wx.ALIGN_CENTER_HORIZONTAL)
        self.SetBackgroundColour('white')

        font = title.GetFont()
        font.PointSize = 12
        font = font.Bold()
        title.SetFont(font)

        # Button to home selected axes
        homeBtn = wx.Button(self, label='Home Selected Axes', pos=(5, 20))

        # Bind home button to its action
        homeBtn.Bind(wx.EVT_BUTTON, self.homeBtnPress)

        # Checkbox for each axis to home
        self.chk1 = wx.CheckBox(self, label="Joint 1", pos=(10, 50))
        self.chk2 = wx.CheckBox(self, label="Joint 2", pos=(10, 70))
        self.chk3 = wx.CheckBox(self, label="Joint 3", pos=(10, 90))
        self.chk4 = wx.CheckBox(self, label="Joint 4", pos=(10, 110))
        self.chk5 = wx.CheckBox(self, label="Joint 5", pos=(10, 130))
        self.chk6 = wx.CheckBox(self, label="Joint 6", pos=(10, 150))

        # Sets checkboxes to default to checked
        self.chk1.SetValue(1)
        self.chk2.SetValue(1)
        self.chk3.SetValue(1)
        self.chk4.SetValue(1)
        self.chk5.SetValue(1)
        self.chk6.SetValue(1)

    # Deals with homing button press
    def homeBtnPress(self, event):
        print("Home Button Pressed")
        if self.chk1.GetValue() and self.chk2.GetValue() and self.chk3.GetValue() and self.chk4.GetValue() and self.chk5.GetValue() and self.chk6.GetValue():
            print("Homing all joints")
            SerialComms.SerialWrite("home")
        else:
            if self.chk1.GetValue():
                print("Homing joint 1")
                SerialComms.SerialWrite("home 1")
            if self.chk2.GetValue():
                print("Homing joint 2")
                SerialComms.SerialWrite("home 2")
            if self.chk3.GetValue():
                print("Homing joint 3")
                SerialComms.SerialWrite("home 3")
            if self.chk4.GetValue():
                print("Homing joint 4")
                SerialComms.SerialWrite("home 4")
            if self.chk5.GetValue():
                print("Homing joint 5")
                SerialComms.SerialWrite("home 5")
            if self.chk6.GetValue():
                print("Homing joint 6")
                SerialComms.SerialWrite("home 6")
