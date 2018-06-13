# -*- coding: utf-8 -*-
import linepy
from linepy import *
from datetime import datetime
import json, time, random, tempfile, os, sys, pytz, urllib, re, ast, string, six, requests, html5lib, urllib3, threading, traceback, atexit, codecs
from humanfriendly import format_timespan, format_size, format_number, format_length
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from urllib import parse

botStart = time.time()
#fakhri = LineClient()
fakhri = LineClient(authToken='EtnQMaTwx9QvLk5SQYF3.gJyRJf1e6Gsb2Azs7BzqWW.2tCzjYWYhZV0Tn6DeRs6yg1MMiYx5kg/whijkLXTJ/A=')
fakhri.log("Auth Token : " + str(fakhri.authToken))
channel = LineChannel(fakhri)


fakhriProfile = fakhri.getProfile()
fakhriSettings = fakhri.getSettings()
fakhriPoll = LinePoll(fakhri)
fakhriMID = fakhri.profile.mid
botStart = time.time()
poll = LinePoll(fakhri)
settings = {
   "setKey": False,
   "keyCommand": "",
}
cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
helpsider="""
╭──「 Menu Message 」
│ setsider
│ ceksider
├──「 INFO 」
│ Creator: @fakhri 
╰──────────

"""
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
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                fakhri.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]           
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)  
def fakhriBot(op):
    try:
#=========================================================================================================================================#
#=========================================================================================================================================#
            if op.type == 0:
                return
            if op.type == 26:
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
                          sendMention(receiver,"Oi @!, terimaka Yang tag gw jomblo ",[sender])
                        #elif text.lower() == 'me':
                         # fakhri.sendMessage(receiver, sender)
                          #print(sender)
                      else:
                         pass
                    else:
                        pass
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
                                if cmd == 'setsider':
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
                                      try:
                                          fakhri.sendMessage(to,'Ceksider tanpa tag on!\n'+readTime)
                                          del cctv['point'][receiver]
                                          del cctv['sidermem'][receiver]
                                          del cctv['cyduk'][receiver]
                                      except:
                                          pass
                                      cctv['point'][receiver] = msg.id
                                      cctv['sidermem'][receiver] = ""
                                      cctv['cyduk'][receiver]=True
                                elif cmd == 'ceksider':
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
                                      if msg.to in cctv['point']:
                                          fakhri.sendText(receiver,'Yang membaca:' + cctv['sidermem'][msg.to] + '\n\nTanggal:\n' + readTime)
                                      else:
                                          fakhri.sendText(receiver, "Ceksider tanpa tag belum di set!\nGunakan perintah !set")          
                except Exception as e:                   
                    fakhri.sendMessage(to,"ERROR : " + str(e))
                    restart_program()       
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
