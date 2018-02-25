# -*- coding: utf-8 -*-
import linepy
from linepy import *
from datetime import datetime
import json, time, random, tempfile, os, sys, pytz, urllib, re, ast, string, six, requests, html5lib
from humanfriendly import format_timespan, format_size, format_number, format_length
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from urllib import parse

botStart = time.time()

#client = LineClient()
client = LineClient(authToken='Ep2nQdBy3dJj1LPiJjT0.V+uWm8q8TMmc3J2Dq76caa.PcrDp/ze9j533fxdhnGjOp4U0Xb7LkImcb65aAsdrDk=')
kc = LineClient(authToken='EppgCPiRm7XGTMzGz8n9.RymJZGAAdJ0Wb6vnuPgsMq.8ND47Sq3m6l9PtsiHm9dpahc1C8YVKCd04aGen5CZ2M=') #login token in here
client.log("Auth Token : " + str(client.authToken))

channel = LineChannel(client)
client.log("Channel Access Token : " + str(channel.channelAccessToken))

clientProfile = client.getProfile()
clientSettings = client.getSettings()
clientPoll = LinePoll(client)
clientMID = client.profile.mid

contact = client.getProfile()
backup = client.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

clientProfile = kc.getProfile()
clientSettings = kc.getSettings()
clientPoll = LinePoll(kc)
clientMID = kc.profile.mid

contact = kc.getProfile()
backup = kc.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

helpMessage ="""Help menu v0.0.1



"""

poll = LinePoll(client)
poll2 = LinePoll(kc)
Amid = client.getProfile().mid
Bmid = kc.getProfile().mid
KAC = [client,kc]
admin = [Amid]
bots = [Amid,Bmid]
mode='self'

settings = {
    "restartPoint":{},
    "restartBot":{},
    "timeRestart":{},
    "userAgent":{},
    "keyCommand":".",
    "autoAdd":False,
    "autoJoin":True,
    "autoReject":False,
    "autoLeave":False,
    "autoRead":True,
    "server":{},
    "changePicture":False,
    "changeGroupPicture":False,
    "autoJoinTicket":True,
}

cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = clientProfile.displayName
myProfile["statusMessage"] = clientProfile.statusMessage
myProfile["pictureStatus"] = clientProfile.pictureStatus

herProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = clientProfile.displayName
myProfile["statusMessage"] = clientProfile.statusMessage
myProfile["pictureStatus"] = clientProfile.pictureStatus


