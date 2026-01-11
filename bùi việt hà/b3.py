#cho trước n tính bin(), hex, otc

def fff(n=8):
    '''ddddd'''
    b = bin(n)
    c = hex(n)
    d = oct(n)
    return b[2::], c[2::], d[2::]
print(fff())





