APP_URL = 'https://www.google.com'
TIMEOUT = 5
try:
    response = requests.get(APP_URL, timeout=TIMEOUT)
if response.status_code == 200:
        print('Application is up!')
    else:
        print(f'Application is down! Status code: {response.status_code}')
except requests.exceptions.RequestException as e:
    print(f'Error: {e}')
