import wx


class TextCommand(wx.Panel):
    def __init__(self, parent, serial):
        wx.Panel.__init__(self, parent=parent, pos=(825, 5), size=(200, 230), style=wx.SUNKEN_BORDER)

        title = wx.StaticText(self, label="Text Command", size=(200, 18), style=wx.ALIGN_CENTER_HORIZONTAL)
        self.SetBackgroundColour('white')

        font = title.GetFont()
        font.PointSize = 12
        font = font.Bold()
        title.SetFont(font)

        # Text control for inputting text commands to be sent directly over serial
        self.comtc = wx.TextCtrl(self, pos=(35, 40))

        # Button to send command string
        com_btn = wx.Button(self, label='Send Command String', pos=(20, 70))

        # Bind zero button to its action
        com_btn.Bind(wx.EVT_BUTTON, self.com_btn_press(self, serial))

    # Deals with zero button press
    def com_btn_press(self, event, serial):
        value = self.comtc.GetValue()
        print("Send Command Button Pressed")
        print(f"Command string is:", value)
        serial.serial_write(value)
