import sys 
import os 
import shutil, errno 


#compress text file, remove whitespaces
def compress_file(filename): 
    fin=open(filename, 'rb') 
    fout=open('temporary', 'wb') 
    s=fin.read() 
    fout.write(b" ".join(s.split()))
    os.remove(filename) 
    os.rename('temporary', filename) 

#recursively walk all subdirectories and compress all files
def do_job(dirname):
    try:
        shutil.copytree(sys.argv[1], sys.argv[2])
    except OSError as exc: 
        if exc.errno == errno.ENOTDIR:
            shutil.copy(sys.argv[1], sys.argv[2])
        else: 
            print('Directory not copied. Error: %s' % exc)
    file_list=[]
    for root, dirs, files in os.walk(sys.argv[2]): 
       for name in files:
        file_list.append(os.path.join(root, name))   
    for x in file_list:
       compress_file(x)
        
def main(): 
     if len(sys.argv)<2:
        print("Directory or file name required!\n")
        return
     else:
         if os.path.isdir(sys.argv[1]):
            if len(sys.argv)<3:
                print("Destination directory name required!\n")
                return
            else :
                do_job(sys.argv[1])
         elif os.path.isfile(sys.argv[1]):
            compress_file(sys.argv[1])
         else:
            print (sys.argv[1]+" was not found in the specified path\n")
     

if __name__ =='__main__': 
            main()
