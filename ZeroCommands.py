import wx

from Serial import SerialComms


class ZeroCommands(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, pos=(620, 235), size=(200, 230), style=wx.SUNKEN_BORDER)

        title = wx.StaticText(self, label="Zeroing", size=(200, 18), style=wx.ALIGN_CENTER_HORIZONTAL)
        self.SetBackgroundColour('white')

        font = title.GetFont()
        font.PointSize = 12
        font = font.Bold()
        title.SetFont(font)

        # Button to zero selected axes
        zeroBtn = wx.Button(self, label='Zero Selected Axes', pos=(5, 20))

        # Bind zero button to its action
        zeroBtn.Bind(wx.EVT_BUTTON, self.zeroBtnPress)

        # Checkbox for each axis to zero
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

    # Deals with zero button press
    def zeroBtnPress(self, event):
        print("Zero Button Pressed")
        if self.chk1.GetValue() and self.chk2.GetValue() and self.chk3.GetValue() and self.chk4.GetValue() and self.chk5.GetValue() and self.chk6.GetValue():
            print("Zeroing all joints")
            SerialComms.SerialWrite("zero")
        else:
            if self.chk1.GetValue():
                print("Zeroing joint 1")
                SerialComms.SerialWrite("zero 1")
            if self.chk2.GetValue():
                print("Zeroing joint 2")
                SerialComms.SerialWrite("zero 2")
            if self.chk3.GetValue():
                print("Zeroing joint 3")
                SerialComms.SerialWrite("zero 3")
            if self.chk4.GetValue():
                print("Zeroing joint 4")
                SerialComms.SerialWrite("zero 4")
            if self.chk5.GetValue():
                print("Zeroing joint 5")
                SerialComms.SerialWrite("zero 5")
            if self.chk6.GetValue():
                print("Zeroing joint 6")
                SerialComms.SerialWrite("zero 6")
