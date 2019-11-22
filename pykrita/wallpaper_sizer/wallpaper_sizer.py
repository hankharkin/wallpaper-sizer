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
            print("Enlarging Image")
            doc.scaleImage(h,v,72,72,"Bicubic")
        elif(v > VERTICAL and h < HORIZONTAL):
            h *= diffH
            v *= diffH
            print("Enlarging Image")
            doc.scaleImage(h,v,72,72,"Bicubic")
        elif(v < VERTICAL and h < HORIZONTAL):
            v *= diffV
            h *= diffV
            print("Enlarging Image")
            doc.scaleImage(h,v,72,72,"Bicubic")
            print("Resizing Again...")
            self.Resize(v,h)
        elif(v > VERTICAL and h > HORIZONTAL):
            v *= diffV
            h *= diffV
            print("Shrinking Image")
            doc.scaleImage(h,v,72,72,"Bell")
            print("Resizing Again...")
            self.Resize(v,h)
        print("Image Ready to be Cropped!")
        print(" " + str(h) + " x " + str(v))
        leftEdge = (h - HORIZONTAL) / 2
        topEdge = (v - VERTICAL) / 2
        doc.resizeImage(leftEdge,topEdge,HORIZONTAL,VERTICAL)

    def wallpaperSizer(self):
        doc = Krita.instance().activeDocument()
        if(doc.height() > doc.width()):
            print("Noooo, this is only for landscape-oriented pictures....for now")
        elif(doc.height() < VERTICAL / 2 or doc.width() < HORIZONTAL / 2):
            print("Image too small to grow to desired size. (It will look like sh**)")
        else:
            self.Resize(doc.height(),doc.width())



Krita.instance().addExtension(WallpaperSizer(Krita.instance()))