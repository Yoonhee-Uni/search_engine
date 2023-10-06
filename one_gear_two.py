import os

# article={'wan':2,
#          'two':2,
#          'three':2,
#          'foor':2}

# inpspts =['wan','two','three','foor','five', 'six']

# result= {}

# x=0

# for inpspt in inpspts:
#     if inpspt in article.keys():
#         result[inpspt] = article[inpspt]
# print([result])    

# def search_box():
#     extract_line =[]
#     counts={}
#     inp=input('What do you want to know: ' )
#     inpspts= inp.split()

#     fhand = open('src/1.txt', 'r')
#     for line in fhand:
#         line = line.rstrip()
#         # print('this',line)
#         counts[line] = counts.get(line,0)+1
#     print(counts)    

    

# search_box()

# file_name = '1.txt'
# searches = ['the','world','champion']
# x = 'the world best champion is our world star player Uni'
# articles = x.split()
# dic= {}

# for search in searches:
#     if search in articles:
#         if file_name not in dic:
#             dic[file_name]= {}
#         dic[file_name][search] = dic[file_name].get(search,0)+1
# print(dic)    

s=[1,1,1,1,2,2,2,3,3,3,]
x=[1,2]
for xs in x:
    while xs in s:
        s.remove(xs)
print(s)