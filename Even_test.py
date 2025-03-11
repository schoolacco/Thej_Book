import requests
from tkinter import *
root = Tk()
root.title("IsEven v9.1.2")
root.minsize(200,200)
root.maxsize(1000,1000)
root.geometry("400x400+20+120")
root.configure(bg="black")
Label(root, text="Enter a number (between 0-999,999):", fg="white", bg="black").pack()
even = Entry(root, bg="black", fg="white")
even.pack()
Button(root, text="Find if number is even", bg="black", fg="white", command=lambda:is_even(even.get())).pack()
# API Base URL
API_URL = "https://api.isevenapi.xyz/api/iseven/"
def is_even(num):
   subroot = Tk()
   subroot.title("Result")
   subroot.configure(bg="black")
   subroot.minsize(200,200)
   subroot.maxsize(1000,1000)
   subroot.geometry("600x400+400+120")
   try:
    if int(num) > 999999 or int(num) < 0:
       print("Enter a number within range")
       pass
    response = requests.get(API_URL + num)
    if response.status_code == 200:
        result = response.json()
    if result["iseven"]:
       label = Label(subroot, text="The number is even.", fg="white", bg="black")
    else:
       label = Label(subroot, text="Your number is odd.", fg="white", bg="black")
    label.pack()
    Label(subroot, text=result["ad"]+"\n[Developer's note: Sorry we can't remove the ads D:]", bg="black", fg="white").pack()
   except NameError:
      print("Enter a number.")

root.mainloop()
