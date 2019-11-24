# wallpaper-sizer
Plugin for Krita used to size images properly for desktop wallpaper
  
While every OS has multiple options for fitting wallpaper to the screen,
these options are in no way of universal quality between different image dimensions.

This plugin will allow you to size images to your desktop by first resizing
the image, keeping the aspect ratio, and then cropping an equal amount off
of the top/bottom, or the left/right sides, as necessary.  If the image is less
than half of the desired width, it will not be resized
as this will result in a poor-quality image.  This may be changed in the future 
to simply offer a warning and then giving the user the option.

Currently, this plugin best for *landscape* oriented images.  It still works fine 
with *portrait* oriented images, but the cropping may cut off too much.

Also, right now, the sizes are hard-coded until I create a docker.

Future plans include image enhancement before and after the resize, presets for different
image uses (facebook cover photos, mobile wallpapers, profile pics, etc.), and batching.
