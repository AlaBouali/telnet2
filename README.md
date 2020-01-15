# telnet
This is an easy to use telnet module to interact with a remote system smoothly over this protocol!

# Install :

pip install telnetlib2

or

pip3 install telnet

# Usage :

import telnetlib2
t=telnetlib.telnet()
ip='192.168.0.32'#just an example
t.login(ip, username='root',password='toor',p=23,timeout=5)
output1=t.execute('echo ala_is_king')
print(output1)
output2=t.execute('cd / && ls')
print(output2)
t.close()