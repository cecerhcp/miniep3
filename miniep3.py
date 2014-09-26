# Cesar Cano de Oliveira e João Henrique Luciano
# NUSP: 8536169 e NUSP: ????
# obs: para executar eu usei python3.3
import sys
import re

arquivo = sys.stdin
output = ''
dnsStarted = False
output = output + arquivo.readline()
match = re.search('\S+\.(\S+\.\S+)\.', arquivo.readline())
if match :
	domain = match.group(1)
else : 
	print('Erro\n')

line = arquivo.readline()
while (line != ''):
	match = re.search('(\S+)\s+A\s+\d+\.\d+\.\d+.\.(\d+)', line)
	if match :
		output = output + match.group(2) + '  PTR  ' +  match.group(1) + '.' + domain + '\n'
		dnsStarted = True
	else :
		if dnsStarted is False:	
			output = output + line
		else : 
			print('Erro!\n')
	line = arquivo.readline()

print(output)

      
