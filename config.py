import pyrebase
#configuration
databaseurl=input("[-] Enter database url        : ")
apikey=     input("[-] Enter API KEY             : ")
projectid=  input("[-] Enter Project ID          : ")
authdomain=projectid+".firebaseapp.com"
storagebucket=input("[-] Enter Storage Bucket url  : ")
appid=      input("[-] Enter App ID              : ")

#connection
firebaseConfig = {
  'apiKey': apikey,
  'authDomain': authdomain,
  'databaseURL': databaseurl,
  'projectId': projectid,
  'storageBucket': storagebucket,
  'appId': appid
}

firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()
auth=firebase.auth()
media=firebase.storage()
