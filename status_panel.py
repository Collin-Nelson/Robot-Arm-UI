import wx, sys


class RedirectText(object):
    def __init__(self, a_xx_text_ctrl):
        self.out = a_xx_text_ctrl

    def write(self, string):
        self.out.WriteText(string)


class status_panel(wx.Panel):
    def __init__(self, parent, serial):
        wx.Panel.__init__(self, parent=parent, pos=(5, 5), size=(400, 800))

        self.serial = serial

        title = wx.StaticText(self, label="Recent Commands", pos=(5, 5), size=(150, 20), style=wx.ALIGN_LEFT)
        self.SetBackgroundColour('white')
        font = title.GetFont()
        font.PointSize = 12
        font = font.Bold()
        title.SetFont(font)

        self.log = wx.TextCtrl(self, pos=(5, 30), size=(390, 300), style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        redir = RedirectText(self.log)
        sys.stdout = redir

        # Title for command input
        text_command_title = wx.StaticText(self, label="Text Command", pos=(5,340), size=(200, 18), style=wx.ALIGN_LEFT)
        self.SetBackgroundColour('white')

        text_command_title.SetFont(font)

        # Text control for inputting text commands to be sent directly over serial
        self.comtc = wx.TextCtrl(self, pos=(5, 370), size=(150,25))

        # Button to send command string
        com_btn = wx.Button(self, label='Send Command String', pos=(170, 370))

        # Bind send command button to its action
        com_btn.Bind(wx.EVT_BUTTON, self.com_btn_press)

        # Joint angle display title
        title2 = wx.StaticText(self, label="Joint Angle Display", pos=(5,420), size=(200, 18), style=wx.ALIGN_LEFT)

        title2.SetFont(font)

        # Add rectangular status lights to display if endstops are currently pressed
        self.statusLight1 = wx.StaticBox(self, wx.ID_ANY, "", size=(20, 20), pos=(10, 450), style=wx.SUNKEN_BORDER)
        self.statusLight2 = wx.StaticBox(self, wx.ID_ANY, "", size=(20, 20), pos=(10, 480), style=wx.SUNKEN_BORDER)
        self.statusLight3 = wx.StaticBox(self, wx.ID_ANY, "", size=(20, 20), pos=(10, 510), style=wx.SUNKEN_BORDER)
        self.statusLight4 = wx.StaticBox(self, wx.ID_ANY, "", size=(20, 20), pos=(10, 540), style=wx.SUNKEN_BORDER)
        self.statusLight5 = wx.StaticBox(self, wx.ID_ANY, "", size=(20, 20), pos=(10, 570), style=wx.SUNKEN_BORDER)
        self.statusLight6 = wx.StaticBox(self, wx.ID_ANY, "", size=(20, 20), pos=(10, 600), style=wx.SUNKEN_BORDER)

        # Labels for the joint angle text boxes
        lbl1 = wx.StaticText(self, label="J1", pos=(40, 450))
        lbl2 = wx.StaticText(self, label="J2", pos=(40, 480))
        lbl3 = wx.StaticText(self, label="J3", pos=(40, 510))
        lbl4 = wx.StaticText(self, label="J4", pos=(40, 540))
        lbl5 = wx.StaticText(self, label="J5", pos=(40, 570))
        lbl6 = wx.StaticText(self, label="J6", pos=(40, 600))
        lbl7 = wx.StaticText(self, label="EE", pos=(40, 630))

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
        lbl7.SetFont(lblfont)

        # Text boxes to display the current angle of each joint
        self.tc1 = wx.TextCtrl(self, pos=(65, 450), style=wx.TE_READONLY)
        self.tc2 = wx.TextCtrl(self, pos=(65, 480), style=wx.TE_READONLY)
        self.tc3 = wx.TextCtrl(self, pos=(65, 510), style=wx.TE_READONLY)
        self.tc4 = wx.TextCtrl(self, pos=(65, 540), style=wx.TE_READONLY)
        self.tc5 = wx.TextCtrl(self, pos=(65, 570), style=wx.TE_READONLY)
        self.tc6 = wx.TextCtrl(self, pos=(65, 600), style=wx.TE_READONLY)
        self.tc7 = wx.TextCtrl(self, pos=(65, 630), style=wx.TE_READONLY)

        # set the angle value in the text control box
        self.tc1.SetValue('0')
        self.tc2.SetValue('0')
        self.tc3.SetValue('0')
        self.tc4.SetValue('0')
        self.tc5.SetValue('0')
        self.tc6.SetValue('0')

    # Deals with send commanad button press
    def com_btn_press(self, event):
        value = self.comtc.GetValue()
        print("Send Command Button Pressed")
        print(f"Command string is:", value)
        self.serial.serial_write(value)

    def set_ls_status_light(self, ls_index, status):
        if ls_index == 1:
            if status == "0":
                self.statusLight1.SetBackgroundColour('white')
            elif status == "1":
                self.statusLight1.SetBackgroundColour('green')
        elif ls_index == 2:
            if status == "0":
                self.statusLight2.SetBackgroundColour('white')
            elif status == "1":
                self.statusLight2.SetBackgroundColour('green')
        elif ls_index == 3:
            if status == "0":
                self.statusLight3.SetBackgroundColour('white')
            elif status == "1":
                self.statusLight3.SetBackgroundColour('green')
        elif ls_index == 4:
            if status == "0":
                self.statusLight4.SetBackgroundColour('white')
            elif status == "1":
                self.statusLight4.SetBackgroundColour('green')
        elif ls_index == 5:
            if status == "0":
                self.statusLight5.SetBackgroundColour('white')
            elif status == "1":
                self.statusLight5.SetBackgroundColour('green')
        elif ls_index == 6:
            if status == "0":
                self.statusLight6.SetBackgroundColour('white')
            elif status == "1":
                self.statusLight6.SetBackgroundColour('green')

        self.Refresh()

    def set_joint_angle(self, joint_id, angle):
        if joint_id == 1:
            self.tc1.SetValue(angle)
        if joint_id == 2:
            self.tc2.SetValue(angle)
        if joint_id == 3:
            self.tc3.SetValue(angle)
        if joint_id == 4:
            self.tc4.SetValue(angle)
        if joint_id == 5:
            self.tc5.SetValue(angle)
        if joint_id == 6:
            self.tc6.SetValue(angle)
        if joint_id == 7:
            if angle == "0":
                self.tc7.SetValue("Closed")
            if angle == "180":
                self.tc7.SetValue("Open")
