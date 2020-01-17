import os

SFN="E:\Python training/Images/banner.jpg"
DFN="E:\Python training/Images/banner1.jpg"

info=os.stat(SFN)
fs=info.st_size
print("Size:%d" %fs)

def copypaste():
    "to copy a file and paste"
    # opening file in read binary mode
    bfr=open(SFN,"rb")
    # opening /creating file in write binary mode
    bfw=open(DFN,"wb")
    for i in range(fs):
        # reading bytes 1 by 1
        bfw.write(bfr.read(1))
        print("Bytes:%d" %i)
    else:
        bfr.close()
        bfw.close()
        print("Copy Paste Done")
# calling function
copypaste()

