import requests
import json
import os


TRELLO_KEY = os.environ['TRELLO_KEY']
TRELLO_TOKEN = os.environ['TRELLO_TOKEN']
url = "https://api.trello.com/1/"
headers = {
    "Accept": "application/json"
}


def create_trello_board():
    full_url = url + "boards/"
    query = {
        'name': 'second board',
        'key': TRELLO_KEY,
        'token': TRELLO_TOKEN
    }

    response = requests.request(
        "POST",
        full_url,
        headers=headers,
        params=query,
        verify=False

    )

    board_id = response.json()['id']
    print(board_id)
    return board_id


def share_trello_board(board_id, email, full_name):

    full_url = (url + "boards/{id}/members").format(id=board_id)

    query = {
        "email": email,
        'key': TRELLO_KEY,
        'token': TRELLO_TOKEN
    }

    payload = json.dumps({
        "fullName": full_name
    })

    response = requests.request(
        "PUT",
        full_url,
        headers=headers,
        params=query,
        data=payload,
        verify=False
    )
    print(response.json())


def start_here():
    url = "https://api.trello.com/1/boards/63650f2c3f1e080042b8df78"

    query = {
      'key': TRELLO_KEY,
      'token': TRELLO_TOKEN
    }
    response = requests.request(
      "GET",
      url,
      headers=headers,
      params=query,
      verify=False
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


new_board_id = create_trello_board()
share_trello_board(new_board_id, "glebza@mail.ru", "bear roars")
#start_here()
