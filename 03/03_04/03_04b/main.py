user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None,
}


def update_preferences(user_pref):
    result = {}
    for key, val in user_pref.items():
        if val is not None:
            result[key] = val
    return result


print(update_preferences(user_preferences))
