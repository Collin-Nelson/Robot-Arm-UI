import wx

from motion_panel import motion_panel
from status_panel import status_panel
from queue_panel import queue_panel
from PoseGeneratorPanel import PoseGeneratorPanel

class main_frame(wx.Frame):
    def __init__(self, serial):
        super().__init__(parent=None, title='Robot Arm UI', size=(1450, 750))

        topPanel = wx.Panel(self)
        constPanel = wx.Panel(topPanel)
        topPanel.SetBackgroundColour('gray')
        panel1 = status_panel(constPanel, serial)

        sizer1 = wx.BoxSizer(wx.VERTICAL)
        sizer1.Add(panel1, 0, wx.EXPAND | wx.ALL, border=10)
        constPanel.SetSizer(sizer1)

        ntbk = wx.Notebook(topPanel)

        tab1 = control_tab(ntbk, serial)
        tab2 = queue_tab(ntbk, serial)

        ntbk.AddPage(tab1, "Manual Control")
        ntbk.AddPage(tab2, "Pose Queue")

        sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer2.Add(constPanel, 0, wx.EXPAND | wx.ALL, border=10)
        sizer2.Add(ntbk, 0, wx.EXPAND | wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        topPanel.SetSizer(sizer2)


class control_tab(wx.Panel):
    def __init__(self, parent, serial):
        wx.Panel.__init__(self, parent)

        self.SetBackgroundColour('gray')

        panel2 = motion_panel(self, serial)

        sizer = wx.GridSizer(1, 1, 5, 5)
        sizer.Add(panel2, 0, wx.EXPAND)
        self.SetSizer(sizer)


class queue_tab(wx.Panel):
    def __init__(self, parent, serial):
        wx.Panel.__init__(self, parent)

        self.SetBackgroundColour('gray')

        panel1 = queue_panel(self, serial)

        sizer = wx.GridSizer(1, 1, 5, 5)
        sizer.Add(panel1, 0, wx.EXPAND)
        self.SetSizer(sizer)

