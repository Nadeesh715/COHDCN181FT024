import sys
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("FILE", type=str)
args = parser.parse_args()

if len(sys.argv)==2:  #checking the number of arguments
    if os.path.isfile(sys.argv[1]): #checking the file existance
        print("HexDump of the file",  sys.argv[1])      
        try:
            with open(args.FILE, "rb") as f:
                n = 0
                b = f.read(16)

                while b:
                    s1 = " ".join([f"{i:02x}" for i in b]) # hex values
                    
                    s2 = "".join([chr(i) if 32 <= i <= 127 else "." for i in b]) # ascii values of the content and replacing nonprintable characters with dot
                
                    snew=s1.replace(" ","") #removing spaces

                    #printing the final result
                    print(f"{n * 16:08x}  {snew[0:4]} {snew[4:8]} {snew[8:12]} {snew[12:16]} {snew[16:20]} {snew[20:24]} {snew[24:28]} {snew[28:32]} {s2}")

                    n += 1
                    b = f.read(16)

        except Exception as e:
            print(__file__, ": ", type(e).__name__, " - ", e, sep="", file=sys.stderr)
    else:
        print("file not found")
else:
    print("Enter one file at a time")
