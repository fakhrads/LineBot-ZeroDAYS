# -*- coding: utf-8 -*-
import linepy
from linepy import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from datetime import datetime
import json, time, random, tempfile, os, sys, pytz, urllib, re, ast, string, six, requests, html5lib, urllib3, threading, traceback, atexit, codecs
from humanfriendly import format_timespan, format_size, format_number, format_length
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from urllib import parse

botStart = time.time()
#fakhri = Linefakhri()
fakhri = LineClient(authToken='EtnCCPgi9OvEaKLJ4tG0.V+uWm8q8TMmc3J2Dq76caa.qc+/doCwIXTnjGl435KeVw9im+Dy4hQ6weufg51ueIY=')
fakhri.log("Auth Token : " + str(fakhri.authToken))
channel = LineChannel(fakhri)

caca = LineClient(authToken='EtEJVlLk6DPiNT4FCTpe.o+bf5EG63+0IyFol0TRH3G.M9bVp8wKNul8q7f8RN8v1SDpqYgUE9rSlbXgVzPTY6Q=')
caca.log("Auth Token : " + str(caca.authToken))

rindu = LineClient(authToken='EtnWkHM14rwmG1ejtZef.D8V3NFiGpU1Xdw6YyUuUJW.n/5MJK+506ijZGJBOdElqpVn39jEefB8jmpQXe4Ddxg=')
rindu.log("Auth Token : " + str(rindu.authToken))


fakhriProfile = fakhri.getProfile()
fakhriSettings = fakhri.getSettings()
fakhriPoll = LinePoll(fakhri)
fakhriMID = fakhri.profile.mid
botStart = time.time()

msg_dict = {}

poll = LinePoll(fakhri)
Amid = fakhri.profile.mid
Bmid = caca.profile.mid
Cmid = rindu.profile.mid
print(Amid)
print(Bmid)
print(Cmid)

zero = [caca,rindu]
zero1 = [fakhri,rindu]
zero2 = [fakhri,caca]
creator = "ubff53033c43cb66302de3d9d43be8200"
admin = ["ubff53033c43cb66302de3d9d43be8200","uc637a4f90f922f70802b7fc9793a60b6","u96a3fdacb37ee963b1ded65be92ce14d",'u62653a9ee029cef2378d344606351333']
bots = [Amid,Bmid,Cmid,admin]

settingsOpen = codecs.open("read.json","r","utf-8")
settings = json.load(settingsOpen)

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except Exception as e:
    print(str(e))
helpsider="""
╭──「 Menu Message 」
│ Help
│ Restart
├──「 PROTECT」
│ Protect「On/Off」
│ ProtectQR 「On/Off」
│ TarikPesan 「On/Off」
│ BalasMention 「On/Off」
│ Gurl
│ CloseURL/OpenURL
│ Ban
│ Clear
│ ClearBan
│ Status
├──「 GROUP 」
│ Spict
│ Scover
│ Svideopict
│ Gantippgrup
│ Set/Cek
├──「 INFO 」
│ Creator: fakhrads
╰──────────

"""
def backupData():
    try:
        backup = settings
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
        return cmd
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                fakhri.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    fakhri.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def restart_program():
    backupData()
    python = sys.executable
    os.execl(python, python, * sys.argv)
def fakhriBot(op):
    try:
