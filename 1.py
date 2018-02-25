# -*- coding: utf-8 -*-
import linepy
from linepy import *
from datetime import datetime
import json, time, random, tempfile, os, sys, pytz, urllib, re, ast, string, six, requests, html5lib
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from urllib import parse
#client = LineClient() #untuk login qr in here
#client = LineClient(id='email kamu', passwd='pasword kamu') #login email in here
client = LineClient(authToken='EpitSM2Da1Fe2yyMCv3d.aA6NmdKbIfWkkBb7wvvj7q.V9XEz62Sym/Gjo83/SZEmVVtMWewwy6dcMZe3+aXNnk=') #login token in here
client.log("Auth Token : " + str(client.authToken))

channel = LineChannel(client)
client.log("Channel Access Token : " + str(channel.channelAccessToken))

helpMessage ="""
─┅═✥Help Command✥═┅─
【1】 Help
【2】 Me
【3】 Gc
【4】
【5】 Gn
【6】 Getsq
【7】 Image:
【8】 Say:
【9】 Unsend me
【10】 Sp
【11】 Lc
【12】 Sticker
【13】 Apakah
【14】 Sytr:
【15】 Tr:
【16】 Spict
【17】 Scover
【18】 Tagall
【19】 Lurking on
【20】 Lurking off
【21】 Lurk reset
【22】 Lurk
【23】 Restart
【24】 Papay

─┅═✥FakhriAdi✥═┅─
"""

poll = LinePoll(client)
mode='self'

