#Thư viện
#Truy cập web và trình duyệt
from re import search
import webbrowser as wb
#Chuyển âm thanh thành văn bản
import speech_recognition as sr
#Chuyển văn bản thành âm thanh
from gtts import gTTS
import pyttsx3
#Xử lí thởi gian
import time
from datetime import date, datetime
#Lấy thông tin từ web
import requests
import ctypes
import json
import urllib
import urllib.request as urllib2
#Mở âm thanh
import playsound
#truy cập, xử lí file hệ thống
import os
#Thư viện Tkinter hỗ trợ giao diện
from tkinter.ttk import Frame, Button, Style
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as mbox
#Truy cập web, trình duyệt, hỗ trợ tìm kiếm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from youtube_search import YoutubeSearch
#from youtubesearchpython import SearchVideos
import wikipedia
#Chọn ngẫu nhiên
import random
#chuyển chữ số sang số
from word2number import w2n #tiếng anh
from vietnam_number import w2n # tiếng việt

#khai báo
wikipedia.set_lang('vi')
language = 'vi'
robot_ear = sr.Recognizer() 
robot_speak = pyttsx3.init()
robot_brain = "Xin chào master"
master = ""
#Giao diện
window = Tk()   
window.geometry("1000x600")
window.title("AI ALICE")
window.configure(bg = "#333131")
canvas = Canvas(
    window,
    bg = "#333131",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas1 = Canvas(
    window,
    bg = "#F8EEEE",
    bd = 0,
    height = 541,
    width = 473,
    highlightthickness = 0,
    relief = "ridge"
)

canvas1.place(x = 0, y = 0)
text_area = Text(
    canvas1, 
    height= 541, 
    width= 473
)
text_area.place(x = 0, y = 0)

#hàm giúp alice nói
def speak(robot_brain):
    print("Alice: " + robot_brain)
    tts = gTTS(text=robot_brain, lang='vi', slow=False)
    tts.save("sound.mp3")
    text_area.insert(INSERT,"ALice: "+robot_brain+"\n")
    playsound.playsound("sound.mp3")
    os.remove("sound.mp3")
    robot_speak.runAndWait()
    window.update()

#Hàm nghe lệnh
def get_audio():
    playsound.playsound("Ping.mp3")
    time.sleep(2)
    print("\nALice:  Đang nghe ...")
    robot_ear = sr.Recognizer()
    with sr.Microphone() as source:
        robot_ear.pause_threshold = 2
        audio = robot_ear.listen(source, phrase_time_limit=6)
        try:
            master = robot_ear.recognize_google(audio, language="vi-VN")
            print("Master: " + master)
            text_area.insert(INSERT,"Master: "+master+"\n")
            return master.lower()
        except:
            print("\n")
            return ""
    
#hàm nói xin chào
def Hello():
    hour = datetime.now().hour
    if hour >= 1 and hour < 12: 
        robot_brain = "Chào buổi sáng tốt lành, master"
    elif hour >= 12 and hour < 18: 
        robot_brain = "Chào buổi chiều tốt lành, master"
    elif hour >= 18 and hour < 22: 
        robot_brain = "Chào buổi tối tốt lành, master"
    else:
        robot_brain = "Buổi đêm vui vẻ, master"
    speak(robot_brain)
    robot_brain = "Alice đã sẵn sàng, master?"
    speak(robot_brain)
    window.update()

#hàm lấy thời gian
def time_message():
    robot_brain = "Bạn muốn xem thời gian cụ thể nào?"
    speak(robot_brain)
    master = get_audio()
    now = datetime.now()
    time0 = now.strftime("%w")
    time1 = int(time0)
    time2 = "Chủ nhật"
    if "giờ" in master: 
        robot_brain = "Bây giờ là %d giờ %d phút %d giây" % (now.hour, now.minute, now.second)
    elif "ngày" in master:
        robot_brain = "Hôm nay là ngày %d tháng %d năm %d" % (now.day, now.month, now.year)
    elif "thứ" in master and time1!=0:
        robot_brain = "Hôm nay là thứ %s" % (time1+1)
    elif "thứ" in master and time1==0:
        robot_brain = "Hôm nay là thứ %s" % (time2)
    elif "hiện tại" in master and time1!=0:
        robot_brain = "Hôm nay là thứ %s ngày %d tháng %d năm %d và bây giờ là %d giờ %d phút %d giây" % (time1+1,now.day, now.month, now.year,now.hour, now.minute, now.second)
    elif "hiện tại" in master and time1==0:
        robot_brain = "Hôm nay là thứ %s ngày %d tháng %d năm %d và bây giờ là %d giờ %d phút %d giây" % (time2,now.day, now.month, now.year,now.hour, now.minute, now.second)
    else:
        speak("Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")
        time.sleep(6)
    speak(robot_brain)


#Tìm kiếm trên google
def findgoogle():
    robot_brain = "Ngài muốn tìm gì trên google, master?"
    speak(robot_brain)
    search = get_audio()
    url = f"http://www.google.com/search?q={search}"
    wb.get().open(url)
    robot_brain = f"Đây là kết quả của tìm kiếm {search} trên google, thưa ngài!!"
    speak(robot_brain)

#Tìm kiếm và mở video trong youtube
def findyoutube():
    robot_brain = "Ngài muốn tìm gì trên youtube, master?"
    speak(robot_brain)
    search = get_audio()
    url = f"http://www.youtube.com/search?q={search}"
    wb.get().open(url)
    robot_brain = f"Đây là kết quả của tìm kiếm {search} trên Youtube, thưa ngài!!"
    speak(robot_brain)
    speak("Ngài muốn mở video luôn không?")
    answer = get_audio()
    if "có" in answer:
        while True:
            result = YoutubeSearch(search, max_results=10).to_dict()
            if result:
                break
        speak("Ngài muốn mở video số mấy vậy?chỉ nói số thôi nha")
        number = get_audio()
        for i in range(len(result)):
            i = w2n(number)
            url = f"http://www.youtube.com" + result[i]['url_suffix']
        wb.get().open(url)
        speak("Mời ngài thưởng thức video")
    elif "không" in answer:
        speak("Ngài còn yêu cầu gì nữa, master?")
        pass

#Xem thời tiết
def current_weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    # Đường dẫn trang web để lấy dữ liệu về thời tiết
    ow_url = "https://api.openweathermap.org/data/2.5/weather?"
    # lưu tên thành phố vào biến city
    city = get_audio()
    # nếu biến city != 0 và = False thì để đấy ko xử lí gì cả
    if not city:
        pass
    # api_key lấy trên open weather map
    api_key = "3eb48f07c0a964bc11da07e05083f94b"
    # tìm kiếm thông tin thời thời tiết của thành phố
    call_url = ow_url + "q=" + city + "&appid=" + api_key +"&units=metric"
    # truy cập đường dẫn của dòng 188 lấy dữ liệu thời tiết
    response = requests.get(call_url)
    # lưu dữ liệu thời tiết dưới dạng json và cho vào biến data
    data = response.json()
    print(data)
    # kiểm tra nếu ko gặp lỗi 404 thì xem xét và lấy dữ liệu
    if data["cod"] != "404":
        # lấy value của key main
        city_res = data["main"]
        # nhiệt độ hiện tại
        current_temperature = city_res["temp"]
        # áp suất hiện tại
        current_pressure = city_res["pressure"]
        # độ ẩm hiện tại
        current_humidity = city_res["humidity"]
        # thời gian mặt trời
        suntime = data["sys"]
        # 	lúc mặt trời mọc, mặt trời mọc
        sunrise = datetime.fromtimestamp(suntime["sunrise"])
        # lúc mặt trời lặn
        sunset = datetime.fromtimestamp(suntime["sunset"])
        # thông tin thêm
        wthr = data["weather"]
        # mô tả thời tiết
        weather_description = wthr[0]["description"]
        # Lấy thời gian hệ thống cho vào biến now
        now = datetime.now()
        # hiển thị thông tin với người dùng
        content = f"""
        Hôm nay là ngày {now.day} tháng {now.month} năm {now.year}
        Mặt trời mọc vào {sunrise.hour} giờ {sunrise.minute} phút
        Mặt trời lặn vào {sunset.hour} giờ {sunset.minute} phút
        Nhiệt độ trung bình là {current_temperature} độ C
        Áp suất không khí là {current_pressure} héc tơ Pascal
        Độ ẩm là {current_humidity}%
        """
        speak(content)
    else:
        # nếu tên thành phố không đúng 
        speak("Không tìm thấy địa chỉ của bạn")

#Đổi ảnh nền
def change_wallpaper():
    speak("Đang thay đổi!!! Ngài vui lòng đợi trong giây lát")
    api_key = "hLcHOGGlLwDNQGimKpkZMAd5HCEqGJXgKtnfnO4v3dk"
    url = 'https://api.unsplash.com/photos/random?client_id=' + \
          api_key  # pic from unspalsh.com
    f = urllib2.urlopen(url)
    json_string = f.read()
    f.close()
    parsed_json = json.loads(json_string)
    photo = parsed_json['urls']['full']
    # Location where we download the image to.
    urllib2.urlretrieve(photo, "img\\a.png")
    image = os.path.join("C:\\Users\\ADMIN\\Desktop\\Python\\Morph\\.venv\\Scripts\\AIALICE-main\\a.png")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 3)
    speak("Đã đổi thành công. Bạn ra home xem có đẹp không nha ?")

