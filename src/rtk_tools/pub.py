from .topic import rtkTopic

import Tkinter as tk
import ttk

import roslib
import rospy
from std_msgs.msg import Bool

class rtkPub(rtkTopic):
  def cb_pub(self):
    if self.discon:
      self.label.config(background='#FF0000')
    else:
      self.pub.publish(self.msg)
      self.label.config(background='#555555')
    self.dimmer=1
  def on_connect(self,topic_type):
    self.pub=rospy.Publisher(self.prop["name"],topic_type,queue_size=1)
    self.msg=topic_type()
    if "data" in self.prop:
      exec("self.msg"+self.prop["data"])
  def __init__(self,page,prop):
    super(rtkPub,self).__init__(page,prop)
    self.io=tk.Button(page.frame,text="Do",command=self.cb_pub)
    self.io.grid(row=len(page.widgets),column=2,sticky="nsw")
    self.dimmer=0
  def reflesh(self):
    if self.discon: super(rtkPub,self).reflesh()
    if self.dimmer>0:
      self.dimmer=self.dimmer-1
      if self.dimmer==0:
        self.label.config(background='#CCCCCC')
    return