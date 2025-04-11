from tkinter import*
import pyqrcode
Window=Tk()
def qrcode():
    qrcode=pyqrcode.create(linkEntry.get())
    qrcode.png('MyQR.png',scale=6)
    photo=PhotoImage(file="MyQR.png")
    label2=Label(Window,image=photo,bd=2,borderwidth=20,bg="orange")
    label2.image=photo
    label2.place(x=100,y=240)
heading=Label(Window,text=" QR Code Generator",font=("time new roman",40),bg='#8470FF',fg='black',anchor='w').place(x=0,y=0,width=900)    
Window.geometry('500x700+250+100')
Window.title("QR Code Genarator")
label1=Label(Window,text=" Enter Your Link: ",font=('time new roman',14),bg="black",fg="#FFF0F5",borderwidth=10)
label1.place(x=10,y=100)
linkValue=StringVar()
linkEntry=Entry(Window,textvariable=linkValue,font=('time new roman',18),borderwidth=7)
linkEntry.place(x=160,y=100)
button1=Button(Window,text='QR Genarate',command=qrcode,font=('time new roman',18))
button1.place(x=100,y=180)


Window.mainloop()
