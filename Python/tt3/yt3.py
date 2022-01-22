
from os import link
from pandas.core.frame import DataFrame
from selenium import webdriver
import pandas as pd
options = webdriver.ChromeOptions()
options.add_argument('headless')

# youtube to mp3
data = pd.read_csv('son/Desktop/TIL/Python/tt3/all.csv')
print(data['title'][0])


# Or export it in many ways, e.g. a list of tuples
tuples = [tuple(x) for x in df.values]
name_list = []
# or export it as a list of dicts
dicts = df.to_dict()
for i in range(106):
    name_list.append(dicts['title'][i])
fail = []
for url in name_list:
    try:
        #유튜브 전용 인스턴스 생성
        yt = YouTube(url)
        # 특정영상 다운로드
        # 확장자 변경
        file_name = yt.title
        save_dir = "./test/"
        yt.streams.filter(only_audio=True).first().download(save_dir, '{}.mp3'.format(file_name ))
        time.sleep(5)
        print('success')
    except:
        fail.append(url)
        print('fail2')
print(fail)


link_list = []
# 다운로드용 링크 생성
for i in range(106):
    try:
        name = data['title'][i]
        print(name)
        name = name.replace('https://www.youtube.com/watch?v=', '')
        print(name)
        target_address = main_address + str(name)
        driver.implicitly_wait(3)
        # url에 접근한다.
        driver.get(target_address)
        driver.implicitly_wait(3)
        p_element = driver.find_element_by_xpath("/html/body/div/div/div/div/a[1]").get_attribute('href')
        print(p_element)
        link_list.append(p_element)
    except: 
        print('fail')
for i in range(len(link_list)):
    print(i+1, link_list[i])

Data_list = DataFrame(link_list)
Data_list.to_csv('son/Desktop/TIL/Python/tt3/data_list.csv', header=False, index=False)

