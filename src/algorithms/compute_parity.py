'''
Problem: https://github.com/adnanaziz/EPIJudge/blob/master/epi_judge_python/parity.py

Approach: 
0. Create hash map for parrity precomputed for n-bit words
1. For each word:
   1.1. Divide word to n-bit chunks
   1.2. For chunk in word:
        1.2.1. parity = hmap[chunk] 
        1.2.2. word_parity ^= parity ?
   1.3. words_parities.append(word_parity)     
2. return word_parities   

'''
def compute_parity(word_array):
   hmap = compute_chunk_maps()      
   for word in word_array:
      word_chunks = get_word_chunks(word)
      for chunk in word_chunks:
         parity = hmap[chunk]
         word_parity &= parity
   word_parities.append(word_parity)         
   return word_parities

