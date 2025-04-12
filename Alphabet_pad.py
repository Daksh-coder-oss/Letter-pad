from tkinter import *
root=Tk()
root.title("Aplphabet Pad")
root.geometry("300x300")
letters=[["A","B","C","D","E","F"],["G","H","I","J","K"]["L","M","N","O","P","Q"],["R","S","T","U","V","W"],["X","Y","Z"]]
for i in range(6):
    root.columnconfigure(i,weight=1,minsize=75)
    root.rowconfigure(i,weight=1,minsize=50)
    for j in range(5):
        frame=Frame(master=root,relief=SUNKEN,borderwidth=1)
        frame.grid(row=j,column=i)
        label=Label(master=frame,text=letters,bg="orange")
        label.pack(padx=6,pady=6)



