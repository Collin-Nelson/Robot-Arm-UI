import wx

from AngleDisplayPanel import AngleDisplayPanel
from AngleInputPanel import AngleInputPanel
from HomeCommands import HomeCommands
from ZeroCommands import ZeroCommands
from TextCommand import TextCommand
from EndEffectorCommand import EndEffectorCommand
from ConsoleOutput import ConsoleOutputPanel
from PosesQueuePanel import PosesQueuePanel
from PoseGeneratorPanel import PoseGeneratorPanel
from AccelSet import AccelSet
from VelSet import VelSet
from MinAngleSet import MinAngleSet
from MaxAngleSet import MaxAngleSet

class MainFrame(wx.Frame):
    def __init__(self, serial):
        super().__init__(parent=None, title='Robot Arm UI', size=(1250, 750))

        topPanel = wx.Panel(self)
        constPanel = wx.Panel(topPanel)
        topPanel.SetBackgroundColour('gray')

        panel1 = ConsoleOutputPanel(constPanel, serial)
        panel2 = AngleDisplayPanel(constPanel, serial)

        sizer1 = wx.BoxSizer(wx.VERTICAL)
        sizer1.Add(panel1, 0, wx.EXPAND | wx.ALL, border=10)
        sizer1.Add(panel2, 0, wx.EXPAND | wx.ALL, border=10)
        constPanel.SetSizer(sizer1)

        ntbk = wx.Notebook(topPanel)

        tab1 = ControlTab(ntbk, serial)
        tab2 = PoseQueueTab(ntbk, serial)
        tab3 = ParametersTab(ntbk, serial)

        ntbk.AddPage(tab1, "Manual Control")
        ntbk.AddPage(tab2, "Pose Queue")
        ntbk.AddPage(tab3, "Set Parameters")

        sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer2.Add(constPanel, 0, wx.EXPAND | wx.ALL, border=10)
        sizer2.Add(ntbk, 0, wx.EXPAND | wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        topPanel.SetSizer(sizer2)


class ControlTab(wx.Panel):
    def __init__(self, parent, serial):
        wx.Panel.__init__(self, parent)

        self.SetBackgroundColour('gray')

        panel2 = AngleInputPanel(self, serial)
        panel3 = EndEffectorCommand(self, serial)
        panel4 = TextCommand(self, serial)
        panel5 = HomeCommands(self, serial)
        panel6 = ZeroCommands(self, serial)

        sizer = wx.GridSizer(2, 3, 5, 5)
        sizer.Add(panel2, 0, wx.EXPAND | wx.ALL, border=0)
        sizer.Add(panel3, 0, wx.EXPAND | wx.ALL, border=0)
        sizer.Add(panel4, 0, wx.EXPAND | wx.ALL, border=0)
        sizer.Add(panel5, 0, wx.EXPAND | wx.ALL, border=0)
        sizer.Add(panel6, 0, wx.EXPAND | wx.ALL, border=0)
        self.SetSizer(sizer)


class PoseQueueTab(wx.Panel):
    def __init__(self, parent, serial):
        wx.Panel.__init__(self, parent)

        self.SetBackgroundColour('gray')

        panel1 = PosesQueuePanel(self, serial)
        panel2 = PoseGeneratorPanel(self, panel1)

        sizer = wx.GridSizer(1, 2, 5, 5)
        sizer.Add(panel1, 0, wx.EXPAND | wx.ALL, border=10)
        sizer.Add(panel2, 0, wx.EXPAND | wx.ALL, border=10)
        self.SetSizer(sizer)


class ParametersTab(wx.Panel):
    def __init__(self, parent, serial):
        wx.Panel.__init__(self, parent)

        self.SetBackgroundColour('gray')

        panel1 = AccelSet(self, serial)
        panel2 = VelSet(self, serial)
        panel3 = MinAngleSet(self, serial)
        panel4 = MaxAngleSet(self, serial)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(panel1, 0, wx.EXPAND | wx.ALL, border=5)
        sizer.Add(panel2, 0, wx.EXPAND | wx.ALL, border=5)
        sizer.Add(panel3, 0, wx.EXPAND | wx.ALL, border=5)
        sizer.Add(panel4, 0, wx.EXPAND | wx.ALL, border=5)
        self.SetSizer(sizer)
