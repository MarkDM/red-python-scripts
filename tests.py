#    Import subprocess so we can use system commands.
import subprocess

#    Import the re module so we can make use of regular expressions. 
import re

cmd = "netsh wlan show profile Marcos key=clear"
cmd = cmd.split(' ')
command_output = subprocess.run(cmd, capture_output = True).stdout.decode(encoding='iso-8859-1')
print(command_output)