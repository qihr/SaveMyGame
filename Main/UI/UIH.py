import wx
import wx.adv
import datetime
from wx.lib.embeddedimage import PyEmbeddedImage
#
# A white box 28x28 pixels
#
toggletest = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAIAAAD9b0jDAAAACXBIWXMAAAsTAAALEwEAmpwY'
    b'AAAAB3RJTUUH4wMfCgElTFaeRQAAAB1pVFh0Q29tbWVudAAAAAAAQ3JlYXRlZCB3aXRoIEdJ'
    b'TVBkLmUHAAAAKElEQVRIx2P8//8/A7UBEwMNwKiho4aOGjpq6Kiho4aOGjpq6OAzFADRYgM1'
    b'8cIRtgAAAABJRU5ErkJggg==')

class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self, frame):
        self.frame = frame
        self.toggle = 0
        wx.adv.TaskBarIcon.__init__(self)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.OnToggle)
        self.font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        self.font.SetPointSize(8)
        self.OnSetIcon(self.NewIcon())

    def CreatePopupMenu(self):
        menu = wx.Menu()
        togglem = wx.MenuItem(menu, wx.NewId(), 'Toggle Icon')
        menu.Bind(wx.EVT_MENU, self.OnToggle, id=togglem.GetId())
        menu.Append(togglem)
        menu.AppendSeparator()
        flashm = wx.MenuItem(menu, wx.NewId(), 'Flashing Icon')
        menu.Bind(wx.EVT_MENU, self.OnTimer, id=flashm.GetId())
        menu.Append(flashm)
        menu.AppendSeparator()
        quitm = wx.MenuItem(menu, wx.NewId(), 'Quit')
        menu.Bind(wx.EVT_MENU, self.OnQuit, id=quitm.GetId())
        menu.Append(quitm)
        return menu

    def NewIcon(self):
        bitmap = wx.Bitmap(toggletest.Bitmap)
        dc = wx.MemoryDC(bitmap)
        # Use current time as text, for want of something useful
        now = datetime.datetime.today()
        text = str(now.minute)+"\n"+str(now.second)
        dc.SetFont(self.font)
        dc.DrawText(text, 2, 2)
        del dc
        return bitmap

    def OnSetIcon(self, bitmap):
        icon = wx.Icon()
        icon.CopyFromBitmap(bitmap)
        self.SetIcon(icon)

    def OnToggle(self, event):
        bitmap = self.NewIcon()
        self.OnSetIcon(bitmap)

    def OnTimer(self,event):
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnUseTimer)
        self.timer.Start(1000)

    def OnUseTimer(self,event):
        self.OnToggle(None)

    def OnQuit(self, event):
        self.RemoveIcon()
        wx.CallAfter(self.Destroy)
        self.frame.Close()

if __name__ == '__main__':
    app = wx.App()
    frame=wx.Frame(None)
    TaskBarIcon(frame)
    app.MainLoop()