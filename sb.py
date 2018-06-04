# -*- coding: utf-8 -*-
import linepy
from linepy import *
from datetime import datetime
import json, time, random, tempfile, os, sys, pytz, urllib, re, ast, string, six, requests, html5lib, urllib3, threading
from humanfriendly import format_timespan, format_size, format_number, format_length
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from urllib import parse

botStart = time.time()

client = LineClient(authToken='Et2VTGQwrBO1NYgvgj87.4jQ8bNKn9QAFKTmHMCnyHW.BrKpVBkhMPed+MG6y9/Kpqn/G1US5XSABqUktywJ4PI=')
client.log("Auth Token : " + str(client.authToken))
channel = LineChannel(client)
client.log("Channel Access Token : " + str(channel.channelAccessToken))
#clients = LineClient(authToken='EsVzA1gFfuU5cS680Yse.qI0GQMY/r9rCXmnoe6YdlG.z+m9QOy5rcxvMtJMYB5do7k4W7w60EKEw/XJ0jwnPu0=')

clientProfile = client.getProfile()
clientSettings = client.getSettings()
clientPoll = LinePoll(client)
clientMID = client.profile.mid

contact = client.getProfile()
backup = client.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

msg_dict = {}

helpmedia="""[Command Media]
☛ !sholat 「nama lokasi」
☛ !quran 「no surat」|「dari ayat」|「ke ayat」
☛ !gambar 「nama gambar」
☛ !iginfo 「username」
☛ !igpost 「username」|「nomor post」
☛ !igstory 「username」|「nomor post」
☛ !ssweb 「link website」
☛ !cuaca 「lokasi」
☛ !smusik 「artis - judul musik」
☛ !slirik 「artis - judul musik」
☛ !checkdate「tanggal-bulan-tahun」 """

helpsider="""[Command Sider]
☛ !setpoint
☛ !view
☛ !delpoint
☛ !resetpoint
=======[]========
☛ !set
☛ !cek"""

helpgroup="""[Command Group]
☛ !openurl
☛ !closeurl
☛ !tagall
☛ !spic 「tag」
☛ !scover 「tag」"""

helpMessage ="""[COMMAND LIST]

【1】!media
【2】!sider
【3】!group
【4】!help
【5】!keluar

versi : 2.0.0
http://fakhrads.xyz
"""
changeLog ="""[ChangeLog]

2.0.0
「Perbaikan bugs!」

"""
poll = LinePoll(client)
Amid = client.getProfile().mid
creator = "ubff53033c43cb66302de3d9d43be8200"
admin = "u8c49973f3ed4038ede20b7301b2c3a1e"

user = {}
limit = 1

settings = {
    "restartPoint":{},
    "restartBot":{},
    "timeRestart":{},
    "userAgent":{},
    "keyCommand":".",
    "members":20,
    "autoAdd":True,
    "autoJoin":True,
    "autoReject":False,
    "autoLeave":False,
    "autoRead":True,
    "server":{},
    "changePicture":False,
    "changeGroupPicture":False,
    "autoJoinTicket":True,
    "setKey": False,
    "keyCommand":"",
    "clock":True,
    "cName":"Mika ",
    "autoRespon": True,
    "unsendMessage": True,
}

cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

read = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "readTime":{},
    "ROM":{},
}
setTime = {}
setTime = read['setTime']
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = clientProfile.displayName
myProfile["statusMessage"] = clientProfile.statusMessage
myProfile["pictureStatus"] = clientProfile.pictureStatus
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@"
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
    client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(0)
    akh = int(0)
    nm = nama
    myid = client.getProfile().mid
    if myid in nm:
        nm.remove(myid)
    for mm in nm:
        akh = akh + 6
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 7
        akh = akh + 1
        bb += "@nrik \n"
        aa = (aa[:int(len(aa)-1)])
        text = bb
    try:
        client.sendMessage(to, text, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        print(error)
def sendMention2(to, text="", mids=[]):
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
        client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def clientBot(op):
    try:
#=========================================================================================================================================#
#=========================================================================================================================================#
            if op.type == 0:
                return

            if op.type == 5:
                print ("[ 5 ] NOTIFIED ADD CONTACT")
                client.sendMessage(op.param1, "Terima kasih telah menambahkan saya sebagai teman :3\nBOT hanya bisa digunakan di grup saja!")

            if op.type == 13:
                if Amid in op.param3:
                  print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
                  group = client.getGroup(op.param1)
                  if len(group.members) < 15:
                      client.acceptGroupInvitation(op.param1)
                      client.sendMessage(op.param1,"Member grup kurang dari 20")
                      client.leaveGroup(op.param1)
                      print(group.name)
                  else:
                    client.acceptGroupInvitation(op.param1)
                    sendMention(op.param1, "Hai @!, Terimaka Terimasih sudah mengundang BOT ini." , [op.param2])
                    
            if op.type in [22, 24]:
                print ("[ 22 And 24 ] NOTIFIED INVITE INTO ROOM & NOTIFIED LEAVE ROOM")
                if settings["autoLeave"] == True:
                    sendMention(op.param1, "Jangan undang aku kak@!")
                    client.leaveRoom(op.param1)
            if op.type == 26:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                to = receiver
                setKey = settings["keyCommand"].title()
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            client.sendChatChecked(receiver, msg_id)
                            contact = client.getContact(sender)
                            if text.lower() == '!me':
                                client.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                                client.tag(receiver, sender)
                                print (sender)
                            elif datetime.today().strftime('%H:%M') == '03:30':
                                grups = client.groups
                                audio = 'http://tinyurl.com/ybaznove'
                                for grup in grups:
                                  client.sendMessage(grup,"[ALARM]\n\nSahur!!! Sahur!!! Sahur!!!\nMari kita sahur!!!")
                                  client.sendAudioWithURL(grup,audio)
                            elif text.lower() == '!sider':
                                na = "Creator This BOT"
                                nam = "Fakhri Adi Saputra"
                                link = "http://line.me/ti/p/~fakhrads"
                                iconlink ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWbDftD-kEKNnwISBfhwQyAVXXRu8WWedQdsGpPGnzUaTH9BdD"                                
                                client.sendMessageWithContent(to,helpsider,nam,link,iconlink)
                            elif text.lower() == '!group':
                                na = "Creator This BOT"
                                nam = "Fakhri Adi Saputra"
                                link = "http://line.me/ti/p/~fakhrads"
                                iconlink ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWbDftD-kEKNnwISBfhwQyAVXXRu8WWedQdsGpPGnzUaTH9BdD" 
                                client.sendMessageWithContent(to,helpgroup,nam,link,iconlink)
                            elif text.lower() == '!media':
                                na = "Creator This BOT"
                                nam = "Fakhri Adi Saputra"
                                link = "http://line.me/ti/p/~fakhrads"
                                iconlink ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWbDftD-kEKNnwISBfhwQyAVXXRu8WWedQdsGpPGnzUaTH9BdD" 
                                client.sendMessageWithContent(to,helpmedia,nam,link,iconlink)  
                            elif text.lower() == '!creator':
                                na = "Creator This BOT"
                                nam = "Fakhri Adi Saputra"
                                link = "http://line.me/ti/p/~fakhrads"
                                iconlink ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWbDftD-kEKNnwISBfhwQyAVXXRu8WWedQdsGpPGnzUaTH9BdD" 
                                client.sendMessageWithContent(to,"Fakhri Adi Saputra",na,link,iconlink)
                            elif text.lower() == '!runtime':
                              if creator in sender:
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                client.sendMessage(msg.to, "Bot sudah berjalan selama {}".format(str(runtime)))
                              else:
                                client.sendMessage(receiver,"Only creator")
                            elif text.lower() == 'tes':
                              if sender not in creator:
                                pass
                              else:
                                  if sender not in user:
                                     user[sender] = 0
                                  if user[sender] >= limit:
                                     client.sendMessage(to,'Command limit!')
                                  else:  
                                      client.sendText(msg.to,"tes")
                                      user[sender] += 1
                            elif msg.text.lower().startswith == '!gn':
                                  X = client.getGroup(msg.to)
                                  X.name = msg.text.replace("!gn ","")
                            elif text.lower() == "!tiket":
                                tiket = client.getUserTicket(Amid)
                                client.sendMessage(receiver, '「 Your Ticket 」\nhttp://line.me/ti/p/{}'.format(tiket))
                            elif text.startswith("!quran "):
                                query = text.replace("!al-qur'an ","")
                                text = query.split("|")
                                surah = int(text[0])
                                ayat1 = int(text[1])
                                ayat2 = int(text[2])
                                result = requests.get("https://farzain.xyz/api/alquran.php?id={}&from={}&to={}".format(surah, ayat1, ayat2))
                                data = result.text
                                data = json.loads(data)
                                if data["status"] == "success":
                                    hasil = "「 Al-Qur'an 」\n"
                                    hasil += "\nName : {}".format(str(data["nama_surat"]))
                                    hasil += "\nMeaning : {}".format(str(data["arti_surat"]))
                                    hasil += "\nAyat :"
                                    for ayat in data["ayat"]:
                                        hasil += "\n{}".format(str(ayat))
                                    hasil += "\nMeaning Ayat :"
                                    for arti in data["arti"]:
                                        hasil += "\n{}".format(str(arti))
                                    client.sendMessage(receiver, str(hasil))
                            elif text.lower() == '!quotes':
                                result = requests.get("https://farzain.xyz/api/quotes.php")
                                data = result.text
                                data = json.loads(data)
                                if data["status"] == "success":
                                    hasil = data['result']
                                    client.sendMessage(receiver, str(hasil))
                            elif "pap:" in text.lower():
                              try:
                                  ayat = text.lower().replace("Pap:","")
                                  linux = "https://api.adorable.io/avatars/300/" + ayat
                                  client.sendImageWithURL(receiver, linux)
                              except Exception as error:
                                  client.sendMessage(to, "error\n" + str(error))
                            elif text.lower() == "!murrotal":
                                 client.sendMessage(to,"[Command Help]\n\nMurrotal 1\n\nNote:tulisnya ayat yak, kan di alquran ada ribuan ayat tuh nah tulisnya gitu, misal ayat ke 4978")
                            elif text.lower().startswith("!murrotal"):
                              try:
                                  sep = text.split(" ")
                                  ayat = text.replace(sep[0] + " ","")
                                  path = "http://islamcdn.com/quran/media/audio/ayah/ar.alafasy/" + ayat
                                  client.sendAudioWithURL(to, path)
                              except Exception as error:
                                  client.sendMessage(to, "error\n" + str(error))
                            elif text.lower().startswith("!sholat"):
                                a = 'Peta Lokasi'
                                c = 'https://png.pngtree.com/element_pic/16/12/02/51e6452ca365f618ab4b723c7aa18be9.jpg'
                                separate = msg.text.split(" ")
                                location = msg.text.replace(separate[0] + " ","")
                                r = requests.get("https://farzain.xyz/api/shalat.php?id={}".format(location))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                if data["status"] == "success":
                                    ret_ = "[ Jadwal Sholat Sekitar " + str(location) + " ]"
                                    ret_ += "\n~Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n~Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    ret_ += "\n~Shubuh : " + data['respon']['shubuh']
                                    ret_ += "\n~Dzuhur " + data['respon']['dzuhur']
                                    ret_ += "\n~Ashar " + data['respon']['ashar']
                                    ret_ += "\n~Maghrib " + data['respon']['maghrib']
                                    ret_ += "\n~Isya " + data['respon']['isya']
                                    ret_ += "\n[ Success ]"
                                    b = data['peta_gambar']
                                    client.sendMessageWithContent(msg.to, str(ret_),a,b,c)
                            elif text.lower().startswith("!gambar"):
                                try:
                                    separate = msg.text.split(" ")
                                    search = msg.text.replace(separate[0] + " ","")
                                    r = requests.get("https://farzain.xyz/api/gambarg.php?id={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["status"] == "success":
                                        client.sendImageWithURL(msg.to,data['url'])
                                    else:
                                        client.sendMessage(to,'Parameter Error!')
                                except Exception as error:
                                    client.sendMessage(msg.to, str(error))
                            elif text.lower().startswith("!smusik "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ Result Music ]"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n╠ {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n╚══[ Total {} Music ]".format(str(len(data["result"])))
                                    ret_ += "\n\nUntuk Melihat Details Music, silahkan gunakan command {}!smusik {} |「number」".format(str(setKey), str(search))
                                    client.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "╔══[ Music ]"
                                            ret_ += "\n╠ Title : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n╠ Album : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n╠ Size : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n╠ Link : {}".format(str(data["result"]["mp3"][0]))
                                            ret_ += "\n╚══[ Finish ]"
                                            client.sendMessage(to, str(ret_))
                                            client.sendAudioWithURL(to, str(data["result"]["mp3"][0]))
                            elif text.lower().startswith("!slirik"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = cond[0]
                                api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ Result Lyric ]"
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n╠ {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n╚══[ Total {} Music ]".format(str(len(data["results"])))
                                    ret_ += "\n\nUntuk Melihat Details Lyric, silahkan gunakan command {}!slirik {} |「number」".format(str(setKey), str(search))
                                    client.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["results"]):
                                        lyric = data["results"][num - 1]
                                        api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                        data = api.text
                                        data = json.loads(data)
                                        lyrics = data["results"]["lyric"]
                                        lyric = lyrics.replace('ti:','Title - ')
                                        lyric = lyric.replace('ar:','Artist - ')
                                        lyric = lyric.replace('al:','Album - ')
                                        removeString = "[1234567890.:]"
                                        for char in removeString:
                                            lyric = lyric.replace(char,'')
                                        client.sendMessage(msg.to, str(lyric))
                            elif text.lower().startswith("!searchyoutube"):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                params = {"search_query": search}
                                r = requests.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╔══[ Youtube Result ]"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                                    ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n╚══[ Total {} ]".format(len(datas))
                                client.sendMessage(to, str(ret_))
                            elif text.lower().startswith("!ytmp3"):
                                a = 'Download Link'
                                icon = 'http://www.bondtechnology.com/wp-content/uploads/2014/12/download-icon-round-looksoftware.png'
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                r = "http://www.convertmp3.io/widget/button/?video={}".format(str(search))
                                client.sendMessageWithContent(to,'Buka dengan browser.\nTekan download link dibawah!',a,r,icon)
                                
                            elif text.lower() == 'restart':
                              if sender in creator:
                                client.sendMessage(receiver,"Rebooting")
                                restart_program()
                              else:
                                client.sendMessage(to,'Kamu bukan creator kampang!')
                            elif text.lower() == '!gurl':
                                if msg.toType == 2:
                                    x = client.getGroup(msg.to)
                                    if x.preventedJoinByTicket == True:
                                        x.preventedJoinByTicket = False
                                        client.updateGroup(x)
                                        gurl = client.reissueGroupTicket(msg.to)
                                        client.sendText(msg.to,"Link grup:\n\nline://ti/g/" + gurl)
                                    else:
                                        gurl = client.reissueGroupTicket(msg.to)
                                        client.sendText(msg.to,"Link grup:\n\nline://ti/g/" + gurl)
                            elif msg.text.lower().startswith('!bc'):
                              if sender in creator:
                                bctext = msg.text.replace("!bc ", "")
                                n = client.getGroupIdsJoined()
                                for manusia in n:
                                    client.sendText(manusia,"[BroadCast]\n\n"+ (bctext))
                              else:
                                  pass
                            elif text.lower() == "!keluar":
                                   client.leaveGroup(msg.to)
                                   client.leaveGroup(msg.to)
                            elif text.lower() == "!openurl":
                                    X = client.getGroup(msg.to)
                                    X.preventedJoinByTicket = False
                                    client.updateGroup(X)
                                    client.sendText(msg.to,"Link QR Terbuka")
                            elif text.lower() == "!closeurl":
                                    X = client.getGroup(msg.to)
                                    X.preventedJoinByTicket = True
                                    client.updateGroup(X)
                                    client.sendText(msg.to,"Link QR Tertutup")
                            elif msg.text.lower().startswith('!ssweb'):
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                r = "https://image.thum.io/get/width/1200/{}".format(query)
                                client.sendImageWithURL(receiver, r)
                            elif msg.text.lower().startswith == '!tanggal':
                                sep = msg.text.split(" ")
                                tanggal = msg.text.replace(sep[0] + " ","")
                                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                data=r.text
                                data=json.loads(data)
                                ret_ = "╔══[ D A T E ]"
                                ret_ += "\n╠ Date Of Birth : {}".format(str(data["data"]["lahir"]))
                                ret_ += "\n╠ Age : {}".format(str(data["data"]["usia"]))
                                ret_ += "\n╠ Birthday : {}".format(str(data["data"]["ultah"]))
                                ret_ += "\n╠ Zodiak : {}".format(str(data["data"]["zodiak"]))
                                ret_ += "\n╚══[ Success ]"
                                client.sendMessage(receiver, str(ret_))
                            elif text.lower() == 'anime':
                                si = ("1","2","3","4","5","6","7","8","9","0")
                                ie = ("1","2","3","4","5","6","7","8","9","0")
                                bi = ("01","02","00")
                                bs = random.choice(bi)
                                io = random.choice(ie)
                                ss = random.choice(si)
                                bis = bs + io + ss
                                oew = "gan/" + bis + ".png"
                                client.sendImage(msg.to, oew)                              
                            elif text.lower().startswith("!cuaca"):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("https://farzain.xyz/api/cuaca.php?id={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    if data["status"] == "success":
                                        ret_ = "╔══[ Weather Status ]"
                                        ret_ += "\n╠ Kondisi cuaca : " + data['respon']['cuaca'].replace("Kondisi cuaca ","")
                                        ret_ += "\n╠ Lokasi : " + data['respon']['tempat'].replace("Temperatur di kota ","")
                                        ret_ += "\n╠ Suhu : " + data['respon']['suhu'].replace("Suhu : ","") + "°C"
                                        ret_ += "\n╠ Kelembaban : " + data['respon']['kelembapan'].replace("Kelembaban : ","") + "%"
                                        ret_ += "\n╠ Tekanan udara : " + data['respon']['udara'].replace("Tekanan udara : ","") + "HPa"
                                        ret_ += "\n╠ Kecepatan angin : " + data['respon']['angin'].replace("Kecepatan angin : ","") + "m/s"
                                        ret_ += "\n╠══[ Time Status ]"
                                        ret_ += "\n╠ Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                        ret_ += "\n╠ Jam : " + datetime.strftime(timeNow,'%H:%M:%S') + " WIB"
                                        ret_ += "\n╚══[ Success ]"
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    client.sendMessage(msg.to, str(error))
                            elif text.lower().startswith("!lokasi "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "[ Location Status ]"
                                        ret_ += "\nLocation : " + data[0]
                                        ret_ += "\nGoogle Maps : " + link
                                        ret_ += "\n[ Success ]"
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    client.sendMessage(msg.to, str(error))
                            elif text.lower().startswith("!iginfo"):
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("https://farzain.xyz/api/ig_profile.php?id={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = "[ Profile Instagram ]"
                                        ret_ += "\nNama : {}".format(str(data["info"]["full_name"]))
                                        ret_ += "\nUsername : {}".format(str(data["info"]["username"]))
                                        ret_ += "\nBio : {}".format(str(data["info"]["bio"]))
                                        ret_ += "\nPengikut : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\nDiikuti : {}".format(str(data["count"]["following"]))
                                        ret_ += "\n Total Post : {}".format(str(data["count"]["post"]))
                                        ret_ += "\n[ https://www.instagram.com/{} ]".format(search)
                                        path = data["info"]["profile_pict"]
                                        client.sendImageWithURL(to, str(path))
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    client.sendMessage(msg.to, str(error))
                            elif text.lower().startswith("!igpost"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")
                                    cond = text.split("|")
                                    username = cond[0]
                                    no = cond[1]
                                    r = requests.get("http://rahandiapi.herokuapp.com/instapost/{}/{}?key=betakey".format(str(username), str(no)))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["find"] == True:
                                        if data["media"]["mediatype"] == 1:
                                            client.sendImageWithURL(msg.to, str(data["media"]["url"]))
                                        if data["media"]["mediatype"] == 2:
                                            client.sendVideoWithURL(msg.to, str(data["media"]["url"]))
                                        ret_ = "╔══[ Info Post ]"
                                        ret_ += "\n╠ Jumlah Like : {}".format(str(data["media"]["like_count"]))
                                        ret_ += "\n╠ Jumlah Comment : {}".format(str(data["media"]["comment_count"]))
                                        ret_ += "\n╚══[ Caption ]\n{}".format(str(data["media"]["caption"]))
                                        client.sendMessage(to, str(ret_))
                                except Exception as error:
                                    client.sendMessage(msg.to, str(error))
                            elif text.lower().startswith("!igstory"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")
                                    cond = text.split("|")
                                    search = str(cond[0])
                                    if len(cond) == 2:
                                        r = requests.get("https://farzain.xyz/api/ig_story.php?id={}".format(search))
                                        data = r.text
                                        data = json.loads(data)
                                        if data["status"] != []:
                                            num = int(cond[1])
                                            if num <= len(data["url"]):
                                                search = data["url"][num - 1]
                                                if search["tipe"] == 1:
                                                    client.sendImageWithURL(to, str(search["link"]))
                                                if search["tipe"] == 2:
                                                    client.sendVideoWithURL(to, str(search["link"]))
                                except Exception as error:
                                    client.sendMessage(msg.to, str(error))
                            elif text.lower() == 'likes':
                                 s = channel.getHomeProfile(sender)
                                 print(s)
                            elif 'like dia ' in text.lower():
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).mid
                                    s = client.getContact(u).displayName
                                    hasil = channel.getHomeProfile(a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        channel.likePost(str(sender), str(result), likeType=random.choice(typel))
                                        channel.createComment(str(sender), str(result), 'Autolike by fakhri')
                                    client.sendText(receiver, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif msg.text.lower().startswith('!sticker'):
                                try:
                                    query = msg.text.replace("!sticker:", "")
                                    query = int(query)
                                    if type(query) == int:
                                        client.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        #client.sendText(receiver, 'https://line.me/S/sticker/'+str(query))
                                    else:
                                        client.sendText(receiver, 'gunakan key sticker angka bukan huruf')
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif msg.text in ["!Key","!Help","!key","!help","Help","help"]:
                                na = "Creator This BOT"
                                nam = "Fakhri Adi Saputra"
                                link = "http://line.me/ti/p/~fakhrads"
                                iconlink ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWbDftD-kEKNnwISBfhwQyAVXXRu8WWedQdsGpPGnzUaTH9BdD" 
                                client.sendMessageWithContent(msg.to,helpMessage,nam,link,iconlink)
                            elif msg.text.lower() == '!changelog':
                                client.sendText(msg.to,changeLog)
                            elif text.lower() == '!speed':
                                start = time.time()
                                client.sendText(receiver, "TestSpeed")
                                elapsed_time = time.time() - start
                                client.sendText(receiver, "%sdetik" % (elapsed_time))
                            elif msg.text.lower().startswith('!spic'):
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).pictureStatus
                                    if "videoProfile='{" in str(client.getContact(u)):
                                        client.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a+'/vp.small')
                                    else:
                                        client.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif msg.text.lower().startswith('!scover'):
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    client.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif msg.text.lower().startswith('!botclone'):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    for mention in mentionees:
                                        contact = mention["M"]
                                        break
                                    try:
                                        client.cloneContactProfile(contact)
                                        client.sendMessage(msg.to, "Sukses di clone!")
                                    except:
                                        client.sendMessage(msg.to, "Gagal clone member")
                            elif text.lower() == '!restoreprofile':
                                try:
                                    clientProfile.displayName = str(myProfile["displayName"])
                                    clientProfile.statusMessage = str(myProfile["statusMessage"])
                                    clientProfile.pictureStatus = str(myProfile["pictureStatus"])
                                    client.updateProfileAttribute(8, clientProfile.pictureStatus)
                                    client.updateProfile(clientProfile)
                                    client.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                                except:
                                    client.sendMessage(msg.to, "Gagal restore profile")
                            elif msg.text.lower() == '!checkmid':
                                separate = msg.text.split(" ")
                                saya = msg.text.replace(separate[0] + " ","")
                                client.sendMessage(receiver, None, contentMetadata={'mid': saya}, contentType=13)
                            elif text.lower() == '!grouplist':
                                    groups = client.groups
                                    ret_ = "╔══[ Group List ]"
                                    no = 0 + 1
                                    for gid in groups:
                                        group = client.getGroup(gid)
                                        ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                        no += 1
                                    ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                                    client.sendMessage(to, str(ret_))
                            elif text.lower() == '!friendlist':
                                contactlist = client.getAllContactIds()
                                kontak = client.getContacts(contactlist)
                                num=1
                                msgs="═════════List Friend═════════"
                                for ids in kontak:
                                    msgs+="\n[%i] %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                                client.sendMessage(msg.to, msgs)

                            elif text.lower() == '!blocklist':
                                blockedlist = client.getBlockedContactIds()
                                kontak = client.getContacts(blockedlist)
                                num=1
                                msgs="═════════List Blocked═════════"
                                for ids in kontak:
                                    msgs+="\n[%i] %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                                client.sendMessage(msg.to, msgs)
                            elif text.lower() == '!tagall':
                              if sender not in user:
                                 user[sender] = 0
                              if user[sender] >= 1:
                                 client.sendMessage(to,'Melebihi batas penggunaan')
                              else:  
                                group = client.getGroup(receiver)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    client.mention(receiver, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    client.mention(receiver, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    client.mention(receiver, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                    client.mention(receiver, nm5)
                                client.sendText(receiver, "Members :"+str(jml))
                                user[sender] += 1
                            elif text.lower() == '!setpoint':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read['readPoint']:
                                        try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                        except:
                                            pass
                                        read['readPoint'][msg.to] = msg.id
                                        read['readMember'][msg.to] = ""
                                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                        read['ROM'][msg.to] = {}
                                        with open('sider.json', 'w') as fp:
                                            json.dump(read, fp, sort_keys=True, indent=4)
                                            client.sendMessage(msg.to,"Ceksider sudah diaktifkan")
                                else:
                                    try:
                                        del read['readPoint'][msg.to]
                                        del read['readMember'][msg.to]
                                        del read['readTime'][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][msg.to] = msg.id
                                    read['readMember'][msg.to] = ""
                                    read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                    read['ROM'][msg.to] = {}
                                    with open('sider.json', 'w') as fp:
                                        json.dump(read, fp, sort_keys=True, indent=4)
                                        client.sendMessage(msg.to, "Set reading point:\n" + readTime)

                            elif text.lower() == '!delpoint':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to not in read['readPoint']:
                                    client.sendMessage(msg.to,"Ceksider sudah dimatikan")
                                else:
                                    try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                    except:
                                          pass
                                    client.sendMessage(msg.to, "Deleted reading point:\n" + readTime)

                            elif text.lower() == '!resetpoint':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read["readPoint"]:
                                    try:
                                        read["readPoint"][msg.to] = True
                                        read["readMember"][msg.to] = {}
                                        read["readTime"][msg.to] = readTime
                                        read["ROM"][msg.to] = {}
                                    except:
                                        pass
                                    client.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                                else:
                                    client.sendMessage(msg.to, "Ceksider belum diaktifkan ngapain di reset?")

                            elif text.lower() == '!view':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        client.sendMessage(receiver,"[ Reader ]:\nNone")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = client.getContacts(chiya)
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = 'Yang telah membaca:\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\nDi set pada: \n" + readTime
                                    try:
                                        client.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    client.sendMessage(receiver,"Sider point belum di set.")
                            elif msg.text.lower().startswith("murottals"):
                                  sep = msg.text.split(" ")
                                  surah = int(text.replace(sep[0] + " ",""))
                                  if 0 < surah < 115:
                                      if surah not in []:
                                          if len(str(surah)) == 1:
                                              audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-00" + str(surah) + "-muslimcentral.com.mp3"
                                              client.sendAudioWithURL(to, audionya)
                                          elif len(str(surah)) == 2:
                                              audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-0" + str(surah) + "-muslimcentral.com.mp3"
                                              client.sendAudioWithURL(to, audionya)
                                          else:
                                              audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-" + str(surah) + "-muslimcentral.com.mp3"
                                              client.sendAudioWithURL(to, audionya)
                                      else:
                                          client.sendMessage(to, "Surah terlalu panjang")
                                  else:
                                      client.sendMessage(to, "Quran hanya 114 surah")   
                            elif msg.text.lower().startswith('!say'):
                                r = text.lower().replace("!say","")
                                path = requests.get("https://farzain.xyz/api/tts.php?id="+ r)
                                data = path.text
                                data = json.loads(data)
                                if data["status"] == "success":
                                   client.sendAudioWithURL(to,data['result'])
                            elif msg.text.lower().startswith('!fs'):
                                r = text.lower().replace("!fs","")
                                path = requests.get("https://farzain.xyz/api/premium/fs.php?apikey=afterXyoufoundY&id="+ r)
                                data = path.text
                                data = json.loads(data)
                                if data["status"] == "success":
                                   client.sendImageWithURL(to,data['url'])        
                            elif text.lower() == 'aggresiveceksider':
                                try:
                                    del cctv['point'][receiver]
                                    del cctv['sidermem'][receiver]
                                    del cctv['cyduk'][receiver]
                                except:
                                    pass
                                cctv['point'][receiver] = msg.id
                                cctv['sidermem'][receiver] = ""
                                cctv['cyduk'][receiver]=True
                            elif text.lower() == 'offaggresiveceksider':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][receiver]=False
                                    client.sendText(receiver, cctv['sidermem'][msg.to])
                                else:
                                    client.sendText(receiver, "Heh belom di Set")
                        #   elif "/ti/g/" in msg.text.lower():
                        #     if settings["autoJoinTicket"] == True:
                        #         link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                        #         links = link_re.findall(text)
                        #         n_links = []
                        #         for l in links:
                        #             if l not in n_links:
                        #                 n_links.append(l)
                        #         for ticket_id in n_links:
                        #             group = client.findGroupByTicket(ticket_id)
                        #             client.acceptGroupInvitationByTicket(group.id,ticket_id)
                        #             client.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
                            elif text.lower() == '!set':
                                try:
                                    client.sendMessage(to,'Aktif!')
                                    del cctv['point'][receiver]
                                    del cctv['sidermem'][receiver]
                                    del cctv['cyduk'][receiver]
                                except:
                                    pass
                                cctv['point'][receiver] = msg.id
                                cctv['sidermem'][receiver] = ""
                                cctv['cyduk'][receiver]=True
                            elif text.lower() == '!cek':
                                if msg.to in cctv['point']:
                                    client.sendText(receiver,'Yang membaca:' + cctv['sidermem'][msg.to])
                                else:
                                    client.sendText(receiver, "Heh belom di Set")          
                except Exception as e:
                    client.sendMessage(to,"ERROR : " + str(e))
                    restart_program()
#=========================================================================================================================================#

#=========================================================================================================================================#
                        
                                   
            if op.type == 65:
              print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
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

            else:
                pass
            if op.type == 55:
                try:
                    if op.param1 in read['readPoint']:
                        if op.param2 in read['readMember'][op.param1]:
                            pass
                        else:
                            read['readMember'][op.param1] += op.param2
                        read['ROM'][op.param1][op.param2] = op.param2
                    else:
                       pass
                except:
                    pass
#=========================================================================================================================================#
            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)

    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))
        restart_program()

while True:
    try:
        ops = clientPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                clientBot(op)
                clientPoll.setRevision(op.revision)
    except Exception as error:
        print(error)
        restart_program()