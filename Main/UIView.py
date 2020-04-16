import wx
import wx.adv
import Config

class MyTaskBarIcon(wx.adv.TaskBarIcon):
    ICON = Config.IconPath  # 图标地址
    ID_ABOUT = wx.NewIdRef()  # 菜单选项“关于”的ID
    ID_EXIT = wx.NewIdRef()  # 菜单选项“退出”的ID
    ID_SHOW_WEB = wx.NewIdRef()  # 菜单选项“显示页面”的ID
    TITLE = "二维码发送程序" #鼠标移动到图标上显示的文字

    def __init__(self):
        wx.adv.TaskBarIcon.__init__(self)
        self.SetIcon(wx.Icon(self.ICON), self.TITLE)  # 设置图标和标题
        self.Bind(wx.EVT_MENU, self.onAbout, id=self.ID_ABOUT)  # 绑定“关于”选项的点击事件
        self.Bind(wx.EVT_MENU, self.onExit, id=self.ID_EXIT)  # 绑定“退出”选项的点击事件
        self.Bind(wx.EVT_MENU, self.onShowWeb, id=self.ID_SHOW_WEB)  # 绑定“显示页面”选项的点击事件

    # “关于”选项的事件处理器
    def onAbout(self, event):
        wx.MessageBox('测试内容', "关于")

    # “退出”选项的事件处理器
    def onExit(self, event):
        wx.Exit()

    # “显示页面”选项的事件处理器
    def onShowWeb(self, event):
        pass

    # 创建菜单选项
    def CreatePopupMenu(self):
        menu = wx.Menu()
        for mentAttr in self.getMenuAttrs():
            menu.Append(mentAttr[1], mentAttr[0])
        return menu

    # 获取菜单的属性元组
    def getMenuAttrs(self):
        return [('进入程序', self.ID_SHOW_WEB),
                ('关于', self.ID_ABOUT),
                ('退出', self.ID_EXIT)]


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self)
        MyTaskBarIcon()#显示系统托盘图标


class MyApp(wx.App):
    def OnInit(self):
        MyFrame()
        return True


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()