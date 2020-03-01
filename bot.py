# -*- coding: utf-8 -*-
#𝓗𝓻𝓡𝓿𝓸_𝓒𝓔𝓞↝𝓗𝓪𝓷LINEBOT販售檔 賴mvp1688
from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,atexit
from gtts import gTTS
from googletrans import Translator
botStart = time.time()
tkn = json.load(codecs.open("tokens.json","r","utf-8"))
cl = LINE(tkn["tokens"][0], appName="IOS\t8.14.2\tIphone X\t8.1.0")
profile = cl.getProfile()
status = str(profile.statusMessage)
lock = _name = "𝓗𝓻𝓡𝓿𝓸_𝓒𝓔𝓞↝𝓗𝓪𝓷 ŁÏŃĚ ßöᴛ運行中...\n\n𝓗𝓻𝓡𝓿𝓸_𝓒𝓔𝓞↝𝓗𝓪𝓷\n\n✔已運行\n\n✔ʙᴏᴛ ʀᴜɴɴɪɴɢᴀ ....\n\n作者:𝓗𝓻𝓡𝓿𝓸_𝓒𝓔𝓞↝𝓗𝓪𝓷 Made in HongKong可以嗎\n我的作者:line.me/ti/p/irdQOk2sYR\n\n✔Line ID:mvp16888\n\n"
if lock not in status:
    profile.statusMessage = lock + status
    cl.updateProfile(profile)
else:
    pass
oepoll = OEPoll(cl)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
lineSettings = cl.getSettings()
clProfile = cl.getProfile()
clMID = cl.profile.mid
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus
admin=['u1f8b4f616d6fb829defd1664545da0e6','u0f3ff7c8aba42b6725638265658aa5b1',clMID]
msg_dict = {}
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
setTime = {}
setTime = wait2['setTime']
bl = [""]
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ 訊息 ] 機器重啟")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def updateProfilePicture(self, path, type='p'):
        files = {'file': open(path, 'rb')}
        params = {'oid': self.profile.mid,'type': 'image'}
        if text.lower() == 'vp':
            params.update({'ver': '2.0', 'cat': 'vp.mp4'})
        data = {'params': self.genOBSParams(params)}
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/p/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Update profile picture failure.')
        return True
def updateProfileVideoPicture(self, path):
        try:
            from ffmpy import FFmpeg
            files = {'file': open(path, 'rb')}
            data = {'params': self.genOBSParams({'oid': self.profile.mid,'ver': '2.0','type': 'video','cat': 'vp.mp4'})}
            r_vp = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/vp/upload.nhn', data=data, files=files)
            if r_vp.status_code != 201:
                raise Exception('Update profile video picture failure.')
            path_p = self.genTempFile('path')
            ff = FFmpeg(inputs={'%s' % path: None}, outputs={'%s' % path_p: ['-ss', '00:00:2', '-vframes', '1']})
            ff.run()
            self.updateProfilePicture(path_p, 'vp')
        except:
            raise Exception('You should install FFmpeg and ffmpy from pypi')
