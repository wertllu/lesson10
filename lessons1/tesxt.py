
# from asyncore import read, write

# # w - write
# # r - read

with open('lessons1/test.txt','r') as f:
    for i in f: 
       print(i)
    # f.write

with open('test2.txt','w') as f:
    f.write('qwerty')