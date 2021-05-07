from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

from telegram.ext import *
from telegram.ext import MessageHandler, Filters
import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import re

length = ''
url = ""
photo = ""
name = ""
caption = ""
seasoncap = ""
newname = ""
r = 1
rawname = ""
text = ""
DB = []
URLS = []
t = 1
k = 1
u = 1
w = 0
n = 1
j = 1
cap = ""
totbutton = ""
chatid = ""


def start_command(update, context):
    update.message.reply_text("Sent ME The Link")
    print(dir(update.message))
    chatid = update.message.chat_id
    print(chatid)


def handle_photo(update, context):
    global DB
    global t
    global driver
    global name
    global chatid
    global w
    global u
    global n
    global length
    global url
    global photo
    global text
    global URLS
    URLS = []
    chatid = update.message.chat_id
    print(chatid)

    update.message.reply_text("OK Wait Let Me HAndle Things From Now")
    photo = update.message.photo[-1].file_id

    text = str(update.message.caption)
    print(text)
    url = re.findall("(?P<url>https?://[^\s]+)", text)
    print(url)
    lines = text.split('\n')
    rawname = lines[0]
    if re.search("🎬Title", rawname):
        name = rawname.replace("🎬Title :", "")

    elif re.search("🎬 Title", rawname):
        name = rawname.replace("🎬 Title :", "")

    elif re.search("📼 Title :", rawname):
        name = rawname.replace("📼 Title :", "")

    elif re.search("Title :", rawname):
        name = rawname.replace("Title :", "")
    else:
        name = rawname
    print(name)
    length = len(url)
    if re.search("Season", text):
        print("season Detected")
        if n == 1:
            name = ""
            n = n + 1
        update.message.reply_text(
            "OK Its a Series \n Sent The Name OK The Series With Season No\nExample:Money Heist S01 ")

        print(name)
        u = 1

        if re.search("Season", text):
            w = 1
    else:
        print("MOvie")
        if re.search("How", text):
            length = length - 1
        for i in range(0, length):
            print("i = ", i)
            pdurl = url[i]
            webmanager(name, pdurl, text, photo, context, update)


def webmanager(name, url, k, photo, context, update):
    global t
    global driver
    global DB
    global chatid
    global caption
    global u
    global r
    global cap
    global length
    global URLS

    if t == 1:
        driver.get('http://www.pdisk.net/upload?type=url')
        email = driver.find_element_by_xpath('//*[@id="app"]/article/div[1]/div[2]/div[1]/span/input')
        email.send_keys("")

        password = driver.find_element_by_xpath('//*[@id="app"]/article/div[1]/div[2]/div[2]/span/input')
        password.send_keys("")

        submit = driver.find_element_by_xpath('//*[@id="app"]/article/div[1]/div[2]/div[3]/button/span')
        submit.click()
        t = t + 1

    time.sleep(1)
    driver.get('http://www.pdisk.net/upload?type=url')
    if t == 2:
        nextbutton = driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/div/div[3]')
        nextbutton.click()
        nextbutton = driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/div/div[3]')
        nextbutton.click()
        nextbutton = driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/div/div[3]')
        nextbutton.click()
        nextbutton = driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/div/div[3]')
        nextbutton.click()
        agreebutton = driver.find_element_by_xpath('//*[@id="control-hooks_checkTos"]')
        agreebutton.click()
        t = t + 1
    upload = driver.find_element_by_xpath('//*[@id="control-hooks_fileUrl"]')
    upload.send_keys(url)
    filename = driver.find_element_by_xpath('//*[@id="control-hooks_fileTitle"]')
    filename.send_keys(name)
    uploadbutton = driver.find_element_by_xpath('//*[@id="control-hooks"]/div[5]/div/div/div/button/span')
    uploadbutton.click()
    driver.get('http://www.pdisk.net/home')
    driver.refresh()
    view = driver.find_element_by_xpath('//*[@id="app"]/section/main/section/main/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]')
    purl = view.text
    print(purl)
    pdiskurl = "http://www.pdisk.net/share-video?videoid={}".format(purl)
    print(pdiskurl)
    if re.search("Season", text):
        URLS.append(pdiskurl)
    if r == 1:
        cap = k.replace(url, pdiskurl)
        r = 2
    else:
        cap = cap.replace(url, pdiskurl)
        print(cap)
        print(length)
        if u == length:
            forwardphoto(update, context, photo, cap)
            if re.search("Season", text):
                print("called button Maker")
                buttonmaker(update, context, photo)
            print(u, length)
        else:
            print(u, length)
    u = u + 1