def helpmessage():
    helpMessage = """«指令表»
★_查看指令表_☆
［Help］查看全部指令
★_狀態查詢_☆
［Rebot］重新啟動機器
［Runtime］查看機器運行時間
［Speed］查看機器速度
［Sp］查看機器速度
［Set］查看設定
［About］查看自己的狀態
［bye］機器退出群組
★_自身設定_☆
［Add On/Off］自動加入好友 開啟/關閉
［Join On/Off］邀請自動進入群組 開啟/關閉
［Leave On/Off］自動離開副本 開啟/關閉
［Read On/Off］自動已讀 開啟/關閉
［Inviteprotect On/Off］群組邀請保護 開啟/關閉
［Reread On/Off］查看收回 開啟/關閉
［Qr On/Off］群組網址保護 開啟/關閉
［Qrjoin On/Off］網址自動入群 開啟/關閉
［Ck On/Off］貼圖資料查詢 開啟/關閉
［Groupprotect On/Off］群組保護 開啟/關閉
［Ptt On/Off］自動進退 開啟/關閉
［sj On/Off］入群通知 開啟/關閉
［sl On/Off］退群通知 開啟/關閉
［ts On/OffI］偵測更新帳號 ex: 個簽, 頭貼, 姓名, 封面 
★_個人設定_☆
［Me］丟出自己好友資料
［MyMid］查看自己系統識別碼
［MyName］查看自己名字
［MyBio］查看自己個簽
［MyPicture］查看自己頭貼網址
［MyCover］查看自己封面網址
［Contact @］標註查看好友資料
［Mid @］標註查看系統識別碼
［Name @］標註查看名稱
［Bio @］標註查看狀態消息
［Pi @］標註查看頭貼
［vi @］標註查看頭貼影片
［Cover @］標注查看封面
［Friendlist］查看好友清單
★_群組設定_☆
［Gowner］查看群組擁有者
［Gurl］丟出群組網址
［O/Curl］打開/關閉群組網址
［Lg］查看所有群組
［Gb］查看群組成員
［Ginfo］查看群組狀態
［Ri @］標註來回機票
［Ri:mid］指定系統識別碼來回機票
［Tk @］標注踢出成員(多踢)
［Mk @］標注踢出成員(單踢)
［Vk @］標註踢出並清除訊息
［Vk:mid］使用系統識別碼踢出並清除訊息
［Nk Name］使用名子踢出成員
［kickall］群組成員全數踢出 #請謹慎使用
［Uk mid］使用系統識別碼踢出成員
［NT Name］使用名子標註成員
［Zk］踢出0字元
［Zt］標註名字0字成員
［Zm］丟出0字成員的系統識別碼
［Cancel］取消所有成員邀請
［Gcancel］取消所有群組邀請
［Gn Name］更改群組名稱
［Gc @］標註查看個人資料
［Inv mid］使用系統識別碼邀請進入群組
［Ban @］標註加入黑單
［Unban @］標註解除黑單
［Mb:mid］使用系統識別碼將該用戶加入黑單
［Mub:mid］使用系統識別碼將該用戶解除黑單
［Clear Ban］清空黑單
［Kill Ban］剔除黑單
［Killbanall］針對所有群組踢出黑單
［Zk］踢出名字0字成員
［banlist］查看黑名單 #
［Sc gid］查看指定群組狀態
［Mc mid］指定mid友資查詢
★_特別設定_☆
［Tagall］標註群組所有成員
［SR/DR］已讀點 開啟/關閉
［LR］查看已讀
［/invitemeto:］使用群組識別碼邀請至群組
［op@］標註加入權限
［deop@］標註取消權限
［mop:mid］使用系統識別碼將該用戶加入權限 #
[mdp:mid］使用系統識別碼將該用戶取消權限 #
［oplist］查詢權限者的系統辨識碼清單
［oplist］查詢權限者清單
［Say 文字 次數］重覆發話
［tag @標記 次數］重覆標記
［call:次數］群組通話邀請
［rall:次數］副本通話邀請
"""
    return helpMessage
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            contact = cl.getContact(op.param1)
            print ("[ 5 ] 通知添加好友 名字: " + contact.displayName)
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                cl.sendMessage(op.param1, "安安！{} 感謝您加我為好友！".format(str(contact.displayName)))
                cl.sendMessage(op.param1, "目前半垢運行中^^")
                cl.sendMessage(op.param1, "我的作者:line.me/ti/p/irdQOk2sYR")
        if op.type == 11:
            group = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            if settings["qrprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    gs = cl.getGroup(op.param1)
                    gs.preventJoinByTicket = True
                    cl.updateGroup(gs)
                    invsend = 0
                    cl.sendMessage(op.param1,cl.getContact(op.param2).displayName + "網址保護中...不要動群組網址！")
                    cl.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            if settings["inviteprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                    time.sleep(0.15)
                    cl.kickoutFromGroup(op.param1,[op.param3])
                    time.sleep(0.15)
                    cl.kickoutFromGroup(op.param1,[op.param2])
            if clMID in op.param3:
                if settings["autoJoin"] == True:
                    try:
                        arrData = ""
                        text = "%s "%('[提示]')
                        arr = []
                        mention = "@x "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention + "招待使用\n半垢運行中..."
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        cl.sendMessage(op.param1, "我的作者：")
                        cl.sendContact(op.param1, "u1f8b4f616d6fb829defd1664545da0e6")
                    except Exception as error:
                        print(error)
            if clMID in op.param3:
                if settings["autoPtt"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1, "自動進退運行中...")
                    cl.leaveGroup(op.param1)
        if op.type == 15:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            if settings["seeLeave"] == True:
                try:
                    arrData = ""
                    text = "%s "%('[提示]')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "退出了 {} ！".format(str(group.name))
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 17:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            if settings["seeJoin"] == True:
                try:
                    arrData = ""
                    text = "%s "%('歡迎')
                    arr = []
                    mention = "@x "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "加入 {} ！".format(str(group.name))
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 19:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            print ("[19]有人把人踢出群組 群組名稱: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid:" + contact1.mid + "\n被踢者: " + contact2.displayName + "\nMid:" + contact2.mid )
            if settings["protect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    if settings["kickContact"] == True:
                        try:
                            arrData = ""
                            text = "%s " %('[警告]')
                            arr = []
                            mention1 = "@arasi "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention1) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':op.param2}
                            arr.append(arrData)
                            text += mention1 + '踢了 '
                            mention2 = "@kick "
                            sslen = str(len(text))
                            eelen = str(len(text) + len(mention2) - 1)
                            arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                            arr.append(arrdata)
                            text += mention2
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            settings["blacklist"][op.param2] = True
                            time.sleep(0.1)
                            cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        settings["blacklist"][op.param2] = True
                        time.sleep(0.1)
            else:
                if settings["kickContact"] == True:
                    try:
                        arrData = ""
                        text = "%s " %('[警告]')
                        arr = []
                        mention1 = "@arasi "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention1) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention1 + '踢了 '
                        mention2 = "@kick "
                        sslen = str(len(text))
                        eelen = str(len(text) + len(mention2) - 1)
                        arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                        arr.append(arrdata)
                        text += mention2
                        cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                    except Exception as error:
                        print(error)
                        if op.param2 in ban["admin"] or op.param2 in ban["bots"] or op.param2 in ban["owners"]:
                            pass
                        if op.param1 in settings["protect"]:
                            ban["blacklist"][op.param2] = True
                            cl.kickoutFromGroup(op.param1,[op.param2])
                        if op.param3 in ban["owners"]:
                            cl.inviteIntoGroup(op.param1,[op.param3])
        if op.type == 22:
            print ("[ 22 ] 通知離開副本")
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 1:
            print ("[1]更新配置文件")
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 7:
               if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    path = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ = "[ 貼圖資料 ]"
                    ret_ += "\n貼圖ID : {}".format(stk_id)
                    ret_ += "\n貼圖包ID : {}".format(pkg_id)
                    ret_ += "\n貼圖網址 : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n貼圖圖片網址：https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
            if msg.contentType == 13:
                if settings["contact"] == True:
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[名稱]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[個簽]:\n" + contact.statusMessage + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[名稱]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[個簽]:\n" + contact.statusMessage + "\n[頭貼網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    if msg.contentMetadata["serviceType"] == 'MH':
                        msg.contentType = 0
                        f_mid = msg.contentMetadata["postEndUrl"].split("userMid=")
                        s_mid = f_mid[1].split("&")
                        mid = s_mid[0]
                        if 'stickerId' not in msg.contentMetadata:
                            if 'mediaOid' in msg.contentMetadata:
                                if 'mediaCount' not in msg.contentMetadata:
                                    list_ = msg.contentMetadata['mediaOid'].split("oid=")
                                    object = list_[1]
                                    try:
                                        arrData = ""
                                        text = "%s\n%s\n"%("---[分享文章預覽]---","[文章作成者]:")
                                        arr = []
                                        mention = "@sheng "
                                        slen = str(len(text))
                                        elen = str(len(text) + len(mention) - 1)
                                        arrData = {'S':slen, 'E':elen, 'M':mid}
                                        arr.append(arrData)
                                        text += mention + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[媒體資訊]:\nhttp://profile.line-cdn.net/r/myhome/h/" + object + "\n數量 : 1" + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                        cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                    except Exception as error:
                                        print(error)
                                else:
                                    list_ = msg.contentMetadata['mediaOid'].split("oid=")
                                    object = list_[1]
                                    num = int(msg.contentMetadata["mediaCount"])
                                    numb = num + 1
                                    number = str(numb)
                                    try:
                                        arrData = ""
                                        text = "%s\n%s\n"%("---[分享文章預覽]---","[文章作成者]:")
                                        arr = []
                                        mention = "@sheng "
                                        slen = str(len(text))
                                        elen = str(len(text) + len(mention) - 1)
                                        arrData = {'S':slen, 'E':elen, 'M':mid}
                                        arr.append(arrData)
                                        text += mention + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[媒體資訊]:\nhttp://profile.line-cdn.net/r/myhome/h/" + object + "\n數量 : " + number + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                        cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                    except Exception as error:
                                        print(error)
                            else:
                                try:
                                    arrData = ""
                                    text = "%s\n%s\n"%("---[分享文章預覽]---","[文章作成者]:")
                                    arr = []
                                    mention = "@sheng "
                                    slen = str(len(text))
                                    elen = str(len(text) + len(mention) - 1)
                                    arrData = {'S':slen, 'E':elen, 'M':mid}
                                    arr.append(arrData)
                                    text += mention + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                    cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                except Exception as error:
                                    print(error)
                        else:
                            if 'mediaOid' not in msg.contentMetadata:
                                try:
                                    arrData = ""
                                    text = "%s\n%s\n"%("---[分享文章預覽]---","[文章作成者]:")
                                    arr = []
                                    mention = "@sheng "
                                    slen = str(len(text))
                                    elen = str(len(text) + len(mention) - 1)
                                    arrData = {'S':slen, 'E':elen, 'M':mid}
                                    arr.append(arrData)
                                    text += mention + "\n[貼圖資訊]:\n" + "貼圖網址 : line://shop/detail/" + msg.contentMetadata["packageId"] + "\n貼圖ID : " + msg.contentMetadata["stickerId"] + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                    cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                except Exception as error:
                                    print(error)
                            else:
                                list_ = msg.contentMetadata['mediaOid'].split("oid=")
                                object = list_[1]
                                try:
                                    arrData = ""
                                    text = "%s\n%s\n"%("---[分享文章預覽]---","[文章作成者]:")
                                    arr = []
                                    mention = "@sheng "
                                    slen = str(len(text))
                                    elen = str(len(text) + len(mention) - 1)
                                    arrData = {'S':slen, 'E':elen, 'M':mid}
                                    arr.append(arrData)
                                    text += mention + "\n[貼圖資訊]:\n" + "貼圖網址 : line://shop/detail/" + msg.contentMetadata["packageId"] + "\n貼圖ID : " + msg.contentMetadata["stickerId"] + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[媒體資訊]:\nhttp://profile.line-cdn.net/r/myhome/h/" + object + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                    cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                except Exception as error:
                                    print(error)
                    if msg.contentMetadata["serviceType"] == 'GB':
                        if 'stickerId' not in msg.contentMetadata:
                            if 'mediaOid' in msg.contentMetadata:
                                if 'mediaCount' not in msg.contentMetadata:
                                    try:
                                        arrData = ""
                                        text = "%s\n%s\n"%("---[群組文章預覽]---","[文章作成者]:")
                                        arr = []
                                        mention = "@sheng "
                                        slen = str(len(text))
                                        elen = str(len(text) + len(mention) - 1)
                                        arrData = {'S':slen, 'E':elen, 'M':sender}
                                        arr.append(arrData)
                                        text += mention + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[媒體資訊]:\nhttp://profile.line-cdn.net/r/myhome/h/" + msg.contentMetadata["mediaOid"] + "\n數量 : 1" + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                        cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                    except Exception as error:
                                        print(error)
                                else:
                                    num = int(msg.contentMetadata["mediaCount"])
                                    numb = num + 1
                                    number = str(numb)
                                    try:
                                        arrData = ""
                                        text = "%s\n%s\n"%("---[群組文章預覽]---","[文章作成者]:")
                                        arr = []
                                        mention = "@sheng "
                                        slen = str(len(text))
                                        elen = str(len(text) + len(mention) - 1)
                                        arrData = {'S':slen, 'E':elen, 'M':sender}
                                        arr.append(arrData)
                                        text += mention + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[媒體資訊]:\nhttp://profile.line-cdn.net/r/myhome/h/" + msg.contentMetadata["mediaOid"] + "\n數量 : " + number + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                        cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                    except Exception as error:
                                        print(error)
                            else:
                                try:
                                    arrData = ""
                                    text = "%s\n%s\n"%("---[群組文章預覽]---","[文章作成者]:")
                                    arr = []
                                    mention = "@sheng "
                                    slen = str(len(text))
                                    elen = str(len(text) + len(mention) - 1)
                                    arrData = {'S':slen, 'E':elen, 'M':sender}
                                    arr.append(arrData)
                                    text += mention + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                    cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                except Exception as error:
                                    print(error)
                        else:
                            if 'mediaOid' not in msg.contentMetadata:
                                try:
                                    arrData = ""
                                    text = "%s\n%s\n"%("---[群組文章預覽]---","[文章作成者]:")
                                    arr = []
                                    mention = "@sheng "
                                    slen = str(len(text))
                                    elen = str(len(text) + len(mention) - 1)
                                    arrData = {'S':slen, 'E':elen, 'M':sender}
                                    arr.append(arrData)
                                    text += mention + "\n[貼圖資訊]:\n" + "貼圖網址 : line://shop/detail/" + msg.contentMetadata["packageId"] + "\n貼圖ID : " + msg.contentMetadata["stickerId"] + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                    cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                except Exception as error:
                                    print(error)
                            else:
                                try:
                                    arrData = ""
                                    text = "%s\n%s\n"%("---[群組文章預覽]---","[文章作成者]:")
                                    arr = []
                                    mention = "@sheng "
                                    slen = str(len(text))
                                    elen = str(len(text) + len(mention) - 1)
                                    arrData = {'S':slen, 'E':elen, 'M':sender}
                                    arr.append(arrData)
                                    text += mention + "\n[貼圖資訊]:\n" + "貼圖網址 : line://shop/detail/" + msg.contentMetadata["packageId"] + "\n貼圖ID : " + msg.contentMetadata["stickerId"] + "\n[文字預覽]:\n" + msg.contentMetadata["text"] + "\n(僅顯示100字)" + "\n[媒體資訊]:\nhttp://profile.line-cdn.net/r/myhome/h/" + msg.contentMetadata["mediaOid"] + "\n[文章網址]:\n" + msg.contentMetadata["postEndUrl"]
                                    cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                                except Exception as error:
                                    print(error)
                    if msg.contentMetadata["serviceType"] == 'AB':
                        if msg.contentMetadata["locKey"] == 'BA':
                            num = int(msg.contentMetadata["mediaCount"])
                            numb = num + 1
                            number = str(numb)
                            try:
                                arrData = ""
                                text = "%s\n%s\n"%("---[群組相簿創建]---","[相簿作成者]:")
                                arr = []
                                mention = "@sheng "
                                slen = str(len(text))
                                elen = str(len(text) + len(mention) - 1)
                                arrData = {'S':slen, 'E':elen, 'M':sender}
                                arr.append(arrData)
                                text += mention + "\n[相簿名稱]: " + msg.contentMetadata["albumName"] + "\n[新增數量]: " + number + "\n[相簿網址]:\n" + msg.contentMetadata["postEndUrl"]
                                cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                            except Exception as error:
                                print(error)
                        if msg.contentMetadata["locKey"] == 'BT':
                            num = int(msg.contentMetadata["mediaCount"])
                            numb = num + 1
                            number = str(numb)
                            try:
                                arrData = ""
                                text = "%s\n%s\n"%("---[群組相簿圖片新增]---","[新增圖片者]:")
                                arr = []
                                mention = "@sheng "
                                slen = str(len(text))
                                elen = str(len(text) + len(mention) - 1)
                                arrData = {'S':slen, 'E':elen, 'M':sender}
                                arr.append(arrData)
                                text += mention + "\n[相簿名稱]: " + msg.contentMetadata["albumName"] + "\n[新增數量]: " + number + "\n[相簿網址]:\n" + msg.contentMetadata["postEndUrl"]
                                cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                            except Exception as error:
                                print(error)
            if msg.contentType == 0:
                if text is None:
                    return
            if sender in admin:
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                elif text.lower() == 'bot':
                    cl.sendMessage(to, "我的作者：")
                    cl.sendContact(to, "u1f8b4f616d6fb829defd1664545da0e6")
                elif "Ri " in msg.text:
                    Ri0 = text.replace("Ri ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                    cl.findAndAddContactsByMid(target)
                                    cl.inviteIntoGroup(to,[target])
                                except:
                                    pass
                elif text.lower() == 'save':
                    backupData()
                    cl.sendMessage(to,"儲存設定成功!")
                elif "Ri:" in msg.text:
                    midd = text.replace("Ri:","")
                    cl.kickoutFromGroup(to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(to,[midd])
                elif "Uk " in msg.text:
                    midd = text.replace("Uk ","")
                    cl.kickoutFromGroup(to,[midd])
                elif "Tk " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in admin:
                            pass
                        else:
                            try:
                                cl.kickoutFromGroup(to,[target])
                            except:
                                pass
                elif "Mk " in msg.text:
                    Mk0 = text.replace("Mk ","")
                    Mk1 = Mk0.rstrip()
                    Mk2 = Mk1.replace("@","")
                    Mk3 = Mk2.rstrip()
                    _name = Mk3
                    gs = cl.getGroup(to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Nk " in msg.text:
                    _name = text.replace("Nk ","")
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "kickall" in msg.text:
                    if settings["kickmeber"] == True:
                        if msg.toType == 2:
                            _name = msg.text.replace("kickall","")
                            gs = cl.getGroup(to)
                            for g in gs.members:
                                try:
                                        cl.sendMessage(msg.to,"很高興認識你們!")
                                        cl.kickoutFromGroup(msg.to,[g.mid])
                                except:
                                    pass
                elif "Zk" in msg.text:
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Vk:" in text:
                    midd = msg.text.replace("Vk:","")
                    cl.kickoutFromGroup(msg.to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                    cl.cancelGroupInvitation(msg.to,[midd])
                elif "Vk " in msg.text:
                        vkick0 = msg.text.replace("Vk ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    cl.kickoutFromGroup(msg.to,[target])
                                    cl.findAndAddContactsByMid(target)
                                    cl.inviteIntoGroup(msg.to,[target])
                                    cl.cancelGroupInvitation(msg.to,[target])
                                except:
                                    pass
                elif "NT " in msg.text:
                    _name = text.replace("NT ","")
                    gs = cl.getGroup(to)
                    targets = []
                    net_ = ""
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            mc = sendMessageWithMention(to,target) + "\n"
                        cl.sendMessage(to,mc)
                elif text.lower() == 'zt':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            sendMessageWithMention(to,target)
                elif text.lower().startswith("x1: "):
                        separate = text.split(" ")
                        string = text.replace(separate[0] + " ","")
                        if len(string) <= 10000000000:
                            profile = cl.getProfile()
                            profile.displayName = string
                            cl.updateProfile(profile)
                            cl.sendMessage(to,"名稱已更改為 " + string + "")	
                elif text.lower() == 'zm':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        mc = "0字元使用者Mid："
                        for mi_d in targets:
                            mc += "\n->" + mi_d
                        cl.sendMessage(to,mc)
                elif "Mc " in msg.text:
                    mmid = msg.text.replace("Mc ","")
                    cl.sendContact(to, mmid)
                elif "Sc " in msg.text:
                    ggid = msg.text.replace("Sc ","")
                    group = cl.getGroup(ggid)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "不明"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    else:
                        gQr = "開啟"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "[群組資料]"
                    ret_ += "\n顯示名稱 : {}".format(str(group.name))
                    ret_ += "\n群組ＩＤ : {}".format(group.id)
                    ret_ += "\n群組作者 : {}".format(str(gCreator))
                    ret_ += "\n成員數量 : {}".format(str(len(group.members)))
                    ret_ += "\n邀請數量 : {}".format(gPending)
                    ret_ += "\n群組網址 : {}".format(gQr)
                    ret_ += "\n群組網址 : {}".format(gTicket)
                    ret_ += "\n[完]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif msg.text in ["c","C","cancel","Cancel"]:
                  if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = (contact.mid for contact in X.invitee)
                        ginfo = cl.getGroup(msg.to)
                        sinvitee = str(len(ginfo.invitee))
                        start = time.time()
                        for cancelmod in gInviMids:
                            cl.cancelGroupInvitation(msg.to, [cancelmod])
                        elapsed_time = time.time() - start
                        cl.sendMessage(to, "已取消完成\n取消時間: %s秒" % (elapsed_time))
                        cl.sendMessage(to, "取消人數:" + sinvitee)
                    else:
                        cl.sendMessage(to, "沒有任何人在邀請中！！")
                elif text.lower() == 'gcancel':
                    gid = cl.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    cl.sendMessage(to, "全部群組邀請已取消")
                    cl.sendMessage(to, "取消時間: %s秒" % (elapsed_time))
                elif "Gn " in msg.text:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        cl.updateGroup(X)
                    else:
                        cl.sendMessage(msg.to,"無法使用在群組外")
                elif text.lower().startswith('op '):
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        inkey = MENTION['MENTIONEES'][0]['M']
                        admin.append(str(inkey))
                        cl.sendMessage(to, "已新增權限！")
                elif text.lower().startswith('deop '):
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        inkey = MENTION['MENTIONEES'][0]['M']
                        admin.remove(str(inkey))
                        cl.sendMessage(to, "已移除權限！")
                elif text.lower().startswith('mop:'):
                        midd = msg.text.replace("mop:","")
                        admin.append(str(midd))
                        cl.sendMessage(to, "已加入權限！")
                elif text.lower().startswith('mdp:'):
                        midd = msg.text.replace("mdp:","")
                        admin.remove(str(midd))
                        cl.sendMessage(to, "已刪除權限！")
                elif text.lower() == 'opmid':
                    if admin == []:
                        cl.sendMessage(to, "沒有權限者")
                    else:
                        mc = "權限者清單："
                        for mi_d in admin:
                            mc += "\n-> " + mi_d
                        cl.sendMessage(to, mc)
                elif text.lower() == 'oplist':
                    if admin == []:
                        cl.sendMessage(to, "沒有權限者")
                    else:
                        mc = "權限者清單："
                        for mi_d in admin:
                            mc += "\n◉ " + cl.getContact(mi_d).displayName
                        cl.sendMessage(to, mc)
                elif "Gc" in msg.text:
                    if msg.toType == 2:
                        key = eval(msg.contentMetadata["MENTION"])
                        u = key["MENTIONEES"][0]["M"]
                        contact = cl.getContact(u)
                        cu = cl.getProfileCoverURL(mid=u)
                        try:
                            cl.sendMessage(msg.to,"名字:\n" + contact.displayName + "\n\n系統識別碼:\n" + contact.mid + "\n\n個性簽名:\n" + contact.statusMessage + "\n\n頭貼網址 :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n封面網址 :\n" + str(cu))
                        except:
                            cl.sendMessage(msg.to,"名字:\n" + contact.displayName + "\n\n系統識別碼:\n" + contact.mid + "\n\n個性簽名:\n" + contact.statusMessage + "\n\n封面網址:\n" + str(cu))
                elif "Inv " in msg.text:
                    midd = msg.text.replace("Inv ","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                elif text.lower() == 'bye':
                    cl.leaveGroup(to)
                elif "Ban" in msg.text:
                    if msg.toType == 2:
                        print ("[Ban] 成功")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    settings["blacklist"][target] = True
                                    cl.sendMessage(to, "已加入黑名單")
                                except:
                                    pass
                elif "Unban" in msg.text:
                    if msg.toType == 2:
                        print ("[UnBan] 成功")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    del settings["blacklist"][target]
                                    cl.sendMessage(to, "已解除黑名單")
                                except:
                                    pass
                elif "Mb:" in msg.text:
                    midd = msg.text.replace("Mb:","")
                    try:
                        settings["blacklist"][midd] = True
                        backupData()
                        cl.sendMessage(to, "已加入黑名單")
                    except:
                        pass
                elif "Mub:" in msg.text:
                    midd = msg.text.replace("Mub:","")
                    try:
                        del settings["blacklist"][midd]
                        backupData()
                        cl.sendMessage(to, "已解除黑名單")
                    except:
                        pass
                elif text.lower() == 'clear ban':
                    for mi_d in settings["blacklist"]:
                        settings["blacklist"] = {}
                    cl.sendMessage(to, "已清空黑名單")
                elif text.lower() == 'banlist':
                    if settings["blacklist"] == {}:
                        cl.sendMessage(to, "沒有黑名單")
                    else:
                        mc = "黑名單："
                        for mi_d in settings["blacklist"]:
                            mc += "\n->" + cl.getContact(mi_d).displayName
                        cl.sendMessage(to, mc)
                elif text.lower() == 'banmid':
                    if settings["blacklist"] == {}:
                        cl.sendMessage(to, "沒有黑名單")
                    else:
                        mc = "黑名單："
                        for mi_d in settings["blacklist"]:
                            mc += "\n->" + mi_d
                        cl.sendMessage(to, mc)
                elif text.lower() == 'kill ban':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in settings["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            print ("1")
                            cl.sendMessage(to, "沒有黑名單")
                            return
                        for jj in matched_list:
                            cl.kickoutFromGroup(to, [jj])
                            cl.sendMessage(to, "黑名單已踢除")
                elif text.lower() == 'killbanall':
                    gid = cl.getGroupIdsJoined()
                    group = cl.getGroup(to)
                    gMembMids = [contact.mid for contact in group.members]
                    ban_list = []
                    for tag in settings["blacklist"]:
                        ban_list += filter(lambda str: str == tag, gMembMids)
                    if ban_list == []:
                        cl.sendMessage(to, "沒有黑名單")
                    else:
                        for i in gid:
                            for jj in ban_list:
                                cl.kickoutFromGroup(i, [jj])
                            cl.sendMessage(i, "已針對所有群組清除黑單！")
                elif "/invitemeto:" in msg.text:
                    gid = msg.text.replace("/invitemeto:","")
                    if gid == "":
                        cl.sendMessage(to, "請輸入群組ID")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg._from)
                            cl.inviteIntoGroup(gid,[msg._from])
                        except:
                            cl.sendMessage(to, "我不在那個群組裡")
                elif text.lower().startswith('call:'):
                    if msg.toType == 2:
                        number = msg.text.replace("call:","")
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        num = int(number)
                        for var in range(0,num):
                            cl.inviteIntoGroupCall(to,gMembMids,1)
                        cl.sendMessage(to, "邀請完畢 共邀請了{}次".format(number))
                elif text.lower().startswith('rall:'):
                    if msg.toType == 1:
                        number = msg.text.replace("rall:","")
                        room = cl.getRoom(to)
                        rMembMids = [contact.mid for contact in room.contacts]
                        num = int(number)
                        for var in range(0,num):
                            cl.inviteIntoGroupCall(to,rMembMids,1)
                        cl.sendMessage(to, "邀請完畢 共邀請了{}次".format(number))
                elif text.lower().startswith('tag '):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    list_ = msg.text.split(" ")
                    number = list_[2]
                    num = int(number)
                    for var in range(0,num):
                        sendMessageWithMention(to, inkey)
                    cl.sendMessage(to, "標註完畢 共標註了{}次".format(number))
                elif text.lower().startswith('say '):
                    list_ = msg.text.split(" ")
                    text = list_[1]
                    number = list_[2]
                    num = int(number)
                    for var in range(0,num):
                        cl.sendMessage(to, text)
                    cl.sendMessage(to, "發送完畢 共發送了{}次".format(number))
                elif text.lower().startswith('post:'):
                    list_ = msg.text.split(":")
                    post = list_[1]
                    number = list_[2]
                    num = int(number)
                    for var in range(0,num):
                        cl.sendPostToTalk(to,post)
                    cl.sendMessage(to, "分享完畢 共分享了{}次".format(number))
                elif text.lower().startswith('talk:'):
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        text = msg.text.replace("talk:","")
                        for mem in group.members:
                            path = "http://dl.profile.line-cdn.net/" + str(mem.pictureStatus)
                            cl.sendMessage(to, text, {'MSG_SENDER_NAME': str(mem.displayName),'MSG_SENDER_ICON': str(path)})
                elif text.lower().startswith('prank '):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    sep = msg.text.split(" ")
                    text = sep[2]
                    contact = cl.getContact(inkey)
                    path = "http://dl.profile.line-cdn.net/" + str(contact.pictureStatus)
                    cl.sendMessage(to, text, {'MSG_SENDER_NAME': str(contact.displayName),'MSG_SENDER_ICON': str(path)})
                elif text.lower().startswith('send-tw '):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-tw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(to,"hasil.mp3")
                elif text.lower().startswith('send-en '):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(to,"hasil.mp3")
                elif text.lower().startswith('send-jp '):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ja'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(to,"hasil.mp3")
                elif text.lower().startswith('send-id '):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(to,"hasil.mp3")
                elif text.lower().startswith('tr-tw '):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-tw')
                    A = hasil.text
                    cl.sendMessage(to, A)
                elif text.lower().startswith('tr-en '):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    cl.sendMessage(to, A)
                elif text.lower().startswith('tr-jp '):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    cl.sendMessage(to, A)
                elif text.lower().startswith('tr-id '):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='id')
                    A = hasil.text
                    cl.sendMessage(to, A)
                elif "/ti/g/" in msg.text.lower():
                    if settings["autoJoinTicket"] == True:
                        link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                        links = link_re.findall(text)
                        n_links = []
                        for l in links:
                            if l not in n_links:
                                n_links.append(l)
                        for ticket_id in n_links:
                            group = cl.findGroupByTicket(ticket_id)
                            cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                            cl.sendMessage(group.id, "網址自動入群-群名 : %s" % str(group.name))
                elif text.lower() == 'test':
                    cl.sendMessage(to, "測試")
                elif msg.text in ["Friendlist"]:
                    anl = cl.getAllContactIds()
                    ap = ""
                    for q in anl:
                        ap += "• "+cl.getContact(q).displayName + "\n"
                    cl.sendMessage(msg.to,"「 朋友列表 」\n"+ap+"人數 : "+str(len(anl)))
                elif text.lower() == 'sp':
                    start = time.time()
                    cl.sendMessage(to, "檢查中...")
                    elapsed_time = time.time()/10 - start/10
                    cl.sendMessage(to,format(str(elapsed_time)) + "秒")
                elif text.lower() == 'speed':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=1000)
                    str1 = str(time0/10)
                    start = time.time()
                    cl.sendMessage(to,'處理速度\n' + str1 + '秒')
                    elapsed_time = time.time()/10 - start/10
                    cl.sendMessage(to,'指令反應\n' + format(str(elapsed_time)) + '秒')
                elif text.lower() == 'rebot':
                    cl.sendMessage(to, "重新啟動中...請稍後...")
                    time.sleep(5)
                    cl.sendMessage(to, "重新啟動完成！")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "機器運行時間 {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "u1f8b4f616d6fb829defd1664545da0e6"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        ret_ = "《關於自己》"
                        ret_ += "\n名稱 : {}".format(contact.displayName)
                        ret_ += "\n群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n封鎖 : {}".format(str(len(blockedlist)))
                        ret_ += "\n《關於機器》"
                        ret_ += "\n版本 : bot V1.0"
                        ret_ += "\n作者 : {}".format(creator.displayName)
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'set':
                    try:
                        ret_ = "[ 設定 ]"
                        if settings["autoAdd"] == True: ret_ += "\n自動加入好友 ✔"
                        else: ret_ += "\n自動加入好友 ✘"
                        if settings["autoJoin"] == True: ret_ += "\n自動加入群組 ✔"
                        else: ret_ += "\n自動加入群組 ✘"
                        if settings["autoJoinTicket"] == True: ret_ += "\n網址自動入群 ✔"
                        else: ret_ += "\n網址自動入群 ✘"
                        if settings["autoLeave"] == True: ret_ += "\n自動離開副本 ✔"
                        else: ret_ += "\n自動離開副本 ✘"
                        if settings["autoRead"] == True: ret_ += "\n自動已讀 ✔"
                        else: ret_ += "\n自動已讀 ✘"
                        if settings["protect"] == True: ret_ += "\n群組保護開啟 ✔"
                        else: ret_ += "\n群組保護關閉 ✘"
                        if settings["inviteprotect"] == True: ret_ += "\n群組邀請保護 ✔"
                        else: ret_ += "\n群組邀請保護 ✘"
                        if settings["qrprotect"] == True: ret_ += "\n群組網址保護 ✔"
                        else: ret_ += "\n群組網址保護 ✘"
                        if settings["contact"] == True: ret_ += "\n詳細資料 ✔"
                        else: ret_ += "\n詳細資料 ✘"
                        if settings["reread"] == True: ret_ += "\n查詢收回開啟 ✔"
                        else: ret_ += "\n查詢收回關閉 ✘"
                        if settings["detectMention"] == False: ret_ += "\n標註回覆開啟 ✔"
                        else: ret_ += "\n標註回覆關閉 ✘"
                        if settings["checkSticker"] == True: ret_ += "\n貼圖資料查詢開啟 ✔"
                        else: ret_ += "\n貼圖資料查詢關閉 ✘"
                        if settings["kickContact"] == True: ret_ += "\n踢人標註開啟 ✔"
                        else: ret_ += "\n踢人標註關閉 ✘"
                        if settings["autoPtt"] == True: ret_ += "\n自動進退開啟 ✔"
                        else: ret_ += "\n自動進退關閉 ✘"
                        if settings["timeline"] == True: ret_ += "\n文章詳情開啟 ✔"
                        else: ret_ += "\n文章詳情關閉 ✘"
                        if settings["seeJoin"] == True: ret_ += "\n入群通知開啟 ✔"
                        else: ret_ += "\n入群通知關閉 ✘"
                        if settings["seeLeave"] == True: ret_ += "\n退群通知開啟 ✔"
                        else: ret_ += "\n退群通知關閉 ✘"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'add on':
                    settings["autoAdd"] = True
                    cl.sendMessage(to, "自動加入好友已開啟 ✔")
                elif text.lower() == 'add off':
                    settings["autoAdd"] = False
                    cl.sendMessage(to, "自動加入好友已關閉 ✘")
                elif text.lower() == 'join on':
                    settings["autoJoin"] = True
                    cl.sendMessage(to, "自動加入群組已開啟 ✔")
                elif text.lower() == 'join off':
                    settings["autoJoin"] = False
                    cl.sendMessage(to, "自動加入群組已關閉 ✘")
                elif text.lower() == 'leave on':
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "自動離開副本已開啟 ✔")
                elif text.lower() == 'leave off':
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "自動離開副本已關閉 ✘")
                elif text.lower() == 'contact on':
                    settings["contact"] = True
                    cl.sendMessage(to, "查看好友資料詳情開啟 ✔")
                elif text.lower() == 'contact off':
                    settings["contact"] = False
                    cl.sendMessage(to, "查看好友資料詳情關閉 ✘")
                elif text.lower() == 'groupprotect on':
                    settings["protect"] = True
                    cl.sendMessage(to, "群組保護已開啟 ✔")
                elif text.lower() == 'groupprotect off':
                    settings["protect"] = False
                    cl.sendMessage(to, "群組保護已關閉 ✘")
                elif text.lower() == 'inviteprotect on':
                    settings["inviteprotect"] = True
                    cl.sendMessage(to, "群組邀請保護已開啟 ✔")
                elif text.lower() == 'inviteprotect off':
                    settings["inviteprotect"] = False
                    cl.sendMessage(to, "群組邀請保護已關閉 ✘")
                elif text.lower() == 'qr on':
                    settings["qrprotect"] = True
                    cl.sendMessage(to, "群組網址保護已開啟 ✔")
                elif text.lower() == 'qr off':
                    settings["qrprotect"] = False
                    cl.sendMessage(to, "群組網址保護已關閉 ✘")
                elif text.lower() == 'reread on':
                    settings["reread"] = True
                    cl.sendMessage(to, "查詢收回開啟 ✔")
                elif text.lower() == 'reread off':
                    settings["reread"] = False
                    cl.sendMessage(to, "查詢收回關閉 ✘")
                elif text.lower() == 'read on':
                    settings["autoRead"] = True
                    cl.sendMessage(to, "自動已讀已開啟 ✔")
                elif text.lower() == 'read off':
                    settings["autoRead"] = False
                    cl.sendMessage(to, "自動已讀已關閉 ✘")
                elif text.lower() == 'qrjoin on':
                    settings["autoJoinTicket"] = True
                    cl.sendMessage(to, "網址自動入群已開啟 ✔")
                elif text.lower() == 'qrjoin off':
                    settings["autoJoinTicket"] = False
                    cl.sendMessage(to, "網址自動入群已關閉 ✘")
                elif text.lower() == 'mention on':
                    settings["detectMention"] = False
                    cl.sendMessage(to, "標註回覆已開啟 ✔")
                elif text.lower() == 'mention off':
                    settings["detectMention"] = True
                    cl.sendMessage(to, "標註回覆已關閉 ✘")
                elif text.lower() == 'ck on':
                    settings["checkSticker"] = True
                    cl.sendMessage(to, "貼圖資料查詢已開啟 ✔")
                elif text.lower() == 'ck off':
                    settings["checkSticker"] = False
                    cl.sendMessage(to, "貼圖資料查詢已關閉 ✘")
                elif text.lower() == 'kc on':
                    settings["kickContact"] = True
                    cl.sendMessage(to, "踢人標註已開啟 ✔")
                elif text.lower() == 'kc off':
                    settings["kickContact"] = False
                    cl.sendMessage(to, "踢人標註已關閉 ✘")
                elif text.lower() == 'ptt on':
                    settings["autoPtt"] = True
                    cl.sendMessage(to, "自動進退已開啟 ✔")
                elif text.lower() == 'ptt off':
                    settings["autoPtt"] = False
                    cl.sendMessage(to, "自動進退已關閉 ✘")
                elif text.lower() == 'tl on':
                    settings["timeline"] = True
                    cl.sendMessage(to, "文章詳情已開啟 ✔")
                elif text.lower() == 'tl off':
                    settings["timeline"] = False
                    cl.sendMessage(to, "文章詳情已關閉 ✘")
                elif text.lower() == 'sj on':
                    settings["seeJoin"] = True
                    cl.sendMessage(to, "入群通知已開啟 ✔")
                elif text.lower() == 'sj off':
                    settings["seeJoin"] = False
                    cl.sendMessage(to, "入群通知已關閉 ✘")
                elif text.lower() == 'sl on':
                    settings["seeLeave"] = True
                    cl.sendMessage(to, "退群通知已開啟 ✔")
                elif text.lower() == 'sl off':
                    settings["seeLeave"] = False
                    cl.sendMessage(to, "退群通知已關閉 ✘")
                elif text.lower() == 'me':
                    sendMessageWithMention(to, sender)
                    cl.sendContact(to, sender)
                elif text.lower() == 'mymid':
                    cl.sendMessage(msg.to,"[MID]\n" +  sender)
                elif text.lower() == 'myname':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"[顯示名稱]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"[狀態消息]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = cl.getContact(sender)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'mycover':
                    me = cl.getContact(sender)
                    cover = cl.getProfileCoverURL(sender)
                    cl.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("contact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            mi_d = contact.mid
                            cl.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "標註者系統辨識碼："
                        for ls in lists:
                            ret_ += "\n" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("name "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ 名稱 ]\n" + contact.displayName)
                elif msg.text.lower().startswith("bio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ 個簽 ]\n" + contact.statusMessage)
                elif msg.text.lower().startswith("picture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                            cl.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("mpicture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                            cl.sendVideoWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cover "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = cl.getProfileCoverURL(ls)
                                cl.sendImageWithURL(msg.to, str(path))
                elif text.lower() == 'gowner':
                    group = cl.getGroup(to)
                    GS = group.creator.mid
                    cl.sendContact(to, GS)
                elif text.lower() == 'gid':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[群組ID : ]\n" + gid.id)
                elif text.lower() == 'gurl':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[ 群組網址 ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "群組網址未開啟，請用Ourl先開啟")
                elif text.lower() == 'ourl':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.sendMessage(to, "群組網址已開啟")
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            cl.sendMessage(to, "成功開啟群組網址")
                elif text.lower() == 'curl':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == True:
                            cl.sendMessage(to, "群組網址已關閉")
                        else:
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                            cl.sendMessage(to, "成功關閉群組網址")
                elif text.lower() == 'ginfo':
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "不明"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    else:
                        gQr = "開啟"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "《群組資料》"
                    ret_ += "\n顯示名稱 : {}".format(str(group.name))
                    ret_ += "\n群組ＩＤ : {}".format(group.id)
                    ret_ += "\n群組作者 : {}".format(str(gCreator))
                    ret_ += "\n成員數量 : {}".format(str(len(group.members)))
                    ret_ += "\n邀請數量 : {}".format(gPending)
                    ret_ += "\n群組網址 : {}".format(gQr)
                    ret_ += "\n群組網址 : {}".format(gTicket)
                    ret_ += "\n[ 完 ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower() == 'gb':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        ret_ = "[成員列表]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n[總共： {} 人]".format(str(len(group.members)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'lg':
                        groups = cl.groups
                        ret_ = "[群組列表]"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n[總共 {} 個群組]".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'tagall':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        cl.sendMessage(to, "總共 {} 個成員".format(str(len(nama))))
                elif msg.text in ["SR","Setread"]:
                    cl.sendMessage(msg.to, "設置已讀點 ✔")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print ("設置已讀點")
                elif msg.text in ["DR","Delread"]:
                    cl.sendMessage(to, "刪除已讀點 ✘")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                        del wait2['setTime'][msg.to]
                    except:
                        pass
                elif msg.text in ["LR","Lookread"]:
                    if msg.to in wait2['readPoint']:
                        print ("查詢已讀")
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendMessage(msg.to, "[已讀順序]:%s\n\n[已讀的人]:\n%s\n查詢時間:[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendMessage(msg.to, "請輸入SR設置已讀點")
        if op.type == 26:
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.toType == 0:
                        cl.log("[%s]"%(msg._from)+msg.text)
                    else:
                        cl.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            cl.sendMessage(at,"[收回訊息者]\n%s\n[收回內容]\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                            print ("收回訊息")
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == False:
                                    contact = cl.getContact(sender)
                                    cl.sendMessage(to, "標我幹嘛？(此為機器自動回覆)")
                                    sendMessageWithMention(to, contact.mid)
                                break
        if op.type == 55:
            try:
                print("[55]通知已讀訊息")
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[★]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[★]" + Name
                        print (time.time() + Name)
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
