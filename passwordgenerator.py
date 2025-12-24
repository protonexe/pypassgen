import random
import pyperclip
if __name__=="__main__":
    z="y"
    x=0
    def strength(length,sc,mode):
        if mode==1:
            if length<=10 or sc==1:
                return "WEAK strength"
            elif 10<=length<12 and sc==2:
                return'MEDIUM strength' 
            elif length>=12 and sc>=3:
                return"STRONG strength"
            else:
                return "WEAK strength"
        elif mode==2:
            if length<=5:
                return"WEAK strength"
            elif 6<=length<8:
                return'MEDIUM strength'
            elif length>=8:
                return"STRONG strength"

            
    while z=="y":
        ch=int(input("Random Character Mode(1) or Passphrase Mode (2):"))
        if ch==1:
            try:
                np=int(input("No of passwords to generate:"))
                lim=int(input("Enter Limit:"))

            except ValueError:
                print("Invalid Input(s)! Using defaults")
                lim=10
                np=2
            if lim<8:
                print('For security purposes, minimum length is 8. Defaulting to 8.')
                lim=8
            elif lim>100:
                print("Value too big! Defaulting to 10.")
                lim=10
            up=input("Include Uppercase? (y/n)")
            lo=input("Include Lowercase (y/n)")
            no=input("Include Numbers? (y/n)")
            sy=input("Include Symbols? (y/n)")
            sc=0
            pool=""
            pwd=[]
            if up=='y':
                pool+="ABCDEFGHIJKLMNOPQRTSUVWXYZ"
                sc+=1
            if no=='y':
                pool+="0123456789"
                sc+=1
            if lo=='y':
                pool+="abcdefghijklmnopqrtsuvwxyz"
                sc+=1
            if sy=='y':
                pool+="[];'./,<>?:}!@#$%^&*()_+-="
                sc+=1
            if pool=="":
                print("No characters selected! Using default values")
                pool="abcdefgh"
            with open("vault.txt" ,"a") as f:
                for q in range(np):
                    if up=='y':
                        pwd.append(random.choice("ABCDEFGHIJKLMNOPQRTSUVWXYZ"))
                    if no=='y':
                        pwd.append(random.choice("0123456789"))
                    if lo=='y':
                        pwd.append(random.choice("abcdefghijklmnopqrtsuvwxyz"))
                    if sy=='y':
                        pwd.append(random.choice("[];'./,<>?:}!@#$%^&*()_+-="))
                    while len(pwd)!=lim:
                        pwd.append(random.choice(pool))
                    random.shuffle(pwd)
                    final_pwd="".join(pwd)
                    label =strength(len(pwd), sc, ch)
                    print(f'{final_pwd:<30} | {label}')
                    pyperclip.copy(final_pwd)
                    x+=1
                    f.write("Password No "+str(x)+"- "+final_pwd+" ("+label+")"+"\n")
                    pwd=[]
        if ch==2:
            sc=0
            st=["cheese","clap","happy","never","always","laughter","funny","passenger","freedom","submarine","tissue","cake","mouse","bottle"]
            pwd=[]
            try:
                np=int(input("No of passwords to generate:"))
                lim=int(input("Enter number of words:"))

            except ValueError:
                print("Invalid Input(s)! Using defaults")
                lim=5
                np=2
            if lim<4:
                print('For security purposes, minimum length is 4. Defaulting to 4.')
                lim=4
            elif lim>10:
                print("Value too big! Defaulting to 5.")
                lim=5
            with open("vault.txt","a") as f:
                for q in range(np):
                    for i in range(lim):
                        pwd.append(random.choice(st))     
                    random.shuffle(pwd)
                    final_pwd="-".join(pwd)
                    label=strength(len(pwd),sc,ch)
                    print(f'{final_pwd:<40} | {label}')
                    x+=1
                    f.write("Password No "+str(x)+"- "+final_pwd+" ("+label+")"+"\n")
                    pyperclip.copy(final_pwd)
                    pwd=[]  
        z=input("Continue? (y/n)")

