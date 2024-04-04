#import cryptography library
from cryptography.hazmat.primitives import hashes
# importing os module
import os

def main():

  # gives the path of demohashing.py
  # path = os.path.realpath(__file__)
  # # gives the directory where demohashing.py
  # # exists
  # dir = os.path.dirname(path)

  os.chdir('RandomBinaryFiles')
  # Confirm the current directory
  directory = os.getcwd()

  print('Current Working Directory is: ', os.getcwd())

  index = 0 

  # iterate over files in
  # that directory
  for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    index += 1
    # checking if it is a file
    if os.path.isfile(f):
        # print(f)
        # opening bin file which is to read
        binFile = open(f,"rb")
          
        # reading data from file.txt and storing
        # it in data
        readBinFile = binFile.read()
        # call all the three methods and pass data
       
        sha256file=cryptSHA256(readBinFile)
        # print("encrypted from sha256 " + str(sha256file)) 
        SHA3_224file=cryptSHA3_224(readBinFile) 
        # print("encrypted from sha3_224 " + str(SHA3_224file)) 
        md5file=cryptMD5(readBinFile)
        # print("encrypted from md5 " + str(md5file)) 

        
        # move up one directory
        
        os.chdir('../HashedValues')

        # create file and add the three hashed values.

        # check index and corrupt hashes 1-5
        if index == 1 or index == 2 or index == 3 or index == 4 or index == 5:

          with open('hashed.txt', 'a') as f:

            # corrupt only md5file
            # convert md5 to string
            corruptedStr=str(md5file)
            # change swap first and last value
            swapValue=swap(corruptedStr)
            print(swapValue)
            print(md5file)
            f.write("File-"+str(index)+ ", "+swapValue +", " +SHA3_224file +", " + sha256file+ '\n')
            

        elif  index == 1 or index == 2 or index == 3 or index == 4 or index == 5:  
        
          with open('hashed.txt', 'a') as f:
            f.write("File-"+str(index)+ ", "+sha256file +", " +SHA3_224file+", " +md5file+ '\n')
           

        else:

         print("happy jamuhuri day!")



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

def swap(string):
     
    # storing the first character
    start = string[0]
     
    # storing the last character
    end = string[10]
     
    swapped_string = end + string[1:-1] + start


    return swapped_string

main() 


