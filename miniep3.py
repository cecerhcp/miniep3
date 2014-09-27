# Cesar Cano de Oliveira - NUSP: 8536169 
# João Henrique Luciano - NUSP: 8535957
# obs: para executar eu usei python3.3
import sys
import re

arquivo = sys.stdin
output = ''
dnsStarted = False
output = output + arquivo.readline()
line = arquivo.readline()
match = re.search('\S+\.(\S+\.\S+)\.', line)
if match :
	domain = match.group(1)
	output = output + line
else : 
	print('Erro - Arquivo de entrada com formato incorreto')
	sys.exit(0)

line = arquivo.readline()
while (line != ''):
	match = re.search('(\S+)\s+A\s+\d+\.\d+\.\d+.\.(\d+)', line)
	if match :
		output = output + match.group(2) + '  PTR  ' +  match.group(1) + '.' + domain + '.\n'
		dnsStarted = True
	else :
		if dnsStarted is False:	
			output = output + line
		else : 
			print('Erro - Arquivo de entrada com formato incorreto')
			sys.exit(0)
	line = arquivo.readline()


print(output)


      
