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
def main(root):
  root.destroy()
  root = Tk()
  s = ttk.Style()
  s.configure('TFrame', background="#300900")
  frame = Frame(root)
  frame.pack(fill=BOTH, expand=TRUE)
  root.state('zoomed')
  root.configure(bg='#300900')
  root.config(width=500, height=500)
  root.title("Layer 1")
  root.maxsize(2000,2000)
  root.minsize(500,500)
  root.geometry("500x500")
  ico = Image.open('test.jpg')
  photo = ImageTk.PhotoImage(ico)
  root.wm_iconphoto(False, photo)
    # Create a canvas object and a vertical scrollbar for scrolling it.
  vscrollbar = ttk.Scrollbar(frame, orient=VERTICAL)
  vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
  scroll_canvas = Canvas(frame, bd=0, highlightthickness=0,
                     yscrollcommand=vscrollbar.set)
  scroll_canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
  vscrollbar.config(command=scroll_canvas.yview)
  # Reset the view
  scroll_canvas.xview_moveto(0)
  scroll_canvas.yview_moveto(0)
  content = ttk.Frame(scroll_canvas, width=4000, height=4000, style='TFrame')
  Label(content, text="Just remember... you did this to yourself - ", bg='#300900', fg='#9a1d00', font=('Public Sans',20)).place(relx=0.32, rely=0.03)
  text = Label(content, text="Dante", bg='#300900', fg='#9a1d00', font=('Edwardian Script ITC',20))
  text.place(relx=0.6, rely=0.035)
  image = Image.open('placeholder.png')
  new_size = (image.width // 2, image.height // 2)  # Example: Shrink by half
  image = image.resize(new_size)
  image = ImageTk.PhotoImage(image)
  # Create a frame inside the canvas which will be scrolled with it.
  #content.interior = interior = ttk.Frame(canvas, width=4000, height=4000)
  Button(content, image=image, padx=0.1, pady=0.1, command=lambda: Questionaire(root)).place(relx=0.1, rely=0.1)
  Message(content, bg='#300900', fg='#9a1d00', text='''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec urna lacinia, dignissim sapien eget, interdum nisi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce non euismod odio, sed vehicula velit. Mauris vitae nulla auctor, euismod nibh vel, ullamcorper ipsum. Fusce aliquet ipsum at est consectetur porta. Curabitur erat mauris, tempor vel pretium nec, molestie sit amet nibh. Aliquam scelerisque gravida diam id porttitor. Vestibulum sit amet sodales purus, sed tincidunt massa. Vestibulum imperdiet dapibus tellus et accumsan. Pellentesque congue nulla a dolor blandit congue sit amet nec sapien. Ut molestie nulla eget nibh fermentum volutpat. Cras libero elit, dapibus non felis vel, molestie porttitor arcu. Morbi pretium diam mauris, in lobortis nulla aliquam blandit. Donec tempor hendrerit libero ullamcorper sodales.
In non lorem porttitor, euismod nulla quis, ultrices sem. Nunc volutpat elit quis urna porttitor gravida. Morbi auctor vestibulum ultricies. Etiam in quam tincidunt, hendrerit enim in, pretium nunc. Nulla imperdiet ex vel porta consectetur. Vestibulum aliquam libero ac nisl facilisis malesuada. Etiam a facilisis ligula.
Donec vitae pellentesque felis. Integer pharetra enim quis purus viverra, congue accumsan nisl molestie. Curabitur sed lacus nibh. Ut egestas urna et dui volutpat, in molestie massa congue. Nam at sem ante. Suspendisse potenti. Praesent congue, felis sit amet cursus viverra, elit tellus facilisis elit, sed hendrerit leo nibh vel neque. Fusce eu turpis ut neque porta ullamcorper sit amet eu tellus. Vivamus lorem odio, ultrices ut ante at, posuere placerat diam. Cras pulvinar lorem non odio mollis, id accumsan lacus ornare. In laoreet aliquet tortor nec bibendum. In vel ligula nibh. Vestibulum semper lorem sed magna mattis, volutpat accumsan nunc cursus. Suspendisse semper pharetra semper. Nulla gravida faucibus nisl, eu laoreet odio porta id.
Sed consequat, velit ut finibus tincidunt, magna lorem congue nulla, vel elementum ex augue vel mauris. Vestibulum ornare mi enim. In volutpat odio lacus, vel iaculis tortor tincidunt nec. Sed hendrerit fermentum purus non tristique. Sed feugiat scelerisque finibus. Fusce porta tristique mattis. Phasellus ullamcorper nisi at vehicula auctor. Cras maximus ultrices purus, et mollis enim finibus id. Aenean gravida, orci ut ultrices dictum, purus diam elementum dolor, id hendrerit lorem felis vel dolor. Sed aliquam tellus urna, et lacinia dui pretium luctus. Nulla pharetra est nunc, vitae consequat orci faucibus sit amet. Vivamus in orci et ligula molestie ornare vel vel enim. Aliquam nisl lectus, condimentum id ultrices eget, ullamcorper a ante.
Nam congue fermentum elit ut interdum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nullam ac eros suscipit, interdum enim nec, facilisis massa. Proin iaculis magna sed nisi fermentum rhoncus. Quisque pulvinar sem quam, ut sollicitudin dolor hendrerit non. Donec non pellentesque ante. Morbi vel feugiat massa. Quisque vestibulum tortor ut risus malesuada, non posuere dui posuere. Nunc molestie sed ipsum at dignissim. Donec vel lobortis arcu. Integer eget tellus in quam dictum volutpat. Donec ullamcorper, turpis luctus aliquam sodales, felis nunc rhoncus turpis, sit amet accumsan tellus magna rhoncus purus. Quisque sit amet convallis lectus, ut sodales erat. Nullam commodo urna lectus, nec dictum libero dictum non. Aliquam erat volutpat.''').place(relx=0.37, rely=0.125)
  Button(content, image=image, padx=0.1, pady=0.1, command=lambda: Questionaire(root)).place(relx=0.45, rely=0.6)
  Message(content, bg='#300900', fg='#9a1d00', text='''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec urna lacinia, dignissim sapien eget, interdum nisi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce non euismod odio, sed vehicula velit. Mauris vitae nulla auctor, euismod nibh vel, ullamcorper ipsum. Fusce aliquet ipsum at est consectetur porta. Curabitur erat mauris, tempor vel pretium nec, molestie sit amet nibh. Aliquam scelerisque gravida diam id porttitor. Vestibulum sit amet sodales purus, sed tincidunt massa. Vestibulum imperdiet dapibus tellus et accumsan. Pellentesque congue nulla a dolor blandit congue sit amet nec sapien. Ut molestie nulla eget nibh fermentum volutpat. Cras libero elit, dapibus non felis vel, molestie porttitor arcu. Morbi pretium diam mauris, in lobortis nulla aliquam blandit. Donec tempor hendrerit libero ullamcorper sodales.
In non lorem porttitor, euismod nulla quis, ultrices sem. Nunc volutpat elit quis urna porttitor gravida. Morbi auctor vestibulum ultricies. Etiam in quam tincidunt, hendrerit enim in, pretium nunc. Nulla imperdiet ex vel porta consectetur. Vestibulum aliquam libero ac nisl facilisis malesuada. Etiam a facilisis ligula.
Donec vitae pellentesque felis. Integer pharetra enim quis purus viverra, congue accumsan nisl molestie. Curabitur sed lacus nibh. Ut egestas urna et dui volutpat, in molestie massa congue. Nam at sem ante. Suspendisse potenti. Praesent congue, felis sit amet cursus viverra, elit tellus facilisis elit, sed hendrerit leo nibh vel neque. Fusce eu turpis ut neque porta ullamcorper sit amet eu tellus. Vivamus lorem odio, ultrices ut ante at, posuere placerat diam. Cras pulvinar lorem non odio mollis, id accumsan lacus ornare. In laoreet aliquet tortor nec bibendum. In vel ligula nibh. Vestibulum semper lorem sed magna mattis, volutpat accumsan nunc cursus. Suspendisse semper pharetra semper. Nulla gravida faucibus nisl, eu laoreet odio porta id.
Sed consequat, velit ut finibus tincidunt, magna lorem congue nulla, vel elementum ex augue vel mauris. Vestibulum ornare mi enim. In volutpat odio lacus, vel iaculis tortor tincidunt nec. Sed hendrerit fermentum purus non tristique. Sed feugiat scelerisque finibus. Fusce porta tristique mattis. Phasellus ullamcorper nisi at vehicula auctor. Cras maximus ultrices purus, et mollis enim finibus id. Aenean gravida, orci ut ultrices dictum, purus diam elementum dolor, id hendrerit lorem felis vel dolor. Sed aliquam tellus urna, et lacinia dui pretium luctus. Nulla pharetra est nunc, vitae consequat orci faucibus sit amet. Vivamus in orci et ligula molestie ornare vel vel enim. Aliquam nisl lectus, condimentum id ultrices eget, ullamcorper a ante.
Nam congue fermentum elit ut interdum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nullam ac eros suscipit, interdum enim nec, facilisis massa. Proin iaculis magna sed nisi fermentum rhoncus. Quisque pulvinar sem quam, ut sollicitudin dolor hendrerit non. Donec non pellentesque ante. Morbi vel feugiat massa. Quisque vestibulum tortor ut risus malesuada, non posuere dui posuere. Nunc molestie sed ipsum at dignissim. Donec vel lobortis arcu. Integer eget tellus in quam dictum volutpat. Donec ullamcorper, turpis luctus aliquam sodales, felis nunc rhoncus turpis, sit amet accumsan tellus magna rhoncus purus. Quisque sit amet convallis lectus, ut sodales erat. Nullam commodo urna lectus, nec dictum libero dictum non. Aliquam erat volutpat.''').place(relx=0.1, rely=0.6)
  scroll_canvas.create_window(0, 0, window=content, anchor=NW)
  scroll_canvas.bind("<Configure>", lambda e: scroll_canvas.configure(scrollregion=scroll_canvas.bbox("all")))
  content.pack()
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
Button(canvas, text="Join the souls of the damned", bg='#300900', fg='#9a1d00' ,font=('Symbol', 15), command=lambda: main(root)).pack()
Label(canvas, text="LEAVE", bg='#300900', fg='#400900', font=('wingdings', 10)).pack()
if __name__ == "__main__":
  root.mainloop()