#phát nhạc trong máy
def play_music():
    speak("Đây là danh sách nhạc trong thư mục của ngài")
    # path là tham số chứa đường dẫn thư mục chứa nhạc
    path = "music"
    myPATH = path
    # lấy file nhạc ra
    ds = os.listdir(myPATH)
    print(ds)
    #in danh sách bài hát
    for a in ds:
        print(str(ds.index(a))+ ":" + a)
        robot_brain= str(ds.index(a))+ ":" + a
        speak(robot_brain)
    speak("Ngài muốn chọn bài hay phát hết??")
    master = get_audio()
    if "chọn bài" in master:
    # mở bài nhạc đã chọn
        speak("Ngài hãy chọn bài!! Chỉ nói số thôi nha ")
        while True:
            number = get_audio()
            i= int(w2n(number))
            speak("Mời Ngài thưởng thức")
            print("\nĐang phát bài :  " + ds[i])
            os.system(myPATH + "\\" + ds[i])
            print("\nĐã phát xong bài : \t\t" + ds[i])
            speak("Đã hết")
            speak("bạn có muốn nghe nữa không??")
            master = get_audio()
            if "không" in master:
                break
    elif "phát hết" in master:
    # phát hết nhạc trong mục
        for i in range(len(ds)):
            print("\nĐang phát bài :  " + ds[i])
            os.system(myPATH + "\\" + ds[i])
            print("\nĐã phát xong bài : \t\t" + ds[i])
        speak("Đã hết")

