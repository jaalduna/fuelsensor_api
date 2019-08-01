from Tkinter import *
from Bootloader import Bootloader
from Fuelsensor_interface import Fuelsensor_interface
import time

class Application(Bootloader,Fuelsensor_interface):
    def __init__(self, root, title):
    	self.bld=Bootloader('192.168.100.187',5000)
    	
        self.root = root
        self.root.title(title) 

        self.label = Label(self.root, text='Hello')
        self.label.grid(row=0, column=0)  
        self.jump=self.bld.jump_to_app()
        self.close=self.bld.close_socket()
    def jump(self):
    	self.jump=self.bld.jump_to_app()
    def altura(self):
    	self.get_height()
    	self.close_socket()


root=Tk()
app=Application(root,"holanda que talca")

app.jump_to_app()
root.mainloop()