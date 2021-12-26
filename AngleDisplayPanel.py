import wx

from random import random


class AngleDisplayPanel(wx.Panel):
    def __init__(self, parent, serial):
        wx.Panel.__init__(self, parent=parent, size=(250, 250), style=wx.SUNKEN_BORDER)

        serial.pass_angle_display_panel(self)

        title = wx.StaticText(self, label="Joint Angle Display", size=(200, 18), style=wx.ALIGN_CENTER_HORIZONTAL)
        self.SetBackgroundColour('white')
        font = title.GetFont()
        font.PointSize = 12
        font = font.Bold()
        title.SetFont(font)

        # Add rectangular status lights to display if endstops are currently pressed
        self.statusLight1 = wx.StaticBox(self, wx.ID_ANY, "", size=(20, 20), pos=(10, 30), style=wx.SUNKEN_BORDER)
        self.statusLight2 = wx.StaticBox(self, wx.ID_ANY, "", size=(20, 20), pos=(10, 60), style=wx.SUNKEN_BORDER)
        self.statusLight3 = wx.StaticBox(self, wx.ID_ANY, "", size=(20, 20), pos=(10, 90), style=wx.SUNKEN_BORDER)
        self.statusLight4 = wx.StaticBox(self, wx.ID_ANY, "", size=(20, 20), pos=(10, 120), style=wx.SUNKEN_BORDER)
        self.statusLight5 = wx.StaticBox(self, wx.ID_ANY, "", size=(20, 20), pos=(10, 150), style=wx.SUNKEN_BORDER)
        self.statusLight6 = wx.StaticBox(self, wx.ID_ANY, "", size=(20, 20), pos=(10, 180), style=wx.SUNKEN_BORDER)

        # Labels for the joint angle text boxes
        lbl1 = wx.StaticText(self, label="J1", pos=(40, 30))
        lbl2 = wx.StaticText(self, label="J2", pos=(40, 60))
        lbl3 = wx.StaticText(self, label="J3", pos=(40, 90))
        lbl4 = wx.StaticText(self, label="J4", pos=(40, 120))
        lbl5 = wx.StaticText(self, label="J5", pos=(40, 150))
        lbl6 = wx.StaticText(self, label="J6", pos=(40, 180))
        lbl7 = wx.StaticText(self, label="EE", pos=(40, 210))

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
        self.tc1 = wx.TextCtrl(self, pos=(65, 30), style=wx.TE_READONLY)
        self.tc2 = wx.TextCtrl(self, pos=(65, 60), style=wx.TE_READONLY)
        self.tc3 = wx.TextCtrl(self, pos=(65, 90), style=wx.TE_READONLY)
        self.tc4 = wx.TextCtrl(self, pos=(65, 120), style=wx.TE_READONLY)
        self.tc5 = wx.TextCtrl(self, pos=(65, 150), style=wx.TE_READONLY)
        self.tc6 = wx.TextCtrl(self, pos=(65, 180), style=wx.TE_READONLY)
        self.tc7 = wx.TextCtrl(self, pos=(65, 210), style=wx.TE_READONLY)

        # set the angle value in the text control box
        self.tc1.SetValue('0')
        self.tc2.SetValue('0')
        self.tc3.SetValue('0')
        self.tc4.SetValue('0')
        self.tc5.SetValue('0')
        self.tc6.SetValue('0')

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
