import wx

from Serial import SerialComms


class EndEffectorCommand(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, pos=(825, 240), size=(200, 230), style=wx.SUNKEN_BORDER)

        title = wx.StaticText(self, label="End Effector Command", size=(200, 18), style=wx.ALIGN_CENTER_HORIZONTAL)
        self.SetBackgroundColour('white')

        font = title.GetFont()
        font.PointSize = 12
        font = font.Bold()
        title.SetFont(font)

        # Buttons to open and close end effector
        openBtn = wx.Button(self, label='Open', pos=(10, 30))
        closeBtn = wx.Button(self, label='Close', pos=(10, 60))

        # Bind buttons to actions
        openBtn.Bind(wx.EVT_BUTTON, self.openBtnPress)
        closeBtn.Bind(wx.EVT_BUTTON, self.closeBtnPress)

    # Deals with button presses
    def openBtnPress(self, event):
        print("Opening Gripper")
        SerialComms.SerialWrite('7:180')

    def closeBtnPress(self, event):
        print("Closing Gripper")
        SerialComms.SerialWrite('7:0')
