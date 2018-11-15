from collections import defaultdict

ADD_INIT, CONFIRM_ADD_LOCATION, ADD_LOCATION, ADD_PHOTO = range(4)

USER_STATE = defaultdict(lambda: ADD_INIT)


def get_state(message):
    return USER_STATE[message.chat.id]


def update_state(message, state):
    USER_STATE[message.chat.id] = state
