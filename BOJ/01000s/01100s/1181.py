########### 실패한 풀이 ###########
# words = int(input()) # 단어 갯수
# lst = [] # 리스트

# for i in range(words):
#     lst.append(input()) # 단어를 받아서 리스트에 저장

# #sort로도 문자열 정렬이 가능
# lst.sort() # 알파벳 순서대로 정렬
# lst.sort(key = len) #문자열 길이 순으로 정렬

# for i in lst:
#     print(i)

########### 실패한 풀이 ###########
# 중복 제거를 안했기 때문
words = int(input()) # 단어 갯수
lst = [] # 리스트

for i in range(words):
    lst.append(input()) # 단어를 받아서 리스트에 저장

#sort로도 문자열 정렬이 가능
set_lst = set(lst)
lst = list(set_lst)
lst.sort() # 알파벳 순서대로 정렬
lst.sort(key = len) #문자열 길이 순으로 정렬

for i in lst:
    print(i)