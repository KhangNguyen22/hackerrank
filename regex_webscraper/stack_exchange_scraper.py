import bs4,sys,re
# text = sys.stdin.read()
text = open("input02.txt","r").read()
soup = bs4.BeautifulSoup(text,'html.parser')
regex = re.compile(r'\s*question-summary-\s*')
list_div = soup.find_all("div",{"class":"question-summary"})
list_a = soup.find_all("a",{"class":"question-hyperlink"})
ago = soup.find_all("span",{"class":"relativetime"})
list_id = []
list_question = []
list_time = []
# print(list_div[1])
for idx,item in enumerate(list_div):
    s= list_div[idx]['id']
    list_id.append(regex.sub('',s))
# print(list_id)
for idx,ittem in enumerate(list_a):
    list_question.append(list_a[idx].getText())
    # print(s)
for idx,item in enumerate(ago):
    list_time.append(ago[idx].getText())
# print(list_time)
for idx, item in enumerate(list_id):
    print(item+";"+list_question[idx].replace("'","&#39;")+";"+list_time[idx])