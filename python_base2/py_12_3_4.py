#!/usr/bin/env python
"""code 12-5"""

import wx

app = wx.App()
win = wx.Frame(None, title = "Simple Editor", size = (410, 335))

bkg = wx.Panel(win)

loadbtn = wx.Button(bkg, label = 'Open')
savebtn = wx.Button(bkg, label = 'Save')

filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style = wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(filename, proportion = 1, flag = wx.EXPAND)
hbox.Add(loadbtn, proportion = 0, flag = wx.LEFT, border = 5)
hbox.Add(savebtn, proportion = 0, flag = wx.LEFT, border = 5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
vbox.Add(contents, proportion = 1, flag = wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border = 5)

bkg.SetSizer(vbox)

win.Show()
app.MainLoop()