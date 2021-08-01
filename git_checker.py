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

def checkAuthorName(logFile, name):
    '''
    저자 이름 확인
    '''
    f = open(logFile, 'r')
    result = True
    for i in f:
        if i.startswith('Author'):
            if i.split()[1] != name:
                result = False
    f.close()
    return result

def checkAuthorEmail(logFile, email):
    '''
    저자 이메일 확인
    '''
    f = open(logFile, 'r')
    result = True
    for i in f:
        if i.startswith('Author'):
            if i.split()[2][1:-1] != email:
                result = False
    f.close()
    return result

logFile = "log.txt"
name = "username"
email = "email@test.com"

print(f'커밋날짜 순서체크 : {checkDateOrder(logFile)}')
print(f'커밋저자 이름체크 : {checkAuthorName(logFile, name)}')
print(f'커밋저자 메일체크 : {checkAuthorEmail(logFile, email)}')

input("엔터를 누르면 종료")