import wx

from Serial import SerialComms


class TextCommand(wx.Panel):
    def __init__(self, parent):
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
        comBtn = wx.Button(self, label='Send Command String', pos=(20, 70))

        # Bind zero button to its action
        comBtn.Bind(wx.EVT_BUTTON, self.comBtnPress)

    # Deals with zero button press
    def comBtnPress(self, event):
        value = self.comtc.GetValue()
        print("Send Command Button Pressed")
        print(f"Test string is:", value)
        SerialComms.SerialWrite(value)