#=========================================================================================================================================#
#=========================================================================================================================================#
            if op.type == 0:
                return
            if op.type == 5:
                na = "Creator This BOT"
                nam = "Selfbot By Fakhrads"
                link = "http://line.me/ti/p/~fakhrads"
                iconlink ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWbDftD-kEKNnwISBfhwQyAVXXRu8WWedQdsGpPGnzUaTH9BdD"
                fakhri.sendMessageWithContent(op.param1,'Cie nge add saya :V',nam,link,iconlink)
            if op.type == 11:
                if settings["qrlink"] == True:
                    if op.param2 in bots:
                      pass
                    if op.param2 not in bots:
                      try:
                          G = fakhri.getGroup(op.param1)
                          G.preventedJoinByTicket = True
                          random.choice(zero).kickoutFromGroup(op.param1,[op.param2])
                          fakhri.updateGroup(G)
                          settings["blacklist"][op.param2] = True
                      except Exception as e:
                          fakhri.log('ERROR!')
                    else:
                        pass
            if op.type == 13:
              if op.param3 in settings["blacklist"]:
                  fakhri.cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(zero).kickoutFromGroup(op.param1, [op.param2])
                  fakhri.sendText(op.param1, "Blacklist Detected")
              else:
                 pass
              if mid in op.param3:
                  fakhri.acceptGroupInvitation(op.param1)
                  X = fakhri.getGroup(op.param1)
                  X.preventJoinByTicket = False
                  fakhri.updateGroup(X)
                  Ti = fakhri.reissueGroupTicket(op.param1)
                  caca.acceptGroupInvitationByTicket(op.param1,Ti)
                  G = caca.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  caca.updateGroup(G)
                  Ticket = caca.reissueGroupTicket(op.param1)
            if op.type == 19:
                print('KICKED!!!')
                if Amid in op.param3:
                    if op.param2 in bots:
                        pass
                    else:
                        random.choice(zero).kickoutFromGroup(op.param1,[op.param2])
                        if op.param2 in settings["blacklist"]:
                            pass
                        if op.param2 in settings["whitelist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = caca.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    caca.updateGroup(G)
                    Ti = caca.reissueGroupTicket(op.param1)
                    fakhri.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = fakhri.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    fakhri.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in settings["blacklist"]:
                        pass
                    if op.param2 in settings["whitelist"]:
                        pass
                    else:
                        settings["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in bots:
                        pass
                    else:
                        random.choice(zero1).kickoutFromGroup(op.param1,[op.param2])
                        if op.param2 in settings["blacklist"]:
                            pass
                        if op.param2 in settings["whitelist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    X = fakhri.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    fakhri.updateGroup(X)
                    Ti = fakhri.reissueGroupTicket(op.param1)
                    caca.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = caca.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    caca.updateGroup(G)
                    Ticket = caca.reissueGroupTicket(op.param1)
                    if op.param2 in settings["blacklist"]:
                        pass
                    if op.param2 in settings["whitelist"]:
                        pass
                    else:
                        settings["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in bots:
                        pass
                    else:
                        random.choice(zero2).kickoutFromGroup(op.param1,[op.param2])
                        if op.param2 in settings["blacklist"]:
                            pass
                        if op.param2 in settings["whitelist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    X = fakhri.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    fakhri.updateGroup(X)
                    Ti = fakhri.reissueGroupTicket(op.param1)
                    rindu.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = rindu.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    rindu.updateGroup(G)
                    Ticket = caca.reissueGroupTicket(op.param1)
                    if op.param2 in settings["blacklist"]:
                        pass
                    if op.param2 in settings["whitelist"]:
                        pass
                    else:
                        settings["blacklist"][op.param2] = True

                if op.param3 not in bots:
                  if settings["protect"] == True:
                    if op.param2 in bots:
                      pass
                    else:
                        if op.param2 not in bots:
                          try:
                              random.choice(zero).kickoutFromGroup(op.param1,[op.param2])
                              fakhri.inviteIntoGroup(op.param1,[op.param3])
                              if op.param2 in settings["blacklist"]:
                                  pass
                              if op.param2 in settings["whitelist"]:
                                  pass
                              else:
                                  settings["blacklist"][op.param2] = True
                          except Exception as e:
                              fakhri.log('ERROR : ' + str(e))
                        else:
                           pass
                  else:
                     pass
            if op.type == 26:
              if settings["tag"] == True:
                try:
                    msg = op.message
                    text = msg.text
                    msg_id = msg.id
                    receiver = msg.to
                    sender = msg._from
                    try:
                        if msg.text != None:
                          if msg.toType == 2:
                            may = fakhri.getProfile().mid
                            if may in str(msg.contentMetadata) and 'MENTION' in str(msg.contentMetadata):
                              sendMention(receiver,"Oi @!, Yang tag gw jomblo!",[sender])
                            #elif text.lower() == 'me':
                             # fakhri.sendMessage(receiver, sender)
                              #print(sender)
                          else:
                             pass
                        else:
                            pass
                    except Exception as e:
                         fakhri.log("[MASALAH] " + str(e))
                except Exception as e:
                         fakhri.log("[MASALAH] " + str(e))
            if op.type == 25:
                try:
                    print ("[ 25 ] SEND MESSAGE")
                    msg = op.message
                    text = msg.text
                    msg_id = msg.id
                    receiver = msg.to
                    sender = msg._from
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == False:
                        setKey = ''
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != fakhri.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if msg.contentType == 0:
                            if text is None:
                                return
                            else:
                                cmd = command(text)
                                if cmd == 'masuk':
                                  X = fakhri.getGroup(msg.to)
                                  X.preventedJoinByTicket = False
                                  fakhri.updateGroup(X)
                                  Ti = fakhri.reissueGroupTicket(msg.to)
                                  caca.acceptGroupInvitationByTicket(msg.to,Ti)
                                  rindu.acceptGroupInvitationByTicket(msg.to,Ti)
                                  G = caca.getGroup(msg.to)
                                  G.preventedJoinByTicket = True
                                  caca.updateGroup(G)
                                elif cmd == "speed":
                                    start = time.time()
                                    fakhri.sendMessage(to, "Speed calculating...")
                                    elapsed_time = time.time() - start
                                    fakhri.sendMessage(to, "[ Speed ]\n {} detik".format(str(elapsed_time)))
                                elif cmd == 'bot':
                                  caca.sendMessage(to,'Caca siap! :)')
                                  rindu.sendMessage(to,'Rindu juga kok!')
                                elif cmd == 'keluar':
                                  caca.leaveGroup(to)
                                  rindu.leaveGroup(to)
                                elif cmd == "qwerty":
                                    fakhri.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                                elif cmd.startswith("cname:"):
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                    if len(string) <= 20:
                                        profile = fakhri.getProfile()
                                        profile.displayName = string
                                        fakhri.updateProfile(profile)
                                        fakhri.sendMessage(to,"Berhasil mengganti display name menjadi{}".format(str(string)))
                                elif cmd.startswith("cbio:"):
                                    sep = text.split(" ")
                                    string = text.replace(sep[0] + " ","")
                                    if len(string) <= 500:
                                        profile = fakhri.getProfile()
                                        profile.statusMessage = string
                                        fakhri.updateProfile(profile)
                                        fakhri.sendMessage(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
                                elif cmd == 'closeurl':
                                  if msg.toType == 2:
                                      x = fakhri.getGroup(msg.to)
                                      if x.preventedJoinByTicket == True:
                                          x.preventedJoinByTicket = False
                                          fakhri.updateGroup(x)
                                elif cmd == 'openurl':
                                  if msg.toType == 2:
                                      x = fakhri.getGroup(msg.to)
                                      if x.preventedJoinByTicket == True:
                                          x.preventedJoinByTicket = False
                                          fakhri.updateGroup(x)
                                elif cmd == 'gurl':
                                  if msg.toType == 2:
                                      x = fakhri.getGroup(msg.to)
                                      if x.preventedJoinByTicket == True:
                                          x.preventedJoinByTicket = False
                                          fakhri.updateGroup(x)
                                          gurl = fakhri.reissueGroupTicket(msg.to)
                                          fakhri.sendText(msg.to,"Link grup:\nline://ti/g/" + gurl)
                                      else:
                                          gurl = fakhri.reissueGroupTicket(msg.to)
                                          fakhri.sendText(msg.to,"Link grup:\nline://ti/g/" + gurl)
                                elif cmd == 'help':
                                    na = "SelfBot By Fakhrads"
                                    nam = "Fakhri"
                                    link = "http://line.me/ti/p/~fakhrads"
                                    iconlink ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWbDftD-kEKNnwISBfhwQyAVXXRu8WWedQdsGpPGnzUaTH9BdD"
                                    fakhri.sendMessageWithContent(to,helpsider,nam,link,iconlink)
                                #------------------------[PROTECT]------------------------------
                                elif cmd.startswith("changekey:"):
                                    sep = text.split(" ")
                                    key = text.replace(sep[0] + " ","")
                                    if " " in key:
                                        fakhri.sendMessage(to, "Key tidak bisa menggunakan spasi")
                                    else:
                                        settings["keyCommand"] = str(key).lower()
                                        fakhri.sendMessage(to, "Berhasil mengubah key command menjadi [ {} ]".format(str(key).lower()))
                                elif cmd == 'protect on':
                                    settings["protect"] = True
                                    fakhri.sendMessage(to,'Proteksi grup dinyalakan!')
                                elif cmd == 'protect off':
                                    settings["protect"] = False
                                    fakhri.sendMessage(to,'Proteksi grup dimatikan!')
                                #------------------------[PROTECT]------------------------------
                                elif cmd == 'balasmention on':
                                    settings["tag"] = True
                                    fakhri.sendMessage(to,'Balas mention dinyalakan!')
                                elif cmd == 'balasmention off':
                                    settings["tag"] = False
                                    fakhri.sendMessage(to,'Balas mention dimatikan!')
                                #---------------------------------------------------------------
                                elif cmd == 'protectqr on':
                                    settings["qrlink"] = True
                                    fakhri.sendMessage(to,'Proteksi QR dinyalakan!')
                                elif cmd == 'protectqr off':
                                    settings["qrlink"] = False
                                    fakhri.sendMessage(to,'Proteksi QR dimatikan')
                                #---------------------------------------------------------------
                                elif cmd == 'tarikpesan on':
                                    settings["unsendMessage"] = True
                                    fakhri.sendMessage(to,'Tarik pesan dinyalakan!')
                                elif cmd == 'tarikpesan off':
                                    settings["unsendMessage"] = False
                                    fakhri.sendMessage(to,'Tarik pesan dimatikan!')
                                #---------------------------[END]------------------------------
                                elif cmd == "status":
                                    try:
                                        ret_ = "╭──「 STATUS」"
                                        if settings["protect"] == True: ret_ += "\n├[ ON ] Proteksi"
                                        else: ret_ += "\n├[ OFF ] Proteksi"
                                        if settings["qrlink"] == True: ret_ += "\n├[ ON ] Proteksi QR"
                                        else: ret_ += "\n├[ OFF ] Proteksi QR"
                                        if settings["unsendMessage"] == True: ret_ += "\n├[ ON ] Tarik Pesan"
                                        else: ret_ += "\n├[ OFF ] Tarik Pesan"
                                        if settings["tag"] == True: ret_ += "\n├[ ON ] Balas Mention"
                                        else: ret_ += "\n├[ OFF ] Balas Mention"
                                        ret_ += "\n╰──「 SETTINGS 」"
                                        fakhri.sendMessage(to, str(ret_))
                                    except Exception as e:
                                        fakhri.sendMessage(msg.to, str(e))
                                #---------------------------------------------------------------
                                elif text.lower() == 'get qr': ## HEADER CONTOH DESKTOPWIN
                                    urllib.request.urlretrieve('http://api.boteater.icu/DEKSTOPWIN', '{}.txt'.format(msg._from))
                                    with open('{}.txt'.format(msg._from), 'r') as f:
                                        qr = f.read()
                                        j = json.loads(qr)
                                        for p in j['result']:
                                            link = (p['linkqr'])
                                            f.close()
                                            boteater.sendMessage(msg.to, link)

                                elif text.lower() == 'get token':
                                    with open('{}.txt'.format(msg._from), 'r') as f:
                                        qr = f.read()
                                        j = json.loads(qr)
                                        for p in j['result']:
                                            link = (p['linktkn'])
                                            f.close()
                                            r = requests.get(link)
                                            ar = r.text
                                            boteater.sendMessage(msg.to, ar)
                                        os.system('rm {}.txt'.format(msg._from))
                                #------------------------------------------------------
                                elif cmd == 'restart':
                                    fakhri.sendMessage(to,'Sudah direstart!')
                                    restart_program()
                                elif text.lower() == "mykey":
                                    fakhri.sendMessage(to, "KeyCommand Saat ini adalah [ {} ]".format(str(settings["keyCommand"])))
                                elif text.lower() == "setkey on":
                                    settings["setKey"] = True
                                    fakhri.sendMessage(to, "Berhasil mengaktifkan setkey")
                                elif text.lower() == "setkey off":
                                    settings["setKey"] = False
                                    fakhri.sendMessage(to, "Berhasil menonaktifkan setkey")
                                elif cmd == 'banlist':
                                    if settings["blacklist"] == {}:
                                        fakhri.sendMessage(msg.to,"╭──「 BLACKLIST」\n├[NONE]\n╰──「 USERS」")
                                    else:
                                        mc = ""
                                        for mi_d in settings["blacklist"]:
                                            mc += "├[" + fakhri.getContact(mi_d).displayName + "]\n"
                                        fakhri.sendText(msg.to,"╭──「 BLACKLIST」\n"+mc+"╰──「 USERS」")

                                elif cmd.startswith("mid "):
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        ret_ = "[ Mid User ]"
                                        for ls in lists:
                                            ret_ += "\n{}".format(str(ls))
                                        fakhri.sendMessage(to, str(ret_))
                                elif cmd.startswith("sname "):
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            contact = fakhri.getContact(ls)
                                            fakhri.sendMessage(to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                                elif cmd.startswith("sbio "):
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            contact = fakhri.getContact(ls)
                                            fakhri.sendMessage(to, "[ Status Message ]\n{}".format(str(contact.statusMessage)))
                                elif cmd.startswith("spict"):
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            contact = fakhri.getContact(ls)
                                            path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                            fakhri.sendImageWithURL(to, str(path))
                                elif cmd.startswith("svideopict"):
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            contact = fakhri.getContact(ls)
                                            path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                            fakhri.sendVideoWithURL(to, str(path))
                                elif cmd.startswith("scover"):
                                    if client != None:
                                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                                            names = re.findall(r'@(\w+)', text)
                                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                            mentionees = mention['MENTIONEES']
                                            lists = []
                                            for mention in mentionees:
                                                if mention["M"] not in lists:
                                                    lists.append(mention["M"])
                                            for ls in lists:
                                                channel = fakhri.getProfileCoverURL(ls)
                                                path = str(channel)
                                                fakhri.sendImageWithURL(to, str(path))
                                elif cmd == 'listmember':
                                    if msg.toType == 2:
                                        group = fakhri.getGroup(to)
                                        ret_ = "╔══[ Member List ]"
                                        no = 0 + 1
                                        for mem in group.members:
                                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                                            no += 1
                                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                                        fakhri.sendMessage(to, str(ret_))
                                elif cmd == 'grouplist':
                                        groups = fakhri.groups
                                        ret_ = "╔══[ Group List ]"
                                        no = 0 + 1
                                        for gid in groups:
                                            group = fakhri.getGroup(gid)
                                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                            no += 1
                                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                                        fakhri.sendMessage(to, str(ret_))
# Pembatas Script #
                                elif cmd == "gantipp":
                                    settings["changePictureProfile"] = True
                                    fakhri.sendMessage(to, "Silahkan kirim gambarnya")
                                elif cmd == "gantippgrup":
                                    if msg.toType == 2:
                                        if to not in settings["changeGroupPicture"]:
                                            settings["changeGroupPicture"].append(to)
                                        fakhri.sendMessage(to, "Silahkan kirim gambarnya")
                                elif "kick " in msg.text.lower():
                                  if msg._from in admin:
                                      if 'MENTION' in msg.contentMetadata.keys()!= None:
                                          names = re.findall(r'@(\w+)', msg.text)
                                          mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                          mentionees = mention['MENTIONEES']
                                          for mention in mentionees:
                                  	         fakhri.kickoutFromGroup(msg.to,[mention['M']])
                                elif 'ban ' in text.lower():
                                      try:
                                          key = eval(msg.contentMetadata["MENTION"])
                                          u = key["MENTIONEES"][0]["M"]
                                          a = fakhri.getContact(u).mid
                                          targets = []
                                          targets.append(a)
                                          if targets == []:
                                             fakhri.sendText(msg.to,"Not found")
                                          else:
                                              for target in targets:
                                                 if target not in admin:
                                                    try:
                                                        settings["blacklist"][a] = True
                                                        f=codecs.open('st2__b.json','w','utf-8')
                                                        json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                                        fakhri.sendText(msg.to,"Sukses blacklist!")
                                                    except:
                                                        fakhri.sendText(msg.to,"Sukses Ditambahkan!")
                                                 else:
                                                    fakhri.sendMessage(to,'Dia admin')
                                      except Exception as e:
                                          fakhri.sendMessage(to,"ERROR : " + str(e))
                                elif 'clear ' in text.lower():
                                      try:
                                          key = eval(msg.contentMetadata["MENTION"])
                                          u = key["MENTIONEES"][0]["M"]
                                          a = fakhri.getContact(u).mid
                                          targets = []
                                          targets.append(a)
                                          if targets == []:
                                              fakhri.sendText(msg.to,"Not found")
                                          if a not in settings['blacklist']:
                                              fakhri.sendMessage(to,'User tidak di blacklist!')
                                          else:
                                              try:
                                                  del settings["blacklist"][a]
                                                  f=codecs.open('st2__b.json','w','utf-8')
                                                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                                  fakhri.sendMessage(msg.to,"Sukses dihapus dari blacklist!")
                                              except Exception as e:
                                                  fakhri.sendMessage(to,"ERROR : " + str(e))
                                      except Exception as e:
                                          fakhri.sendMessage(to,"ERROR : " + str(e))
                                elif cmd == 'clearban':
                                      settings["blacklist"] = {}
                                      fakhri.sendMessage(to,'Sukses menghapus semua banned user!')
                                elif cmd == 'set':
                                      try:
                                          fakhri.sendMessage(to,'Ceksider tanpa tag on!')
                                          del cctv['point'][receiver]
                                          del cctv['sidermem'][receiver]
                                          del cctv['cyduk'][receiver]
                                      except:
                                          pass
                                      cctv['point'][receiver] = msg.id
                                      cctv['sidermem'][receiver] = ""
                                      cctv['cyduk'][receiver]=True
                                elif cmd == 'cek':
                                      if msg.to in cctv['point']:
                                          fakhri.sendText(receiver,'Yang membaca:' + cctv['sidermem'][msg.to])
                                      else:
                                          fakhri.sendText(receiver, "Ceksider tanpa tag belum di set!\nGunakan perintah !set")
                        elif msg.contentType == 1:
                          if settings["changePictureProfile"] == True:
                              path = fakhri.downloadObjectMsg(msg_id)
                              settings["changePictureProfile"] = False
                              fakhri.updateProfilePicture(path)
                              fakhri.sendMessage(to, "Berhasil mengubah foto profile")
                          if msg.toType == 2:
                              if to in settings["changeGroupPicture"]:
                                  path = fakhri.downloadObjectMsg(msg_id)
                                  settings["changeGroupPicture"].remove(to)
                                  fakhri.updateGroupPicture(to, path)
                                  fakhri.sendMessage(to, "Berhasil mengubah foto group")
                except Exception as e:
                    fakhri.log("ERROR : " + str(e))
                    restart_program()
            if op.type == 26:
                try:
                    print ("[ 26 ] RECIEVE MESSAGE")
                    msg = op.message
                    text = msg.text
                    msg_id = msg.id
                    receiver = msg.to
                    sender = msg._from
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != fakhri.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if settings["unsendMessage"] == True:
                            try:
                                msg = op.message
                                if msg.toType == 0:
                                    #fakhri.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                                    pass
                                else:
                                    #fakhri.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                                    msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                            except Exception as error:
                                logError(error)
                        if msg.contentType == 0:
                            if text is None:
                                return
                except Exception as error:
                    traceback.print_tb(error.__traceback__)
            if op.type == 65:
                print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
                if settings["unsendMessage"] == True:
                    try:
                        at = op.param1
                        msg_id = op.param2
                        if msg_id in msg_dict:
                            if msg_dict[msg_id]["from"]:
                                contact = fakhri.getContact(msg_dict[msg_id]["from"])
                                if contact.displayNameOverridden != None:
                                    name_ = contact.displayNameOverridden
                                else:
                                    name_ = contact.displayName
                                    ret_ = "╭──「 Canceled Message 」"
                                    ret_ += "\n│Sender : @!"
                                    ret_ += "\n│ Dikirim pada : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                    ret_ += "\n│ Tipe Data : {}".format(str(Type._VALUES_TO_NAMES[msg_dict[msg_id]["contentType"]]))
                                    ret_ += "\n│ Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                    ret_ += "\n╰──「Tercydux 」"
                                    sendMention(at, str(ret_), [contact.mid])
                                del msg_dict[msg_id]
                            else:
                                fakhri.sendMessage(at,"SentMessage cancelled,But I didn't have log data.\nSorry > <")
                    except Exception as error:
                        traceback.print_tb(error.__traceback__)
            if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = fakhri.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n☑ " + Name
                                print('READERS : '+ Name)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass
#=========================================================================================================================================#
            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)

    except Exception as e:
         pass

while True:
    try:
        ops = fakhriPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                fakhriBot(op)
                fakhriPoll.setRevision(op.revision)
    except Exception as error:
        print(error)
        restart_program()
