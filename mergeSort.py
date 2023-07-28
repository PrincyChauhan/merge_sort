def Merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
            
    result+=left[i:]
    result+=right[j:]  
    return result  
            
def MergeSort(list):
    if(len(list)<=1):
        return list 
    mid=int(len(list)/2)
    left=MergeSort(list[:mid]) # start from 0 to mid-1
    right=MergeSort(list[mid:]) # start from mid to end
    return Merge(left,right)

arr=[9,3,7,1,7,10,2]
print(MergeSort(arr))           
                
                    