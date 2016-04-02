import struct
p = 37975227936943673922808872755445627854565536638199
q = 40094690950920881030683735292761468389214899724061
n = p*q
e = 65537
phi = (p-1)*(q-1)
d = 1435319569480661473883310243084583371347212233430112391255270984679722445287591616684593449660400673 # inverse_mod(e,totient)
# print((e*d)%phi) <- is 1
for filenum in range(1,17):
    a = open(str(filenum)+'.enc','rb')
    s = a.read()
    a.close()
    data = int.from_bytes(s, byteorder='big') # converts it to an integer
    decoded = hex(pow(data,d,n)).replace('0x','') # gets hex data of decoded thing
    out = ''
    for i in range(0,len(decoded)//2*2,2): # convert hex to ascii by taking 2 chars at a time
        c = ''.join(decoded[i:i+2])
        out += chr(int(c,16))
    print(out, end = '')
