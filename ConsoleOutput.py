import wx, sys


class RedirectText(object):
    def __init__(self, aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self, string):
        self.out.WriteText(string)


class ConsoleOutputPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, pos=(5, 5), size=(1225, 225), style=wx.SUNKEN_BORDER)

        title = wx.StaticText(self, label="Console Output", pos=(5, 5), size=(200, 20), style=wx.ALIGN_LEFT)
        self.SetBackgroundColour('white')
        font = title.GetFont()
        font.PointSize = 12
        font = font.Bold()
        title.SetFont(font)

        self.log = wx.TextCtrl(self, pos=(0, 30), size=(1220, 190), style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        redir = RedirectText(self.log)
        sys.stdout = redir
