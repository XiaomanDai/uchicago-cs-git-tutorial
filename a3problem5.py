# problem 5
# Xiaoman Dai
def caesar_encrypt(key, message):
  encrypted_message = ''
  for i in range(len(message)):
    char = message[i]
    if char.isupper():
      encrypted_message += chr((ord(char) + key - 65) % 26 + 65)
    elif char.isspace():
      encrypted_message += ' '
    else:
      encrypted_message += chr((ord(char) + key - 97) % 26 + 97)
  return encrypted_message

print(caesar_encrypt(15, 'mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp'))
# output is 'believe you can and you are halfway there'
