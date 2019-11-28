import os
import logging
from devmob_sheets import MembersRegister
from telegram.ext import CommandHandler, Updater, MessageHandler, BaseFilter
from telegram import ForceReply

class FilterMeet(BaseFilter):
    def filter(self, message):
        return message.from_user.username == "OiAlex" and "REUNIÃO" in message.text
filter_meet = FilterMeet()
members = MembersRegister()

def batata(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="batata")

def chama(update, context):
    usernames = "\n".join(members.getTelegramUsernames())
    reply = update.message

    if(reply.reply_to_message is None and not filter_meet.filter(reply)):
        context.bot.send_message(chat_id=update.effective_chat.id, text=usernames)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=usernames, reply_to_message_id=reply.message_id)

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

chama_handler = CommandHandler('chama', chama)
dispatcher.add_handler(chama_handler)

batata_handler = CommandHandler('batata', batata)
dispatcher.add_handler(batata_handler)

meet_handler = MessageHandler(filter_meet, chama)
dispatcher.add_handler(meet_handler)

updater.start_polling()
