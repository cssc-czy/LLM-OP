import json, os, requests, subprocess, sys, urllib
from baidusearch.baidusearch import search as baidusearch

def exec(command):
    res = subprocess.run(command.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if res.returncode == 0:
        res =  "执行成功，返回结果如下：\n" + res.stdout.decode('GBK')
    else:
        res =  "执行失败，报错如下：\n" +  res.stderr.decode('GBK')
    print(f"stdio>\t {res}")
    return res

def baidu_search(context):
    res = baidusearch(context)
    return json.dumps(res,ensure_ascii=False)

def bing_search(context):
    pass

def url_to_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else: 
        return f"请求失败，状态码：{response.status_code}，要不换个链接试试，以及要不考虑一下国内的镜像"

def download_and_extract(url, save_dir):
    try:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        filename = url.split('/')[-1]
        save_path = os.path.join(save_dir, filename)
        urllib.request.urlretrieve(url, save_path)
        return f'成功下载{filename}至：{save_dir}'
    except:
        return f'下载失败，要不换个链接试试，以及要不考虑一下国内的镜像'

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    return f'成功写入文件：{file_path}'

funcs_map = {"exec":exec,
             "baidu_search": baidu_search,
             "url_to_text": url_to_text,
             "download_and_extract": download_and_extract,
             "write_file": write_file
             } 
if __name__ == "__main__":
    print(exec("dir"))
    # print(
    #     subprocess.run('netstat -ano |findstr :80', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # )