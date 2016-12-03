
import wx


#----------------------------------------------------------------------

class TestListBox(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                      'twelve', 'thirteen', 'fourteen']

        wx.StaticText(self, -1, "This example uses the wx.ListBox control.", (120, 10))
        wx.StaticText(self, -1, "Select one:", (100, 50))
        self.lb1 = wx.ListBox(self, 60, (1, 1), (90, 120), sampleList,  wx.LB_SINGLE)
        self.Bind(wx.EVT_LISTBOX, self.EvtListBox, self.lb1)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.EvtListBoxDClick, self.lb1)
        self.lb1.Bind(wx.EVT_RIGHT_UP, self.EvtRightButton)
        self.lb1.SetSelection(3)
        self.lb1.Append("with data", "This one has data");
        self.lb1.SetClientData(2, "This one has data");

    def EvtListBox(self, event):
        self.log.WriteText('EvtListBox: %s, %s, %s, %s\n' %
                           (event.GetString(),
                            event.IsSelection(),
                            event.GetSelection(),
                            event.GetClientData()))

        lb = event.GetEventObject()
        data = lb.GetClientData(lb.GetSelection())

        if data is not None:
            self.log.WriteText('\tdata: %s\n' % data)


    def EvtListBoxDClick(self, event):
        self.log.WriteText('EvtListBoxDClick: %s\n' % self.lb1.GetSelection())
        self.lb1.Delete(self.lb1.GetSelection())

    def EvtMultiListBox(self, event):
        self.log.WriteText('EvtMultiListBox: %s\n' % str(self.lb2.GetSelections()))

    def EvtRightButton(self, event):
        self.log.WriteText('EvtRightButton: %s\n' % event.GetPosition())

        if event.GetEventObject().GetId() == 70:
            selections = list(self.lb2.GetSelections())
            selections.reverse()

            for index in selections:
                self.lb2.Delete(index)

#----------------------------------------------------------------------

def runTest(frame, nb, log):
    win = TestListBox(nb, log)
    return win

#----------------------------------------------------------------------



overview = """<html><body>
<h2><center>DemoName</center></h2>

Say something nice here

</body></html>
"""



if __name__ == '__main__':
    import sys,os
    import run
    run.main(['', os.path.basename(sys.argv[0])] + sys.argv[1:])

