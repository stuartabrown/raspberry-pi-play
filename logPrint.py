import datetime
def logPrint(s):
    now = datetime.datetime.now()
    filename='/home/pi/log'+now.strftime('%Y-%m-%d')+'.txt'    
    f=open(filename,'a')
    f.write(now.strftime('%H:%M:%S')+' '+s+'\n')
    # f.write(len(sys.argv))
      
    f.close()