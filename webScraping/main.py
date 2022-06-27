from bs4 import BeautifulSoup
import requests
import time

def findJoba():
    print('Put in some skills that you are now familiar with.')
    unfamiliarSkill = input('>')
    print(f'Filtering out {unfamiliarSkill}')
    htmlText = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    # print(htmlText)
    soup = BeautifulSoup(htmlText, 'lxml')
    # jobs = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
    jobss = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, jobs in enumerate(jobss):
        publishedDate = jobs.find('span', class_ = 'sim-posted').span.text

        if 'few' in publishedDate:
            company = jobs.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = jobs.find('span', class_ = 'srp-skills').text.replace(' ','')
            info = jobs.header.h2.a['href']
            if unfamiliarSkill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company hiring: {company.strip()} \n")
                    f.write(f"Skills required: {skills.strip()} \n")
                    f.write(f"More information at: {info}")
                print(f'File saved in {index}')

                print('*' * 30)

if __name__ == '__main__':
    while True:
        findJoba()
        timeWait = 15
        print(f"Waiting {timeWait} minutes...")
        time.sleep(timeWait * 60)
        