import os, time, shutil

path = input("Enter directory: ")
days = 30
secs = time.time() - (days*24*60*60)

if os.path.exists(path):
  for root, dirs, files in os.walk(path):
    
    if secs >= os.stat(root).st_ctime:
      shutil.rmtree(root)
      
    else:      
      for dirct in dirs:
        path1 = (os.path.join(root, dirct))
        
        if secs >= os.stat(path1).st_ctime:
          shutil.rmtree(path1)

      for file in files:
        path2 = (os.path.join(root, file))
        
        if secs >= os.stat(path2).st_ctime:
          shutil.rmtree(path2)
          
  print("Deleted Old Files!")
  
else:
  print("Could not find directory: " + path)
