import wx


class EndEffectorCommand(wx.Panel):
    def __init__(self, parent, serial):
        wx.Panel.__init__(self, parent=parent, pos=(825, 240), size=(200, 230), style=wx.SUNKEN_BORDER)

        title = wx.StaticText(self, label="End Effector Command", size=(200, 18), style=wx.ALIGN_CENTER_HORIZONTAL)
        self.SetBackgroundColour('white')

        font = title.GetFont()
        font.PointSize = 12
        font = font.Bold()
        title.SetFont(font)

        # Buttons to open and close end effector
        open_btn = wx.Button(self, label='Open', pos=(10, 30))
        close_btn = wx.Button(self, label='Close', pos=(10, 60))

        # Bind buttons to actions
        open_btn.Bind(wx.EVT_BUTTON, self.open_btn_press(self, serial))
        close_btn.Bind(wx.EVT_BUTTON, self.close_btn_press(self, serial))

    # Deals with button presses
    def open_btn_press(self, event, serial):
        print("Opening Gripper")
        serial.serial_write('7:180')

    def close_btn_press(self, event, serial):
        print("Closing Gripper")
        serial.serial_write('7:0')
