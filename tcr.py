# -*- coding: utf-8 -*-
#Created and Edited By Fakhri Adi Saputra
#Source Code from linepy and TCR
import linepy
from linepy import *
from datetime import datetime
import json, time, random, tempfile, os, sys, pytz, urllib, re, ast, string, six, requests
from gtts import gTTS
from googletrans import Translator

#client = LineClient() #untuk login qr in here
#client = LineClient(id='email kamu', passwd='pasword kamu') #login email in here
cl = LineClient(authToken='Ep14aMuYOSHRiDvTC8D9.HREEJr+HML0xdmLglWlQEq.AfHTg5kfULifV3O/bTpElAZ+agRQorjuUCqSUxsIqRo=') #login token in here
cl.log("Auth Token : " + str(cl.authToken))

kc = LineClient(authToken='Epj5Gcjm4PWOF3Py4go5.NI2t5tOpB6nIzFS6YnQXfq.QCCGLiICV5Fy8VqMHXVCS/Iy/3Hrqulm/PUR9kq1K30=') #login token in here
kc.log("Auth Token : " + str(kc.authToken))

kc = kk = ki
helpMessage ="""
"""

poll = LinePoll(cl)
poll2 = LinePoll(ki)
Amid = cl.getProfile().mid
Bmid = ki.getProfile().mid
KAC = [cl,ki,kc,kk]
admin = ['ubff53033c43cb66302de3d9d43be8200']
bots = [Amid,Bmid,'ubff53033c43cb66302de3d9d43be8200']

