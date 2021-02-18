from tkinter import * 
window = Tk ()

window.geometry("600x600")
window.config(background='blue')
Background = 'blue'
frame = Frame(window, bg = Background)
boutton = Button(frame, text = "Restart", font = ("Helvetica", 60), bg = "white", fg = Background)
boutton.grid(row = 2, column=0)
canvas.create_rectangle(100, 50, 400, 200, fill='green')



window.mainloop()