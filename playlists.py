def playlist(songs):
    # Write your code here
    count = 0
    remainder = {}
    for i in songs:
        #print("Remainder: ", remainder)
        if i %60 == 0 and 0 in remainder:
            count = count + remainder[0]
            #print(count)
            #print("*****")
        elif 60 - (i%60) in remainder:
            count = count + remainder[60-(i%60)]
            #print(count)
            #print("$$$$$")
        if i%60 in remainder:
            remainder[i%60]+=1
        else:
            remainder[i%60]=1
        
    #print(remainder)
        
    return count
