# coding=utf-8

from bs4 import BeautifulSoup
import time
import requests as req
import sys
import re
from extractor import Extractor
baiduUrl = "http://www.baidu.com"
sougouUrl = "http://www.sogou.com"
baiduUrl = "http://m.baidu.com"
fopath = "E:\\BaiduArrange-master\\txt\\"
# 取出一个网页的html的方法封装
def get_html(url,index):
    header = [{
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.45 Safari/537.36',
		'Cookie': 'BIDUPSID=57570A2560D5C8A0EF905A474E610A43; PSTM=1592441007; BAIDUID=57570A2560D5C8A098225421C101BB2F:FG=1; BD_UPN=12314753; MSA_WH=360_640; BDUSS=VJ2UzVRY0I1RHVpQXVIcGc4dlN3VXE1UHc0Y3FsREhjU1l-MXdHYX5hbzlXVWhmSVFBQUFBJCQAAAAAAAAAAAEAAAAUUXlBztvAssCywLK1xLqjvccAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD3MIF89zCBfc; yjs_js_security_passport=4f2ce142928fb653932e98e13343c572c8c7ef89_1596592754_js; delPer=0; BD_CK_SAM=1; BDUSS_BFESS=VJ2UzVRY0I1RHVpQXVIcGc4dlN3VXE1UHc0Y3FsREhjU1l-MXdHYX5hbzlXVWhmSVFBQUFBJCQAAAAAAAAAAAEAAAAUUXlBztvAssCywLK1xLqjvccAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD3MIF89zCBfc; shifen[176642276251_11877]=1596601360; rsv_jmp_slow=1596602459238; PSINO=7; shifen[156782553295_78217]=1596605941; shifen[180498753392_17025]=1596605946; shifen[173942149822_15865]=1596606064; shifen[162524204246_32914]=1596606194; BCLID=11398511109520225175; BDSFRCVID=pvDOJeC629tMpE5r24pUMeKt7gK2WAcTH6aosrXTREbYpl_Le4hKEG0PoM8g0Kub7PoUogKK3gOTH4DF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tRAOoCKaJKvqKRopMtOhq4tehHRtWMJ9WDTm_Dou0JDBqUo4D6O03Mu8yp8fLPFfaNr9-pPKKR7MhJbt0tbpeM_zyf6TeRcn3mkjbn7Dfn02OPKz0T5Y3P4syP4eKMRnWnnRKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJDJCF5hKPle5ubjTPSMMrX5C6qKCoJ3R3H5bRoHRj1D5K_-P6MX4tOWMT-0bFHKbK2LCQcqC_m24OYbfP3jUteWxQWaan7_JjOQUnTEJ52jUjbqf0S2x_q0xQxtNRg-CnjtpvhHCTx0pbobUPUDUJ9LUkJ3gcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj0DKLtKthMDKxejRjhCCDbfrH2-6MbK60BbK82tt38qjqXU6qLT5Xjh3PB4tq-JuJWfJz5lvMMn3o-tAbjp0njxQyJf3k-2Kt-C5qBhTsoJjthUonDh89bG7MJUntHmPDBRTO5hvvhn3O3MAMQMKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQbG_EJ58jJnPf_IKQKRbHKRopMtOhq4tehHRItJ39WDTm_D_Xbp62sD54D6O_yfu8yp8fKMPHQ262-pPKKR75qxn20xoDWJ8jBPv-tPvi3mkjbn7zfn02OP5Pjp3o3t4syP4eKMRnWnnRKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJDJCF5hKtmj5tMjjP_bMLX5to05TIX3b7Ef-J-sh7_bf--D6F3Xq34tRDHJTRP2R5cbI3JOIo5Ltbxy5K_hpbHXp3N3CrkQnR7BnKMjhvHQT3mhUrbbN3i-4DfLIOPWb3cWKOJ8UbSjMOPBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JD-50exbH55uetbFfox5; BA_HECTOR=qmq8; H_PS_PSSID=32294_1425_32439_32359_32327_31660_32046_32393_32405_32429_32116_32092; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; sugstore=1; H_PS_645EC=157bGDQAwOM%2FTHwnnPprPTFWDmA%2BsoIu6BC4y58SJx2suy%2Bp4NYVSW8R%2B1w; COOKIE_SESSION=30_2_9_9_1_10_0_0_9_4_60_5_0_4_0_0_1596606110_1596606068_1596607460%7C9%23123_63_1596606062%7C9'
    },{
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
       'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.45 Mobile Safari/537.36'
    }]

    '''
    proxy = '121.204.206.220:28803'

    proxies={
       'http':'http://'+proxy,
       'https':'https://'+proxy
    }
    '''
    

    f = req.get(url,headers=header[index],verify=False)
    f.encoding = 'utf-8'
    soup = BeautifulSoup(f.content, "lxml")
    return soup


