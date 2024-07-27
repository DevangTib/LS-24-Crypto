import numpy as np
from sympy import Matrix

text=input("Enter plaintext: ")
text=text[:9].upper()

array_p=np.zeros((3,int(len(text)/3)),dtype=int)
for i in range(len(text)):
    array_p[i%3][int(i/3)]=ord(text[i])

P=array_p-65
# print(array_p)
cipher=input("Enter the cipher text: ")
cipher=cipher[:9].upper()

array_c=np.zeros((3,int(len(cipher)/3)),dtype=int)
for i in range(len(cipher)):
    array_c[i%3][int(i/3)]=ord(cipher[i])

C=array_c-65
# print(array_c)
# print(P)
# print(C)
P_matrix = Matrix(P)
C_matrix = Matrix(C)
# we have C=K*P mod 26
# we need to find K, knowing C and P.
    # print(P_matrix)
    # print(C_matrix)

    # Calculate the inverse of P modulo 26
try:
    P_inv_mod26 = P_matrix.inv_mod(26)
except ValueError:
    print("Matrix P is not invertible modulo 26.")
    # error if not invertible
    exit()

# Calculate K
K = (C_matrix * P_inv_mod26) % 26

# Convert back to numpy array if needed
K = np.array(K).astype(int)
# converting K into numpy matrix
    # print("Key matrix K:")
#print(K)
key=""
for row in range(3):
    for col in range(3):
        key=key+chr(K[row][col]+65)
        #extracting the key and printing
print("KEY is:")
print(key)