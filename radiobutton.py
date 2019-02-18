import tkinter as tk

root  = tk.Tk()
v = tk.IntVar()
v.set(1)

language = [("python",1),("perl",2),("java",3),("c++",4),("C",5)]

def ShowChoices():
	print(v.get())
tk.Label(root,text ="choose your favourate programming language...",justify=tk.LEFT,padx=20).pack()

for val,language in enumerate(language):
	#tk.Radiobutton(root,text=language,padx=20,variable=v,command=ShowChoices,value=val).pack(anchor =tk.W)
	   tk.Radiobutton(root, 
                  text=language,
                  indicatoron = 0,
                  width = 20,
                  padx = 20, 
                  variable=v, 
                  command=ShowChoices,
                  value=val).pack(anchor=tk.W)
	
	
root.mainloop()
