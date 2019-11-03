
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
from sec import *
im="001.png"


def hash(im):
    i=mpimg.imread(im).min(axis=2)
    # print(mpimg.imread(im))
    j=np.rint(i)
    return (1-j).sum()

def hash2(im):
    i=mpimg.imread(im).min(axis=2)
    j=np.rint(i)
    return [int(i) for i in list((1-j).sum(axis=1))]

def new(im):
    i=mpimg.imread(im).max(axis=2)
    j=np.rint(i)
    j=1-j
    # print(j[:,1:],j.sum(axis=0)[0])
    while True:
        if j[-1].sum()==0:
            j=j[:-1]
        else:
            break
    
    while True:
        if j[0].sum()==0:
            j=j[1:]
        else:
            break
    
    while True:
        if j.sum(axis=0)[0]==0:
            j=j[:,1:]
        else:
            break
    
    while True:
        if j.sum(axis=0)[-1]==0:
            j=j[:,:-1]
        else:
            break
    j=1-j
    j=j[:,:,np.newaxis]
    k=np.concatenate((j,j,j),axis=2)
    mpimg.imsave("../new/"+im,k)

u={
    112:"i",
    253:"V",
    438:"B",
    358:"O",
    389:"R",
    311:"w",
    281:"0",
    354:"K",
    367:"G",
    325:"g",
    227:"o",
    316:"A",
    414:"N",
    341:"S",
    297:"U",

}
# print(hash("001.png"))
# exit(0)

# new("001.png")
# exit(0)

im="../cropped/086.png"
im="../cropped/130.png"
im="../cropped/156.png"
# im="../cropped/183.png"
# im="../cropped/206.png"


# i=mpimg.imread(im).min(axis=2)
# i=np.rint(i*5)
# i=5-i
# print(i.sum())
# exit()

jb=[" "for i in range(2160)]

for i,j,k in os.walk("../cropped/"):
    for f in k:
        im="../cropped/"+f
        try:
            i=mpimg.imread(im).min(axis=2)
        except:
            continue
        i=np.rint(i*5)
        i=5-i
        j=i.sum()
        if j==640:

            print(f,"l",i.max(axis=0))
            jb[int(f[:f.find(".")])]="l"
        elif j==672:
            print(f,"I",i.max(axis=0))
            jb[int(f[:f.find(".")])]="I"
open("1.txt","w").write("".join(jb))
exit(0)
# for i,j,k in os.walk("."):
#     for f in k:
#         print(f)
#         if f[-1]=="y":
#             continue
#         # print(f,hash(f))
#         new(f)

def getc(h):
    j=1000000
    p=0
    
    for i in v:
        if len(v[i])!=len(h):
            continue
        s=np.abs(np.array(v[i])-np.array(h)).sum()
        if s<j:
            j=s
            p=i

    # print(j)
    if j>10:
        return None
    return p

sb={}
for i,j,k in os.walk("."):
    for f in k:
        # print(f)
        if f[-1]=="y" or f=="1.png":
            continue
        # print(f,getc(hash2(f)),hash2(f))
        # if not getc(hash2(f)):
            # c=input()

        sd=mpimg.imread(f).shape[:2]
        if sd not in sb:
            sb[sd]=1
        else:
            sb[sd]+=1
        
print(sb)
# print()
# s=""
# for i in range(1,2160):
#     f=str(i).rjust(3,'0')
#     f=f+".png"
#     s+=getc(hash2(f))

#     if not getc(hash2(f)):
#         c=input()

# s=s.replace("_","").replace("^","")
# print(s)