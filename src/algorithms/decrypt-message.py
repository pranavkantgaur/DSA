# https://www.pramp.com/challenge/8noLWxLP6JUZJ2bA2rnx
def decrypt(word):
  result  = []
  second = 1
  
  letter_id = 0
  while(letter_id < len(word)):
    result[letter_id] = word[letter_id] - second
    
    if result[letter_id] < 97:
      result[letter_id] += 26
    second += result[letter_id]
    letter_id += 1
  return result 
