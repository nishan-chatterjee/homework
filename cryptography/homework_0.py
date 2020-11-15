from bitarray import bitarray

x = [bitarray('0111011'), bitarray('0010000'), bitarray('0100110'), bitarray('0111110'), bitarray('0010111')]
k = bitarray('0011011')
c = bitarray('1101000')
encrypt = []
decrypt = []
for index in x:
    encrypt.append(index ^ k)
    decrypt.append((index ^ k) ^ k)
print(crypt)
