import requests
import os
import time
from tkinter import *
root = Tk()
root.title("IsEven v9.1.2")
root.minsize(200,200)
root.maxsize(1000,1000)
root.geometry("400x400+20+120")
root.configure(bg="black")
Label(root, text="Enter a number (between 0-999,999):")
even = StringVar()
Entry(root, even)
# API Base URL
API_URL = "https://api.isevenapi.xyz/api/iseven/"
def is_even(num):
    if int(num) > 999999 or int(num) < 0:
       raise SyntaxError
    response = requests.get(API_URL + num)
    if response.status_code == 200:
        result = response.json()
    else:
       raise KeyError
    return result
while True:
  try:
    even = is_even(input("Enter a number (between 0-999,999): "))
    if even["iseven"]:
       print("The number is even.")
    else:
       print("Your number is odd.")
    print(even["ad"]+"\nDeveloper's note: Sorry we can't remove the ads :(")
  except KeyError:
     print("Enter a NUMBER!")
  except SyntaxError:
     print("Enter a number within the range.")
  time.sleep(5)
  os.system('cls')
