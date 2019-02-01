import requests, re, os, urllib

def mkdir(path):
	# print('mkdir', path)
	if not os.path.exists(path):
		os.makedirs(path)

def get(url, path):
	print('get', urllib.parse.unquote(url), urllib.parse.unquote(path))
	if url[-1] == '/':
		mkdir(urllib.parse.unquote(path))
		length   = len(re.split(r'://[\S]*?/', url)[-1]) + 1
		content  = requests.get(url).text
		children = re.findall(r'<li class="mdui-list-item mdui-ripple">\n			<a href="[\s\S]*?">', content)
		folders  = [children[i][52 + length:-2] for i in range(1, len(children))]
		children = re.findall(r'<li class="mdui-list-item file mdui-ripple">\n			<a href="[\s\S]*?" target="_blank">', content)
		files    = [children[i][57 + length:-18] for i in range(0, len(children))]
		for child in files + folders:
			get(url + child, path + child)
	else:
		pass
		os.system('wget {url} -O {path}'.format(url=url, path=urllib.parse.unquote(path)))

if __name__ == '__main__':
	url  = 'https://drive.bakaawt.com/Videos/%E6%B4%9B%E8%B0%B7%E6%98%A5%E5%AD%A3%E5%9B%9E%E6%94%BE/TG/%E5%A4%8D%E8%B5%9B/'
	path = os.getcwd() + '/down/'
	get(url, path)