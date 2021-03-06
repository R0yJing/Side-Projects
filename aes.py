#128 bit aes using bit hackery
import math

keys = [0] * 11
inv_sbox = [0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB, 
            0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB, 
            0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E, 
            0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25, 
            0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92, 
            0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
            0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06, 
            0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B, 
            0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73, 
            0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E, 
            0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B, 
            0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4, 
            0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F, 
            0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF, 
            0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61, 
            0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]

sbox =     [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
            0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
            0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
            0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
            0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
            0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
            0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
            0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
            0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
            0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
            0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
            0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
            0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
            0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
            0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
            0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]

RCs =      [0, 0x1, 0x2, 0x4, 0x8, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]
BWIDTH = 8

def subblocki(binblock, sub, i, unit = 32):
    mask = 0xffffffff000000000000000000000000
    #sub is already correctly aligned
    return ~(mask >> (i * unit)) & binblock | sub

def getithblock(i, binblock, unit=32):
    mask = 0xffffffff000000000000000000000000
    binblock = (mask >> (i * unit)) & binblock    
    return binblock

def getsbox(state):
    return sbox[(state >> 4) * 16 + (state & 0xf)]
    
def g(binblock, rci):
    
    '''
    32 bit, consisting of 4 2-bytes
    '''
    
    firstblock = binblock >> (8 * 3)
    binblock <<= 8
    
    binblock %= 0x100000000
    
    binblock |= firstblock
    temp = binblock
 
    for i in range(0, 4):

        
        binblock = binblock & ~(0xff << i * BWIDTH) | (getsbox(temp & 0xff) << (i * BWIDTH))
        
        temp >>= BWIDTH

    #adding RC
    binblock ^= ( RCs[rci] << 3 * BWIDTH)
    return binblock

def realign(block, frm, to, unit = 32):
    if (frm < to):
        return block >> (to - frm) * unit
    else:
        return block << (frm - to) * unit
    
def keyschedule(binblock, numrounds = 1):
    
    keys[0] = binblock
    
    for i in range(1, numrounds):
        gLastblock =  g(getithblock(3, binblock), i)

        xor = getithblock(0, binblock) ^ realign(gLastblock, 3, 0)
        
        binblock = subblocki(binblock, xor, 0)
       
        for j in range(1, 4):
            xor = realign(getithblock(j - 1, binblock), j-1, j) ^ getithblock(j,binblock)
            binblock = subblocki(binblock, xor, j)
            
        keys[i] = binblock
    return keys

def bytesub(x):
    m = 0xff
    new = 0
    for i in range(0, 4*4):
        new += getsbox(m & x) << (i * BWIDTH)
        x >>= BWIDTH
    return new


def multGF(y, x, mod = 0x11B):
   
    ix = 0
    iy = 0
    lenpx = math.ceil(math.log2(x + 1))
    lenpy = math.ceil(math.log2(y + 1))
    polyx = [0] * lenpx
    polyy = [0] * lenpy
    
    modlen = math.ceil((math.log2(mod+1)))
    Px = [0]*modlen
    z = 0
    while mod != 0:
        Px[z] = mod&1
        mod>>=1
        z+=1
        
    while x != 0:
        polyx[ix] = x & 1
        x >>= 1
        ix+=1

    while y != 0:
        polyy[iy] = y & 1
        y >>= 1
        iy+=1
    poly = [0] * (lenpx + lenpy -1)
    #carries = [0] * (lenpx + lenpy)
    #apply summation
    
    for i in range(0, lenpx):
        for j in range(0, lenpy):
            poly[i+j] = poly[i+j] ^ (polyx[i] * polyy[j]) 
    
    biggest=-1

    for i in range(lenpy + lenpx -2, -1, -1):
        if poly[i] != 0:
            biggest = i
            break

    remainder = poly
    pxend = 8
    newBiggest = -1
    while biggest >= pxend:
        newFound = False
        for i in range(biggest, biggest - pxend - 1, -1):
            j = i - biggest + pxend
            remainder[i] = remainder[i] ^ Px[j]
            if remainder[i] == 1 and not newFound:
                newBiggest = i
                newFound = True
        if newBiggest != -1:     
            biggest = newBiggest
        else:
            for i in range(i -1, -1, -1):
                if remainder[i] == 1:
                    biggest = i
                    #cannot put newbiggest here
                    break


    acc = 0
    i = 0
    b =1
    while i < biggest + 1:
        acc += remainder[i] * b
        b <<= 1
        i+=1
    return acc

