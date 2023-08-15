def binary_search(list,element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start<=end):
        print("Step",steps,":",str(list[start:end+1]))

        steps+=1
        middle =(start+end)//2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle-1
        else:
            start=middle+1
    return -1

my_list =[]
for i in range(200):
    my_list.insert(-1,i)
my_list


my_list =(1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20)
target = int(input("Enter the number to search :"))
binary_search(my_list,target)


