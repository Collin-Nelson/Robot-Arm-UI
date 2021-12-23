import wx

from Serial import SerialComms


class PosesQueuePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, pos=(5, 5), size=(200, 550), style=wx.SUNKEN_BORDER)

        title = wx.StaticText(self, label="Pose Queue", pos=(5, 5), size=(200, 20), style=wx.ALIGN_LEFT)
        self.SetBackgroundColour('white')
        font = title.GetFont()
        font.PointSize = 12
        font = font.Bold()
        title.SetFont(font)

        global tcQueue
        tcQueue = wx.TextCtrl(self, pos=(0, 30), size=(200, 470), style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)

        # Button to run the pose queue
        runAllBtn = wx.Button(self, label='Run Queue', pos=(5, 505), size=(175, 30))

        # Bind button to its action
        runAllBtn.Bind(wx.EVT_BUTTON, self.runAllBtnPress)

    # Actions for button
    def runAllBtnPress(self, event):
        num = tcQueue.GetNumberOfLines()
        for i in range(num):
            # SerialComms.SerialWrite(tcQueue.GetLineText(self, i))
            print(tcQueue.GetLineText(i))
            lineLen = tcQueue.GetLineLength(i)
            tcQueue.Remove(0, lineLen)

    def AddToQueue(string):
        tcQueue.write(string)
