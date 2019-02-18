import tkinter as tk
"""
def fun():
	print('tkinter is very easy  to understandz')
	#root.quit()
	for i in range(100):
		main()
"""	

def main():	
	root = tk.Tk()
	root['bg'] = 'orange'
	root.geometry('500x500')

	frame = tk.Frame(root)
	frame.pack()

	button= tk.Button(frame,text="another window",command=print('hello'),fg='black',width=20,height=10)
	button.pack(side=tk.LEFT)
	root.mainloop()

for i in range(100):
	main()
