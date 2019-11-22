# wallpaper-sizer
Plugin for Krita used to size images properly for desktop wallpaper

I made this plugin so I could size images properly to fit my desktop.  
While every OS has multiple options for fitting wallpaper to the screen,
these options are by no way universal.

This plugin will allow you to size images to your desktop by first resizing
the image, keeping the aspect ratio, and then cropping an equal amount off
of the top/bottom, or the left/right sides, as necessary.  If the image is less
than half of the desired resolution in either dimension, it will not be resized
as this will result in a poor-quality image.  This may be changed in the future 
to simply offer a warning and then giving the user the option.

Currently, this plugin ony works for *landscape* oriented images.  

Also, right now, the sizes are hard-coded until I create a docker.
