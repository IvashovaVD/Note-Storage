import requests
from datetime import date

id_get_folder = 19
id_delete_folder = 71
id_put_folder = 15
id_user = 49


def test_post_folder():
    folder = {"num_user": id_user, "name": "Test folder"
                                           + str(date.today())}
    r = requests.post("http://127.0.0.1:8000/main/folders/", data=folder)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    assert r.text


def test_delete_folder():
    response = requests.delete("http://127.0.0.1:8000/main/folders/"
                               + str(id_delete_folder) + "/")
    assert response.status_code == 204


def test_put_folder():
    folder = {"num_user": id_user, "name": "Test folder" + str(id_put_folder)}
    response = requests.put('http://127.0.0.1:8000/main/folders/'
                            + str(id_put_folder) + "/", data=folder)
    assert response.text


def test_get_folder():
    response = requests.get('http://127.0.0.1:8000/main/folders/'
                            + str(id_get_folder) + "/")
    assert response.status_code == 200
