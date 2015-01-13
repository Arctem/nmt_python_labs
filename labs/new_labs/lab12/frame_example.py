import tkinter

#remove one frame, add another
def add_remove(to_remove, to_add):
  to_remove.grid_remove()
  to_add.grid(row=0, column=0)


def main():
  window = tkinter.Tk()

  #Create frames.
  left_frame = tkinter.Frame(window)
  mid_frame = tkinter.Frame(window)
  right_frame = tkinter.Frame(window)

  #Create button for left-most frame.
  tmp_button = tkinter.Button(left_frame, text='Go right.',
    command=lambda: add_remove(left_frame, mid_frame))
  tmp_button.grid(row=0, column=0)

  #Create buttons for middle frame.
  tmp_button = tkinter.Button(mid_frame, text='Go left.',
    command=lambda: add_remove(mid_frame, left_frame))
  tmp_button.grid(row=0, column=0)
  tmp_button = tkinter.Button(mid_frame, text='Go right.',
    command=lambda: add_remove(mid_frame, right_frame))
  tmp_button.grid(row=0, column=1)

  #Create button for right-most frame.
  tmp_button = tkinter.Button(right_frame, text='Go left.',
    command=lambda: add_remove(right_frame, mid_frame))
  tmp_button.grid(row=0, column=0)

  left_frame.grid(row=0, column=0)

  window.mainloop()

if __name__ == '__main__':
  main()