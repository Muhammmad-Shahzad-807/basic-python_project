import os
folder_name="myproject"
if not os.path.exists (folder_name):
    os.mkdir(folder_name)
    print(f"folder '{folder_name}'created")
else: 
   print("already exist")

with open ("test.txt", "w") as f:
    print("biryani","pen","burger")
    item=(input("enter your list"))
    item=item.split()

   #
new_list=[]
for x in item:
    new_list.append(x)
 
    item=new_list
    
    print(type(item))
item_price={
   " burger":250,
    "biryani":300,
    "pen":20,
    "rough_cppy":500

}
sum=0
saved_file=[]
for x in item:
    saved_file.append(x)
    sum+=item_price[x]
    print(f"your total bill is {sum}")

          