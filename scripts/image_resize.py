from PIL import Image
import glob, os

def resize( filename, scale ):
    with open(filename, 'r+b') as f:
        with Image.open(f) as image:

            height, width = image.size

            new_h = height/scale
            new_w = width/scale

            #print(new_h)
            #print(new_w)

            outfile = filename.replace('in','out')
            outdir = os.path.dirname(outfile)

            if not os.path.exists(outdir):
                os.makedirs(outdir)

            cover = image.resize((new_h, new_w), Image.ANTIALIAS)
            cover.save(outfile)

            print("Resized file: " + outfile + ", by scale of " + str(scale))

if __name__ == '__main__':

    filelist = [os.path.join(root, name)
             for root, dirs, files in os.walk('./in/')
             for name in files
             if name.endswith((".JPEG", ".JPG"))]

    for file in filelist:
        resize(file, 4)







