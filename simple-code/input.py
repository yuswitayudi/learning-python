from datetime import datetime


tahun = input("When you year born? ")

umur = datetime.today().year - int(tahun)
hobi = input("What are you looking for? ")
print("So your age is " + str(umur)+" and you hobby is " + hobi)