def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(0)
    akh = int(0)
    nm = nama
    myid = kc.getProfile().mid
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
        kc.sendMessage(to, text, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        print(error)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

while True:
    try:
        ops=poll.singleTrace(count=50)
        if ops != None:
          for op in ops:
#=========================================================================================================================================#
            #if op.type in OpType._VALUES_TO_NAMES:
            #    print("[ {} ] {}".format(str(op.type), str(OpType._VALUES_TO_NAMES[op.type])))
#=========================================================================================================================================#


            if op.type == 11:
                print ("[ 11 ] NOTIFIED UPDATE GROUP")
                if op.param3 == "1":
                    group = client.getGroup(op.param1)
                    contact = client.getContact(op.param2)
                    arg = "   Changed : Group Name"
                    arg += "\n   New Group Name : {}".format(str(group.name))
                    arg += "\n   Executor : {}".format(str(contact.displayName))
                    print (arg)
                elif op.param3 == "4":
                    group = client.getGroup(op.param1)
                    contact = client.getContact(op.param2)
                    if group.preventedJoinByTicket == False:
                        gQr = "Opened"
                    else:
                        gQr = "Closed"
                    arg = "   Changed : Group Qr"
                    arg += "\n   Group Name : {}".format(str(group.name))
                    arg += "\n   New Group Qr Status : {}".format(gQr)
                    arg += "\n   Executor : {}".format(str(contact.displayName))
                    print (arg)


            if op.type == 17:
                print ("[ 17 ]  NOTIFIED ACCEPT GROUP INVITATION")
                group = client.getGroup(op.param1)
                contact = client.getContact(op.param2)
                arg = "   Group Name : {}".format(str(group.name))
                arg += "\n   User Join : {}".format(str(contact.displayName))
                print (arg)

            if op.type == 19:
                print ("[ 19 ] NOTIFIED KICKOUT FROM GROUP")
                group = client.getGroup(op.param1)
                contact = client.getContact(op.param2)
                victim = client.getContact(op.param3)
                arg = "   Group Name : {}".format(str(group.name))
                arg += "\n   Executor : {}".format(str(contact.displayName))
                arg += "\n   Victim : {}".format(str(victim.displayName))
                print (arg)

            if op.type == 19:
                if Amid in op.param3:
                    G = kc.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kc.updateGroup(G)
                    Ti = kc.reissueGroupTicket(op.param1)
                    client.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = client.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    client.updateGroup(X)
                    Ti = client.reissueGroupTicket(op.param1)

                if Bmid in op.param3:
                    G = client.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    client.updateGroup(G)
                    Ti = client.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kc.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)

            if op.type == 22:
                print ("[ 22 ] NOTIFIED INVITE INTO ROOM")
                if settings["autoLeave"] == True:
                    client.sendMessage(op.param1, "Goblok ngapain invite gw")
                    client.leaveRoom(op.param1)

            if op.type == 24:
                print ("[ 24 ] NOTIFIED LEAVE ROOM")
                if settings["autoLeave"] == True:
                    client.sendMessage(op.param1, "Grup apa ini?")
                    client.leaveRoom(op.param1)

            #if op.type == 26:
                #msg = op.message
                #text = msg.text
                #msg_id = msg.id
                #receiver = msg.to
                #sender = msg._from
                #try:
                    #if msg.text != None:
                        #if msg.toType == 2:
                           #may = client.getProfile().mid
                            #if may in str(msg.contentMetadata) and 'MENTION' in str(msg.contentMetadata):
                                #pilih = ['Perlu apa?']
                                #rslt = random.choice(pilih)
                                #kc.sendText(msg.to, str(rslt))
                            #else:
                                #pass

                        #else:
                            #pass
                    #else:
                        #pass
                #except Exception as e:
                     #client.log("ERROR cuk")
            if op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            client.sendChatChecked(receiver, msg_id)
                            contact = client.getContact(sender)
                            if text.lower() == 'restart':
                                client.sendMessage(to, "Sudah Mi Di Restart Sundala")
                                restartBot()
                            if text.lower() == 'runtime':
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                client.sendMessage(msg.to, "Bot sudah berjalan selama {}".format(str(runtime)))
                            elif ("tes" in msg.text):
                                 kc.sendText(msg.to,"tes")
                            elif ("gn " in msg.text):
                                 X = client.getGroup(msg.to)
                                 X.name = msg.text.replace("Gn ","")
                                 client.updateGroup(X)
                            elif text.lower() == 'cancelall':
                                 print('Cancel Executed')
                                 gid = kc.getGroupIdsInvited()
                                 for i in gid:
                                     kc.rejectGroupInvitation(i)
                                     kc.sendText(msg.to,"All invitations have been refused")
                            elif text.lower() == 'announce':
                                gett = client.getChatRoomAnnouncements(receiver)
                                for a in gett:
                                    aa = client.getContact(a.creatorMid).displayName
                                    bb = a.contents
                                    cc = bb.link
                                    textt = bb.text
                                    client.sendText(receiver, 'Link: ' + str(cc) + '\nText: ' + str(textt) + '\nMaker: ' + str(aa))
                            elif text.lower() == 'unsend me':
                                client.unsendMessage(msg_id)
                            elif text.lower() == 'add all':
                                ap = kc.getGroups([msg.to])
                                semua = [contact.mid for contact in ap[0].members]
                                nya = ap[0].members
                                for a in nya:
                                    Mi_d = str(a.mid)
                                    kc.findAndAddContactsByMid(Mi_d)
                            elif text.lower() == 'gurl':
                                if msg.toType == 2:
                                    x = kc.getGroup(msg.to)
                                    if x.preventedJoinByTicket == True:
                                        x.preventedJoinByTicket = False
                                        kc.updateGroup(x)
                                        gurl = kc.reissueGroupTicket(msg.to)
                                        kc.sendText(msg.to,"Link grup:\n\nline://ti/g/" + gurl)
                                    else:
                                        gurl = kc.reissueGroupTicket(msg.to)
                                        kc.sendText(msg.to,"Link grup:\n\nline://ti/g/" + gurl)
                            elif "Group bc " in msg.text:
                                bctext = msg.text.replace("Group bc ", "")
                                n = kc.getGroupIdsJoined()
                                for manusia in n:
                                    kc.sendText(manusia, (bctext))
                            elif "clonegc " in msg.text:
                                print ('Cloning Group')
                                gName = msg.text.replace("clonegc ","")
                                ap = client.getGroups([msg.to])
                                semua = [contact.mid for contact in ap[0].members]
                                client.createGroup(gName, semua)
                            elif text.lower() == 'getsq':
                                a = client.getJoinedSquares()
                                squares = a.squares
                                members = a.members
                                authorities = a.authorities
                                statuses = a.statuses
                                noteStatuses = a.noteStatuses
                                txt = str(squares)+'\n\n'+str(members)+'\n\n'+str(authorities)+'\n\n'+str(statuses)+'\n\n'+str(noteStatuses)+'\n\n'
                                txt2 = ''
                                for i in range(len(squares)):
                                    txt2 += str(i+1)+'. '+str(squares[i].invitationURL)+'\n'
                                client.sendText(receiver, txt2)
                            elif text.lower() == "keluar":
                                   kc.leaveGroup(msg.to)
                            elif text.lower() == "masuk":
                                    G = client.getGroup(msg.to)
                                    ginfo = client.getGroup(msg.to)
                                    G.preventedJoinByTicket = False
                                    client.updateGroup(G)
                                    invsend = 0
                                    Ticket = client.reissueGroupTicket(msg.to)
                                    kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    G = client.getGroup(msg.to)
                                    G.preventedJoinByTicket = True
                                    client.updateGroup(G)
                                    G.preventedJoinByTicket(G)
                                    client.updateGroup(G)
                            elif text.lower() == "openurl":
                                    X = kc.getGroup(msg.to)
                                    X.preventedJoinByTicket = False
                                    kc.updateGroup(X)
                                    kc.sendText(msg.to,"Sudah terbuka masterku")
                            elif text.lower() == "closeurl":
                                    X = kc.getGroup(msg.to)
                                    X.preventedJoinByTicket = True
                                    kc.updateGroup(X)
                                    kc.sendText(msg.to,"Sudah tertutup masterku")
                            elif 'carilagu ' in msg.text.lower():
                                try:
                                    songname = msg.text.lower().replace('carilagu ','')
                                    params = {'songname': songname}
                                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.parse.urlencode(params))
                                    data = r.text
                                    data = json.loads(data)
                                    for song in data:
                                        hasil = 'Ini lagumu fakhri\n'
                                        hasil += 'Judul : ' + song[0]
                                        hasil += '\nDurasi : ' + song[1]
                                        hasil += '\nLink Download : ' + song[4]
                                        kc.sendText(msg.to, hasil)
                                        kc.sendText(msg.to, "Tunggu audionya ya..")
                                        kc.sendAudioWithURL(msg.to, song[4])
                                except Exception as njer:
                                    client.sendText(msg.to, str(njer))
                            elif "carilirik " in msg.text.lower():
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                params = {'songname': search}
                                with requests.session() as web:
                                    web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                    r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.parse.urlencode(params))
                                    try:
                                        data = json.loads(r.text)
                                        for song in data:
                                            songs = song[5]
                                            lyric = songs.replace('ti:','Title - ')
                                            lyric = lyric.replace('ar:','Artist - ')
                                            lyric = lyric.replace('al:','Album - ')
                                            removeString = "[1234567890.:]"
                                            for char in removeString:
                                                lyric = lyric.replace(char,'')
                                            ret_ = "╔══[ Lyric ]"
                                            ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                            ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                            ret_ += "\n╠ Link : {}".format(str(song[4]))
                                            ret_ += "\n╚══[ Finish ]\n{}".format(str(lyric))
                                            kc.sendMessage(to, str(ret_))
                                    except:
                                        kc.sendMessage(to, "Lirik tidak ditemukan")
                            elif "screenshotwebsite " in msg.text.lower():
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                with requests.session() as web:
                                    r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                    data = r.text
                                    data = json.loads(data)
                                    kc.sendImageWithURL(to, data["result"])
                            elif "checkdate " in msg.text.lower():
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
                                kc.sendMessage(to, str(ret_))
                            elif text.lower() == 'groupcreator':
                                group = kc.getGroup(to)
                                GS = group.creator.mid
                                kc.sendContact(to, GS)
                            elif text.lower() == 'groupid':
                                gid = kc.getGroup(to)
                                kc.sendMessage(to, "[ID Group : ]\n" + gid.id)
                            elif text.lower() == 'grouppicture':
                                group = kc.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                kc.sendImageWithURL(to, path)
                            elif text.lower() == 'groupname':
                                gid = kc.getGroup(to)
                                kc.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                            elif text.lower() == 'groupticket':
                                if msg.toType == 2:
                                    group = kc.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        ticket = kc.reissueGroupTicket(to)
                                        kc.sendMessage(to, "[ Group Ticket ]\nhttps://kc.me/R/ti/g/{}".format(str(ticket)))
                                    else:
                                        kc.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                            elif "instagraminfo" in msg.text.lower():
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                with requests.session() as web:
                                    web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                    r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                                    try:
                                        data = json.loads(r.text)
                                        ret_ = "╔══[ Profile Instagram ]"
                                        ret_ += "\n╠ Nama : {}".format(str(data["user"]["full_name"]))
                                        ret_ += "\n╠ Username : {}".format(str(data["user"]["username"]))
                                        ret_ += "\n╠ Bio : {}".format(str(data["user"]["biography"]))
                                        ret_ += "\n╠ Pengikut : {}".format(format_number(data["user"]["followed_by"]["count"]))
                                        ret_ += "\n╠ Diikuti : {}".format(format_number(data["user"]["follows"]["count"]))
                                        if data["user"]["is_verified"] == True:
                                            ret_ += "\n╠ Verifikasi : Sudah"
                                        else:
                                            ret_ += "\n╠ Verifikasi : Belum"
                                        if data["user"]["is_private"] == True:
                                            ret_ += "\n╠ Akun Pribadi : Iya"
                                        else:
                                            ret_ += "\n╠ Akun Pribadi : Tidak"
                                        ret_ += "\n╠ Total Post : {}".format(format_number(data["user"]["media"]["count"]))
                                        ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                                        path = data["user"]["profile_pic_url_hd"]
                                        kc.sendImageWithURL(to, str(path))
                                        kc.sendMessage(to, str(ret_))
                                    except:
                                        kc.sendMessage(to, "Pengguna tidak ditemukan")
                            elif "instagrampost" in msg.text.lower():
                                separate = msg.text.split(" ")
                                user = msg.text.replace(separate[0] + " ","")
                                profile = "https://www.instagram.com/" + user
                                with requests.session() as x:
                                    x.headers['user-agent'] = 'Mozilla/5.0'
                                    end_cursor = ''
                                    for count in range(1, 999):
                                        print('PAGE: ', count)
                                        r = x.get(profile, params={'max_id': end_cursor})

                                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                                        j    = json.loads(data)

                                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']:
                                            if node['is_video']:
                                                page = 'https://www.instagram.com/p/' + node['code']
                                                r = x.get(page)
                                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                                print(url)
                                                kc.sendVideoWithURL(msg.to,url)
                                            else:
                                                print (node['display_src'])
                                                kc.sendImageWithURL(msg.to,node['display_src'])
                                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)
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
                            elif 'lc ' in text.lower():
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).mid
                                    s = client.getContact(u).displayName
                                    hasil = channel.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        channel.like(str(sender), str(result), likeType=random.choice(typel))
                                        channel.comment(str(sender), str(result), 'Autolike by fakhri')
                                    client.sendText(receiver, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'gc ' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    cname = client.getContact(u).displayName
                                    cmid = client.getContact(u).mid
                                    cstatus = client.getContact(u).statusMessage
                                    cpic = client.getContact(u).picturePath
                                    #print(str(a))
                                    client.sendText(receiver, 'Nama : '+cname+'\nMID : '+cmid+'\nStatus Msg : '+cstatus+'\nPicture : http://dl.profile.kc.naver.jp'+cpic)
                                    client.sendMessage(receiver, None, contentMetadata={'mid': cmid}, contentType=13)
                                    if "videoProfile='{" in str(client.getContact(u)):
                                        client.sendVideoWithURL(receiver, 'http://dl.profile.kc.naver.jp'+cpic+'/vp.small')
                                    else:
                                        client.sendImageWithURL(receiver, 'http://dl.profile.kc.naver.jp'+cpic)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'sticker:' in msg.text.lower():
                                try:
                                    query = msg.text.replace("sticker:", "")
                                    query = int(query)
                                    if type(query) == int:
                                        client.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        client.sendText(receiver, 'https://kc.me/S/sticker/'+str(query))
                                    else:
                                        client.sendText(receiver, 'gunakan key sticker angka bukan huruf')
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif msg.text in ["Key","Help","key","help"]:
                                client.sendText(msg.to,helpMessage)
                            elif "yt:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("yt:", "")
                                    query = query.replace(" ", "+")
                                    x = client.youtube(query)
                                    client.sendText(receiver, x)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif "image:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("image:", "")
                                    images = client.image_search(query)
                                    client.sendImageWithURL(receiver, images)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'say:' in msg.text.lower():
                                try:
                                    isi = msg.text.lower().replace('say:','')
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp.mp3')
                                    client.sendAudio(receiver, 'temp.mp3')
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'apakah ' in msg.text.lower():
                                try:
                                    txt = ['iya','tidak','bisa jadi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    client.sendAudio(receiver, 'temp2.mp3')
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif "sytr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text
                                    tts = gTTS(text=A, lang=isi[1], slow=False)
                                    tts.save('temp3.mp3')
                                    client.sendAudio(receiver, 'temp3.mp3')
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif "tr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text
                                    client.sendText(receiver, str(A))
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif text.lower() == 'speed':
                                start = time.time()
                                client.sendText(receiver, "TestSpeed")
                                elapsed_time = time.time() - start
                                client.sendText(receiver, "%sdetik" % (elapsed_time))
                            elif 'spic' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).pictureStatus
                                    if "videoProfile='{" in str(client.getContact(u)):
                                        client.sendVideoWithURL(receiver, 'http://dl.profile.kc.naver.jp/'+a+'/vp.small')
                                    else:
                                        client.sendImageWithURL(receiver, 'http://dl.profile.kc.naver.jp/'+a)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'scover' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    client.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif "cloneprofile " in msg.text.lower():
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
                            elif "wifeclone " in msg.text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    for mention in mentionees:
                                        contact = mention["M"]
                                        break
                                    try:
                                        kc.cloneContactProfile(contact)
                                        kc.sendMessage(msg.to, "Sukses di clone!")
                                    except:
                                        kc.sendMessage(msg.to, "Gagal clone member")
                            elif text.lower() == 'restoreprofile':
                                try:
                                    clientProfile.displayName = str(myProfile["displayName"])
                                    clientProfile.statusMessage = str(myProfile["statusMessage"])
                                    clientProfile.pictureStatus = str(myProfile["pictureStatus"])
                                    client.updateProfileAttribute(8, clientProfile.pictureStatus)
                                    client.updateProfile(clientProfile)
                                    client.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                                except:
                                    client.sendMessage(msg.to, "Gagal restore profile")
                            elif "checkmid" in msg.text.lower():
                                separate = msg.text.split(" ")
                                saya = msg.text.replace(separate[0] + " ","")
                                client.sendMessage(receiver, None, contentMetadata={'mid': saya}, contentType=13)

                            elif text.lower() == 'friendlist':
                                contactlist = client.getAllContactIds()
                                kontak = client.getContacts(contactlist)
                                num=1
                                msgs="═════════List Friend═════════"
                                for ids in kontak:
                                    msgs+="\n[%i] %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                                client.sendMessage(msg.to, msgs)

                            elif text.lower() == 'blocklist':
                                blockedlist = client.getBlockedContactIds()
                                kontak = client.getContacts(blockedlist)
                                num=1
                                msgs="═════════List Blocked═════════"
                                for ids in kontak:
                                    msgs+="\n[%i] %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                                client.sendMessage(msg.to, msgs)
                            elif text.lower() == 'tagall':
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
                            elif text.lower() == 'lurking on':
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
                                            client.sendMessage(msg.to,"Lurking already on")
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
                                        kc.sendMessage(msg.to, "Set reading point:\n" + readTime)

                            elif text.lower() == 'lurking off':
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
                                    client.sendMessage(msg.to,"Lurking already off")
                                else:
                                    try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                    except:
                                          pass
                                    kc.sendMessage(msg.to, "Delete reading point:\n" + readTime)

                            elif text.lower() == 'lurking reset':
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
                                    client.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")

                            elif text.lower() == 'lurk':
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
                                        xpesan = 'Lurkers:\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\nLurking time: \n" + readTime
                                    try:
                                        kc.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    client.sendMessage(receiver,"Lurking has not been set.")
                            elif text.lower() == 'ceksider':
                                try:
                                    del cctv['point'][receiver]
                                    del cctv['sidermem'][receiver]
                                    del cctv['cyduk'][receiver]
                                except:
                                    pass
                                cctv['point'][receiver] = msg.id
                                cctv['sidermem'][receiver] = ""
                                cctv['cyduk'][receiver]=True
                            elif text.lower() == 'offread':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][receiver]=False
                                    client.sendText(receiver, cctv['sidermem'][msg.to])
                                else:
                                    client.sendText(receiver, "Heh belom di Set")
                            elif text.lower == "papay":
                                client.sendMessage(to, "Mencoba keluar dari group")
                                client.leaveGroup(to)
                                client.sendText(receiver, 'Mode Public ON')
                            elif text.lower == "tes":
                                pesan = "yes"
                                client.sendMessage(msg.to,pesan)
                            elif text.lower() == 'restart':
                                restart_program()
                except Exception as e:
                    client.log("ERROR cuk" + str(e))
#=========================================================================================================================================#

#=========================================================================================================================================#
            elif op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                pref=['eh ada','hai kak','aloo..','nah','lg ngapain','halo','sini kak']
                                client.sendText(op.param1, str(random.choice(pref))+' '+Name)
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
