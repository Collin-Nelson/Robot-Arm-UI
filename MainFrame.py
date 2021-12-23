import wx

from AngleDisplayPanel import AngleDisplayPanel
from AngleInputPanel import AngleInputPanel
from HomeCommands import HomeCommands
from ZeroCommands import ZeroCommands
from TextCommand import TextCommand
from EndEffectorCommand import EndEffectorCommand
from ConsoleOutput import ConsoleOutputPanel

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='UI Test', size=(1250, 750))

        p = wx.Panel(self)
        nb = wx.Notebook(p)

        tab1 = ControlTab(nb)
        tab2 = Tab2(nb)

        nb.AddPage(tab1, "Tab 1")
        nb.AddPage(tab2, "Tab 2")

        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)


class ControlTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        # t = wx.StaticText(self, -1, "Controls Tab", (20,20))

        self.SetBackgroundColour('gray')

        self.Panel = AngleDisplayPanel(self)
        self.Panel = AngleInputPanel(self)
        self.Panel = HomeCommands(self)
        self.Panel = ZeroCommands(self)
        self.Panel = TextCommand(self)
        self.Panel = EndEffectorCommand(self)
        self.Panel = ConsoleOutputPanel(self)



class Tab2(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        # t = wx.StaticText(self, -1, "Second Tab", (20,20))

        self.SetBackgroundColour('gray')