#wikipedia
def knowledge():
    try:
        speak("Thưa Ngài, Ngài muốn tìm gì ạ ?")
        text = get_audio()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        dem = 0
        for content in contents[1 : ]:
            if dem < 2:
                speak("Bạn có muốn biết thêm không ???")
                ans = get_audio()
                if 'có' not in ans:
                    break
            dem += 1
            speak(content)
        speak("Đã hết cảm ơn Ngài đã lắng nghe")
    except:
         speak(f"Alice không định nghĩa được thuật ngữ của Ngài !!!")

#chức năng
def func1():
    content="""
            Alice có những chức năng sau đây:
            1.Chào hỏi
            2.Thông báo thời gian 
            3.Dự báo thời tiết 
            4.Tìm kiếm trên google
            5.Tìm kiếm và mở video trên youtube
            6.Thay đổi hình nền máy tính
            7.Mở nhạc trong thư mục có sẵn
            8.Đọc thông tin trên wikipedia
            9.Tạm biệt"""
    speak(content)
    
def main():
    print("AI Alice Starting......")
    Hello()
    while True:
        #.lower() có tác dụng với cả chữ thường
        
        master = get_audio()
        #master = "Google"
        #get_command()
        if "thời gian" in master:
            time_message()
        elif master == "":
            speak("Ngài hãy ra lệnh đi!!")
        elif "google" in master:
            findgoogle()
        elif "youtube" in master:
            findyoutube()
        elif "wiki" in master:
            knowledge()
        elif "mở nhạc" in master:
            play_music()
        elif "đổi hình nền" in master:
            change_wallpaper()
        elif "thời tiết" in master:
            current_weather()
        elif "chức năng" in master:
            func1()
        elif "tạm biệt" in master:
            robot_brain = "tạm biệt ngài!! Chúc ngài may mắn !!!"
            speak(robot_brain)
            break
        else:
            speak("Tôi chưa hiểu ý của ngài, Ngài lặp lại được không?")

#Giao  dien
m = Image.open("C:\\Users\\ADMIN\\Desktop\\Python\\Morph\\.venv\\Scripts\\AIALICE-main\\img0.png")
img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    bg = "#333131",
    highlightthickness = 0,
    command = main,
    activebackground= "#333131",
    relief = "flat")

b0.place(
    x = 667, y = 278,
    width = 134,
    height = 130,
    )
Label = Label(
    window,
    text= "Trợ Lý ảo Alice",
    bg = "#3C3939",
    fg= "white",
    font ="Inter, 40",
)
Label.place(
    x= 559, y=31,
    width = 376,
    height =113
)
entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    207.5, 570.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#fbf8f8",
    highlightthickness = 0,
    )

entry0.place(
    x = 36.5, y = 550,
    width = 342.0,
    height = 39)
img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    bg = "#333131",
    highlightthickness = 0,
    activebackground= "#333131",
    relief = "flat")

b1.place(
    x = 408, y = 550,
    width = 51,
    height = 41)
window.resizable(False, False)
window.mainloop()
