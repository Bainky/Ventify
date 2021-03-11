def clean_dict(json):
    """
    Remove keys with the value None from the dictionary
    """
    for key, value in list(json.items()):
        if value is None:
            del json[key]
        elif isinstance(value, dict):
            clean_dict(value)
    return json