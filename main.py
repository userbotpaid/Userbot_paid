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

link = ""
sorted_links = []
gg = 0
movie_varient = []
length = ''
url = ""
photo = ""
name = ""
caption = ""
seasoncap = ""
newname = ""
txxt = ""
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
length_var = 0


def start_command(update, context):
    update.message.reply_text("Sent Me Any Pdisk Post")
    chatid = update.message.chat_id
    print(chatid)
def reset_command(update, context):
    global DB
    global t
    global driver
    global name
    global chatid
    global w
    global u
    global k
    global n
    global length
    global url
    global photo
    global text
    global URLS
    global movie_varient
    global length_var
    global txxt
    global r
    global gg
    global sorted_links
    global caption
    global seasoncap
    global newname
    global rawname
    global cap
    global j
    gg = 0
    movie_varient = []
    sorted_links = []
    length = ''
    url = ""
    photo = ""
    name = ""
    caption = ""
    seasoncap = ""
    newname = ""
    txxt = ""
    r = 1
    rawname = ""
    chatid = update.message.chat_id
    print(chatid)
    DB = []
    movie_varient = []
    length = ''
    u = 1
    chatid = ""
    length_var = 0
    url = []
    URLS = []
    text = ""
    cap = ""
    t = 1
    
    u = 1
    w = 0
    n = 1
    j = 1
    update.message.reply_text("Reset And Ready")
    w = 1
    main()

def link_command(update, context):
    global sorted_links
    link = str(update.message.text)
    print(link)
    link = link.replace("/link", "")
    name_matches = re.finditer("📝 File Name: ", link)
    name_match_positions = [match.start() + 13 for match in name_matches]

    name_end_matches = re.finditer("⚖️ File Size", link)
    name_end_match_positions = [match.start() - 2 for match in name_end_matches]

    names = []
    for idx, name in enumerate(name_match_positions):
        s = name
        e = name_end_match_positions[idx]
        names.append(link[s:e])

    links = re.findall("(?P<url>https?://[^\s]+)", link)

    s = []
    e = []
    for name in names:
        match = re.search(r'S\d\dE\d\d', name)
        se = match.group()
        s.append(se[1:3])
        e.append(se[4:6])

    items_raw = {}
    for idx, item in enumerate(names):
        items_raw[idx] = (s[idx], e[idx], links[idx])
    sort1 = sorted(items_raw.items(), key=lambda x: (x[1], x[0]))

    sorted_links = [link[1][2] for link in sort1]

    print(sorted_links)
    update.message.reply_text("Hmm Sent the Name /name")

