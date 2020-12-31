MAX_CAFFE = 5
sum_caffe = 0
needed_caffe = 0

while True:
    line = input()
    if line == 'END':
        break
    if line.isupper():
        needed_caffe = 2
    else:
        needed_caffe = 1

    if line == 'coding' or line == 'CODING':
        sum_caffe += needed_caffe
    elif line == 'dog' or line == 'DOG' or line == 'cat' or line == 'CAT':
        sum_caffe += needed_caffe
    elif line == 'movie' or line == 'MOVIE':
        sum_caffe += needed_caffe
    else:
        sum_caffe += 0

    if sum_caffe > MAX_CAFFE:
        print('You need extra sleep')
        break
if sum_caffe <= MAX_CAFFE:
    print(sum_caffe)
