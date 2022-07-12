import json
import requests
from oauth2client.service_account import ServiceAccountCredentials
import os

from zizou.settings import BASE_DIR

PROJECT_ID = 'examen2-bf1d9'
BASE_URL = 'https://fcm.googleapis.com'
FCM_ENDPOINT = 'v1/projects/' + PROJECT_ID + '/messages:send'
FCM_URL = BASE_URL + '/' + FCM_ENDPOINT
SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']

# [START retrieve_access_token]
def _get_access_token():
    """Retrieve a valid access token that can be used to authorize requests.
    :return: Access token.
    """

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        os.path.join(BASE_DIR, 'google-access-examen2.json'), SCOPES)
    access_token_info = credentials.get_access_token()
    return access_token_info.access_token


# [END retrieve_access_token]


def _send_fcm_message(fcm_message):
    # [START use_access_token]
    headers = {
        'Authorization': 'Bearer ' + _get_access_token(),
        'Content-Type': 'application/json; UTF-8',
    }
    # [END use_access_token]

    resp = requests.post(FCM_URL, data=json.dumps(
        fcm_message), headers=headers)

    if resp.status_code == 200:
        print('Message sent to Firebase for delivery, response:')
        print(resp.text)
    else:
        print('Unable to send message to Firebase')
        print(resp.text)


def _build_common_message(a, b, r):
    body = f"{a} + {b} = {r}"
    return {
        'message': {
            'topic': 'exam2',
            'notification': {
                'title': 'Resultado de suma',
                'body': body
            }
        }
    }


def sendSumNotification(a, b, r):
    common_message = _build_common_message(a, b, r)
    print('FCM request body for message using common notification object:')
    print(json.dumps(common_message, indent=2))
    _send_fcm_message(common_message)
