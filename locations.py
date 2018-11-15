from collections import defaultdict

LOCATIONS = defaultdict(lambda: [])


def update_location(user_id, key, value, record_idx=None):
    if record_idx and LOCATIONS.get(user_id) and len(LOCATIONS[user_id]) >= record_idx:
        LOCATIONS[user_id][record_idx][key] = value

    LOCATIONS[user_id].append({key: value})


def get_locations(user_id):
    return LOCATIONS[user_id]


def delete_locations(user_id):
    if user_id in LOCATIONS:
        del (LOCATIONS[user_id])
