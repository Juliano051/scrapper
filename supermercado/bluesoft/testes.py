import os

newpath = './temp/'
if not os.path.exists(newpath):
    os.makedirs(newpath)

else:
    print("Pasta ja existe")
