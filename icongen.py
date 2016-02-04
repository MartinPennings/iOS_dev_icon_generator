import os, sys
from PIL import Image



def makeThumb(size_square,orgfile, prefix="thumb_"):
    destfile=prefix + orgfile.split(".")[0] + ".png"
    try:
        im = Image.open(orgfile).convert("RGB")
        im.thumbnail((size_square,size_square))
        im.save(destfile, "PNG")
        print("icon created")
    except IOError:
        print("cannot create icon for", orgfile)

#######################################
# enter your original icon file here
original_file="icon_org.png"
#######################################


# App icon: iPhone 6s Plus and iPhone 6 Plus (@3x)
# Spotlight icon: iPhone 6s Plus and iPhone 6 Plus (@3x)
makeThumb(180,original_file,"th180")

# iPad Pro (@2x)
makeThumb(167,original_file,"th167")

# iPad and iPad mini (@2x)
makeThumb(152,original_file,"th152")

# App icon: iPhone 6s, iPhone 6 and iPhone 5 (@2x), iPhone 4s(@2x)
# Spotlight: iPhone 6s, iPhone 6, iPad and iPad mini (@2x), iPad Pro (@2x)
makeThumb(120,original_file,"th120")

# Spotlight: iPhone 5, iPhone 4s
makeThumb(80,original_file,"th80")

#App icon: iPad 2 and iPad mini (@1x)
makeThumb(76,original_file,"th76")

#Spotlight iPad 2 and iPad mini 
makeThumb(60,original_file,"th60")



