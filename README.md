# telnetlib2
This is an easy to use telnet module to interact with a remote system smoothly over this protocol!

# Install :

pip install telnetlib2

or

pip3 install telnetlib2

# Usage :

import telnetlib2
<br>t=telnetlib.telnet()
<br>ip='192.168.0.32'#just an example
<br>t.login(ip, username='root',password='toor',p=23,timeout=5)
<br>output1=t.execute('echo ala_is_king')
<br>print(output1)
<br>output2=t.execute('cd / && ls')
<br>print(output2)
<br>t.close()
