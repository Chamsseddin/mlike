from time import sleep
import mlike

def main():
    n = input('Enter phone number: ')
    r = {
        'success': s,
        'failed': f
    }
    
    while True:
        for i in range(n, n + 10):
            try:
                status = mlike.Client(i).set_credit()['status']
                if status == 200:
                      r['success'] += 1
                else:
                    r['failed'] += 1
            except:
                sleep(10)
            print(r, end = '\r')
            sleep(30)

main()
