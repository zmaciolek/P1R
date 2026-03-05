from collections import Counter
import sys

args = sys.argv[1:]
temp = 0

def most_frequent(args):
    print(args)
    args=args.replace(" ","")
    temp = Counter(args).most_common(1)
    
    print(temp)
    
    
most_frequent(input("Podaj liste: "))

