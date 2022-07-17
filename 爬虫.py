import requests


url = 'https://app.gsxt.gov.cn/gsxt/corp-query-app-search-1.html'
header = {
'Host': 'app.gsxt.gov.cn',
'Connection': 'keep-alive',
'Content-Length': 451,
'Accept': 'application/json',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'
}
data = {

}
resp = requests.post(url=url, data=data)

print(resp.ok)
print(resp.text)
print(resp.content.decode('utf-8'))

