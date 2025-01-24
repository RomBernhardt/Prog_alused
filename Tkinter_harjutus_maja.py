import tkinter as tk

def maja():
    aken = tk.Tk()
    aken.title("Maja")

    
    canvas = tk.Canvas(aken, width=400, height=400, bg="white")
    canvas.pack()

    canvas.create_rectangle(100, 150, 300, 350, fill="lightgray", outline="black")

    canvas.create_polygon(100, 150, 300, 150, 200, 50, fill="black", outline="black")

    canvas.create_rectangle(180, 250, 220, 350, fill="saddlebrown", outline="black")

    canvas.create_rectangle(120, 180, 160, 220, fill="lightblue", outline="black")

    canvas.create_rectangle(240, 180, 280, 220, fill="lightblue", outline="black")

    canvas.create_rectangle(240, 50, 260, 130, fill="gray", outline="black")

    aken.mainloop()

maja()
