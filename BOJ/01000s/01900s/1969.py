import sys 
input = sys.stdin.readline

n, m = map(int, input().split()) # DNA의 수, 문자열길이

dna_list = []
s = ''
dna = ['A', 'C', 'G', 'T']
hamming_distance = 0

for i in range(n):
  data = input().rstrip()
  dna_list.append(data)
  
for i in range(m):
  a_count = c_count = g_count = t_count = 0
  for j in range(n):
    if dna_list[j][i] == dna[0]:
      a_count += 1
    elif dna_list[j][i] == dna[1]:
      c_count += 1
    elif dna_list[j][i] == dna[2]:
      g_count += 1
    elif dna_list[j][i] == dna[3]:
      t_count += 1
  
  count_list = [a_count, c_count, g_count, t_count]
  selected_data = dna[count_list.index(max(count_list))]
  s += selected_data
  
  for k in range(n):
    if dna_list[k][i] != selected_data:
      hamming_distance += 1

print(s)
print(hamming_distance)