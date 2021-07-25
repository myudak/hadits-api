import requests as rq
from bs4 import BeautifulSoup as bs

def cari():

  link="https://www.hadits.id/"

  #ke web +parse
  a = rq.get(link)
  soup = bs(a.text,"html.parser")

  #nemuin acak
  c = soup.find("input",{"value":"Hadits Acak"})

  #ketemu
  temuan = c['onclick'][18:-1]
  webAcak = rq.get(link+temuan)
  soup = bs(webAcak.text,"html.parser")

  src = soup.select('.hadits-header  h2')

  judul = soup.select(".hadits-content h1")[0].text

  isi = soup.select(".hadits-content p")[0].text

  terjemah = soup.select(".hadits-content >p")[1].text

  objek = dict()
  objek['src'] = src[0].text
  objek['judul'] = judul
  objek['isi'] = isi
  objek['terjemah'] = terjemah


  return objek
