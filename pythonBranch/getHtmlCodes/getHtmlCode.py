import datetime
import sys
import re


class htmlTags:
    def check_file(self,htmlCodes):
        issuccess=True
        datas=""
        if htmlCodes.endswith('.html'):
            txt=open(htmlCodes,'r')
            datas=txt.read()
        else:
            print "The existing file is not html file"
            issuccess=False   
        return datas,issuccess
    def remove_comment_line(self,datas):
        issuccess = True
        try:
            htmlText=re.sub(r'<!.+-->',"",datas)
        except Exception as exception:
            issuccess=False 
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return issuccess,htmlText
    
    def split_file(self,htmlText):
        issuccess = True
        try:
            groupoftags=[]
            groupofkeys=[]
            groupofvalues=[]
            for line in htmlText.splitlines():
                if " " in line:
                    words=line.split(" ")
                    words=filter(None, words)
                    word=words[0]
                    tag=word[1:]
                    groupoftags.append(tag)
                    for index in range(1,len(words)):
                        checkword=words[index]
                        if "=" in checkword:
                            keyvalue=checkword.split("=")
                            groupofkeys.append(keyvalue[0])
                            value = keyvalue[1].translate(None, '/">"')
                            groupofvalues.append(value)
                        else:
                            pass
                else:
                    if "<" in line and ">" in line:
                        words=re.findall(r'[\w]+',line)
                        if len(words)==1:
                            word=words[0] 
                            groupoftags.append(word)
                        elif len(words)>1:
                            for index in range(0,len(words)):
                                if "=" in words[index]:
                                    word=words[index]
                                    keyvalue=text.split("=")
                                    groupofkeys.append(keyvalue[0])
                                    value = keyvalue[1].translate(None, '/">"')
                                    groupofvalues.append(value[1])
                                else:
                                    groupoftags.append(words[0])
                    else:
                        pass
            groupoftags=list(set(groupoftags))
        except Exception as exception:
            issuccess=False 
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return groupoftags,groupofkeys,groupofvalues,issuccess
                 
    def display(self,tags,keys,values):
        issuccess = True
        try:
            prompt=1
            while prompt<=4:
                if prompt==1:
                    print "Tags in html file:"
                    for tag in tags:
                        print tag  

                elif prompt==2:
                    print "Keys in html file:"
                    for key in keys:
                        print key   
                elif prompt==3:
                    if len(keys)==len(values):
                        print "Values with corressponding key:"
                        for count in range(0,len(keys)):
                            print keys[count],"=",values[count]
                else:
                    if prompt==4:
                        inputKey=raw_input("Enter key:")
                        if inputKey in keys:
                            resultIndex=keys.index(inputKey)
                            print keys[resultIndex],"=",values[resultIndex]
                        else:
                            print "Enter the correct key to know the value:"
                prompt+=1            
        except Exception as exception:
            issuccess=False 
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
        return issuccess
        
start = datetime.datetime.now()    
if __name__=='__main__':
    if len(sys.argv)>1:
        code=htmlTags()
        datas,check=code.check_file(sys.argv[1])
        if check:
            check,htmlText=code.remove_comment_line(datas)
            if check:
                tags,keys,values,check=code.split_file(htmlText)
                if check:
                    code.display(tags,keys,values)
finish = datetime.datetime.now()
print finish-start
