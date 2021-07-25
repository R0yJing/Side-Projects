#3des and des
import math


s1 =[
14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13
]

s2 =[
15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9
]

s3 =[
10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8
,13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,
13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,
1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12
]

s4 =[
7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15
,13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,
10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,
3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14
]

s5 =[
2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,
14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,
4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,
11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3
]

s6 =[
12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,
10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,
9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,
4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13
]

s7 =[
4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,
13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,
1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,
6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12
]

s8 =[
13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,
1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,
7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,
2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11
]
sboxes = [s1, s2, s3, s4, s5,s6,s7,s8]

P =[
    16,7,20,21,29,12,28,17,
1,15,23,26,5,18,31,10,
2,8,24,14,32,27,3,9,
19,13,30,6,22,11,4,25
    ]
#E box
expPerm =[
32,1,2, 3,  4, 5,
4, 5,6, 7,  8, 9,
8,9,10,11,12,13,
12,13,14,15,16,17,
16,17,18,19,20,21,
20,21,22,23,24,25,
24,25,26,27,28,29,
28,29,30,31,32,1
]

PC_1 = [
    57,49,41,33,25,17,9,
1,58,50,42,34,26,18,
10,2,59,51,43,35,27,
19,11,3,60,52,44,36,
63,55,47,39,31,23,15,
7,62,54,46,38,30,22,
14,6,61,53,45,37,29,
21,13,5,28,20,12,4
    ]
PC_2 =[
14,17,11,24,1,5,3,28,
15,6,21,10,23,19,12,4,
26,8,16,7,27,20,13,2,
41,52,31,37,47,55,30,40,
51,45,33,48,44,49,39,56,
34,53,46,42,50,36,29,32
]

IP=[
58,50,42,34,26,18,10,2,
60,52,44,36,28,20,12,4,
62,54,46,38,30,22,14,6,
64,56,48,40,32,24,16,8,
57,49,41,33,25,17,9,1,
59,51,43,35,27,19,11,3,
61,53,45,37,29,21,13,5,
63,55,47,39,31,23,15,7
]

IP_1=[
40,8,48,16,56,24,64,32,
39,7,47,15,55,23,63,31,
38,6,46,14,54,22,62,30,
37,5,45,13,53,21,61,29,
36,4,44,12,52,20,60,28,
35,3,43,11,51,19,59,27,
34,2,42,10,50,18,58,26,
33,1,41,9,49,17,57,25
]
def p(b):
    strr = '0' * (32 - math.ceil(math.log2(b + 1))) + bin(b)[2::]
    
    news = list(' ' *32)
    for i in range(0,32):
        news[i] = strr[P[i] - 1]
 
    
    return int(''.join(news), 2)

def S(b, ith):
    
    #6 bits
    rowpos = (b >> 4 & 0b10) | (b & 1)
    
    colpos = (b % 2**5) >> 1
    
    return sboxes[ith][rowpos * 16 + colpos]

def E(orig):

    strr = '0' * (32 - math.ceil(math.log2(orig + 1))) + bin(orig)[2::]
    
    news = list(' ' *48)
    for i in range(0,48):
        news[i] = strr[expPerm[i] - 1]
 
    
    return int(''.join(news), 2)


def f(r, k):
    r = k ^ E(r)
    
    #r now 48 bits
    r1 = 0
    for i in range(0,8):
        _r = S(r & (2**6 -1), 8 - i - 1)
        r1 |= _r << (i * 4)
        r >>= 6
    y = p(r1)
    
    return y

def ip(b):
    news = [0] *64
    strr = '0' * (64 - math.ceil(math.log2(b + 1))) + bin(b)[2::]
    
    for i in range(0, 64):
        news[i] = strr[IP[i] - 1]
    return int(''.join(news), 2)

def ip_1(b):
    news = list(' ' * 64)
    
    strr = '0' * (64 - math.ceil(math.log2(b + 1))) + bin(b)[2::]
    
    for i in range(0, 64):
        news[i] = strr[IP_1[i] - 1]
    return int(''.join(news), 2)


def pc_1(m):
    #input is 64 bits
    #truncated to 56 bits
    news = list(' ' *56)
    strr = '0' * (64 - math.ceil(math.log2(m + 1))) + bin(m)[2::]
    for i in range(0, 56):
        news[i] = strr[PC_1[i] - 1]
    return int(''.join(news), 2)

def pc_2(m):
    '''from 56 to 48 bits'''
    news = [0] * 48
    strr = '0' * (56 - math.ceil(math.log2(m + 1))) + bin(m)[2::]
   
    for i in range(0, 48):
        
        news[i] = strr[PC_2[i] - 1]
        
    return int(''.join(news), 2)

def ls(b, num, bitwidth = 28):
    return ((b << num) & ((1<<bitwidth) - 1)) + (b >> (bitwidth - num ))
    

def keyschedule(k):
    k = pc_1(k)
    i = 1
    keys = [0] * 16

    while i < 17:
        d = k&(2**28 - 1)
        c = k >> 28
        
        if i == 1 or i == 2 or i == 9 or i == 16:
            c= ls(c, 1)
            d = ls(d, 1)
        else:
            c= ls(c, 2)
            d = ls(d, 2)
        k = ((c << 28) % 128) | d
        
        keys[i - 1] = pc_2(k)
        
        i += 1

    return keys

def rs(b, n, bitwidth =28):
    return b >> n | ((b << (bitwidth - n)) & ((1<<bitwidth) - 1))

def dec(k, plaintext):

    plaintext = ip(plaintext)
    l = plaintext >> 32
    r = plaintext % 2**32
    i = 1
    k = pc_1(k)
    
    while i < 17:
        
        ###############

        d = k&(2**28 - 1)
        c = k >> 28

        if i == 1: #round 16 of enc
            
            pass
        elif i == 2 or i == 9 or i == 16:
            c = rs(c, 1)
            d = rs(d, 1)
        else:
            c= rs(c, 2)
            d = rs(d, 2)
        
        #################
        #derive k i after right shift
        k = (c << 28) | d
        templ = l
        l = r
        r = templ ^ f(r, pc_2(k))
        i+=1
    
    #swap places (l and r)
    return ip_1((r << 32) % 2**64 | l)

lastl =0
lastr=0
keys = [0] *16 

def _3des_enc(k0, k1, k2, plaintext):
    return dec(k2, enc(k1, dec(k0, plaintext)))
def _3des_dec(k0, k1, k2, ciphert):
    return enc(k0, dec(k1, enc(k2, ciphert)))

def enc(k, plaintext):
    plaintext = ip(plaintext)
    i =1
    l = plaintext >> 32
    r = plaintext & (2**32-1)
    k = pc_1(k)
    c0=k >>28
    d0 =k%2**28

    while i < 17:
        ####################
        d = k&(2**28 - 1)
        c = k >> 28
        
        if i == 1 or i == 2 or i == 9 or i == 16:

            c= ls(c, 1)
            d = ls(d, 1)
            
        else:
            c = ls(c, 2)
            d = ls(d, 2)
        k = (c << 28) | d

        keys[i - 1] = k
        print(hex(c), hex(d))
        ####################
        
        templ = l
        l = r        
        #k is 56 bits
        r = templ ^ f(r,pc_2(k))
     
        i+=1
    return ip_1(((r << 32) % 2**64) | l)

#demo: encrypt then decrypt using the same keys should give the original plaintext
print(hex(_3des_dec(0xdead, 0xdead, 0xdead, _3des_enc(0xdead, 0xdead, 0xdead, 0xdeadbeef))))
