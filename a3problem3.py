# problem 3
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

print(caesar_encrypt(12, 'Experience is the teacher of all things')) # Qjbqduqzoq ue ftq fqmotqd ar mxx ftuzse

def caesar_decrypt(key, message):
  decrypted_message = ''
  for i in range(len(message)):
    char = message[i]
    if char.isupper():
      decrypted_message += chr((ord(char) - key - 65) % 26 + 65)
    elif char.isspace():
      decrypted_message += ' '
    else:
      decrypted_message += chr((ord(char) - key - 97) % 26 + 97)
  return decrypted_message

print(caesar_decrypt(12, 'Experience is the teacher of all things')) # Sldsfwsbqs wg hvs hsoqvsf ct ozz hvwbug
