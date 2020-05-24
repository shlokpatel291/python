try:
    f= open("fileabc.txt",'r')
    print(f.read())
    f.close()
   
except IOError:
    print("file not found")

except ZeroDivisionError:
    print("cant divide by zero")