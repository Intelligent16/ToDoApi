from data_base import todos, last_id


def find_by_id(id: int):
    for i in todos:
        if i.id == id:
            return i
    return None


def get_and_increment_id():
    id = last_id["id"]
    last_id["id"] += 1
    return id
