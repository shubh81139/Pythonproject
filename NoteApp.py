from tkinter import *
from tkinter import filedialog, messagebox
import os

# Function to clear the text area
def new_file():
    global file
    text_area.delete(1.0,END)     # delete function will delete all the things from first line(1.0) to last line(END)

# Function to open a file
def open_file():
  global file  
  file = filedialog.askopenfilename(defaultextension=".txt")
  if file:
    try:
      root.title(os.path.basename(file) + "- Notepad")   # ye step kya kar raha hai ki os module ka use kar k path k base name ko title me likh raha hai
      with open(file, "r") as f:
        text_area.delete(1.0, END)
        text_area.insert(1.0, f.read())
    except FileNotFoundError:
      messagebox.showerror("Error", "File not found!")

# Function to save a file
def save_file():
  global file  
  file = filedialog.asksaveasfilename(defaultextension=".txt")
  if file:
    try:
      with open(file, "w") as f:
        f.write(text_area.get(1.0, END))
        root.title(os.path.basename(file) + "- Notepad")
    except (IOError, PermissionError) as e:
      messagebox.showerror("Error", f"Error saving file: {e}")
      
       
# Function to (placeholder) handle cut
def cut():
    text_area.event_generate(("<<Cut>>"))    # event_generate() is a inbuilt finction of tkinter that handel these type of function.
 
# Function to (placeholder) handle copy
def copy():
  text_area.event_generate(("<<Copy>>"))

# Function to (placeholder) handle paste
def paste():
  text_area.event_generate(("<<Paste>>"))

# Function to show license information
def show_license():
  messagebox.showinfo("License", "This notepad is provided without a specific license.")

# Create the main window
root = Tk()
root.geometry("500x450")
root.title("Notepad")
root.configure(background="red")

# Create a text widget for editing content
text_area = Text(root, wrap=WORD)
text_area.pack(fill=BOTH, expand=True)

# Create menu bar elements
menu_bar = Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu (placeholders)
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

menu_bar.add_cascade(label="Edit", menu=edit_menu)

# About menu
about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label="View License", command=show_license)

menu_bar.add_cascade(label="About", menu=about_menu)


# Adding the Scroll Bar : variable name followed by = Scrollbar(place where we want to add scroll)
scroll =Scrollbar(text_area)
scroll.pack(side=RIGHT,fill =Y)
scroll.config(command=text_area.yview)
text_area.config(yscrollcommand=scroll.set)

# Run the main application loop
root.mainloop()













# from tkinter import *

# root =Tk()
# root.geometry("455x233")
# root.title("Note App")
# # root.wm_iconbitmap("D:\Python\note appp.ico")  # This step id used to add icon and it should be ico file.

# root.configure(background="beige")               # This is used to set the background color. 



# Button(text="Close",command=root.destroy).pack(anchor=E)       # root.destroy help to close the GUI.

# root.mainloop()