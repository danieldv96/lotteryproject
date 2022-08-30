import requests
import bs4
import pandas as pd
loturl = "https://www.loterias.com/baloto/resultados/{}"


def funcbaloto(url):
    base_url = url
    anios = [2010, 2011, 2012, 2013, 2014, 2015,
             2016, 2017, 2018, 2019, 2020, 2021, 2022]
    mydict = {}
    mylist = []
    myloto = {}
    lotolist = []
    exceptlist = []
    luckynumber = []
    i = 0
    j = 0

    for n in anios:
        i = 0
        j = 0
        mylist = []
        lotolist = []
        scrape_url = base_url.format(n)
        res = requests.get(scrape_url)
        soup = bs4.BeautifulSoup(res.text, "lxml")
        revrequest = soup.select("br")
        ballinfo = soup.select(".ball")
        if n == 2017:
            # this year was when revancha was created, thus exception is needed
            for n in range(18, 104):
                exceptlist.append(revrequest[n].next_sibling)

        if n in anios[:7]:
            for item in revrequest:

                if item.next_sibling == 'Millions':
                    continue
                while j % 6 != 0 or j == 0:

                    mylist.append(int(ballinfo[j].getText()))
                    j += 1
                if j % 6 == 0 and j != len(ballinfo):
                    mydict[item.next_sibling] = mylist
                    mylist = []
                    mylist.append(int(ballinfo[j].getText()))
                    j += 1
        if n == anios[7]:
            for item in revrequest:

                if item.next_sibling in exceptlist:

                    if item.next_sibling == 'Millions':
                        continue
                    while j % 6 != 0 or j == 0:

                        mylist.append(int(ballinfo[j].getText()))
                        j += 1
                    if j % 6 == 0 and j != len(ballinfo):
                        mydict[item.next_sibling] = mylist
                        mylist = []
                        mylist.append(int(ballinfo[j].getText()))
                        j += 1

                else:

                    if item.next_sibling == 'Millions':
                        continue
                    while j % 6 != 0 or j == 0:

                        mylist.append(int(ballinfo[j].getText()))
                        j += 1
                    if j % 6 == 0 and j != len(ballinfo):
                        mydict[item.next_sibling] = mylist
                        mylist = []
                        lotolist.append(int(ballinfo[j].getText()))
                        j += 1
                    while j % 6 != 0:

                        lotolist.append(int(ballinfo[j].getText()))
                        j += 1
                    if j % 6 == 0 and j != len(ballinfo):
                        myloto[item.next_sibling] = lotolist
                        lotolist = []
                        mylist.append(int(ballinfo[j].getText()))
                        j += 1
        if n in anios[8:]:
            for item in revrequest:

                if item.next_sibling == 'Millions':
                    continue
                while j % 6 != 0 or j == 0:

                    mylist.append(int(ballinfo[j].getText()))
                    j += 1
                if j % 6 == 0 and j != len(ballinfo):
                    mydict[item.next_sibling] = mylist
                    mylist = []
                    lotolist.append(int(ballinfo[j].getText()))
                    j += 1
                while j % 6 != 0:
                    lotolist.append(int(ballinfo[j].getText()))
                    j += 1
                if j % 6 == 0 and j != len(ballinfo):
                    myloto[item.next_sibling] = lotolist
                    lotolist = []
                    mylist.append(int(ballinfo[j].getText()))
                    j += 1
    normal = pd.DataFrame.from_dict(mydict, orient='index')
    revancha = pd.DataFrame.from_dict(myloto, orient='index')
    lottery = pd.concat([normal, revancha], axis=0)

    for k in range(0, 6):
        luckynumber.append(lottery[k].value_counts().idxmax())

    print(luckynumber)
    return luckynumber


if __name__ == '__main__':
    funcbaloto(loturl)
