#reading a file:-

#print("hello")
#t=open('text','r')
#print(t.read())
#t.close()


#writing a data into file:-

#t=open('text','w')
#t.write('raman')
#t.close()


#writelines:-

#t=open('text','w')
#t.writelines(['paramjeet\n','rupinder\n','paramveer\n','raman\n','parneet'])
#t.close()


#to check the file is readable or not:-

#t=open('text','r')
#print(t.readable())
#print(t.read())
#t.close()


#using of append:-

#t=open('text','a+')
#t.write('\nare siblings')
#print(t)


#read+write:-

#t=open('extra','w+')
#t.write('raman')
#print(t.read())


#readline:-

t=open('text','r')
l=t.readlines()
for x  in l:
    print(x)