import requests,os,asyncio
from time import sleep
R = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
P = '\u001b[35m'
Y = '\033[1;33m'
W = "\033[0m"
logo1= G+f'''
         @@@  @@@ @@@  @@@ @@@  @@@ 
         @@!  @@@ @@!  !@@ @@!  @@@ 
         @!@  !@!  !@@!@!  @!@  !@!
'''
logo2= R+f'''
         !!:  !!!  !: :!!  !!:  !!! 
          :.:: :  :::  :::  :.:: :
          
       {Y}  [+] {G}Scripte : TikPlus
       {Y}  [+] {G}Creator : UxU_dz

'''
async def login_oauth(phone,s):
        print(Y+'➥ '+W+f"Loging To {phone}")
        
        url1 ="http://93.115.79.8:8091/api/user/create"
        headers1 = {'Accept':'*/*',
            'user-agent':'Dart/2.9 (dart:io)',
            'content-type':'application/x-www-form-urlencoded; charset=utf-8',
            'Content-Length':'52'}
        data1 = {'country_code':'+213',
            'phone':phone,
            'platform':'android'}
        r = s.post(url1,headers=headers1,data=data1)
        c = str(r.headers)
       
        url2 = "http://93.115.79.8:8091/oauth/token"
        headers2 = {'Accept':'*/*',
        'user-agent':'Dart/2.9 (dart:io)',
        'content-type':'application/x-www-form-urlencoded; charset=utf-8',
        'Content-Length':'133'}
        data2 = 'client_id=8&client_secret=+o96RSCtoN1Ltw9iDegqjCyB37xXQtv7pO1qRcMte&grant_type=password&username='+phone+'&password=mLikeUser0O%2A%2A'
        r = s.post(url2,headers=headers2,data=data2)
        tk = 'Bearer '+ r.json()["access_token"]
        return tk
async def get_credit(tk,s) :
        url = "http://93.115.79.8:8091/api/user/credit/get/all"
        headers = {'Accept':'*/*',
    'user-agent':'Dart/2.9 (dart:io)',
    'authorization':str(tk),
    'Content-Length':'0',
    'Content-Type':'application/x-www-form-urlencoded'}
        r = s.post(url,headers=headers)
        credit =r.json()["credit"]
        print(Y+'➥ '+W+'credit :'+str(credit))
        return int(credit)    
async def set_credit(tk,s) :
        url = "http://93.115.79.8:8091/api/user/credit/set/ads"
        headers = {'Accept':'*/*',
    'user-agent':'Dart/2.9 (dart:io)',
    'authorization':str(tk),
    'Content-Length':'0',
    'Content-Type':'application/x-www-form-urlencoded'}
        r = s.post(url,headers=headers).json()
        if int(r["status"]) == 200 :
            credit =r["credit"]
            print(G+'[☑️] Successful claim'+W+':\n  ➽ coin :'+str(credit))
            return int(credit)
        elif int(r["status"]) ==412 :
            print(R+'[x] Fail claim')
            return 0
        else :
            print('Error claim')
            return 0
async def tikplus(phone) :
    with requests.Session() as s :
        token =await login_oauth(phone,s)
        Update=await get_credit(token,s)+await set_credit(token,s)
        print(Y+'➥ '+G+'Update credit :'+W+str(Update))
#--------------- this claim coins---------------------        
async def select_claim() :
    while True :
        phone=779759835 
        try :
            for i in range(100): 
                os.system('cls')
                try :
                    await tikplus(str(phone))
                    sleep(2)
                except :
                    try :
                        print('Wait to server ...')
                        sleep(10)
                        await tikplus(str(phone))
                    except :
                        continue
                phone+=1
        except :
            print('KeyError')
            sleep(30)

#----------------this set order-----------------------------------
async def Get_Order() :
    phone=str(input("phone :"))
    with requests.Session() as s :
        token =await login_oauth(phone,s)
        print(await get_credit(token,s))
        url = 'http://93.115.79.8:8091/api/categories/get/all/en'
        headers = {
            'accept-encoding':'gzip',
            'user-agent':'Dart/2.9 (dart:io)',
            'authorization':str(token),
            'host':'93.115.79.8:8091'
            }
        r=s.post(url,headers=headers)
        #print(r.json())  
        print(f'''
        [x]choose :
            [1] instagram
            [2] twitter
            [3] tiktok
            [4] youtube
            [5] facebook
        ''')
        choice=(int(input("Your choice :")))
        id=r.json()['categories'][choice-1]['id']
        url=f"http://93.115.79.8:8091/api/services/get/{id}"
        r=s.post(url,headers=headers).json()
        # print(r.json())  
        #print(r)
        services=r['services']
        print('[x]choose :')
        ch=1;
        for i in services :
            choose=i['name']
            print(f"\t[{ch}] {choose}")
            ch+=1
        choice=(int(input("Your choice :")))
        print(f"[+] {services[choice-1]['name']} :")
        id=services[choice-1]['id']
        url=f"http://93.115.79.8:8091/api/services/pieces/get/{id}"
        r=s.post(url,headers=headers).json()
        #print(r)
        services=r['pieces']
        ch=1
        for i in services :
            choose=i['piece']
            choos=i['credit']
            print(f"\t[{ch}] Order {choose} with {choos} credit ")
            ch+=1
        choice=(int(input("Your choice :")))
        id=services[choice-1]['id']
        print(id)
        link=input('URL :')
        #link=(urllib.parse.quote(input('URL :'), safe=""))
        url="http://93.115.79.8:8091/api/order/take"
        data = {'piece_id':str(id),
                'link':str(link)}
        r=s.post(url,headers=headers,data=data).text
        print(r)
        if "200" in r :
            print(f"[☑️] Successful Order {services[choice-1]['piece']} ")
        elif '666' in r :
            print('less credit')
        else :
            print("Fail connection  ")
            
asyncio.run(Get_Order())
