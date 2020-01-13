# telnet
This is an easy to use telnet module to interact with a remote system smoothly over this protocol!

# Install :

pip install telnet

or

pip3 install telnet

# Usage :

import telnet
t=telnet.telnet()
ip='192.168.0.32'#just an example
t.login(ip, username='root',password='toor',p=23,timeout=5)
output1=t.execute('echo ala_is_king')
print(output1)
output2=t.execute('cd / && ls')
print(output2)
t.close()
