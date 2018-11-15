import telebot

import settings
import states
from locations import get_locations, update_location, delete_locations

bot = telebot.TeleBot(settings.TOKEN)

confirmations = ("yes", "yep", "yay", "yeah", "ja", "si", "vi", "да")


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, text='''Welcome to Remember Locations Bot!
    Here is the list of available commands:
    
    /add - create new location
    /list - show last 10 added locations
    /reset - wipe all your records
    /help or /start - show this message
    ''')


@bot.message_handler(commands=['add', ], func=lambda msg: states.get_state(msg) == states.ADD_INIT)
def handle_add_location(message):
    bot.send_message(message.chat.id, text='Set name for the place')
    states.update_state(message, states.ADD_LOCATION)


@bot.message_handler(content_types=['location'])
def handle_receive_location(message):
    bot.send_message(message.chat.id, text='Your location: {}\n\nDo you want to save it?'.format(message.location))
    # TODO: Add parser
    states.update_state(message, states.CONFIRM_ADD_LOCATION)


@bot.message_handler(func=lambda msg: states.get_state(msg) == states.CONFIRM_ADD_LOCATION)
def confirm_add_location(message):
    if message.text.lower() in confirmations:
        print("we're here!")
        handle_add_location(message)
    else:
        states.update_state(message, states.ADD_INIT)


@bot.message_handler(func=lambda msg: states.get_state(msg) == states.ADD_LOCATION)
def add_title(message):
    update_location(message.chat.id, 'title', message.text)
    bot.send_message(message.chat.id, text='Take a photo of the place')
    states.update_state(message, states.ADD_PHOTO)


@bot.message_handler(func=lambda msg: states.get_state(msg) == states.ADD_PHOTO, content_types=['photo', ])
def add_photo(message):
    # TODO: Add parser
    print("len(message.photo):", len(message.photo))

    bot.send_message(message.chat.id, text='All done. Thanks.')
    states.update_state(message, states.ADD_INIT)


@bot.message_handler(commands=['list', ])
def handle_list_locations(message):
    locations = get_locations(message.chat.id)

    if not locations:
        bot.send_message(message.chat.id, text='Nothing to show. Feel free to /add new location!')
        return

    last_ten = ['{}. {}'.format(n + 1, v) for n, v in enumerate(loc.get('title') for loc in locations[-10:])]
    message_to_user = '\n'.join(['Here is the list of your latest saved locations:', *last_ten])
    bot.send_message(message.chat.id, text=message_to_user)


@bot.message_handler(commands=['reset', ])
def handle_reset_locations(message):
    locations = get_locations(message.chat.id)

    if not locations:
        bot.send_message(message.chat.id, text='Nothing to delete. Feel free to /add new location!')
        return

    delete_locations(message.chat.id)
    bot.send_message(message.chat.id, text="Done. All your locations were removed.")


if __name__ == '__main__':
    bot.polling(none_stop=True)
