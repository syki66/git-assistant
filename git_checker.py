from datetime import datetime

def checkDateOrder(logFile):
    '''
    git log --date=format:'%Y-%m-%d %H:%M:%S' > log.txt
    커밋날짜 순서 체크
    '''
    f = open(logFile, 'r')
    prev = ""
    result = True
    for i, v in enumerate(f):
        if v.startswith('Date'):
            current = datetime.strptime(' '.join(v.split()[1:]), '%Y-%m-%d %H:%M:%S')
            if i == 2:
                prev = datetime.strptime(' '.join(v.split()[1:]), '%Y-%m-%d %H:%M:%S')
                continue
            if current > prev:
                print(f'error : {current}')
                result = False
            prev = current
    f.close()
    return result

print(f'커밋날짜 순서체크 : {checkDateOrder("log.txt")}')
input("")