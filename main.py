import os

a = """
enter the number of the action you want to do:
1 - erase all datas of the key
2 - saturate the key
3 - change disk
"""

inputedByUsrdisk = str(input("enter the letter (D:?) of the key: "))
if ":" in inputedByUsrdisk:
    disk = inputedByUsrdisk
else:
    disk = inputedByUsrdisk + ":"

def run():
    print("")
    global disk   
    print("chosen disk: " + disk)
    print(a)
    b = str(input("action to realise: "))
    
    if "1" in b:
        c = str(input("do you really want to do this action ? [Y, N]"))
        if "Y" in c:
            os.system(f"format {disk} /FS:exFAT /Q")
            print("SUCCESSFUL OPERATION")
        else:
            print("SUCCESSFULY CANCELED OPERATION")
    elif "2" in b:
        c = str(input("do you really want to do this action ? [Y, N]"))
        if "Y" in c:
            os.system(f"cipher /w:{disk}:\\")
            print("SUCCESSFUL OPERATION")
        else:
            print("SUUCCESSFULY CANCELED OPERATION")
            
    elif "3" in b:
        inputedByUsrdisk = str(input("enter the new drive letter: "))
        if ":" in inputedByUsrdisk:
            disk = inputedByUsrdisk
        else:
            disk = inputedByUsrdisk + ":"
        run()
        
run()
