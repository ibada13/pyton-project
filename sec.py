


name = input("enter your name : ")
find =False
pos = None



with open("start.txt","r") as e :
        ar = e.read().split(" ")
        x = len(ar)
for i in range(x):
    if(name == ar[i] ): 
        find = True
        pos = i+1
        break


if find : 
     print("the name exist in the file the postion of your name is ",pos)
else :##i>x
        add = input("\n 1 - if you want to add the mame to the list enter 1 \n 2 - else enter  anything else 1 \n");
        if(add=="1"): 
             with open("start.txt","a") as e :
                   e.write(" "+name)
                   e.close()
                   print("done adding")
        else:
             print("done")    
              
