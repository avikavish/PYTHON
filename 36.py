
#WAP  to print the recurcive function to print all element in a list
#hint:use list & index as parameter


def printlist(list,index=0):
    if(index == len(list)):
        return
    printlist(list,index+1)
    print(list[index])

cities =["jabalpur","bhopal" ,"indore"]
printlist(cities)
