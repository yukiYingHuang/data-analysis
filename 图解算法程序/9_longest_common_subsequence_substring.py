import numpy as np
word_a='fish'
word_b='fosh'
cell1 = np.empty((len(word_a),len(word_b)))
cell2 = np.empty((len(word_a),len(word_b)))

# longest common subsequence
for i in range(len(word_a)):
  for j in range(len(word_b)):
    # cell1[i][j] = 0

    if word_a[i] == word_b[j]:
      # The letters match.
      cell1[i][j] = cell1[i-1][j-1] + 1
    else:
      # The letters don't match.
      cell1[i][j] = max(cell1[i-1][j], cell1[i][j-1])
print(cell1)
# loc1 = np.where(cell1 == np.max(cell1))  #确定最大值的位置
max1 = np.max(cell1)
print("the number of longest commom subsequence",max1)

# longest common substring
for i in range(len(word_a)):
  for j in range(len(word_b)):
    # cell2[i][j] = 0

    if word_a[i] == word_b[j]:
      # The letters match.
      cell2[i][j] = cell2[i-1][j-1] + 1
    else:
      # The letters don't match.
      cell2[i][j] = 0
print(cell2)
max2 = np.max(cell2)
print("the number of longest commom substring",max2)


'''
[[ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  2.  2.]
 [ 1.  1.  2.  3.]]
the number of longest commom subsequence 3.0
[[ 1.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  1.  0.]
 [ 0.  0.  0.  2.]]
the number of longest commom substring 2.0
'''