## 该函数用于处理用户自定义参数，第一个参数为搜索目标，第二个参数为搜索页码
def argument_deal():
    arg = [0,0,0]

    arg[0] = 1
    arg[1] = sys.argv[1].encode('gbk').decode('gbk') #命令行如果有中文参数，需要按gbk解码，不然会显示乱码

    return arg


def main():
  tims = sys.argv[2]
  timer(int(tims))

 

def timer(n):
    page = sys.argv[3]
    while True:
      for i in range(int(page)):
        writetext_baidu(i*10)
        writetext_souguo(i+1)
        writetext_mbaidu()
      time.sleep(n)



def writetext_baidu(page):
    p = str(page)
    #fo = open("E:\\BaiduArrange-master\\result.txt", "a+",encoding='utf-8-sig')
    arg = argument_deal()
    target = "720全景"
	#print arg
    if arg[0] == 1:
        target = arg[1]
    elif arg[0] == 2:
        target = arg[1]
        pages = int(arg[2])+1 #注意这里要把参数中的字符串转换为数字，否则会造成后面死循环
    print(baiduUrl+"/s?ie=UTF-8&wd="+target+"&pn="+p)
    soup = get_html(baiduUrl+"/s?ie=UTF-8&wd="+target+"&pn="+p,0)
    id_div = soup.find(id='content_left')

    cl_div = soup.find_all('div', class_='c-abstract')
    #print(soup)
    #print(id_div.find_all('a',class_='ec_tuiguang_pplink'))
    #print(id_div.find_all('a',class_='ec_tuiguang_link'))
    for gg in cl_div:
         #print(gg.find_all('a',class_='ec_tuiguang_pplink'))
         #print(gg.find_all('a',class_='ec_tuiguang_link'))
         if (gg.find_all('a',class_='ec_tuiguang_pplink')): 
              writfile_baidu(gg.find('a').get('href'))

         if (gg.find_all('a',class_='ec_tuiguang_link')):
              writfile_baidu(gg.find('a').get('href'))


    #fo.close()

def writetext_mbaidu():

    arg = argument_deal()
    target = "720全景"
	#print arg
    if arg[0] == 1:
        target = arg[1]
    elif arg[0] == 2:
        target = arg[1]
        pages = int(arg[2])+1 #注意这里要把参数中的字符串转换为数字，否则会造成后面死循环
    print(baiduUrl+"/s?&word="+target)
    soup = get_html(baiduUrl+"/s?&word="+target,1)
    #id_div = soup.find(id='content_left')

    cl_div = soup.find_all('div', class_='c-container')
    #print(soup.find_all('span',class_='ec-tuiguang'))
    for gg in cl_div:
         if (gg.find_all('span',class_='ec-tuiguang')): 
              writfile_sougou(gg.find('a').get('href'))


def writetext_souguo(page):
    p = str(page)
    arg = argument_deal()
    target = "720全景"
    if arg[0] == 1:
        target = arg[1]
    elif arg[0] == 2:
        target = arg[1]
        pages = int(arg[2])+1 #注意这里要把参数中的字符串转换为数字，否则会造成后面死循环
    print(sougouUrl+"/tx?hdq=sogou-site-706608cfdbcc1886&ekv=3&ie=utf8&query="+target+"&page="+p)
    soup = get_html(sougouUrl+"/tx?hdq=sogou-site-706608cfdbcc1886&ekv=3&ie=utf8&query="+target+"&page="+p,0)
    id_div = soup.find(id='promotion_adv_container')
    #print(id_div)
    cl_div = id_div.find_all('div', class_='biz_rb')
    #print(cl_div)
    for gg in cl_div:
         writfile_sougou(gg.find('h3').find('a').get('href'))
         #print(gg.find('h3').find('a').get('href'))



def writfile_baidu(a_url):
  u = Extractor.get_url(a_url,'baidu')
  print(u)
  fo = open(fopath+u+".txt", "w+",encoding='utf-8-sig')
              								 
  ext = Extractor(url=a_url,blockSize=5, image=False)
  #print(ext.getContext())
  try:
     fo.write(ext.getContext())
  except:
     print('error');
  fo.close()


def writfile_sougou(a_url):
  u = Extractor.get_url(a_url,"sougou")
  print(u)
  fo = open(fopath+u+".txt", "w+",encoding='utf-8-sig')
  #print(Extractor.geta_url_sougou(a_url))   
  ext = Extractor(url=Extractor.geta_url_sougou(a_url),blockSize=5, image=False)
  #print(ext.getContext())
  try:
     fo.write(ext.getContext())
  except:
     print('error');
  fo.close()


if __name__=='__main__':
       main()

