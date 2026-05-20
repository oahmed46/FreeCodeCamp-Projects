test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}

def lower_tuple(tup):
    key, value = tup
    key = key.lower()
    value = value.lower()
    return key,value

def add_setting(current_settings, new_setting):
    key, value = lower_tuple(new_setting)

    if key in current_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        current_settings.update({key:value})
        return f"Setting '{key}' added with value '{value}' successfully!"
    

def update_setting(current_settings, new_setting):
    key, value = lower_tuple(new_setting)

    if key in current_settings:
        current_settings.update({key:value})
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    

def delete_setting(current_settings, key):
    key = key.lower()

    if key in current_settings:
        current_settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(current_settings):
    if not current_settings:
        return "No settings available."
    text = "Current User Settings:\n"
    for setting in current_settings.items():
        key, value = setting
        text += f"{key.capitalize()}: {value}\n"
    return text

print(view_settings(test_settings))
