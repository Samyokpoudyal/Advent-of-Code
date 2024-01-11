#opening the file to read data 
with open (r"C:\Users\acer\Desktop\AOC\day1 datas.txt" , 'r') as read:
    read=read.readlines()

list_of_numbers=['0','1','2','3','4','5','6','7','8','9']

sum=0
#main logic of the program
for letter in read:
    list=[]
    for alp in letter:
        
        if alp  in list_of_numbers:
           list.append(alp)

      
    
    num=list[0]+list[(len(list)-1)]
    print(list)
    print(num)
    sum=sum+int(num)
    
        
print(sum)


    
           
           
    
    