import subprocess

# Execuring a <netsh wlan show profiles> command in cmd and getting output in the form of list.
# Use .decode('utf-8') if using an english version of windows.
netsh_out = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp866').split('\n')
profiles = []
keys  = []


# Running through the list and finding elements which contain wifi profile names.
for i in netsh_out:
	if "All User Profile" in i or "Все профили пользователей" in i:
		# Splitting and slicing so we get pure net name. Then append to the list.
		profiles.append(i.split(':')[1][1:-1])
	

for i in profiles: 
	result = subprocess.check_output(['netsh','wlan','show','profile',i ,'key=clear']).decode('cp866').split('\n')
	print(result)
	for x in result:
		if "Содержимое ключа" in x or "Key Content" in x:
			keys.append(x.split(':')[1][1:-1])

# Create a file and save the gotten profile names and their keys.
f = open("WifiPassKeys.txt", "a")
for i in range(len(keys)):
	f.write(f'{profiles[i]} : {keys[i]} \n')
f.close()

