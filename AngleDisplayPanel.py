import wx

class AngleDisplayPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, pos=(5, 5), size=(200, 200), style=wx.SUNKEN_BORDER)

        title = wx.StaticText(self, label="Joint Angle Display", size=(200, 18), style=wx.ALIGN_CENTER_HORIZONTAL)
        self.SetBackgroundColour('white')
        font = title.GetFont()
        font.PointSize = 12
        font = font.Bold()
        title.SetFont(font)

        # Add rectangular status lights to display if endstops are currently pressed
        self.statusLight1 = wx.StaticBox(self, wx.ID_ANY, "", size=(20, 20), pos=(5, 25), style=wx.SUNKEN_BORDER)
        self.statusLight2 = wx.StaticBox(self, wx.ID_ANY, "", size=(20, 20), pos=(5, 55), style=wx.SUNKEN_BORDER)
        self.statusLight3 = wx.StaticBox(self, wx.ID_ANY, "", size=(20, 20), pos=(5, 85), style=wx.SUNKEN_BORDER)
        self.statusLight4 = wx.StaticBox(self, wx.ID_ANY, "", size=(20, 20), pos=(5, 115), style=wx.SUNKEN_BORDER)
        self.statusLight5 = wx.StaticBox(self, wx.ID_ANY, "", size=(20, 20), pos=(5, 145), style=wx.SUNKEN_BORDER)
        self.statusLight6 = wx.StaticBox(self, wx.ID_ANY, "", size=(20, 20), pos=(5, 175), style=wx.SUNKEN_BORDER)

        # Labels for the joint angle text boxes
        lbl1 = wx.StaticText(self, label="J1", pos=(40, 25))
        lbl2 = wx.StaticText(self, label="J2", pos=(40, 55))
        lbl3 = wx.StaticText(self, label="J3", pos=(40, 85))
        lbl4 = wx.StaticText(self, label="J4", pos=(40, 115))
        lbl5 = wx.StaticText(self, label="J5", pos=(40, 145))
        lbl6 = wx.StaticText(self, label="J6", pos=(40, 175))

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
        self.tc1 = wx.TextCtrl(self, pos=(65, 25), style=wx.TE_READONLY)
        self.tc2 = wx.TextCtrl(self, pos=(65, 55), style=wx.TE_READONLY)
        self.tc3 = wx.TextCtrl(self, pos=(65, 85), style=wx.TE_READONLY)
        self.tc4 = wx.TextCtrl(self, pos=(65, 115), style=wx.TE_READONLY)
        self.tc5 = wx.TextCtrl(self, pos=(65, 145), style=wx.TE_READONLY)
        self.tc6 = wx.TextCtrl(self, pos=(65, 175), style=wx.TE_READONLY)

        # set the angle value in the text control box
        self.tc1.SetValue('0')
        self.tc2.SetValue('0')
        self.tc3.SetValue('0')
        self.tc4.SetValue('0')
        self.tc5.SetValue('0')
        self.tc6.SetValue('0')
