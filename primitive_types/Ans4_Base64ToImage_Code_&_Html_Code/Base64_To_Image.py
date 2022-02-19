import base64

# taking the encode.bin string
file = open('encode.bin', 'rb')
byte = file.read()
file.close()

# This is the out put of the encode.bin string
decodeit = open('This is UJM logo .PNG', 'wb')
decodeit.write(base64.b64decode((byte)))
decodeit.close()