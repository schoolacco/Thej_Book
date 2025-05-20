from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
def insert(string, root, list):
  Label(root, text=string, bg='#300900', fg='#9a1d00').place(relx=0.075, rely=0.05)
  for item in list:
    item.destroy()
  Button(root, text="Continue", bg='#300900', fg='#9a1d00', command= lambda: root.destroy()).place(relx=0.0675, rely=0.1)
def Questionaire(root, order, answers, bg):
  subroot = Toplevel(root)
  subroot.configure(bg=bg)
  subroot.config(width=200, height=200, cursor='star')
  subroot.title("Question")
  subroot.maxsize(2000,2000)
  subroot.minsize(200,200)
  subroot.geometry("500x500")
  ico = Image.open('test.jpg')
  photo = ImageTk.PhotoImage(ico)
  subroot.wm_iconphoto(False, photo)
  b1 = Button(subroot, text=answers[0], command=lambda: insert(order[0], subroot, List))
  b1.place(relx=0, rely=0)
  b2 = Button(subroot, text=answers[1], command=lambda: insert(order[1], subroot, List))
  b2.place(relx=0.15, rely=0.1)
  b3 = Button(subroot, text=answers[2], command=lambda: insert(order[2], subroot, List))
  b3.place(relx=0, rely=0.1)
  b4 = Button(subroot, text=answers[3], command=lambda: insert(order[3], subroot, List))
  b4.place(relx=0.15, rely=0)
  List = [b1,b2,b3,b4]
def layer(root, images, texts, command, bg, fg, intro_text, orders, answers):
    root.destroy()
    root = Tk()
    root.state('zoomed')
    root.configure(bg=bg)
    root.title("Layer 1")
    ico = Image.open('test.jpg')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)

    # Main Frame + Canvas + Scrollbar
    frame = Frame(root, bg=bg)
    frame.pack(fill=BOTH, expand=True)

    canvas = Canvas(frame, bg=bg, bd=0, highlightthickness=0)
    scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.pack(fill=BOTH, expand=True)

    # Content Frame inside Canvas
    content = Frame(canvas, bg=bg)
    canvas.create_window((0, 0), window=content, anchor=NW)

    def update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    content.bind("<Configure>", update_scrollregion)

    # Content starts here
    Label(content, text=intro_text, 
          bg=bg, fg=fg, font=('Public Sans', 20)).pack(pady=10)
    for i in range(len(images)):
    # Load images
      image = Image.open(images[i-1])
      image = image.resize((image.width // 2, image.height // 2))
      img_tk = ImageTk.PhotoImage(image)
      Button(content, image=img_tk, padx=1, pady=1, command=lambda: Questionaire(root, orders[i-1], answers[i-1], bg)).pack(pady=10)
      Message(content, bg=bg, fg=fg, width=800, text=texts[i-1]).pack(pady=10)
      Button(content, text="Descend deeper", bg=bg, fg=fg, command=command)
    root.mainloop()

root = Tk()
root.state('zoomed')
root.configure(bg='#300900')
root.title("Heck*")
root.maxsize(2000,2000)
root.minsize(500,500)
root.geometry("500x500")
ico = Image.open('test.jpg')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
canvas = Canvas(root, bg="#300900", width=500, height=500, bd=0, cursor="circle")
canvas.pack(fill=BOTH, expand=True)
Label(canvas, text="Welcome to the world of Dante's Inferno" ,bg='#300900', fg='#9a1d00', font=('Terminal', 50)).pack()
Label(canvas, text="\n \n \n \n \n \n \n \n",bg='#300900', fg='#9a1d00').pack()
Button(canvas, text="Join the souls of the damned", bg='#300900', fg='#9a1d00' ,font=('Symbol', 15), command=lambda: layer(root, ["placeholder.png", "placeholder.png"], ["lorem ipsum", "lorem ipsum"], bg="#300900", fg='#9a1d00', intro_text="Just remember... you did this to yourself", 
                                                                                                                           command=layer(root, ["placeholder.png", "placeholder.png"], ["lorem ipsum", "lorem ipsum"], bg="#300900", fg='#9a1d00', intro_text="Just remember... you did this to yourself", 
                                                                                                                                         command=None))).pack()
Label(canvas, text="LEAVE", bg='#300900', fg='#400900', font=('wingdings', 10)).pack()
if __name__ == "__main__":
  root.mainloop()