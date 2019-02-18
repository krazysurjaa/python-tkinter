from tkinter import *
root = Tk()

def var_states():
	print("male : %d,\n female : %d" %(var1.get(),var2.get()))
	
Label(root,text="Your sex : ").grid(row = 0,sticky=W)
var1 = IntVar()
Checkbutton(root,text="male",variable=var1).grid(row=1,sticky=W)
var2 = IntVar()
Checkbutton(root,text="female",variable=var2).grid(row=2,sticky=W)
Button(root,text="Quit",command=root.quit).grid(row=3,sticky=W,pady=4)
Button(root,text="Show",command=var_states).grid(row=4,sticky=W,pady=4)
mainloop()


