from tkinter import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

def run():
    options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    url = "https://www.daejin.ac.kr/index.do?sso=ok"
    driver.get(url)

    # 팝업창 닫기
    try:
        popup = driver.window_handles
        for i in popup :
            if i != popup[0] : #리스트의 첫 값은 팝업창이 아니라 윈도우창!!!!!!
                driver.switch_to.window(i)
                driver.close()
        driver.switch_to.window(popup[0])
    except:
        pass

    driver.find_element(By.XPATH, "//*[@id='main']/div/div[1]/div/div/div[1]/div/ul/li[1]/a/dl/dt/div/span/img").click() # 포털대진 클릭
    driver.find_element(By.XPATH, "//*[@id='LOGIN_INPUT_ID']").send_keys(idEntry.get()) # id입력
    driver.find_element(By.XPATH, "//*[@id='LOGIN_INPUT_PW']").send_keys(pwEntry.get()) # pw입력
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div[1]/form/div/div/table/tbody/tr/td[2]/button").click() #로그인 클릭

    # 팝업창 닫기
    try:
        popup = driver.window_handles
        for i in popup :
            if i != popup[0] : #리스트의 첫 값은 팝업창이 아니라 윈도우창!!!!!!
                driver.switch_to.window(i)
                driver.close()
        driver.switch_to.window(popup[0])
    except:
        pass

    driver.find_element(By.XPATH, "//*[@id='main']/div/div[1]/div/div/div[1]/div/ul/li[1]/a/dl/dt/div/span/img").click() # 포털대진 클릭

    # 팝업창 닫기
    try:
        popup = driver.window_handles
        for i in popup :
            if i != popup[0] : #리스트의 첫 값은 팝업창이 아니라 윈도우창!!!!!!
                driver.switch_to.window(i)
                driver.close()
        driver.switch_to.window(popup[0])
    except:
        pass

    # frame -> 페이지 안에 또 다른 페이지를 넣는 것
    # 따라서 포털대진에 들어간 후 내부의 frame으로 들어가줘야 함
    driver.switch_to.frame(driver.find_element(By.NAME, "BBF"))
    driver.switch_to.frame(driver.find_element(By.NAME, "LF"))
    driver.find_element(By.XPATH, "//*[@id='MFX8']/table/tbody/tr/td[2]/a").click() # 성적 정보 클릭
    driver.find_element(By.XPATH, "//*[@id='MFX9']/ul/li[1]/a").click() # 성적 클릭

    driver.switch_to.default_content() # 아예 처음으로 이동
    driver.switch_to.frame(driver.find_element(By.NAME, "BBF"))
    driver.switch_to.frame(driver.find_element(By.NAME, "RF"))
    driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td/table[2]/tbody/tr[2]/td[1]/a").click() # 성적조회 및 성적표출력 클릭

    driver.switch_to.default_content() # 아예 처음으로 이동
    driver.switch_to.frame(driver.find_element(By.NAME, "BBF"))
    driver.switch_to.frame(driver.find_element(By.NAME, "RF"))
    driver.switch_to.frame(driver.find_element(By.NAME, "RTF"))
    dropdown = Select(driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[2]/select"))
    dropdown.select_by_value("1") # 전체 선택

    driver.switch_to.default_content() # 아예 처음으로 이동
    driver.switch_to.frame(driver.find_element(By.NAME, "BBF"))
    driver.switch_to.frame(driver.find_element(By.NAME, "RF"))
    driver.switch_to.frame(driver.find_element(By.NAME, "RCF"))
    averScore = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table[13]/tbody/tr/td[6]").text

    averScore = "전체평균 : " + averScore
    averScoreLabel = Label(window, text=str(averScore), font=20 ,height=2)
    averScoreLabel.grid(column=2, row=2)
    
if __name__ == "__main__" :
    window = Tk()
    window.title("성적확인")
    window.geometry("800x600")
    window.resizable(height=False, width=False)

    idLabel = Label(window, text="ID", font=14, height=2) #id라벨
    pwLabel = Label(window, text="PW", font=14, height=2) #pw라벨
    idEntry = Entry() #id입력창
    pwEntry = Entry() #pw입력창
    runBtn = Button(window, text="실행", height=3, width=10, command=run) # 실행버튼

    idLabel.grid(column=0, row=0)
    pwLabel.grid(column=0, row=1)
    idEntry.grid(column=1, row=0)
    pwEntry.grid(column=1, row=1)
    runBtn.place(x=400, y=500)

    window.mainloop()

