from Tkinter import *


raiz=Tk()
raiz.title("Fuel Sensor")
raiz.resizable(1,1)
raiz.iconbitmap("C:/Users/HP/Desktop/fuelsensor_api/icon/aiko_ico3.ico")
raiz.geometry("650x350")
#raiz.config(bg="blue")

miFrame=Frame(raiz,width=650,height=350) # empaqueta el frame en la raiz
miFrame.pack(side="left",anchor="n") # posiciona el frame arriba en la parte izquierda
miFrame.pack(fill="both", expand="True") #expande el fram en x y en y 
#miFrame.config(bg="red")
miFrame.config(cursor="hand2") #cambiar icono cursor
#miFrame.config(cursor="pirate")

miLabel=Label(miFrame, text="Bienvenido a Fuel Sensor",font=("Comic Sans MS", 18)) #especifico que el label iran e miFrame
miLabel.grid(row=0, column=2, sticky="e", pady=10)


cuandroIp=Entry(miFrame)
cuandroIp.grid(row=1, column=1,sticky="e",padx=2,pady=2)
cuandroPort=Entry(miFrame)
cuandroPort.grid(row=2, column=1,sticky="e",padx=2,pady=2)

ipLabel= Label(miFrame, text="IP: ")
ipLabel.grid(row=1, column=0,sticky="e",padx=2,pady=2)
portLabel= Label(miFrame, text="Port: ")
portLabel.grid(row=2, column=0,sticky="e",padx=2,pady=2)

botonAplicar=Button(miFrame, text="enviar")
botonAplicar.grid(row=3, column=1,sticky="e",padx=2,pady=2)






raiz.mainloop()