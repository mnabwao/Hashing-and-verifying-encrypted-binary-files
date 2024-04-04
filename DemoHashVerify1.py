#import cryptography library
from cryptography.hazmat.primitives import hashes
# importing os module
import os

def main():

  # gives the path of demo.py
  # path = os.path.realpath(__file__)
  # # gives the directory where demo.py
  # # exists
  # dir = os.path.dirname(path)

  os.chdir('RandomBinaryFiles')
  # Confirm the current directory
  directory = os.getcwd()

  # print('Current Working Directory is: ', os.getcwd())

  index = 0 
#   read the file with hashed content   
  arr=readHashedFile()
  
  # iterate over files in
  # that directory
  for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # index += 1
    # checking if it is a file
    if os.path.isfile(f):
        # print(f)
        # opening bin file which is to read
        binFile = open(f,"rb")
          
        # reading data from file.txt and storing
        # it in data
        readBinFile = binFile.read()
          
        # printing data
        # print(index) 

        # call all the three methods and pass data
       
        sha256file=cryptSHA256(readBinFile)
        # print("encrypted from sha256 " + str(sha256file)) 
        SHA3_224file=cryptSHA3_224(readBinFile) 
        # print("encrypted from sha3_224 " + str(SHA3_224file)) 
        md5file=cryptMD5(readBinFile)
        # print("encrypted from md5 " + str(md5file)) 
        
       

        for x in arr:
          # with open('File-hashes.txt', 'a') as f:
          #   f.write("File-"+str(index)+ ", "+sha256file +", " +SHA3_224file+", " +md5file+ '\n')
          # print("hashed values "+x[:-1])
          # print("sha256 values "+sha256file)
          # print("sha 224 values "+SHA3_224file)
          # print("md5 values "+md5file)
          # print("....................................//")
        #  for i in x:
        # #   print(i)  
        # //check length of the strings
         if len(x[:-1])==len(str(sha256file)):
          # check for sha256
            if str(x[:-1]) == str(sha256file):
                print('Success sha256')
            else:
              print("Corrupted sha256 is "+ x[:-1])


         if len(x[:-1])==len(str(SHA3_224file)): 
                # check for SHA#_224
              if str(x[:-1])==  str(SHA3_224file) :
                print('Success  SHA3_224')
              else:
               print("Corrupted SHA3_224 is "+ x[:-1])

         if len(x[:-1])==len(str(md5file)): 
              #check for md5   
              if str(x[:-1])==  str(md5file) :
                print('Success md5')
              else:
               print("Corrupted md5 is "+ x[:-1])
         
        
  
             


def  cryptSHA256(data):
    digest = hashes.Hash(hashes.SHA256())

    digest.update(data)

    c =digest.finalize()

    return str(c)

def  cryptSHA3_224(data):
  digest = hashes.Hash(hashes.SHA224())

  digest.update(data)

  c =digest.finalize()

  return str(c)


def  cryptMD5(data):
  digest = hashes.Hash(hashes.MD5())

  digest.update(data)

  c =digest.finalize()
 
  return str(c)

def readHashedFile():
    os.chdir('../HashedValues')
    # print('Current Working Directory is: ', os.getcwd())
    # opening file.txt which is to read
    f = open('hashed.txt')
    
    # reading data from file.txt and storing
    # it in data
    data = f.read()
    
    # printing data
    # print(data)

    #split string by ,
    splits = data.split(' ')

    # print(list2)

    return splits
         

main() 


