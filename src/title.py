from .widget import rtkWidget

import Tkinter as tk
import ttk

class rtkTitle(rtkWidget):
  def __init__(self,page,prop):
    super(rtkTitle,self).__init__(page,prop)
    self.label.config(foreground='#FFFFFF')
    self.label.config(background='#555555')
    self.label.config(anchor='w')
    self.label.grid_forget()
    self.label.grid(row=len(page.widgets),column=1,columnspan=2,sticky="nsew")
  def reflesh(self):
    return
