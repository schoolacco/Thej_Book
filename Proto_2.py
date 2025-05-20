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
def layer(images, texts, command, bg, fg, intro_text, orders, answers):
    global root
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
    Message(content, text=intro_text, width=800, bg=bg, fg=fg, font=('Public Sans', 20)).pack(pady=10)
    image_ref = []
    for i in range(len(images)):
    # Load images
      image = Image.open(images[i])
      image = image.resize((image.width // 2, image.height // 2))
      img_tk = ImageTk.PhotoImage(image)
      image_ref.append(img_tk)
      Button(content, image=img_tk, padx=1, pady=1, command=lambda: Questionaire(root, orders[i], answers[i], bg)).pack(pady=10)
      Message(content, bg=bg, fg=fg, width=800, text=texts[i]).pack(pady=10)
    Button(content, text="Descend deeper", bg=bg, fg=fg, command=command).pack()
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
Button(canvas, text="Join the souls of the damned", bg='#300900', fg='#9a1d00' ,font=('Symbol', 15), command=lambda: layer(["placeholder.png", "placeholder.png"], ["lorem ipsum", "lorem ipsum"], bg="#300900", fg='#9a1d00', intro_text="Just remember... you did this to yourself, Welcome to the threshold of Hell, here you'll find the apathetic.", orders=["Incorrect", "Incorrect", "Correct", "Incorrect"], answers=["Answer1", "Answer2", "Answer3", "Answer4"], 
                                                                                                                           command=lambda: layer(["placeholder.png", "placeholder.png"], ["lorem ipsum", "lorem ipsum"], bg="#251317", fg='#FFFFFF', intro_text="This is Limbo, the first circle of Hell, here you will find pagans and the unbaptized.", orders=["Incorrect","Correct", "Incorrect", "Incorrect"], answers=["Answer1", "Answer2", "Answer3", "Answer4"], 
                                                                                                                            command=lambda: layer(["placeholder.png", "placeholder.png"], ["lorem ipsum", "lorem ipsum"], bg="#1B1D2A", fg='#FFFFFF', intro_text="This is the 2nd circle of Hell, here the lustful are punished", orders=["Incorrect","Correct", "Incorrect", "Incorrect"], answers=["Answer1", "Answer2", "Answer3", "Answer4"],
                                                                                                                             command=lambda: layer(["placeholder.png", "placeholder.png"], ["lorem ipsum", "lorem ipsum"], bg="#745E3F", fg='#FFFFFF', intro_text="This is 3rd circle of Hell, here the gluttonous are punished", orders=["Incorrect","Correct", "Incorrect", "Incorrect"], answers=["Answer1", "Answer2", "Answer3", "Answer4"], 
                                                                                                                              command=lambda: layer(["placeholder.png", "placeholder.png"], ["lorem ipsum", "lorem ipsum"], bg="#98754B", fg='#FFFFFF', intro_text="This is 4th circle of Hell, here the avarcious and the spendthrifts are punished", orders=["Incorrect","Correct", "Incorrect", "Incorrect"], answers=["Answer1", "Answer2", "Answer3", "Answer4"], 
                                                                                                                               command=lambda: layer(["placeholder.png", "placeholder.png"], ["lorem ipsum", "lorem ipsum"], bg="#4D4742", fg='#FFFFFF', intro_text="This is 5th circle of Hell, here the wrathful and the melancholic are punished", orders=["Incorrect","Correct", "Incorrect", "Incorrect"], answers=["Answer1", "Answer2", "Answer3", "Answer4"], 
                                                                                                                                command=lambda: layer(["placeholder.png", "placeholder.png"], ["lorem ipsum", "lorem ipsum"], bg="#494949", fg='#FFFFFF', intro_text="This is 6th circle of Hell, here lies the heretics", orders=["Incorrect","Correct", "Incorrect", "Incorrect"], answers=["Answer1", "Answer2", "Answer3", "Answer4"], 
                                                                                                                                 command=lambda: layer(["placeholder.png", "placeholder.png"], ["lorem ipsum", "lorem ipsum"], bg="#2B0A05", fg='#FFFFFF', intro_text="Welcome, you have come far travellar, this is the 1st ring of Hell of the 7th circle, the layer of Malice, containing the punishments of those whose who have commited sins of violence and inhumanity. The first ring contains those who bring violence upon others or their property.", orders=["Incorrect","Correct", "Incorrect", "Incorrect"], answers=["Answer1", "Answer2", "Answer3", "Answer4"], 
                                                                                                                                  command=lambda: layer(["placeholder.png", "placeholder.png"], ["lorem ipsum", "lorem ipsum"], bg="#707070", fg='#FFFFFF', intro_text="This is the 2nd ring of the 7th circle, here lies those who have commited violence against themself or their property. You cannot take the easy way to Paradise.", orders=["Incorrect","Correct", "Incorrect", "Incorrect"], answers=["Answer1", "Answer2", "Answer3", "Answer4"], 
                                                                                                                                   command=lambda: layer(["placeholder.png", "placeholder.png"], ["lorem ipsum", "lorem ipsum"], bg="#938676", fg='#FFFFFF', intro_text="The 3rd and last ring of the 7th circle of Hell, here you find those who dared to hurt God and Nature, they deserved no lesser of a fate.", orders=["Incorrect","Correct", "Incorrect", "Incorrect"], answers=["Answer1", "Answer2", "Answer3", "Answer4"], 
                                                                                                                                    command=lambda: layer(["placeholder.png", "placeholder.png"], ["lorem ipsum", "lorem ipsum"], bg="#826A3C", fg='#FFFFFF', intro_text="You have ventured very far traveller, to the 8th circle of Hell, here you shall find those who have commited sins of deceit against those who have no cause of trust. The pimps and seducers, the flatterers, the simonists, the soothsayers, the corrupt officials, the hypocrites, the theieves, the intellectually dishonest, the rabble-rousers and the counterfeiters, all in their own smaller boliga (all in one place cause I'm lazy).", orders=["Incorrect","Correct", "Incorrect", "Incorrect"], answers=["Answer1", "Answer2", "Answer3", "Answer4"], 
                                                                                                                                     command=lambda: layer(["placeholder.png", "placeholder.png"], ["lorem ipsum", "lorem ipsum"], bg="#3C4FB2", fg='#FFFFFF', intro_text="Your journey approaches its end traveller, this is the 9th and final circle of Hell, containing all of those who have commited sins of deceit against those who have cause to trust, those who have dared to decieve their family, their nation, benefactors and have dared to defy xenia, you approach the centre, if you truly wish to see those who have commited the most foul sins.", orders=["Incorrect","Correct", "Incorrect", "Incorrect"], answers=["Answer1", "Answer2", "Answer3", "Answer4"], 
                                                                                                                                      command=lambda: layer(["placeholder.png", "placeholder.png"], ["lorem ipsum", "lorem ipsum"], bg="#300900", fg='#9a1d00', intro_text="...", orders=["Incorrect","Correct", "Incorrect", "Incorrect"], answers=["Answer1", "Answer2", "Answer3", "Answer4"], command=lambda: root.destroy() )))))))))))))).pack()
Label(canvas, text="LEAVE", bg='#300900', fg='#400900', font=('wingdings', 10)).pack()
if __name__ == "__main__":
  root.mainloop()