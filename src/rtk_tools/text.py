from .widget import rtkWidget
from . import dictlib

import Tkinter as tk
import ttk

import roslib
import rospy

class rtkText(rtkWidget):
  interval=1
  def __init__(self,page,prop):
    super(rtkText,self).__init__(page,prop)
    self.parse(prop["name"])
    self.io=tk.Entry(page.frame,
      font=self.label["font"],
      width=self.Config["width"][1])
    self.io.grid(row=len(page.widgets),column=2,sticky="nswe")
    self.io.insert(0,'---')
    self.value=''
    self.io.bind('<Key-Return>',self.on_change)
    self.io.bind('<KeyPress>',self.on_key)
    self.io.bind('<FocusOut>',self.on_abort)
    self.set_timeout(1)

  def parse(self,str):
    keys=str.split("/")
    self.lb=""
    self.rb=""
    for k in keys:
      if len(k)==0: continue
      self.lb=self.lb+"{'"+k+"':"
      self.rb=self.rb+'}'
  def set(self,value):
    self.io.delete(0,tk.END)
    self.io.insert(0,value)
    param=eval(self.lb+"'"+value+"'"+self.rb)
    dictlib.merge(self.Param,param)
    self.value=value
    rospy.set_param(self.prop["name"],value)
  def on_change(self,event):
    self.set(self.io.get())
    self.io.config(foreground='#000000')
  def on_key(self,event):
    self.io.config(foreground='#FF0000')    
  def on_abort(self,event):
    self.io.config(foreground='#000000')
    self.set(self.value)
  def on_timeout(self):
    try:
      value=rospy.get_param(self.prop["name"])
      if value!=self.value:
        self.set(value)
    except:
      rospy.logwarn("param "+self.prop["name"]+" not found")
    self.set_timeout(self.interval)
    return

