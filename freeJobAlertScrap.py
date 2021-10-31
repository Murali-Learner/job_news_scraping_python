import requests
from bs4 import BeautifulSoup

# 
# new_update=input("If You Want To New Updates [Y] [N]: ")
res=requests.get(f"https://www.freejobalert.com/notification-status/")
soup = BeautifulSoup(res.content, 'lxml')
body=soup.find('body')

# mainContent=(((body.find('div',{'class':'Main'})).find('div',{'class':'Sheet'})).find_all('div',{'id':'post-722762'})[0])

categories=((body.find('div',{'class':'Main'})).find('div',{'class':'Sheet'})).find('div',{'id':'post-722762'}).find_all('p')

# print(categories[2:].text)
newUpdates=(((body.find('div',{'class':'Main'})).find('div',{'class':'Sheet'})).find_all('div',{'id':'post-722762'})[0])

# print(newUpdates.get("class"))
_p=[textvalues.find("strong").text for textvalues in (newUpdates.find_all('p'))[2:]]
_tables=[tablevalues.find("tbody").find_all("tr")[1:] for tablevalues in (newUpdates.find_all("table"))[3:]]
# (_tables[0][0].find_all("td"))
def tdHandler(tdval):
    tdList=[]
    for tdsingle in tdval.find_all("td"):
        if(tdsingle.findChildren("a")==[]):
            tdList.append(tdsingle.text)
        else:
            tdList.append(tdsingle.find_all("a")[0].get("href"))
    return '-fjb-'.join(str(tdvalues) for tdvalues in tdList)
# tdHandler(table[0]).split("-fjb-")
[print((table)) for table in _tables]  
# print(tdHandler(_tables[0][0].find_all("td")).split("-fjb-"))
  
# for _trs in list(_tables[0]):
#     print(_trs.find_all("td"))
    # [print((tr)) for tr in (_trs.find_all("td"))]
job_dic={}
# def get_tablevalues(tablevalue):
#     return (tablevalue.find_all("td"))
for header in range(len(_p)):
    # tablevalue=get_tablevalues
    job_dic[_p[header]]=_tables[header]
# print(list(job_dic.keys())[0])
# print(list(job_dic.values())[0])
# get_tablevalues(_tables[0][0])
# print(len(_tables))
# print(((_tables[0][0]).find_all("td")))
# print(len(_tables))

# for p in _p:
#     print(p.find("strong").text)

   

# selection=categories[2:]+tablevals
# seleList=[]
# for i in range(len(selection)):
#     seleList.append(selection[i])
    
    # print(i+pi)
# print(len(selection))
# print(seleList)



# if new_update.lower() == "y":
#     print('New Updates\n')
#     newUpdates=(((body.find('div',{'class':'Main'})).find('div',{'class':'Sheet'})).find_all('div',{'id':'post-722762'})[0])
#     tablevals= ((newUpdates.find_all("table",{"border":"2"})))[1].find("tbody").find_all("tr")
#     for table in tablevals[1:]:
#         try:
#             postName=((table.find("td",{"style":"width: 64.8148%;"}).find("span")))
#             uploadDate=table.find("td")
#             moreinfo=table.find('td',{'style':'border: 1px solid #000000; width: 18.5185%;'}).find("a").get("href")
            
#             print(f"\t Upload Date: {uploadDate.text}\n")
#             print(f"\tPost Name: {postName.text}\n")
#             print(f"\tMore Info: {moreinfo}\n")
#         except:
#             pass
    
# elif new_update.lower() == "n":
#     categories=((body.find('div',{'class':'Main'})).find('div',{'class':'Sheet'})).find('div',{'id':'post-722762'}).find_all('p')
#     cat_list=[]
#     for i in range(len(categories)):
#         try:
#             cat_list.append([i].text)

#             print(f'{i+1}:{categories[i+2].text}')
#         except:
#             pass    


# print(tablevals[1:].spilt('\n'))
# tablevals= ((body.find('div',{'class':'Main'})).find('div',{'class':'Sheet'})).find('div',{'id':'post-722762'}).find_all("table").find('tbody').
# print(tablevals[1:].text)
# varList=[]
# for i in range(len(tablevals)):
#     varList.append(tablevals[i].text)
   
# print(varList.text)