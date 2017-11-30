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
            self.text=datas
        else:
            print "The existing file is not txt or html"
            issuccess=False   
        return datas,issuccess
    
    def split_file(self,datas):
        issuccess = True
        try:
            htmlText=re.sub(r'<!.+-->',"",datas)
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
                            groupofvalues.append(keyvalue[1])
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
                                    groupofvalues.append(keyvalue[1])
                                else:
                                    groupoftags.append(words[0])
                    else:
                        pass
            groupoftags=list(set(groupoftags))
            self.groupoftags=groupoftags
            self.groupofkeys=groupofkeys
            self.groupofvalues=groupofvalues
        except Exception as exception:
            issuccess=False 
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
        return groupoftags,groupofkeys,groupofvalues,issuccess
                 
    def display(self,tags,keys,values):
        issuccess = True
        try:
            prompt=int(raw_input("""Enter 1.For tags,
  2.For keys,
  3.For values,
  4.For search values of corresponding key\n"""))
            if prompt==1:
                for tag in tags:
                    print tag
                self.display(tags,keys,values)   

            elif prompt==2:
                for key in keys:
                    print key
                self.display(tags,keys,values)   
            elif prompt==3:
                if len(keys)==len(values):
                    for count in range(0,len(keys)):
                        print keys[count],"=",values[count]
                    self.display(tags,keys,values)
            elif prompt==4:
                inputKey=raw_input("Enter key:")
                if inputKey in keys:
                    resultIndex=keys.index(inputKey)
                    print keys[resultIndex],"=",values[resultIndex]
                    
                else:
                    print "Enter the correct key"
                    self.display(tags,keys,values)
        except Exception as exception:
            issuccess=False 
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
        return issuccess
        
start = datetime.datetime.now()    
if __name__=='__main__':
    if len(sys.argv)>1:
        code=htmlTags()
        datas,check=code.check_file(sys.argv[1])
        if check:
            tags,keys,values,check=code.split_file(datas)
            if check:
                code.display(tags,keys,values)
finish = datetime.datetime.now()
print finish-start
