import requests
from datetime import date

id_get_note = 1
id_delete_note = 35
id_put_note = 1
id_folder = 4


def test_post_note():
    note = {
        "name": "Заметка" + str(date.today()),
        "textn": "z vika",
        "urln": "hhh",
        "available": False,
        "num_folder": id_folder
    }
    r = requests.post("http://127.0.0.1:8000/main/notes/", data=note)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    assert r.text == "didn't create"


def test_delete_note():
    response = requests.delete("http://127.0.0.1:8000/main/notes/"
                               + str(id_delete_note)+ "/")
    assert response.text == "don't athtorization"


def test_get_note():
    response = requests.get('http://127.0.0.1:8000/main/notes/'
                            + str(id_get_note) + "/")
    assert response.text == "don't athtorization"


def test_put_note():
    folder = {"name": "Test folder" + str(id_put_note)}
    response = requests.put('http://127.0.0.1:8000/main/notes/'
                            + str(id_put_note) + "/", data=folder)
    assert response.text == "didn't change"
