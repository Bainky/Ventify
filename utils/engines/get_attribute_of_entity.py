from json import load


def get_attributes_of_object():
    """
    Retrieving all json file data.
    """
    with open("./data/entities.json") as f:
        categories = load(f)
    return categories