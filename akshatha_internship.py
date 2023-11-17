from tkinter import *
from tkinter.simpledialog import askstring,askinteger
def frame_sentence():
    name = name_tf.get()
    age = age_tf.get()
    import cv2
    import os
    import string
    img = cv2.imread("pexels-photo-1631677.png") # Replace with the correct image path
    d = {}
    for i in range(255):
        d[chr(i)] = i
    m = 0
    n = 0
    z = 0
    for i in range(len(name)):
        img[n, m, z] = d[name[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    cv2.imwrite("encryptedImage.jpg", img)
    os.system("start encryptedImage.jpg") # Use 'start' to open the image on Windows
    disp_tf.insert(0,f'encryptedImage.jpg')
def framg():
    age= age_tf.get()
    name= name_tf.get()
    pas=descipline_tf .get()
    import cv2
    img = cv2.imread("pexels-photo-1631677.png")
    m = 0
    n = 0
    z = 0
    d = {}
    c = {}
    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    for i in range(len(name)):
        img[n, m, z] = d[name[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    n = 0
    m = 0
    z = 0
    message = ""
    if age == pas:
        for i in range(len(name)):
            message = message + c[img[n,m,z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        fig_tf.insert(0,"Decryption message is: ")
        fig_tf.insert(28,message)
    else:
        fig_tf.insert(0,f'YOU ARE NOT auth')
    

ws = Tk()
ws.title('stegonagraph')
ws.geometry('400x300')
ws.config(bg='#6B007B')


name_tf = Entry(ws, bg='#A66999',fg='#FFBBED')
age_tf = Entry(ws,bg='#A66999',fg='#FFBBED')
descipline_tf = Entry(ws,bg='#A66999',fg='#FFBBED')

name_lbl = Label(
    ws,
    text='enter the message',
    bg='#FFBBED',
    fg='#330033'
)
age_lbl = Label(
    ws,
    text='enter the password',
    bg='#FFBBED',
    fg='#330033'
)

decrypt_lbl = Label(
    ws,
    text='enter passcode for Decryption',
    bg='#FFBBED',
    fg='#330033'
)

name_lbl.pack()
name_tf.pack()
age_lbl.pack()
age_tf.pack()

    
btn = Button(
    ws,
    text='encrypt',
    relief=SOLID,
    bg='#5B2071',
    fg='#FFBBED',
    command=frame_sentence
)
btn.pack(pady=10)

disp_tf = Entry(
    ws, 
    width=15,
    font=('Arial', 12)
    )

disp_tf.pack(pady=5)

decrypt_lbl.pack()
descipline_tf.pack()

btn = Button(
    ws,
    text='decrypt',
    relief=SOLID,
    bg='#5B2071',
    fg='#FFBBED',
    command=framg
)
btn.pack(pady=10)
fig_tf = Entry(
    ws, 
    width=30,
    font=('Arial', 10)
    )
fig_tf.pack(pady=5)
ws.mainloop()
