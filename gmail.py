r,y,z=0,0,0
email= input("Enter your Email :")
if len(email)>=10: # email length is >=6 for example a@gmail.com
    if email[0].isalpha(): # this condition cheack no start any digit 
        if("@" in email)and (email.count("@")==1): # this condition  cheack "@" usee only one time
            if (email[-4]==".") ^ (email[-3]=="."): # for cheack "." use only  index no -4 or -3
                for a in email:# this loop cheack  any space & Upper case & spacel charector in email 
                    if a==a.isspace():
                        r=1
                    elif a.isalpha():
                        if a==a.upper():
                            y=1
                    elif a.isdigit():
                        continue
                    elif a=="_"or a=="@" or a==".":
                        continue
                    else:
                        z==1
                if r==1 or y==1 or z==1:
                    print("wrong email please cheack")
            else:
                print("wrong email only use one @ at a time")
        else:
            print(" Wrong Email3")
    else:
        print("wrong Email2")

else:
    print("wrong Email1")
    