from decouple import config
import itertools
import websocket
import json
import time

KEY_INTERVAL = 0.2

def send_key(key, repeat=1):
    for n in range(repeat):
        url = f'ws://{config('HOST')}:{config('PORT')}/api/v2/channels/samsung.remote.control'
        connection = websocket.create_connection(url)
        payload = json.dumps({
            'method': 'ms.remote.control',
            'params': {
                'Cmd': 'Click',
                'DataOfCmd': key,
                'Option': 'false',
                'TypeOfRemote': 'SendRemoteKey'
            }
        })
        connection.send(payload)
        time.sleep(KEY_INTERVAL)

def combinations():
    digits = list(range(1,10))
    comb = list(itertools.product(digits, repeat=4))
    return comb

def send_pin(code):
    send_key('KEY_UP')
    send_key('KEY_ENTER')
    print(f'Testando: {code}')
    for digit in code:
        if digit == None:
            continue
        send_key(f'KEY_{digit}')
        time.sleep(1)
    time.sleep(3)

if __name__ == "__main__":
    combos = combinations()
    for code in combos:
        try:
            send_pin(code)
        except Exception as e:
            print(f"Erro enviando o pin {code}: {e}")