settings = {
    "restartPoint":{},
    "restartBot":{},
    "timeRestart":{},
    "userAgent":{},
    "keyCommand":".",
    "autoAdd":False,
    "autoJoin":False,
    "autoReject":False,
    "autoLeave":True,
    "autoRead":False,
    "server":{},
    "changePicture":False,
    "changeGroupPicture":False,
    "autoJoinTicket":False,
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

clientProfile = client.getProfile()
clientSettings = client.getSettings()
clientPoll = LinePoll(client)
clientMID = client.profile.mid

contact = client.getProfile()
backup = client.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

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

            if op.type == 13:
                print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
                group = client.getGroup(op.param1)
                contact = client.getContact(op.param2)
                if settings["autoJoin"] == True:
                    if settings["autoReject"]["status"] == True:
                        if len(group.members) > settings["autoReject"]["members"]:
                            client.acceptGroupInvitation(op.param1)
                        else:
                            client.rejectGroupInvitation(op.param1)
                    else:
                        client.acceptGroupInvitation(op.param1)
                gInviMids = []
                for z in group.invitee:
                    if z.mid in op.param3:
                        gInviMids.append(z.mid)
                listContact = ""
                if gInviMids != []:
                    for j in gInviMids:
                        name_ = client.getContact(j).displayName
                        listContact += "\n      + {}".format(str(name_))

                arg = "   Group Name : {}".format(str(group.name))
                arg += "\n   Executor : {}".format(str(contact.displayName))
                arg += "\n   List User Invited : {}".format(str(listContact))
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

            if op.type == 22:
                print ("[ 22 ] NOTIFIED INVITE INTO ROOM")
                if settings["autoLeave"] == True:
                    client.sendMessage(op.param1, "Goblok ngapain invite gw")
                    client.leaveRoom(op.param1)

            if op.type == 24:
                print ("[ 24 ] NOTIFIED LEAVE ROOM")
                if settings["autoLeave"] == True:
                    client.sendMessage(op.param1, "Goblok ngapain invite gw")
                    client.leaveRoom(op.param1)

            if op.type == 26:
                msg = op.message
                if msg.text != None:
                    if msg.toType == 2:
                        may = client.getProfile().mid
                        if may in str(msg.contentMetadata) and 'MENTION' in str(msg.contentMetadata):
                            pilih = ['Ya?','Hm?','Ada apa?']
                            rslt = random.choice(pilih)
                            client.sendText(msg.to, str(rslt))
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
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
                            if text.lower() == 'me':
                                client.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                                client.tag(receiver, sender)
                            elif ("Gn " in msg.text):
                                 X = client.getGroup(msg.to)
                                 X.name = msg.text.replace("Gn ","")
                                 client.updateGroup(X)
                            

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
                            elif "Add all" in msg.text:
                                ap = client.getGroups([msg.to])
                                semua = [contact.mid for contact in ap[0].members]
                                nya = ap[0].members
                                for a in nya:
                                    Mi_d = str(a.mid)
                                    client.findAndAddContactsByMid(Mi_d)
                            elif msg.text in ["Gurl"]:
                                if msg.toType == 2:
                                    x = client.getGroup(msg.to)
                                    if x.preventJoinByTicket == True:
                                        x.preventJoinByTicket = False
                                        client.updateGroup(x)
                                        gurl = client.reissueGroupTicket(msg.to)
                                        client.sendText(msg.to,"line://ti/g/" + gurl)
                                    else:
                                            if wait["lang"] == "JP":
                                                client.sendText(msg.to,"Can't be used outside the group")
                                            else:
                                                client.sendText(msg.to,"Not for use less than group")
                            elif "Group bc " in msg.text:
                                bctext = msg.text.replace("Group bc ", "")
                                n = client.getGroupIdsJoined()
                                for manusia in n:
                                    client.sendText(manusia, (bctext))
                            elif "CloneeGc " in msg.text:
                                gName = msg.text.replace("CloneeGc ","")
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
                            elif 'cekig ' in msg.text.lower():
                                try:
                                    instagram = msg.text.lower().replace("cekig ","")
                                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                                    soup = BeautifulSoup(html.text, 'html5lib')
                                    data = soup.find_all('meta', attrs={'property':'og:description'})
                                    text = data[0].get('content').split()
                                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                    text1 = data1[0].get('content').split()
                                    user = "Name: " + text[-2] + "\n"
                                    user1 = "Username: " + text[-1] + "\n"
                                    followers = "Followers: " + text[0] + "\n"
                                    following = "Following: " + text[2] + "\n"
                                    post = "Post: " + text[4] + "\n"
                                    link = "Link: " + "https://www.instagram.com/" + instagram
                                    detail = "========INSTAGRAM INFO USER========\n"
                                    details = "\n========INSTAGRAM INFO USER========"
                                    client.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                                    client.sendImageWithURL(msg.to, text1[0])
                                except Exception as njer:
                                    client.sendText(msg.to, str(njer))
                            elif 'carilagu ' in msg.text.lower():
                                try:
                                    songname = msg.text.lower().replace('carilagu ','')
                                    params = {'songname': songname}
                                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.parse.urlencode(params))
                                    data = r.text
                                    data = json.loads(data)
                                    for song in data:
                                        hasil = 'This is Your Music\n'
                                        hasil += 'Judul : ' + song[0]
                                        hasil += '\nDurasi : ' + song[1]
                                        hasil += '\nLink Download : ' + song[4]
                                        client.sendText(msg.to, hasil)
                                        client.sendText(msg.to, "Please Wait for audio...")
                                        client.sendAudioWithURL(msg.to, song[4])
                                except Exception as njer:
                                    client.sendText(msg.to, str(njer))
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
                                        channel.comment(str(sender), str(result), 'Auto Like by nrik')
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
                                    client.sendText(receiver, 'Nama : '+cname+'\nMID : '+cmid+'\nStatus Msg : '+cstatus+'\nPicture : http://dl.profile.line.naver.jp'+cpic)
                                    client.sendMessage(receiver, None, contentMetadata={'mid': cmid}, contentType=13)
                                    if "videoProfile='{" in str(client.getContact(u)):
                                        client.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                                    else:
                                        client.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'sticker:' in msg.text.lower():
                                try:
                                    query = msg.text.replace("sticker:", "")
                                    query = int(query)
                                    if type(query) == int:
                                        client.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        client.sendText(receiver, 'https://line.me/S/sticker/'+str(query))
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
                                        client.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a+'/vp.small')
                                    else:
                                        client.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
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
                                        client.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                                    except:
                                        client.sendMessage(msg.to, "Gagal clone member")
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
                                        client.sendMessage(msg.to, "Set reading point:\n" + readTime)

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
                                    client.sendMessage(msg.to, "Delete reading point:\n" + readTime)

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
                                        client.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
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
                            elif text.lower() == 'restart':
                                restart_program()
                except Exception as e:
                    client.log("[SEND_MESSAGE] ERROR : " + str(e))
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
