from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from krita import *

VERTICAL = 2520
HORIZONTAL = 3640

class WallpaperSizer(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction("wallSizer", "Wallpaper Sizer", "tools/scripts")
        action.triggered.connect(self.wallpaperSizer)

    def Resize(self,v,h):
        diffV = VERTICAL/v
        diffH = HORIZONTAL/h
        doc = Krita.instance().activeDocument()

        if(v < VERTICAL and h > HORIZONTAL):
            v *= diffV
            h *= diffV
            print("Height too small, Enlarging Image")
            doc.scaleImage(h,v,doc.xRes(),doc.yRes(),"Bicubic")
            self.Resize(v,h)
        elif(v > VERTICAL and h < HORIZONTAL):
            h *= diffH
            v *= diffH
            print("Width too small, Enlarging Image")
            doc.scaleImage(h,v,doc.xRes(),doc.yRes(),"Bicubic")
            self.Resize(v,h)
        elif(v < VERTICAL and h < HORIZONTAL):
            if(diffH < diffV):
                v *= diffV
                h *= diffV
            elif(diffH > diffV):
                v *= diffH
                h *= diffH
            print("Both height and width too small, Enlarging Image")
            doc.scaleImage(h,v,doc.xRes(),doc.yRes(),"Bicubic")
            print("Calling Resize function Again...")
            self.Resize(v,h)
        elif(v > VERTICAL and h > HORIZONTAL):
            if(diffH < diffV):
                v *= diffV
                h *= diffV
            elif(diffH > diffV):
                v *= diffH
                h *= diffH
            print("Both height and width too big, Shrinking Image")
            doc.scaleImage(h,v,doc.xRes(),doc.yRes(),"Bell")
            print("Resizing Again...")
            self.Resize(v,h)
        else:
            # print("Image Ready to be Cropped!")
            QMessageBox.information(QWidget(), "Crop", "Image Ready to be Cropped!")
            leftEdge = (h - HORIZONTAL) / 2
            topEdge = (v - VERTICAL) / 2
            doc.resizeImage(leftEdge,topEdge,HORIZONTAL,VERTICAL)
            doc.save()

    def wallpaperSizer(self):
        doc = Krita.instance().activeDocument()
        # if(doc.height() > doc.width()):
        #     print("Noooo, this is only for landscape-oriented pictures....for now")
        if(doc.height() < VERTICAL / 2 or doc.width() < HORIZONTAL / 2):
            QMessageBox.information(QWidget(), "Too small", "Image too small to grow to desired size. It will look like sh**!")
        else:
            self.Resize(doc.height(),doc.width())



Krita.instance().addExtension(WallpaperSizer(Krita.instance()))