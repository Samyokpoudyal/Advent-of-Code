

#opening the file to read data 
with open (r"C:\Users\acer\Desktop\AOC\sample.txt.txt",'r') as read:
    read=read.readlines()

#main logic of the program

nested_list=[
    ['one','two','three','four','five','six','seven','eight','nine'],
    ['1','2','3','4','5','6','7','8','9']
]

def convert(string):
    if ('one' in string):
        return '1'
    elif ('two' in string):
        return '2'
    elif ('three' in string):
        return '3'
    elif ('four' in string):
        return '4'
    elif ('five' in string):
        return '5'
    elif ('six' in string):
        return '6'
    elif ('seven' in string):
        return '7'
    elif ('eight' in string):
        return '8'
    elif ('nine' in string):
        return '9'


new_list=[]

sum_of_numbers=''
total_sum=0
for letter in read:
    letters=''
    appended_list=[]
    
    for alp in letter:
        
        letters=letters+alp
        
        for ali in nested_list[0]:
           
            if  ali in letters : 
                appended_list.append(ali)
                letters=''
        

        for al in nested_list[1]:   
            if al in letters:
                appended_list.append(al)
                letters=''
    print(letter)
    
    for alphabet in nested_list[0]:
        for al in appended_list:
            if al == alphabet:
                poing_value=appended_list.index(alphabet)
                l=convert(alphabet)
                appended_list[poing_value]=l
            
            
            
    print(appended_list)

    new_list=appended_list[0]+appended_list[len(appended_list)-1]
    l=''
    new_list=list(new_list)
    print(new_list)
    for k in new_list:
        l=l+k
        
    total_sum=total_sum+int(l)  
    
    print(total_sum)
    
        
        
        