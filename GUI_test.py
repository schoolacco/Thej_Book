from tkinter import *
root = Tk()
root.title('test')
root.configure(bg='light grey')
root.maxsize(1000,1000)
root.minsize(100,100)
root.geometry("300x300+120+50")
Label(root, text="Cool example text here.", bg="dark grey").pack()
n = 1
subroot = None
var = StringVar()
GUIs = [root]
def Example_Command():
  global n
  print([(i*i) for i in range(n)])
  n += 1
def destroy(List):
  global n, GUIs
  if n > 1:
    for GUI in List:
      GUI.destroy()
  else:
    subroot = Tk()
    subroot.title(':(')
    subroot.configure(bg='grey')
    subroot.maxsize(1000,1000)
    subroot.geometry("300x300+120+50")
    Label(subroot, text="No", fg='red', bg="grey").pack()
    GUIs.append(subroot)
    subroot.mainloop()
def New_GUI(root):
  global GUIs
  root = Tk()
  root.title('New_GUI :)')
  root.configure(bg='grey')
  root.maxsize(1000,1000)
  root.geometry("300x300+120+50")
  Label(root, text="You made a new GUI!", bg="grey").pack()
  GUIs.append(root)
  root.mainloop()
  Label(root, text="Cool example text here.", bg="dark grey").pack()
Button(root, text="Example Button", bg="aquamarine", command=Example_Command).pack()
Button(root, text="Open another GUI", bg="light blue", command=lambda: New_GUI(subroot)).pack()
Button(root, text="Quit :(", fg='crimson', bg="blue", command=lambda: destroy(GUIs)).pack()
OptionMenu(root, var, *[i*i for i in range(100)]).pack()
root.mainloop()
