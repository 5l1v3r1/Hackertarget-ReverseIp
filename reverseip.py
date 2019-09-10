from urllib.request import urlopen as o
lists = open('ip.txt', 'r').read().split('\n')
for ip in lists:
    print('Looking', ip)
    grab = 'null'
    try:
        grab = o('https://api.hackertarget.com/reverseiplookup/?q=' + ip).read().decode('utf-8')
    except:
        continue
    if 'error check' in grab:
        print('Check ip format in input file')
        continue
    if 'No records' in grab:
        print('No reverse IP record available')
        continue
    grab = grab.split('\n')
    for domain in grab:
        open('grabbed.txt', 'a+').write(domain + '\n')