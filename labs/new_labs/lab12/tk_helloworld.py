import tkinter

window = tkinter.Tk()
window.title("Title!") # Notice dat title!
window.config(background = "white")

left_frame = tkinter.Frame(window, width = 200, height = 400)
left_frame.grid(row = 0, column = 0, padx = 10, pady = 3)

right_frame = tkinter.Frame(window, width = 200, height = 400)
right_frame.grid(row = 0, column = 1, padx = 10, pady = 3)

helloworld = tkinter.Text(left_frame, width = 30, height = 10)
helloworld.insert(tkinter.END, "Hello World on the left")
helloworld.grid(row = 0, column = 0)

helloworldr = tkinter.Text(right_frame, width = 30, height = 10)
helloworldr.insert(tkinter.END, "Hello World on the right")
helloworldr.grid(row = 0, column = 0)

window.mainloop()
