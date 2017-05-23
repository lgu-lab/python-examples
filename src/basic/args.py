import sys

# 2 def same name : no error

def args():
    print ( "arguments :" , sys.argv )
    print ( "arguments count = ", len(sys.argv))
    for idx, arg in enumerate(sys.argv) :
        print(" . ", idx, "arg = ", arg)
    print("end of loop : idx = ", idx)

#def args():
#    print ( "Override the previous fonction (no error in execution)" )

def main():
    print ( "arguments :" , sys.argv )
    print ( "arguments count = ", len(sys.argv))
    for arg in sys.argv :
        print("arg = ", arg)

    # call args
    args()

if __name__ == '__main__':
    main()
