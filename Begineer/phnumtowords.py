number=input("Enter you Phone number!")
words=""
for i in range(len(number)):
    if(number[i]=='1'):
        words+="One "
    elif(number[i]=='2'):
        words+="Two "
    elif(number[i]=='3'):
        words+="Three "
    elif(number[i]=='4'):
        words+="Four "
    elif(number[i]=='5'):
        words+="Five "
    elif(number[i]=='6'):
        words+="Six "
    elif(number[i]=='7'):
        words+="Seven "
    elif(number[i]=='8'):
        words+="Eight "
    elif(number[i]=='9'):
        words+="Nine "
    else:
        words+="Zero"
        
print(words)

digits={
    "1":"One ",
    "2":"Two ",
    "3":"Three ",
    "4":"Four ",
    "5":"Five ",
    "6":"Six ",
    "7":"Seven ",
    "8":"Eight ",
    "9":"Nine ",
    "0":"Zero "
}
words2=""
for ch in number:
    words2+=digits.get(ch,"!")
    
print(words2)
    
        