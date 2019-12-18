import tkinter

class Window(tkinter.Tk) :
    def __init__(self,title,width=800,height=600,x_pos=10,y_pos=10) :
        super().__init__()
        self.title(title)
        self.geometry(str(width) +"x"+ str(height)+ "+" + str(x_pos) +"+"+ str(y_pos))
        self.resizable(False,False)
        self.width = width; self.height = height; self.x_pos=x_pos;self.y_pos=y_pos;self.title = title
        self.menu()
    def doNothing(self) :
        filewin = tkinter.Toplevel(self)
        button = tkinter.Button(filewin,text="Do nothing button")
        button.pack()

    def menu(self) :
        menubar = tkinter.Menu(self)
        filemenu = tkinter.Menu(menubar,tearoff=0)
        filemenu.add_command(label="Open",command=self.doNothing)
        filemenu.add_command(label="Save",command=self.doNothing)
        filemenu.add_command(label="Histogram",command=self.doNothing)
        menubar.add_cascade(label="File",menu=filemenu)
        filemenu = tkinter.Menu(menubar,tearoff=0)
        filemenu.add_command(label="RGB_ToGray",command=self.doNothing)
        filemenu.add_command(label="Thresholding",command=self.doNothing)
        filemenu.add_command(label="Stretching",command=self.doNothing)
        filemenu.add_command(label="Mean Filter",command=self.doNothing)
        filemenu.add_command(label="Median Filter",command=self.doNothing)
        menubar.add_cascade(label="Normal Filter",menu=filemenu)
        filemenu = tkinter.Menu(menubar,tearoff=0)
        filemenu.add_command(label="1. Model",command=self.doNothing)
        filemenu.add_command(label="2. Model",command=self.doNothing)
        filemenu.add_command(label="3. Model",command=self.doNothing)
        filemenu.add_command(label="4. Model",command=self.doNothing)
        filemenu.add_command(label="5. Model",command=self.doNothing)
        menubar.add_cascade(label="Style Transfer",menu=filemenu)
        filemenu = tkinter.Menu(menubar,tearoff=0)
        filemenu.add_command(label="Resize",command=self.doNothing)
        filemenu.add_command(label="Cut",command=self.doNothing)
        filemenu.add_command(label="Rotate",command=self.doNothing)
        menubar.add_cascade(label="Resizing",menu=filemenu)

        self.config(menu=menubar)


if __name__ == "__main__" :
    win = Window("BangGyoo Proj")
    win.mainloop()
