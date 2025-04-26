user_preferences = {
    "language": "English",
    "font_size": "14px",
    "timezone": "GMT",
    "currency": "USD",
    "enable_location": False,
    "volume_level": 80,
    "date_format": "MM/DD/YYYY",
}


user_preferences["language"] = "Spanish"
user_preferences["volume_level"] = 50
user_preferences["highlight_color"] = "Yellow"

del user_preferences["currency"]
user_preferences.pop("date_format")
removed_item = user_preferences.pop("enable_location", "N/A")
print(user_preferences)
