from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
from telegram.ext import *
from telegram.ext import MessageHandler, Filters
import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import re
link = ""
p = False
pp = True
fileneemDB = []
pas = ""
sorted_links = []
credDB = []
cred = ""
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
fileneem = ""
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
kkkk = 0



def start_command(update, context):
    update.message.reply_text("Sent ME The Any Pdisk Post")
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
    global kkkk
    kkkk = 0
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
    k = 1
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
    global pp
    global pas
    URLS = []
    url = []
    chatid = update.message.chat_id
    print(chatid)

    if p == True:
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
        URLS = []

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
    else:
        update.message.reply_text("You are Not Loged in\n  sent /login yourpassword")







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
    global p
    global pp
    global pas

    if t == 1:

        driver.get('http://www.pdisk.net/upload?type=url')
        email = driver.find_element_by_xpath('//*[@id="app"]/article/div[1]/div[2]/div[1]/span/input')
        email.send_keys("dhanush544531@gmail.com")

        password = driver.find_element_by_xpath('//*[@id="app"]/article/div[1]/div[2]/div[2]/span/input')
        password.send_keys(pas)

        submit = driver.find_element_by_xpath('//*[@id="app"]/article/div[1]/div[2]/div[3]/button/span')
        submit.click()
        t = t + 1


    time.sleep(1)
    driver.get('http://www.pdisk.net/upload?type=url')
    if t == 2:
        try:
            nextbutton = driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/div/div[3]')
            update.message.reply_text("Login Sucessfull")

        except:
            update.message.reply_text("Invalid Password\nSend /login yourpassword")
            t =1
            p = False
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
    update.message.reply_text(f"Uploaded {name.encode('ascii',errors='ignore').decode()}")
    driver.get('http://www.pdisk.net/home')
    driver.refresh()
    view = driver.find_element_by_xpath(
        '//*[@id="app"]/section/main/section/main/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]')
    purl = view.text
    pdiskurl = "http://www.pdisk.net/share-video?videoid={}".format(purl)
    print(pdiskurl)

    URLS.append(pdiskurl)

    if r == 1:
        cap = k.replace(url, pdiskurl)  # url is the urls of the previous text
        print("k.replcae === ", cap)
        r = 2
        if u == length:
            forwardphoto(update, context, photo, cap)
            movie_button(update, context, photo)


    else:
        cap = cap.replace(url, pdiskurl)
        print("caption Before Forwareding === ", cap)
        print("length= ", length)
        if u == length:
            print(cap)
            forwardphoto(update, context, photo, cap)
            movie_button(update, context, photo)
            print(u, length)
        else:
            print(u, length)
    u = u + 1


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

def handle_files(update,context):
    global fileneem
    global h
    global fileneemDB

    time.sleep(7)
    fileneem = str(update.message.document.file_name)
    fileneemDB.append(fileneem)

    update.message.reply_text("OK please Wait I Will Upload the files and sent in back to u")
    context.bot.forward_message(chat_id='1676646973', from_chat_id="868213406", message_id=update.effective_message.message_id)
def url_command(update,context):
    url = str(update.message.text)
    url = url.replace("/url ", "")
    print(url)
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
    global fileneem
    global fileneemDB
    global kkkk
    global p

    fileneem = fileneemDB[kkkk]

    if p == True:
        if t == 1:
            driver.get('http://www.pdisk.net/upload?type=url')
            email = driver.find_element_by_xpath('//*[@id="app"]/article/div[1]/div[2]/div[1]/span/input')
            email.send_keys("dhanush544531@gmail.com")

            password = driver.find_element_by_xpath('//*[@id="app"]/article/div[1]/div[2]/div[2]/span/input')
            password.send_keys(pas)

            submit = driver.find_element_by_xpath('//*[@id="app"]/article/div[1]/div[2]/div[3]/button/span')
            submit.click()
            t = t + 1

        time.sleep(1)
        driver.get('http://www.pdisk.net/upload?type=url')
        if t == 2:
            try:
                nextbutton = driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/div/div[3]')
                context.bot.send_message(chat_id="868213406", text="Login Sucessfull")

            except:
                context.bot.send_message(chat_id="868213406", text="Invalid Password\nSend /login yourpassword")
                t = 1
                p = False
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
        filename.send_keys(fileneem)

        uploadbutton = driver.find_element_by_xpath('//*[@id="control-hooks"]/div[5]/div/div/div/button/span')
        uploadbutton.click()
        driver.get('http://www.pdisk.net/home')
        driver.refresh()
        driver.refresh()
        view = driver.find_element_by_xpath('//*[@id="app"]/section/main/section/main/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[2]')
        purl = view.text
        pdiskurl = "http://m.pdisk.net/share-video?videoid={}".format(purl)
        print(pdiskurl)
        context.bot.send_message(chat_id="868213406", text=pdiskurl)
        kkkk = kkkk + 1

    else:
        context.bot.send_message(chat_id="868213406", text="You are Not Loged in\nsent /login yourpassword")

def login_command(update,context):
    global pp
    global p
    global pas
    temp = str(update.message.text)
    pas = temp.replace("/login ", "")
    update.message.reply_text("Trying To Login")
    if pas != "":
        pp = True
        p = True
        update.message.reply_text("Sent The Message Again")
    else:
        update.message.reply_text("Invailid Password")







def main():
    global k
    global u
    global r
    print("Bot Has Started")
    updater = Updater("1664124045:AAGN4IzOmw_PrwSTR9NSx9Ri7Vp4j3-KpIQ", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("Start", start_command))
    dp.add_handler(CommandHandler("Link", link_command))
    dp.add_handler(CommandHandler("Name", name_command))
    dp.add_handler(CommandHandler("Reset", reset_command))
    dp.add_handler(CommandHandler("Login", login_command))
    dp.add_handler(CommandHandler("Url", url_command))
    dp.add_handler(MessageHandler(Filters.photo, handle_photo))

    dp.add_handler(MessageHandler(Filters.document, handle_files))
    if k == 1:
        updater.start_polling()
        k = k + 1
    r = 1
    u = 1


main()
