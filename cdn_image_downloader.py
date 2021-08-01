import urllib.request
import os

def downloadCDNImage(logFile):
    '''
    git grep user-images\.githubusercontent\.com $(git rev-list --all) > log.txt
    '''
    ext_list = ['.jpg', '.jpeg', '.png', '.gif', '.tif', '.tiff', '.webp', '.bmp']
    array = []
    f = open(logFile, 'r', encoding='utf-8')
    for i, line in enumerate(f):       
        start = line.find("user-images.githubusercontent.com")
        end = line.find(".", start + 40)
        while(start != -1):
            link = line[start - 8:end]
            ext = line[end:end + 5]
            if ext.lower() in ext_list:
                array.append(f'{link}{ext}')
            elif ext[:-1].lower() in ext_list:
                array.append(f'{link}{ext[:-1]}')
            start = line.find("user-images.githubusercontent.com", end)
            end = line.find(".", start + 40)
    f.close()
    array = list(set(array))

    success = True
    try:
        dir_name = 'output'
        os.makedirs(f'./{dir_name}')
        for i, url in enumerate(array):
            print(f'다운로드 : {i} / {len(array)} 개')
            ext = url.split('.')[-1]
            urllib.request.urlretrieve(url, f'{dir_name}/output{i}.{ext}')
    except Exception as e:
        print(f'에러 발생 : {e}')
        success = False
    
    if success:
        print('다운로드 성공')
    else:
        print('다운로드 실패')

logFile = "log.txt"
downloadCDNImage(logFile)