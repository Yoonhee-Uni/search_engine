import os

def search_box():
    counts={}
    countsall={}
    rems = ['in', 'the', 'of', 'and', 'a', 'an', 'at', 'as', 'by', 'in', 'on', 'to', 'how', 'what', 'with']

    inp=input('What do you want to know: ' )
    searches= inp.split()

    for rem in rems:
        while rem in searches:
            new_searches = searches.remove(rem)
            # print('this',new_searches)
    
    # print('your search is: ', searches)

    src_folder = 'src'
    # get all the list of files in 'src'
    file_list = os.listdir(src_folder)

    for file_name in file_list:
        file_path = os.path.join(src_folder, file_name) 
        countsall[file_name] =0
        with open(file_path, 'r') as fhand:
            for line in fhand:
                line = line.rstrip().split()
            # print(file_name, line)
            
                for search in searches:
                    if search in line:
                        countsall[file_name] += 1

                        # if file_name not in counts:
                            # counts[file_name]={}
                            # countsall[file_name] =0

                        # counts[file_name][search] = counts[file_name].get(search,0)+1
                        


    # sorted_counts= dict(sorted(counts.items()))     
    # print(sorted_counts)
    sorted_by_high_to_low = sorted(countsall.items(), key=lambda x:x[1], reverse = True)
    converted_dict = dict(sorted_by_high_to_low)
    first_key = list(converted_dict.keys())[0]
    # print('countsall',converted_dict) 
    # print('first key', first_key)

    article = open(f'src/{first_key}', 'r')
    print(article.read())

    
                


search_box()



#file name = filename
#file list = all in [3.txt, 4.txt ,1, 2]
#f=file안에 내용들

# def file_finder():   
#     counts = {}
#     src_folder = 'src'
#     #get all the list of files in 'src'
#     file_list = os.listdir(src_folder)
#     for file_name in file_list:
#         file_path = os.path.join(src_folder, file_name) 
#         fhand= open(file_path, 'r')
#         for f in fhand:
#             f= f.rstrip()
#             print(f)

# file_finder()



# def file_finder():   
#     counts = {}
#     src_folder = 'src'
#     #get all the list of files in 'src'
#     file_list = os.listdir(src_folder)
#     for file_name in file_list:
#         file_path = os.path.join(src_folder, file_name) 
#         fhand= open(file_path, 'r')
#         for f in fhand:
#             words = f.split()
#             for word in words :
#                 counts[word] =counts.get(word, 0)+1


#         print(fhand)

# file_finder()
