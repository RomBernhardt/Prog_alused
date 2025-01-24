import tkinter as tk

def rakvere_lipp():

    aken = tk.Tk()
    aken.title("Lipp")
    aken.configure(bg="white")
    
    canvas = tk.Canvas(aken, width=400, height=200, bg="yellow")
    canvas.pack()

    canvas.create_rectangle(0, 0, 400, 80, fill="blue", outline="blue")
    canvas.create_rectangle(0, 200, 400, 120, fill="blue", outline="blue")
    canvas.create_rectangle(0, 100, 400, 100, fill="yellow", outline="yellow")
    
    aken.mainloop()

rakvere_lipp()
