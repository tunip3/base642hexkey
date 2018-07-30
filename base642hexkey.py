import binascii
import base64
inp=input("please enter b64 key ")
array = base64.standard_b64decode(inp)
out=binascii.hexlify(bytearray(array))
out=str(out)
out=out.replace("b'","")
out=out.replace("'","")
out=out.upper()
print(out)
