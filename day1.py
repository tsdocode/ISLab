import array as arr

#List 
lst = [1,2,3, [3,4],'a']

print(lst[:])


dim2 = [
        [1,2,3],
        [4,5,6]
        ]

print(dim2[1])


#Array
_arr = arr.array('l', [1,2,3])

print(type(_arr))

#Set
tp = set([1,2,2,3,4])

print(tp)


#Dictionary

_dict = {
        'mot' : 1,
        'hai' : 2
        }



print(_dict['hai']
)




i = 0 
for i in range(10):
        if (i == 3): continue
        print(i)
        
    
    
# str = "String ne"


for x in range(9, 0, -1):
    print(x, end = ' ')