settings = {
    "restartPoint":{},
    "restartBot":{},
    "timeRestart":{},
    "userAgent":{},
    "keyCommand":".",
    "autoAdd":False,
    "Protectgr":True,
    "blacklist":{},
    "whitelist":{},
    "autoJoin":False,
    "autoReject":False,
    "autoLeave":True,
    "autoRead":False,
    "server":{},
    "changePicture":False,
    "changeGroupPicture":False,
    "autoJoinTicket":False,
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

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
            if op.type == 5:
                print ("[ 5 ] NOTIFIED ADD CONTACT")
                if settings["autoAdd"] == True:
                    cl.findAndAddContactsByMid(op.param1)
                cl.sendMessage(op.param1, "Halo {} terimakasih telah menambahkan saya sebagai teman :3".format(str(cl.getContact(op.param1).displayName)))
                arg = "   New Friend : {}".format(str(cl.getContact(op.param1).displayName))
                print (arg)

            if op.type == 11:
                if settings["Protectgr"] == True:
                    if op.param2 not in bots:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = True
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        kk.updateGroup(G)
                    else:
                        pass
            if op.type == 13:
                if op.param3 in Amid:
                    if op.param2 in admin:
                        cl.acceptGroupInvitation(op.param1)
                    if op.param3 in Bmid:
                      if op.param2 in admin:
                        ki.acceptGroupInvitation(op.param1)

                if Amid in op.param3:
                    if op.param2 not in admin:
                        pass
                    else:
                        G = cl.getGroup(op.param1)
                        cl.acceptGroupInvitation(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        G.preventedJoinByTicket = True
                        kc.updateGroup(G)
                        cl.sendText(op.param1,"Ketik 'Help' untuk bantuan\n\nHarap gunakan dengan bijak!")


            if op.type == 17:
                print ("[ 17 ]  NOTIFIED ACCEPT GROUP INVITATION")
                group = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2)
                arg = "   Group Name : {}".format(str(group.name))
                arg += "\n   User Join : {}".format(str(contact.displayName))
                print (arg)

            if op.type == 19:
                if Amid in op.param3:
                    if op.param2 in bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        if op.param2 in settings["whitelist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    cl.updateGroup(X)
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
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        if op.param2 in settings["whitelist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in settings["blacklist"]:
                        pass
                    if op.param2 in settings["whitelist"]:
                        pass
                    else:
                        settings["blacklist"][op.param2] = True
                if Cmid in op.param3:
                    if op.param2 in bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        if op.param2 in settings["whitelist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in settings["blacklist"]:
                        pass
                    if op.param2 in settings["whitelist"]:
                        pass
                    else:
                        settings["blacklist"][op.param2] = True
                if Dmid in op.param3:
                    if op.param2 in bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        if op.param2 in settings["whitelist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in settings["blacklist"]:
                        pass
                    if op.param2 in settings["whitelist"]:
                        pass
                    else:
                        settings["blacklist"][op.param2] = True

                if op.param3 not in bots:
                    if op.param2 in bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,admin)
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        if op.param2 in settings["whitelist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    kk.inviteIntoGroup(X,admin)
                    if op.param2 in settings["blacklist"]:
                        pass
                    if op.param2 in settings["whitelist"]:
                        pass
                    else:
                        settings["blacklist"][op.param2] = True

                if admin in op.param3:
                    if op.param2 in bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,admin)
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        if op.param2 in settings["whitelist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    kk.inviteIntoGroup(X,admin)
                    if op.param2 in settings["blacklist"]:
                        pass
                    if op.param2 in settings["whitelist"]:
                        pass
                    else:
                        settings["blacklist"][op.param2] = True

                if bots not in op.param3:
                    if op.param2 in bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        if op.param2 in settings["whitelist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    kk.inviteIntoGroup(X,admin)
                    if op.param2 in settings["blacklist"]:
                        pass
                    if op.param2 in settings["whitelist"]:
                        pass
                    else:
                        settings["blacklist"][op.param2] = True

            if op.type == 22:
                print ("[ 22 ] NOTIFIED INVITE INTO ROOM")
                if settings["autoLeave"] == True:
                    cl.sendMessage(op.param1, "Goblok ngapain invite gw")
                    cl.leaveRoom(op.param1)

            if op.type == 24:
                print ("[ 24 ] NOTIFIED LEAVE ROOM")
                if settings["autoLeave"] == True:
                    cl.sendMessage(op.param1, "Goblok ngapain invite gw")
                    cl.leaveRoom(op.param1)

            if op.type == 26:
                msg = op.message
                if msg.text != None:
                    if msg.toType == 2:
                        may = cl.getProfile().mid
                        if may in str(msg.contentMetadata) and 'MENTION' in str(msg.contentMetadata):
                            pilih = ['yang tag sy semoga jomblo seumur hidup','ngapain tag tag woe, kangen?','ada apa ini? ko di tag?','duhh kena tag, dianya kesepian kali yah','gk usah tag, gift tikel aja']
                            rslt = random.choice(pilih)
                            cl.sendText(msg.to, str(rslt))
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            if op.type == 15:
              if op.param2 not in bots:
                cl.sendText(op.param1,"Good Bye " + cl.getContact(op.param2).displayName +  "\nSee You Next Time . . . (p′︵‵。) 🤗")
                cl.inviteIntoGroup(op.param1,[op.param2])
                print ("MEMBER HAS LEFT THE GROUP")
            if op.type == 26:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            cl.sendChatChecked(receiver, msg_id)
                            contact = cl.getContact(sender)
                            if text.lower() == 'me':
                                cl.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                                cl.tag(receiver, sender)
                            elif ("Gn " in msg.text):
                                 X = cl.getGroup(msg.to)
                                 X.name = msg.text.replace("Gn ","")
                                 cl.updateGroup(X)
                            elif text.lower() == 'announce':
                                gett = cl.getChatRoomAnnouncements(receiver)
                                for a in gett:
                                    aa = cl.getContact(a.creatorMid).displayName
                                    bb = a.contents
                                    cc = bb.link
                                    textt = bb.text
                                    cl.sendText(receiver, 'Link: ' + str(cc) + '\nText: ' + str(textt) + '\nMaker: ' + str(aa))
                            elif text.lower() == 'unsend me':
                                cl.unsendMessage(msg_id)
                            elif text.lower() == 'getsq':
                                a = cl.getJoinedSquares()
                                squares = a.squares
                                members = a.members
                                authorities = a.authorities
                                statuses = a.statuses
                                noteStatuses = a.noteStatuses
                                txt = str(squares)+'\n\n'+str(members)+'\n\n'+str(authorities)+'\n\n'+str(statuses)+'\n\n'+str(noteStatuses)+'\n\n'
                                txt2 = ''
                                for i in range(len(squares)):
                                    txt2 += str(i+1)+'. '+str(squares[i].invitationURL)+'\n'
                                cl.sendText(receiver, txt2)
                            elif 'lc ' in text.lower():
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = cl.getContact(u).mid
                                    s = cl.getContact(u).displayName
                                    hasil = channel.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        channel.like(str(sender), str(result), likeType=random.choice(typel))
                                        channel.comment(str(sender), str(result), 'Auto Like by nrik')
                                    cl.sendText(receiver, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                                except Exception as e:
                                    cl.sendText(receiver, str(e))
                            elif "leave all group" == msg.text:
                              if msg._from in admin:
                                 gid = cl.getGroupIdsJoined()
                                 for i in gid:
                                     cl.sendText(i,"Bot di paksa keluar oleh owner!")
                                     cl.leaveGroup(i)
                                     ki.leaveGroup(i)
                                     kk.leaveGroup(i)
                                     kc.leaveGroup(i)
                                     cl.sendText(msg.to,"Success leave all group")
                            elif 'gc ' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    cname = cl.getContact(u).displayName
                                    cmid = cl.getContact(u).mid
                                    cstatus = cl.getContact(u).statusMessage
                                    cpic = cl.getContact(u).picturePath
                                    #print(str(a))
                                    cl.sendText(receiver, 'Nama : '+cname+'\nMID : '+cmid+'\nStatus Msg : '+cstatus+'\nPicture : http://dl.profile.line.naver.jp'+cpic)
                                    cl.sendMessage(receiver, None, contentMetadata={'mid': cmid}, contentType=13)
                                    if "videoProfile='{" in str(cl.getContact(u)):
                                        cl.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                                    else:
                                        cl.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic)
                                except Exception as e:
                                    cl.sendText(receiver, str(e))
                            elif 'sticker:' in msg.text.lower():
                                try:
                                    query = msg.text.replace("sticker:", "")
                                    query = int(query)
                                    if type(query) == int:
                                        cl.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        cl.sendText(receiver, 'https://line.me/S/sticker/'+str(query))
                                    else:
                                        cl.sendText(receiver, 'gunakan key sticker angka bukan huruf')
                                except Exception as e:
                                    cl.sendText(receiver, str(e))
                            elif msg.text in ["Key","Help","key","help"]:
                                cl.sendText(msg.to,helpMessage)
                            elif "yt:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("yt:", "")
                                    query = query.replace(" ", "+")
                                    x = cl.youtube(query)
                                    cl.sendText(receiver, x)
                                except Exception as e:
                                    cl.sendText(receiver, str(e))
                            elif "image:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("image:", "")
                                    images = cl.image_search(query)
                                    cl.sendImageWithURL(receiver, images)
                                except Exception as e:
                                    cl.sendText(receiver, str(e))
                            elif 'say:' in msg.text.lower():
                                try:
                                    isi = msg.text.lower().replace('say:','')
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(receiver, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(receiver, str(e))
                            elif 'apakah ' in msg.text.lower():
                                try:
                                    txt = ['iya','tidak','bisa jadi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    cl.sendAudio(receiver, 'temp2.mp3')
                                except Exception as e:
                                    cl.sendText(receiver, str(e))
                            elif "sytr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text
                                    tts = gTTS(text=A, lang=isi[1], slow=False)
                                    tts.save('temp3.mp3')
                                    cl.sendAudio(receiver, 'temp3.mp3')
                                except Exception as e:
                                    cl.sendText(receiver, str(e))
                            elif "tr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text
                                    cl.sendText(receiver, str(A))
                                except Exception as e:
                                    cl.sendText(receiver, str(e))
                            elif text.lower() == "keluar":
                                   kk.leaveGroup(msg.to)
                                   ki.leaveGroup(msg.to)
                                   kc.leaveGroup(msg.to)
                            elif text.lower() == "masuk":
                                    G = cl.getGroup(msg.to)
                                    ginfo = cl.getGroup(msg.to)
                                    G.preventedJoinByTicket = False
                                    cl.updateGroup(G)
                                    invsend = 0
                                    Ticket = cl.reissueGroupTicket(msg.to)
                                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                    G = cl.getGroup(msg.to)
                                    G.preventedJoinByTicket = True
                                    cl.updateGroup(G)
                                    G.preventedJoinByTicket(G)
                                    cl.updateGroup(G)
                            elif text.lower() == 'speed':
                                start = time.time()
                                cl.sendText(receiver, "TestSpeed")
                                elapsed_time = time.time() - start
                                cl.sendText(receiver, "%sdetik" % (elapsed_time))
                            elif 'spic' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = cl.getContact(u).pictureStatus
                                    if "videoProfile='{" in str(cl.getContact(u)):
                                        cl.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a+'/vp.small')
                                    else:
                                        cl.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    cl.sendText(receiver, str(e))
                            elif 'scover' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    cl.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    cl.sendText(receiver, str(e))
                            elif text.lower() == 'tagall':
                                group = cl.getGroup(receiver)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    cl.mention(receiver, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    cl.mention(receiver, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                    cl.mention(receiver, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    cl.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    cl.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    cl.mention(receiver, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    cl.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    cl.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    cl.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    cl.mention(receiver, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    cl.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    cl.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    cl.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    cl.mention(receiver, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                    cl.mention(receiver, nm5)
                                cl.sendText(receiver, "Members :"+str(jml))
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
                                            cl.sendMessage(msg.to,"Lurking already on")
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
                                        cl.sendMessage(msg.to, "Set reading point:\n" + readTime)

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
                                    cl.sendMessage(msg.to,"Lurking already off")
                                else:
                                    try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                    except:
                                          pass
                                    cl.sendMessage(msg.to, "Delete reading point:\n" + readTime)

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
                                    cl.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                                else:
                                    cl.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")

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
                                        cl.sendMessage(receiver,"[ Reader ]:\nNone")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = cl.getContacts(chiya)
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
                                        cl.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    cl.sendMessage(receiver,"Lurking has not been set.")
                            elif text.lower == "papay":
                                cl.sendMessage(to, "Mencoba keluar dari group")
                                cl.leaveGroup(to)
                            elif text.lower() == 'restart':
                                restart_program()
                except Exception as e:
                    cl.log("[SEND_MESSAGE] ERROR : " + str(e))
#=========================================================================================================================================#
#=========================================================================================================================================#
            if op.type == 55:
                print ("[ 55 ] NOTIFIED READ MESSAGE")
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
        cl.log("[SINGLE_TRACE] ERROR : " + str(e))
#==================================================================================================================#
