from tkinter import *

root = Tk()
root.title("Heondo GUI")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="/Users/parkheondo/Desktop/PyHD/makegui/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")
    
    global photo2 # Garbage Collection(불필요한 메모리 공간 해제)를 막아주기위해 전역변수로 선언.
    photo2 = PhotoImage(file="/Users/parkheondo/Desktop/PyHD/makegui/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()