def name_command(update, context):
    global DB
    global neem
    global sorted_links
    neem = str(update.message.text)
    if len(DB) != 3:
        DB.append(neem)
        if len(DB) == 1:
            update.message.reply_text("Ok Now sent season number /name\nExample: 01")
        if len(DB) == 2:
            update.message.reply_text("Ok Now sent Starting Episode /name\nExample: 01")
    else:
        update.message.reply_text("Ok Great!!, Please Wait")

    if len(DB)==3:
        update.message.reply_text("OK")
        neem = DB[0]
        se = DB[1]
        ep = DB[2]
        neem = neem.replace("/name", "")
        se = str(se.replace("/name",""))
        ep = int(ep.replace("/name", ""))
        ll = 0
        butt1 = ""
        if (len(sorted_links)% 2) == 0:
            x = 1
            for i in range(0, int((sorted_links) / 2)):
                y = x + 1
                if i == 0:
                    butt1 = f"Episode {i + ep}={sorted_links[i]} + Episode {i + gg + 1}={sorted_links[i + 1]}\n"
                else:
                    butt1 = butt1 + f"Episode {i + x + ep}={sorted_links[i + x]} + Episode {i + ep + y}={sorted_links[i + y]}\n"
                    x = x + 1
                update.message.reply_text(butt1)

        else:
            ken = len(sorted_links) + 1
            ken = int(ken / 2)
            x = 1
            for i in range(0, ken):
                if i == 0:
                    butt1 = f"Episode {i + ep}={sorted_links[i]} + Episode {i + ep + 1}={sorted_links[i + 1]}\n"
                else:
                    try:
                        y = x + 1
                        butt1 = butt1 + f"Episode {i + x + ep}={sorted_links[i + x]} + Episode {i + ep + y}={sorted_links[i + y]}\n"
                        x = x + 1
                    except:
                        butt1 = butt1 + f"Episode {i + x + ep}={sorted_links[i + x]}"
                        update.message.reply_text(butt1)





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
    global movie_varient
    global length_var
    global txxt
    URLS = []
    url = []
    chatid = update.message.chat_id
    print(chatid)

    update.message.reply_text("OK Wait Let Me HAndle Things From Now")
    photo = update.message.photo[-1].file_id

    text = str(update.message.caption)
    txxt = text
    print(text)
    url = re.findall("(?P<url>https?://[^\s]+)", text)
    print(url)
    regrex_pattern = re.compile(pattern="["
                                        u"\U0001F600-\U0001F64F"  # emoticons
                                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                        "]+", flags=re.UNICODE)
    if re.search(":-", txxt):
        txxt = txxt.replace(":-", "")
    elif re.search(":", txxt):
        txxt = txxt.replace(":", "")
    elif re.search("", txxt):
        txxt = txxt.replace(":", "")
    txxt = txxt.replace("-", "")
    textd = regrex_pattern.sub(r'', txxt)

    movie_var = re.findall(r'\n(.*?)(\n)?http', textd)

    movie_varient = [item[0] for item in movie_var]
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

    elif re.search("🎬", rawname):
        name = rawname.replace("🎬", "")

    elif re.search("📼", rawname):
        name = rawname.replace("📼", "")

    else:
        name = rawname

    length = len(url)
    length_var = len(movie_varient)
    if re.search("Season", text):
        print("season Detected")
        URLS = []
        if n == 1:
            name = ""
            n = n + 1
        update.message.reply_text(
            "OK Its a Series \n Sent The Name Of The Series With Season Number\nExample:Money Heist S01 ")

        u = 1

        if re.search("Season", text):
            w = 1
    else:
        print("Movie Detected")
        u = 1
        if re.search("How", text):
            length = length - 1
            length_var = length_var - 1
        for i in range(0, length):
            print("i = ", i)
            pdurl = url[i]
            nam = str(name.encode('ascii', errors='ignore').decode()) + " - " + movie_varient[i]
            webmanager(nam, pdurl, text, photo, context, update)


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
        email.send_keys("dhanush544531@gmail.com")

        password = driver.find_element_by_xpath('//*[@id="app"]/article/div[1]/div[2]/div[2]/span/input')
        password.send_keys("dhanush787")

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
    filename.send_keys(name.encode('ascii', errors='ignore').decode())

    uploadbutton = driver.find_element_by_xpath('//*[@id="control-hooks"]/div[5]/div/div/div/button/span')
    uploadbutton.click()
    update.message.reply_text(f"Uploaded {name}")
    driver.get('http://www.pdisk.net/home')
    driver.refresh()
    view = driver.find_element_by_xpath(
        '//*[@id="app"]/section/main/section/main/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]')
    purl = view.text
    pdiskurl = "http://www.pdisk.net/share-video?videoid={}".format(purl)
    print(pdiskurl)

    URLS.append(pdiskurl)
    if r == 1:
        cap = k.replace(url, pdiskurl)  # url in the urls of the previous text

        r = 2
    else:
        cap = cap.replace(url, pdiskurl)

        print("length= ", length)
        if u == length:
            forwardphoto(update, context, photo, cap)
            if re.search("Season", text):
                print("called button Maker")
                buttonmaker(update, context, photo)
            else:
                movie_button(update, context, photo)
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
    global gg
    r = 1
    if w == 1:
        name = ""
        name = str(update.message.text)

        w = w + 1
        if re.search("How", text):
            length = length - 1
        w = 2
    if name != "":
        if w == 4:
            gg = int(update.message.text)
            for i in range(0, length):

                if i + gg <= 9:
                    newname = name + f"E0{i + gg}"
                elif i + gg >= 10:
                    newname = name + f"E{i + gg}"

                pdurl = url[i]
                webmanager(newname, pdurl, text, photo, context, update)
        else:
            update.message.reply_text("Episode")
            w = 4



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
    for i in range(0, len(URLS)):
        button.append([InlineKeyboardButton(text=f'Episode {i + gg}', url=URLS[i])])

    for l in range(1, 20):
        if re.search(f"S0{l}", newname):
            seasonname = name.replace(f"S0{l}", f"Season {l}")
        elif re.search(f"S{l}", newname):
            seasonname = newname.replace(f"S{l}", f"Season {l}")
    context.bot.send_photo(chat_id=chatid, photo=photo, caption=seasonname, reply_markup=InlineKeyboardMarkup(button))
    if (len(URLS)%2) == 0:
        x = 1
        for i in range(0, int(len(URLS)/2)):
            y = x + 1
            if i == 0:
                butt1 = f"Episode {i + gg}={URLS[i]} + Episode {i + gg + 1}={URLS[i + 1]}\n"
            else:
                butt1 = butt1 + f"Episode {i + x + gg}={URLS[i + x]} + Episode {i + gg + y}={URLS[i + y]}\n"
                x = x+1
    else:
        ken = len(URLS)+1
        ken = int(ken/2)
        x=1
        for i in range(0, ken):
            if i == 0:
                    butt1 = f"Episode {i + gg}={URLS[i]} + Episode {i + gg + 1}={URLS[i + 1]}\n"
            else:
                try:
                    y = x + 1
                    butt1 = butt1 + f"Episode {i + x + gg}={URLS[i + x]} + Episode {i + gg + y}={URLS[i + y]}\n"
                    x = x + 1
                except:
                    butt1 = butt1 + f"Episode {i + x + gg}={URLS[i + x]}"





    update.message.reply_text(butt1)

    r = 1

    name = ""


def movie_button(update, context, photo):
    global movie_varient
    global length_var
    global URLS
    button = []

    for i in range(0, len(URLS)):
        button.append([InlineKeyboardButton(text=movie_varient[i], url=URLS[i])])

    context.bot.send_photo(chat_id=chatid, photo=photo, caption=name, reply_markup=InlineKeyboardMarkup(button))


def forwardphoto(update, context, photo, c):
    global r
    global u
    global seasoncap
    u = 1
    c = re.sub('@[^\s]+', '@AllMoviesAskForMovies', c)
    context.bot.send_photo(chat_id=chatid, photo=photo, caption=c)
    r = 1

    print("U reseted to ", u)

    seasoncap = ""


def main():
    global k
    global u
    global r
    print("Bot Has Started")
    updater = Updater("1745412728:AAGJMHH85G4EP-ngtvn4xTVcegJiTzjFHck", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("Start", start_command))
    dp.add_handler(CommandHandler("Link", link_command))
    dp.add_handler(CommandHandler("Name", name_command))
    dp.add_handler(CommandHandler("Reset", reset_command))
    dp.add_handler(MessageHandler(Filters.photo, handle_photo))
    dp.add_handler(MessageHandler(Filters.text, handle_Seasons))
    if k == 1:
        updater.start_polling()
        k = k + 1
    r = 1
    u = 1


main()
