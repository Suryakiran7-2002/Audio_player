import tkinter as tk
r = tk.Tk()
r.title('tk')
l1=tk.Label(r,text="Regno")
l1.grid(row=0)
t=tk.Entry(r)
t.grid(row=0,column=1)
l1=tk.Label(r,text="Name:")
l1.grid(row=1)
t=tk.Entry(r)
t.grid(row=1,column=1)
l1=tk.Label(r,text="Dept")
l1.grid(row=2)
t=tk.Entry(r)
t.grid(row=2,column=1)
l1=tk.Label(r,text="Gender")
l1.grid(row=3)
radio_var = tk.IntVar()
r1=tk.Radiobutton(r,text="Male",variable = radio_var,value = 1)
r1.grid(row=3,column=1)
r2=tk.Radiobutton(r,text="Female",variable = radio_var,value = 2)
r2.grid(row=3,column=2)
l1=tk.Label(r,text="Age")
l1.grid(row=5)
t=tk.Entry(r)
t.grid(row=5,column=1)
b1=tk.Button(r,text="Insert")
b1.grid(row=6,column=0)
b2=tk.Button(r,text="Update")
b2.grid(row=6,column=1)
b3=tk.Button(r,text="Delete")
b3.grid(row=7,column=0)
b4=tk.Button(r,text="Select")
b4.grid(row=7,column=1)

ch1v = tk.IntVar()
ch2v = tk.IntVar()
ch1 = tk.Checkbutton(r,text = '7:15pm',variable = ch1v,onvalue = 1, offvalue = 0)
ch1.grid(row = 4, column = 1)
ch2 = tk.Checkbutton(r,text = '9am',variable = ch2v,onvalue = 1, offvalue = 0)
ch2.grid(row = 4, column = 2)

l_time = tk.Label(r,text = 'Time of show').grid(row = 4,column = 0)
r.mainloop()