import random
print("\tRW50ZXIgdGhlIHNlbnRlbmNlOiA=",end="")
V29yZHM_ = input()
d29yZHNw = V29yZHM_.split()

def jumb(d29yZA__):
    print("\n\tQ29ycmVjdCB3b3JkOiA="+d29yZA__)
    anVtYmxl = ""
    while d29yZA__:
        cG9zaXRpb24_ = random.randrange(len(d29yZA__))
        anVtYmxl += d29yZA__[cG9zaXRpb24_]
        d29yZA__ = d29yZA__[:cG9zaXRpb24_] + d29yZA__[(cG9zaXRpb24_ + 1):]
        while anVtYmxl == d29yZA__:
            cG9zaXRpb24_ = random.randrange(len(d29yZA__))
            anVtYmxl += d29yZA__[cG9zaXRpb24_]
            d29yZA__ = d29yZA__[:cG9zaXRpb24_] + d29yZA__[(cG9zaXRpb24_ + 1):]
    return anVtYmxl

anVtYmxpc3Q_=[]

for dw__ in d29yZHNw:
    YQ__=jumb(dw__)
    print("\tSnVtYmxlZCB3b3JkOg==", YQ__,"\n")
    anVtYmxpc3Q_.append(YQ__)

anVtYnN0cg__ = " ".join(anVtYmxpc3Q_)
print("\t",V29yZHM_)
print("\t",anVtYnN0cg__)
