                  
def main() : 
    BatchName = ["PPA" , "Python" , "LB" , "Angular" , "LSP" , "C#"]
    BatchFees = [18500 , 18700 , 19000 , 19200 , 18200 , 21000]          

    for i in range (len(BatchName)):
        print("Batch Name  : " , BatchName[i])
        print("Batch Fees  : " , BatchFees[i])
        print()


    BatchDetails = {
        "BatchName" : "BatchValue",
        "Python"   : "18500" ,
        "c++"   : "128500" ,
        "C"   : "183500" ,
        "Angular"   : "184500" 
    }
         
    for i in range (len(BatchDetails)):
        print(BatchDetails)
    print()
    print("Only Batches")

    for i in BatchDetails :
        print(i)
    print()
    print("Only Values")



    for i in BatchDetails :
        print(BatchDetails[i])
    print()
    print("Both")


    for i in BatchDetails :
        print(i ,BatchDetails[i])
    print()
    print("Both")

    # print(type(BatchDetails) ,    BatchDetails )
         
         
if (__name__ == "__main__"):
    main()