def shiftrows(x, start = 0, fin = 3, step = 1):
    
    #3 positions right shift
    #select b[4:7]
    #convert to columnwise form
    x = preshiftRows(x)
    fullM = ((1 << 32) - 1)
    headMask = 0xff
    if step == -1:
        headMask += 0xffff00
    for i in range(start, fin, step):
        ls = (3-i)* BWIDTH
        rs = (i + 1) * BWIDTH

        tailMask = (fullM  - headMask)
       
        headX = headMask & x
        tailX = tailMask & x
        x &= ~fullM
        x += (headX << ls) + (tailX >> rs)
        if step == 1:
            headMask = (headMask << BWIDTH) | headMask
        else:
            headMask = (headMask & (headMask >> BWIDTH))
        fullM <<= 32
        headMask <<= 32
    return postshiftRows(x)
        
    #2positions
    #1 positions

def expGF(x,y, mod):
    acc = x
    for i in range(1,y):
        acc = multGF(acc, x, mod)

    return acc

def printMat(xMat):
    for i in range(0, 4):
        for j in range(0, 4):
            print((xMat[i * 4 + j]), end=", ")
        print()
        
def mixcolumns(x, inv = False): 

    mat =None
    if inv:
        mat = [0x0e, 0x0b, 0x0d, 0x09,
               0x09, 0x0e, 0x0b, 0x0d,
               0x0d, 0x09, 0x0e, 0x0b,
               0x0b, 0x0d, 0x09, 0x0e]
    else:
        mat = [2, 3, 1, 1,
               1, 2, 3, 1,
               1, 1, 2, 3,
               3, 1, 1, 2]

    xMat = [0] * 16

    for i in range(0, 16):
        xMat[(3 - (i % 4)) * 4 + (3 - i // 4)] = x & 0xff
        x >>= BWIDTH
    result = [0] * 16
   
    #mat x input matrix
    
    for r in range(0, 4):
        for c in range(0, 4):
            rr = 0
            for k in range(0, 4): rr ^= multGF(mat[r*4 + k], xMat[k*4 + c])
            result[r*4 + c] = rr
    
    acc = 0
    shift = 1
    for i in range(0, 16):
        acc += result[(3 - (i % 4)) * 4 + (3 - i // 4)] * shift
        shift <<= BWIDTH

    return acc
def preshiftRows(x):
    acc = 0
    offsetx = 0
    for i in range(0, 4):
        
        offsety = 0
        for j in range(0, 4):
            v = x & 0xff
            acc += (v << offsety) << offsetx
            offsety += 32
            x >>= BWIDTH
        offsetx += BWIDTH
    return acc
            
def postshiftRows(x):
    acc = 0
    offsety = 0
    for i in range(0, 4):
        
        offsetx =0
        for j in range(0, 4):
            v = x & 0xff
            acc += (v << offsety) << offsetx
            offsetx += 32
            x >>= BWIDTH
        offsety += BWIDTH
    return acc

def inv_keyschedule(key):
    
    keys[0] = key
    for i in range(1, 11):
        for j in range(3, 0, -1):

            xor = getithblock(j, key) ^ realign(getithblock(j - 1, key), j - 1, j)
            key = subblocki(key, xor, j)
        
        first = getithblock(0, key)
        gLast = realign(g(getithblock(3, key), 11 -i), 3, 0)
        key = subblocki(key, first ^ gLast, 0)
        
        keys[i] = key
    return keys

def inv_shiftrows(x):
    return shiftrows(x, 2, -1, -1)

def inv_bytesub(x):
    acc =0
    #assume bit length of 128
    shift = 1
    for i in range(0, 16):
        v = x & 0xff
        x >>= BWIDTH
        acc += inv_sbox [(v >> 4) * 16 + (v & 0xf)] * shift
        shift <<= BWIDTH
    return acc
def enc(x, k):
 
    keys = keyschedule(k, 11)
    
    x ^= keys[0]
    i=1
    while i < 10:
        x = bytesub(x)
        x = shiftrows(x)
        x = mixcolumns(x)
        x ^= keys[i]
       
        i += 1
    x = bytesub(x)
    x = keys[10] ^ shiftrows(x)
    return x

def dec(x, k):
    keys = keyschedule(k)
    x ^= keys[10]
    x = inv_bytesub(inv_shiftrows(x))
    for i in range(1, 10):
        x ^= keys[10 - i]
        x = inv_mixcolumns(x)
        x = inv_shiftrows(x)
        x = inv_bytesub(x)
       

    x ^= keys[0]
    return x

def inv_mixcolumns(x):
    return mixcolumns(x, True)

x0 =0x112233445566778899aabbccddeeff
k0 = 0x102030405060708090a0b0c0d0e0f
#demo: encrypt then decrypt using the same keys should give the original plaintext
print(hex(dec(enc(x0, k0), k0)))
