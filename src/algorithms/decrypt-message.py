# https://www.pramp.com/challenge/8noLWxLP6JUZJ2bA2rnx
def decrypt(word):
  decrypt_str  = ""
  second = 1
  
  letter_id = 0
  while(letter_id < len(word)):
    decrypt_ascii = ord(word[letter_id]) - second
    while decrypt_ascii < 97:
      decrypt_ascii += 26
    decrypt_str += chr(decrypt_ascii)
    second += decrypt_ascii
    letter_id += 1
  return decrypt_str 
