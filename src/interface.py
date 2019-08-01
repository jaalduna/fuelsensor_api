from Tkinter import *
import sys
from Bootloader import Bootloader



		
#---------Raiz Ventana-----------------------------
raiz=Tk()
raiz.title("Fuel Sensor")
raiz.resizable(1,1)
raiz.iconbitmap("C:/Users/HP/Desktop/fuelsensor_api/icon/aiko_ico3.ico")# icono Aiko en la parte superior izquierda
#raiz.geometry("650x350")# dimenciones de pantalla                                                                                                                                                                                     
#raiz.config(bg="blue")


#----------Frame1--------------------
miFrame=Frame(raiz,width=650,height=350) # empaqueta el frame en la raiz y lo dimensiona
miFrame.pack(side="left",anchor="n") # posiciona el frame arriba en la parte izquierda
miFrame.pack(fill="both", expand="True") #expande el fram en x y en y 
#miFrame.config(bg="red")
miFrame.config(cursor="hand2") #cambiar icono cursor
#miFrame.config(cursor="pirate")

#------------Label de Bienvenida------

miLabel=Label(miFrame, text="Bienvenido a Fuel Sensor",font=("Comic Sans MS", 18)) #especifico que el label iran e miFrame
miLabel.grid(row=0, column=0, sticky="w", pady=10, columnspan=2) # columnspan significa el num de colums que ocupa

#--------entradas en pantalla-----------------

ipCuadro=StringVar()
portCuadro=StringVar()

cuandroIp=Entry(miFrame, textvariable=ipCuadro)
cuandroIp.grid(row=1, column=1,sticky="w",padx=2,pady=2)
cuandroPort=Entry(miFrame, textvariable=portCuadro)
cuandroPort.grid(row=2, column=1,sticky="w",padx=2,pady=2)
cuandroVersion=Entry(miFrame, textvariable=ipCuadro)
cuandroVersion.grid(row=3, column=1,sticky="w",padx=2,pady=2)
cuandroJumpToApp=Entry(miFrame, textvariable=ipCuadro)
cuandroJumpToApp.grid(row=4, column=1,sticky="w",padx=2,pady=2)


#--------Label---------------------
ipLabel= Label(miFrame, text="IP: ")
ipLabel.grid(row=1, column=0,sticky="e",padx=2,pady=2)
portLabel= Label(miFrame, text="Port: ")
portLabel.grid(row=2, column=0,sticky="e",padx=2,pady=2)

#---------botones bootloader con cuadros al lado-------------
botonVersion=Button(miFrame, text="Version")
botonVersion.grid(row=3, column=0,sticky="e",padx=2,pady=2)


botonJumpToApp=Button(miFrame, text="Jump to app")
botonJumpToApp.grid(row=4, column=0,sticky="e",padx=2,pady=2)







raiz.mainloop()