from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
def insert(string, root, list):
  Label(root, text=string, bg='#300900', fg='#9a1d00').place(relx=0.075, rely=0.05)
  for item in list:
    item.destroy()
  Button(root, text="Continue", bg='#300900', fg='#9a1d00', command= lambda: root.destroy()).place(relx=0.0675, rely=0.1)
def Questionaire(root):
  subroot = Toplevel(root)
  subroot.configure(bg='#300900')
  subroot.config(width=200, height=200, cursor='star')
  subroot.title("Question")
  subroot.maxsize(2000,2000)
  subroot.minsize(200,200)
  subroot.geometry("500x500")
  ico = Image.open('test.jpg')
  photo = ImageTk.PhotoImage(ico)
  subroot.wm_iconphoto(False, photo)
  b1 = Button(subroot, text="Answer 1", command=lambda: insert("Incorrect", subroot, List))
  b1.place(relx=0, rely=0)
  b2 = Button(subroot, text="Answer 2", command=lambda: insert("Incorrect", subroot, List))
  b2.place(relx=0.15, rely=0.1)
  b3 = Button(subroot, text="Answer 3", command=lambda: insert("Correct", subroot, List))
  b3.place(relx=0, rely=0.1)
  b4 = Button(subroot, text="Answer 4", command=lambda: insert("Incorrect", subroot, List))
  b4.place(relx=0.15, rely=0)
  List = [b1,b2,b3,b4]
def main(root, image1, image2, text1, text2):
    root.destroy()
    root = Tk()
    root.state('zoomed')
    root.configure(bg='#300900')
    root.title("Layer 1")
    ico = Image.open('test.jpg')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)

    # Main Frame + Canvas + Scrollbar
    frame = Frame(root, bg='#300900')
    frame.pack(fill=BOTH, expand=True)

    canvas = Canvas(frame, bg="#300900", bd=0, highlightthickness=0)
    scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.pack(fill=BOTH, expand=True)

    # Content Frame inside Canvas
    content = Frame(canvas, bg="#300900")
    canvas.create_window((0, 0), window=content, anchor=NW)

    def update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    content.bind("<Configure>", update_scrollregion)

    # Content starts here
    Label(content, text="Just remember... you did this to yourself", 
          bg='#300900', fg='#9a1d00', font=('Public Sans', 20)).pack(pady=10)

    # Load images
    image = Image.open(image1)
    image = image.resize((image.width // 2, image.height // 2))
    img_tk = ImageTk.PhotoImage(image)
    image = Image.open(image2)
    image = image.resize((image.width // 2, image.height // 2))
    img_tk_2 = ImageTk.PhotoImage(image)
    Button(content, image=img_tk, padx=1, pady=1, command=lambda: Questionaire(root)).pack(pady=10)
    Message(content, bg='#300900', fg='#9a1d00', width=800, text=text1).pack(pady=10)
    Button(content, image=img_tk_2, padx=1, pady=1, command=lambda: Questionaire(root)).pack(pady=10)
    Message(content, bg='#300900', fg='#9a1d00', width=800, text=text2).pack(pady=10)
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
Button(canvas, text="Join the souls of the damned", bg='#300900', fg='#9a1d00' ,font=('Symbol', 15), command=lambda: main(root, "placeholder.png", "placeholder.png", "lorem ipsum", "lorem ipsum")).pack()
Label(canvas, text="LEAVE", bg='#300900', fg='#400900', font=('wingdings', 10)).pack()
if __name__ == "__main__":
  root.mainloop()