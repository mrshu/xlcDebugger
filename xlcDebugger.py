#!/usr/bin/env python
import wx

from list import DebugListCtrl

class xlcDebugger(wx.Frame):
	def __init__(self, parent, id, title = 'xlcDebugger'):
		display = wx.DisplaySize()
		wx.Frame.__init__(self, parent, id, title, size = (1024, 768))
		
		self.splitter = wx.SplitterWindow(self, -1, style=wx.SP_BORDER)

		self.bars = wx.Panel(self.splitter)
		self.bars.SetBackgroundColour(wx.WHITE)
		

		self.messages = wx.Panel(self.splitter)
		self.list = DebugListCtrl(self.messages)	
		listbox = wx.BoxSizer(wx.VERTICAL)
		listbox.Add(self.list, 1, wx.EXPAND, 0)
		
		self.messages.SetSizer(listbox)

		self.splitter.SplitHorizontally(self.bars, self.messages)

		self.Centre()
		self.Maximize()
		self.Show(True)

if __name__ == "__main__":
	app = wx.App()
	xlcDebugger(None, -1)
	app.MainLoop()

