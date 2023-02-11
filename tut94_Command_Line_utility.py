import argparse
import sys

def calc(args):
    if args.o=='add':
        return args.x + args.y
    elif args.o=='mul':
        return args.x * args.y
    elif args.o=='div':
        return args.x / args.y
    elif args.o=='sub':
        return args.x - args.y
    else:
        return "somthing wrong"

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=1.0,help="ENter First Number. This is a utility for calculation, please contact harry bhai")
    parser.add_argument('--y', type=float, default=3.0,help="Enter Second number This is a utility for calculation, please contact harry bhai")
    parser.add_argument('--o', type=str, default="add", help="This is a utility for calculation, please contact harry bhai")

    args=parser.parse_args()
    sys.stdout.write(str(calc(args)))  ## standard out put

