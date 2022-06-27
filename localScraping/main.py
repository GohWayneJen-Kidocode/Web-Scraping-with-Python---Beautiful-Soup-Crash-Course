from bs4 import BeautifulSoup

with open('base.html', 'r') as html_file:
    content = html_file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    # print(soup)
    # contentH5 = soup.find_all('h5')
    # # print(tags)
    # for course in contentH5:
    #     print(course.text)

    courseCards = soup.find_all('div', class_ = 'card')
    for course in courseCards:
        # print(course.h5)
        courseName = course.h5.text
        coursePrice = course.a.text.split()[-1]

        # print(courseName)
        # print(coursePrice)

        print(f'The {courseName} course costs {coursePrice}.')