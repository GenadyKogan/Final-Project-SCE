  
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To Code at Codemy.com')
#root.iconbitmap('E:/Python/FinalProject/Final-Project-SCE/Test/website.jpg')


my_img = ImageTk.PhotoImage(Image.open("E:/Python/FinalProject/Final-Project-SCE/Test/website.jpg"))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()