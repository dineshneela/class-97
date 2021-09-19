intro= input("enter your introduction: ")
charectercount=0
wordcount=1
for charecter in intro:
    charectercount=charectercount+1
    if(charecter==' '):
        wordcount=wordcount+1
print("number of words in the string are: ")
print(wordcount)
print("number of charecters in the string are: ")
print(charectercount)
