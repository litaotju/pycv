# -*- coding:utf-8 -*- #

# dependencies
import os 
import wx
import cv2
import numpy as np

# user library
import display as dp

class MyFrame(wx.Frame):
    
    def __init__(self, title, pos, size):
        wx.Frame.__init__(self, None, -1, title, pos, size)
        self.initMemu()
        self.initStatus()
        self.initLog()

    def initMemu(self):
        # 例化1个Munu对象,添加两个Item
        menuFile = wx.Menu()
        menuFile.Append(3, "Open")
        menuFile.AppendSeparator()
        menuFile.Append(1, "Exit")

        menuDraw = wx.Menu()
        menuDraw.Append(4, "Draw")

        menuAbout = wx.Menu()
        menuAbout.Append(2, "About")

        # 例化一个menuBar，并且将该menuFile传递给menuBar
        menuBar = wx.MenuBar()
        menuBar.Append(menuFile, "File")
        menuBar.Append(menuDraw, "Draw")
        menuBar.Append(menuAbout, "About")

        # 将上面这个menuBar，传递给self.SetMenuBar()这个函数
        self.SetMenuBar(menuBar)    
        self.Bind(wx.EVT_MENU, self.OnExit, id = 1)
        self.Bind(wx.EVT_MENU, self.OnAbout, id = 2)
        self.Bind(wx.EVT_MENU, self.OnOpen, id = 3)
        self.Bind(wx.EVT_MENU, self.OnDraw, id = 4)

    def initStatus(self):
        self.CreateStatusBar()
        self.SetStatusText("This is Status Text")

    def initLog(self):
        self.mainlogger = wx.Log()
        wx.Log_SetActiveTarget(self.mainlogger)


    def OnOpen(self, event):
        '''打开图片的界面
        '''
        pic_wildcard = "All files(*.*)|*.*|Picture files(*.jpg)|*.jpg"
        dlg = wx.FileDialog(self, message = "Open paint file...",  
                            defaultDir = os.getcwd(),   
                            style = wx.OPEN,  
                            wildcard = pic_wildcard
            )

        filename = None
        if dlg.ShowModal() == wx.ID_OK:  
            filename = dlg.GetPath()  
            self.mainlogger.LogText("Opening file %s" % filename)
            dlg.Destroy()
        if filename:
            ext = os.path.splitext(filename)
            if ext[1] == ".jpg":
                dp.displayImg(filename)
            elif ext[1] == ".avi":
                print filename
                dp.displayVideo(filename)
            else:
                wx.MessageBox("UnSupported File Format")
                self.mainlogger.LogText("%s" % str(ext))
        else:       
            wx.MessageBox("There is a Problem Opening File")

    def OnExit(self, event):
        print "Exiting..."
        self.Close()
        
    def OnDraw(self, event):
        "在屏幕上画一个圆圈"
        def draw_circle(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDBLCLK:
                cv2.circle(img, (x,y), 100, (255,0,0), -1)
            elif event == cv2.EVENT_RBUTTONDBLCLK:
                cv2.circle(img, (x,y), 50, (0, 255, 0), -1)
        # Create a black image, a window and bind the function to window
        img = np.zeros((512,512,3), np.uint8)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image',draw_circle)
        while(1):
            cv2.imshow('image',img)
            if cv2.waitKey(20) & 0xFF == 27:
                break
        cv2.destroyAllWindows()    

    def OnAbout(self, event):
        wx.MessageBox("This is a wxPython Hello GUI sample,",
                "About Hello GUI",wx.OK|wx.ICON_INFORMATION, self)

    