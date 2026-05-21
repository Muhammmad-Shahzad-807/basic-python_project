import os
from datetime import date
file="claude_project.txt"
def your_daily_session():
    topics=input("what did you learn today")
    hour=input("how much you studied")
    today=date.today()
#
    with open(file,"a") as f:
      f.write(f"{topics}|{today}|{hour}hrs\n")

def view_all_session():
     if not os.path.exists(file):
        print("No sessions logged yet.\n")
        return

     with open(file,"r") as f:
      line=f.readlines()
      for i in line:
        print(" -", i.strip())
def  total_hour():
   if not os.path.exists(file):
       print("data not found")
    
   with open (file,"r") as f:
    total_hour=0
    for lines in f:
     parts = lines.strip().split("|")
     if len(parts)==3:
      hrs=lines[2].replace("hrs","").split()
      total_hour+=float(hrs)


   
while True  :
  print("choose 1 for your input:")
  print("choose 2 for your view: ")
  print("choose 3 foryour total: ")
  print("choose 4 foryour total: ")
  print("choose 5 foryour total: ")
  choice = input("Choose an option (1-4): ")
  if choice=="1":
    your_daily_session()
  elif choice=="2":
     view_all_session()
  elif choice=="3":
    total_hour()
  elif choice=="4":
    break
  else:
    print("choose between 1 and 4")


                      