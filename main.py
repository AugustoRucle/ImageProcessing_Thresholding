import tkinter as tk  # for python 3
import numpy as np
import pygubu, cv2
from tkinter import filedialog, messagebox
from skimage import img_as_float, img_as_ubyte
from matplotlib import pyplot as plt

class Application:
    def __init__(self, master):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('UI.ui')

        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('OeH', master)
        builder.connect_callbacks(self)

    def GetImage(self):
        path =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        if(len(path) != 0):
            try:

                img_normal = cv2.imread('{}'.format('C:\\Users\\AugustoRuCle\\Documents\\Universidad\\Python\\IA\Corte-1\\CienciaColorAndSegmentation\\Images\\hw2_book_page_1.jpg'))
                img_gray = cv2.imread('{}'.format(path), 0)

                cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
                cv2.imshow('Image', self.img_normal)

                self.img_normal = img_normal
                self.image_gray = img_gray
            except:
                messagebox.showerror("Error", "Algo a salido mal, verifique que el contenido seleccionado sea una imagen")
    
    def Start_Thresholding_Global(self):

        path = 'C:\\Users\\AugustoRuCle\\Documents\\Universidad\\Python\\IA\Corte-1\\CienciaColorAndSegmentation\\Images\\hw2_book_page_1.jpg'

        img_normal = cv2.imread('{}'.format(path))
        img_gray = cv2.imread('{}'.format(path), 0)

        
        #Show image normal and image with Thresholding
        ret2,th2 = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
        cv2.imshow('Image', img_gray)
        cv2.namedWindow('THRESH_OTSU', cv2.WINDOW_NORMAL)
        cv2.imshow('THRESH_OTSU', th2)


    def GetHistogram_Global(self):
        path = 'C:\\Users\\AugustoRuCle\\Documents\\Universidad\\Python\\IA\Corte-1\\CienciaColorAndSegmentation\\Images\\hw2_book_page_1.jpg'
        img_gray = cv2.imread('{}'.format(path), 0)
        ret2,th2 = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        xposition = [ret2, 140000]
        y, x, _ = plt.hist(img_gray.ravel(), 256, [0, 256])
        plt.axvline(x=ret2, ymin=0, ymax= y.max(), color='k', linestyle='--')
        plt.ylabel('Numero de pixeles')
        plt.xlabel("Nivel en grises")
        plt.title('Histrograma')
        plt.show()

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
