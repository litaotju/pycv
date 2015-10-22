# -*- coding:utf-8 -*- #
try:
    import cv2
    import wx
except ImportError,e:
    print e
    exit(-1)
# user defined module
from frame import MyFrame

                
class App(wx.App):
    def OnInit(self):
        self.frame = MyFrame("FirstFrame",(60, 60), (400,400) )
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True
        
def Main():
    app = App()
    app.MainLoop()

if __name__ ==  "__main__":
    Main()
