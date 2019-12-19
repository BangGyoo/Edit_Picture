import cv2
import tkinter
from PIL import Image, ImageTk
'''
win = tkinter.Tk()
win.geometry('800x800')
tkinter.canvas = tkinter.Canvas(win,width=799,height=799)
tkinter.canvas.pack()
pil_image = Image.open('./Image/mario.png')

pil_image = pil_image.resize((400, 400))
rgb_image = pil_image.convert('RGB').load()
for i in range(20) :
    for j in range(20) :
        rgb_image[200+i,200+j] = (255,255,255)

rgb_image = pil_image.convert('RGB')

#ttttt = ImageTk.PhotoImage(rgb_image)
ttttt = ImageTk.BitmapImage(rgb_image)
magesprite = tkinter.canvas.create_image(400,400,image=image)
win.mainloop()
'''
def convert_to_tkimage():
        global src

        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

        img = Image.fromarray(binary)
        imgtk = ImageTk.PhotoImage(image=img)

        label.config(image=imgtk)
        label.image = imgtk
window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("500x700+100+100")

src = cv2.imread("./Image/heart.png")
src = cv2.resize(src, (400, 400))

img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

img = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image=img)

label = tkinter.Label(window, image=imgtk)
label.pack(side="top")

button = tkinter.Button(window, text="test", command=convert_to_tkimage)
button.pack(side="bottom", expand=True, fill='both')

window.mainloop()