def handle_Seasons(update, context):
    global name
    global w
    global u
    global r
    global length
    global newname
    r = 1
    if w == 1:
        name = ""
        name = str(update.message.text)
        print(name)
        w = w + 1
        if re.search("How", text):
            length = length - 1
    if name != "":
        for i in range(0, length):

            print("i = ", i)
            if i <= 9:
                newname = name + f"E0{i + 1}"
            elif i >= 10:
                newname = name + f"E{i + 1}"
            print("name :", newname)
            pdurl = url[i]
            webmanager(newname, pdurl, text, photo, context, update)


def buttonmaker(update, context, photo):
    global newname
    global URLS
    global j
    global name
    global seasoncap
    global z
    global totbutton
    global u
    u = 1
    j = 1
    button = []
    for i in range(0, len(URLS)-1):
        button.append([InlineKeyboardButton(text=f'Episode {i+1}', url =URLS[i])])


    for l in range(1, 20):
        if re.search(f"S0{l}", newname):
            seasonname = name.replace(f"S0{l}", f"Season {l}")
        elif re.search(f"S{l}", newname):
            seasonname = newname.replace(f"S{l}", f"Season {l}")
    context.bot.send_photo(chat_id=chatid, photo=photo, caption=seasonname, reply_markup=InlineKeyboardMarkup(button))
    if len(URLS) % 2 == 0:
        leng = int(len(URLS) / 2)
        leng_type = "even"
    else:
        leng = len(URLS) - 1
        leng = int(leng / 2)
        leng_type = "odd"
    y = 0
    x = 1
    try:
        if leng_type == "even":
            print("even")
            for i in range(leng):
                ep1 = x
                ep2 = x + 1
                url1 = URLS[y]
                url2 = URLS[x]
                butt1 = f"[Episode {ep1}](buttonurl://{url1})"
                y = y + 1
                x = x + 1
                butt2 = f"[Episode {ep2}](buttonurl://{url2})"

                y = y + 1
                x = x + 1

                totbutton = totbutton + "\n" + butt1 + "\n" + butt2
        if leng_type == "odd":
            print("odd")
            for i in range(leng):
                ep1 = x
                ep2 = x + 1
                url1 = URLS[y]
                url2 = URLS[x]
                butt1 = f"[Episode {ep1}](buttonurl://{url1})"
                y = y + 1
                x = x + 1
                butt2 = f"[Episode {ep2}](buttonurl://{url2}:same)"

                y = y + 1
                x = x + 1
                totbutton = totbutton + butt1 + "\n" + butt2
            if leng_type == "odd":
                ep1 = x
                url1 = URLS[y]
                extrabutton = f"[Episode {ep1}](buttonurl://{url1})"
                totbutton = totbutton + "\n" + extrabutton

        seasoncap = seasonname + "\n" + totbutton

        print(seasoncap)
        update.message.reply_text(seasoncap)
        forwardphoto(update, context, photo, seasoncap)

    except:
        print("caption too long")
        u =1


    r = 1

    name = ""


def forwardphoto(update, context, photo, c):
    global r
    global u
    global seasoncap
    u = 1
    context.bot.send_photo(chat_id=chatid, photo=photo, caption=c)
    r = 1


    print("U reseted to ", u)

    seasoncap = ""


def main():
    global k
    global u
    global r
    print("Bot Has Started")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("Start", start_command))
    dp.add_handler(MessageHandler(Filters.photo, handle_photo))
    dp.add_handler(MessageHandler(Filters.text, handle_Seasons))
    if k == 1:
        updater.start_polling()
        k = k + 1
    r = 1
    u = 1


main()

