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


class MainFrame(wx.Frame):
    def __init__(self, serial):
        super().__init__(parent=None, title='Robot Arm UI', size=(1250, 750))

        p = wx.Panel(self)
        nb = wx.Notebook(p)

        tab1 = ControlTab(nb, serial)
        tab2 = PoseQueueTab(nb, serial)
        tab3 = ParametersTab(nb)

        nb.AddPage(tab1, "Manual Control")
        nb.AddPage(tab2, "Pose Queue")
        nb.AddPage(tab3, "Set Parameters")

        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)


class ControlTab(wx.Panel):
    def __init__(self, parent, serial):
        wx.Panel.__init__(self, parent)
        # t = wx.StaticText(self, -1, "Controls Tab", (20,20))

        self.SetBackgroundColour('gray')

        self.Panel = AngleDisplayPanel(self, serial)
        self.Panel = AngleInputPanel(self, serial)
        self.Panel = HomeCommands(self, serial)
        self.Panel = ZeroCommands(self, serial)
        self.Panel = TextCommand(self, serial)
        self.Panel = EndEffectorCommand(self, serial)
        self.Panel = ConsoleOutputPanel(self, serial)


class PoseQueueTab(wx.Panel):
    def __init__(self, parent, serial):
        wx.Panel.__init__(self, parent)
        # t = wx.StaticText(self, -1, "Second Tab", (20,20))

        self.SetBackgroundColour('gray')

        self.Panel = PosesQueuePanel(self, serial)
        self.Panel = PoseGeneratorPanel(self, self.Panel)
        # self.Panel = ConsoleOutputPanel(self, serial)


class ParametersTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        # t = wx.StaticText(self, -1, "Second Tab", (20,20))

        self.SetBackgroundColour('gray')
