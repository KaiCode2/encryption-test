import gmpy2
from egcd import egcd
import random


class RSA:
    def __init__(self):
        def initialize(self):
            first = gmpy2.next_prime(int(random.random() * 1000))
            second = gmpy2.next_prime(int(random.random() * 1000))
            self.max = first * second
            et = (first - 1) * (second - 1) # Computer Eulers totient
            self.public_key = egcd(gmpy2.next_prime((int(random.random() * 1000000) % (et - 3)) + 3) , et)[1] # Select prime number [3, et)
            self.private_key = egcd(self.public_key, et)[1] # Computer modular inverse

            # Hack I made to ensure keys are non negative
            if self.public_key <= 0 or self.private_key <= 0:
                initialize(self)
        initialize(self)

    def encrypt(self, plain_text):
        return pow(plain_text, self.public_key) % self.max

    def decrypt(self, cipher_text):
        return pow(cipher_text, self.private_key) % self.max


rsa = RSA()

print('encrypt')
cipher = rsa.encrypt(100)
print(cipher)
print('decrypt')
og = rsa.decrypt(cipher)
print(og)
