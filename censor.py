#This is a program to censor any words a user wants to censor from a passage of text.


def censor(text,words):
    a=[]
    a.append(text)
    for i in range (0,len(words)):
        b=words[i]
        c=a[i]
        d=(c.replace(words[i],(b[0]+(len(b)-2)*'*'+b[len(b)-1])))
        a.append(d)
    return a[-1]

#Test case for this censorship program:
textinput=("it\'s a beautiful day here in Waterloo, the snow is glowing in the sunlight")
words2censor=["snow","sunlight","beautiful"]
print(censor(textinput,words2censor))