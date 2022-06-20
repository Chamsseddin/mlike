from time import sleep
import mlike

def main():
    n = input('Enter phone number: ')
    result = {
        'success': 0,
        'failed': 0
    }
    
    while True:
        for i in range(n, n + 10):
            try:
                status = mlike.Client(i).set_credit()['status']
                if status == 200:
                      result['success'] += 1
                else:
                    result['failed'] += 1
            except:
                sleep(10)
            print(result, end = '\r')
            sleep(30)

main()
