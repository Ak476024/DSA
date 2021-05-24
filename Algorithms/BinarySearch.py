# Find the mid of array
# Check if the that's the element
# If element is less than mid then l=0; right=mid-1
# if element is greater than mid then l= mid+1;


class BinarySearch:

  def exists(self,arr,ele,left,right):
    if right>=left:
      mid =(left+right)//2
      print (mid)
      if (arr[mid] == ele):
        return True
      if(arr[mid]<ele):
        return self.exists(arr,ele,mid+1,right)
      if(arr[mid]>ele):
        return self.exists(arr,ele,left,mid-1)
    else:
      print("number doesn't exists")
      return False

arr=[1,2,5,9,33,66,99,100]
print(BinarySearch().exists(arr,3,0,len(arr)-1))