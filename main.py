import tkinter
import tkinter.filedialog
import cv2
from PIL import Image, ImageTk

class Window(tkinter.Tk) :
    def __init__(self,title,window_size = 600,x_pos=10,y_pos=10) :
        super().__init__()
        self._saved = False
        self.title(title)
        self.geometry(str(window_size) +"x"+ str(window_size + 10)+ "+" + str(x_pos) +"+"+ str(y_pos))
        self.resizable(False,False)
        self._window_size = window_size; self._x_pos=x_pos;self._y_pos=y_pos;self._title = title
        self.menu()
    def doNothing(self) :
        filewin = tkinter.Toplevel(self)
        button = tkinter.Button(filewin,text="Do nothing button")
        button.pack()
    def open(self) : 
        file = tkinter.filedialog.askopenfilename(title = "choose image file",filetypes=[('png images','.png'),('gif images','.gif')])
        self._src = cv2.imread(file) # orig file
        src = cv2.resize(self._src, self.calc_resize(len(self._src[0]),len(self._src) )) # Is resized file 
        img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        self._imgtk = ImageTk.PhotoImage(image=img) # Do not deallocate variables.
        self.image = tkinter.Label(self, image=self._imgtk)
        self.image.pack(side="bottom")
        
    def display_color_histogram(self) :
        HIST_WIDTH = 512; HIST_HEIGHT = 400; HIST_TERM = 5000
        filewin = tkinter.Toplevel(self,width=HIST_WIDTH,height= HIST_HEIGHT)
        canvas = tkinter.Canvas(filewin,bg= '#ffffff',width=HIST_WIDTH,height=HIST_HEIGHT)
        canvas.pack()
        hist = [ cv2.calcHist([self._src],[i],None,[256],[0,256]) for i in range(3) ] # args = calcHist(images,channels,mast,histsize,ranges)
        
        hist_sum = [0,0,0]
        for i in range(3) :
            for j in range(256) : hist_sum[i] += hist[i][j] # calc total_sum for average

        for i in range(256) :
            canvas.create_rectangle((HIST_WIDTH//256)*i,HIST_HEIGHT,(HIST_WIDTH//256)*i,HIST_HEIGHT - int(hist[0][i]/hist_sum[0] * HIST_TERM),fill='#ff0000',outline='#ff0000')
            canvas.create_rectangle((HIST_WIDTH//256)*i,HIST_HEIGHT,(HIST_WIDTH//256)*i,HIST_HEIGHT - int(hist[1][i]/hist_sum[1] * HIST_TERM),fill='#00ff00',outline='#00ff00')
            canvas.create_rectangle((HIST_WIDTH//256)*i,HIST_HEIGHT,(HIST_WIDTH//256)*i,HIST_HEIGHT - int(hist[2][i]/hist_sum[2] * HIST_TERM),fill='#0000ff',outline='#0000ff')




    def calc_resize(self,width,height) : # it's resizing size overflow
        if width > height :
            flag = True
        else :
            flag = False
        if width > self._window_size and flag == True :
            height = height * self._window_size / width
            width = self._window_size
        elif height > self._window_size and flag == False :
            width = width * self._window_size / height
            height = self._window_size
        return (int(width),int(height))
    def save(self) :
        if self._saved == False :
            file = tkinter.filedialog.asksaveasfilename(title = "save image file",defaultextension=".png",filetypes=(('png images','*.png'),('gif images','*.gif')))
            cv2.imwrite(file,self._src) 
            self._saved = True




    def menu(self) :
        menubar = tkinter.Menu(self)
        filemenu = tkinter.Menu(menubar,tearoff=0)
        filemenu.add_command(label="Open",command=self.open)
        filemenu.add_command(label="Save",command=self.save)
        filemenu.add_command(label="Histogram",command=self.display_color_histogram)
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
