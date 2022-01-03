from tkinter import *


class front:
    def onclick(self):
        print("clicked meee")
    def go(self):
        root=Tk()
        root.geometry("600x600")
        lable=Label(root,text="hello buy")
        lable.grid(row=0,column=0,padx=100,pady=100)
        butto=Button(root, text="do it", command=self.onclick, bg="green")
        butto.grid(row=4,column=3,pady=21)
        root.mainloop()
