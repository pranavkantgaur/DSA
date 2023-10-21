# could be used to create dp array for very large state-space where pre-allocating arrays will be inefficient.
# inserting solution for state <key1, key2> while developing memoization solution:
dict = {}
if key1 in dict.keys():
  if key2 in dict[key1].keys():
    dict[key1][key2] = x
  else:
    dict[key1][key2] = {}
else:
  dict[key1] = {}
