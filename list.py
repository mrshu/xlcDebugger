#!/usr/bin/python

# autowidth.py

import wx
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin

class DebugListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin):
	def __init__(self, parent):
		wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT)
		ListCtrlAutoWidthMixin.__init__(self)
		
		self.InsertColumn(0, 'time', width = 140)
		self.InsertColumn(1, 'type', width = 140)
		self.InsertColumn(2, 'function', width = 200)
		self.InsertColumn(3, 'message', wx.LIST_FORMAT_LEFT, 90)

