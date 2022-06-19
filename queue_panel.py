import wx


class queue_panel(wx.Panel):
    def __init__(self, parent, serial):
        wx.Panel.__init__(self, parent=parent, pos=(415, 5), size=(400, 465))

        self.serial = serial

        self.filename = "temp"

        title = wx.StaticText(self, label="Pose Queue", pos=(5, 5), size=(200, 20), style=wx.ALIGN_LEFT)
        self.SetBackgroundColour('white')
        font = title.GetFont()
        font.PointSize = 12
        font = font.Bold()
        title.SetFont(font)

        # tcQueue
        self.tcQueue = wx.TextCtrl(self, pos=(5, 30), size=(185, 355),
                                   style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)

        # Button to run or clear or save or load the pose queue
        run_btn = wx.Button(self, label='Run Queue', pos=(5, 430), size=(90, 30))
        clear_btn = wx.Button(self, label='Clear Queue', pos=(100, 395), size=(90, 30))
        save_btn = wx.Button(self, label='Save Queue', pos=(5, 395), size=(90, 30))
        load_btn = wx.Button(self, label='Load Queue', pos=(100, 430), size=(90, 30))

        # Bind buttons to their actions
        run_btn.Bind(wx.EVT_BUTTON, self.run_btn_press)
        clear_btn.Bind(wx.EVT_BUTTON, self.clear_btn_press)
        save_btn.Bind(wx.EVT_BUTTON, self.save_btn_press)
        load_btn.Bind(wx.EVT_BUTTON, self.load_btn_press)

        # Command input section
        command_input_title = wx.StaticText(self, label="Command Input", size=(200, 18), pos=(220,5), style=wx.ALIGN_LEFT)
        command_input_title.SetFont(font)

        # Text input to add command to queue
        self.command_input_tc = wx.TextCtrl(self, pos=(220, 35), size=(150,25))

        # Button to to add pose to the queue
        add_to_queue_btn = wx.Button(self, label='Add to Queue', pos=(220, 65), size=(175, 30))

        # Bind buttons to actions
        add_to_queue_btn.Bind(wx.EVT_BUTTON, self.add_to_queue_btn_press)

    # Actions for button
    def btn1_press(self, event):
        print("Add to queue button pressed")
        value1 = self.tc1.GetValue()


    # Actions for button
    def run_btn_press(self, event):
        num = self.tcQueue.GetNumberOfLines()
        for i in range(num - 1):
            line_len = self.tcQueue.GetLineLength(0)
            self.serial.serial_write(self.tcQueue.GetLineText(0))
            print(self.tcQueue.GetLineText(0))
            self.tcQueue.Remove(0, line_len + 2)

    def clear_btn_press(self, event):
        while self.tcQueue.GetNumberOfLines() > 1:
            length = self.tcQueue.GetLineLength(0)
            self.tcQueue.Remove(0, length + 2)

    def save_btn_press(self, event):
        dialog = wx.FileDialog(self, 'Choose a file')
        if dialog.ShowModal() == wx.ID_OK:
            self.filename = dialog.GetFilename()
            save_file = open(self.filename, 'w')  # open the file (self.filename) to store our saved data
            save_file.write(
                self.tcQueue.GetValue())  # get our text from the textctrl, and write it out to the file we just opened.
            save_file.close()  # and then close the file.

    def load_btn_press(self, event):
        dialog = wx.FileDialog(self, 'Choose a File')
        if dialog.ShowModal() == wx.ID_OK:
            self.filename = dialog.GetFilename()
            loadfile = open(self.filename, 'r')
            lines = loadfile.readlines()
            for line in lines:
                self.tcQueue.write(line)
            loadfile.close()

    def add_to_queue_btn_press(self, event):
        value = self.command_input_tc.GetValue()
        self.tcQueue.write(value)
