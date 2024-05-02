from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes
import requests
import uuid
TOKEN='6934680718:AAG2qAHel6GuC9NgzxWy9OPvbqpfic7bSyk'
BOTUSERNAME='@Mac_OsBot'
#Functions
def exchanged_rate(amount):
    url = "https://www.blockonomics.co/api/price?currency=USD"
    r = requests.get(url)
    response = r.json()
    return amount/response['price']
def get():
    api_key = 'pj0LgQwm9o3gy8M2THSalKErb1poZlTKhQA1XYfpB4k'
    amount = float(10.00)
    url = 'https://www.blockonomics.co/api/new_address'
    headers = {'Authorization': "Bearer " + api_key}
    r = requests.post(url, headers=headers)
    if r.status_code == 200:
        address = r.json()['address']
        bits = exchanged_rate(amount)
        return address
    else:
        return r

def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'hello' in processed:
        return 'Hey there!'
    
    if 'how much' in processed:
        return "Just $10"
    
    if 'supported' in processed:
        return "All MACOS including T1/T2 and M1-M2 series"
    
    return 'I do not understand what you wrote...'



# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    order_id = uuid.uuid1()
    chat_id = update.message.chat.id
    data = {
        'chat_id':chat_id,
        'order_id':order_id
    }
    response=requests.post(url="https://achlive-api.vercel.app/pay/create/telegram/",data=data)
    await update.message.reply_text('Hello! Thanks for chatting with me!. I am a macbook/macos icloud/mdm bypass bot')

    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    order_id = uuid.uuid1()
    chat_id = update.message.chat.id
    data = {
        'chat_id':chat_id,
        'order_id':order_id
    }
    response=requests.post(url="https://achlive-api.vercel.app/pay/create/telegram/",data=data)
    await update.message.reply_text('Hello! Thanks for chatting with me!. How may i help you today')


async def mdmbypass_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    addr=get()
    order_id = uuid.uuid1()
    chat_id = update.message.chat.id
    data = {
        'chat_id':chat_id,
        'order_id':order_id,
        'address':addr
    }
    response=requests.post(url="https://achlive-api.vercel.app/pay/create/telegram/",data=data)
    await update.message.reply_text(f'Pay $10 into this address to receive your link to our free site.\n{addr}')


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


async def handle_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    chat_id: str = update.message.chat.id
    order_id = uuid.uuid1()
    chat_id = update.message.chat.id
    data = {
        'chat_id':chat_id,
        'order_id':order_id
    }
    response=requests.post(url="https://achlive-api.vercel.app/pay/create/telegram/",data=data)
    print(chat_id)
    if message_type == 'group':
        if BOTUSERNAME in text:
            new_text: str = text.replace(BOTUSERNAME,'').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    
    await update.message.reply_text(response)

print('Starting bot...')
app= Application.builder().token(TOKEN).build()

  #commands
app.add_handler(CommandHandler('start',start_command))
app.add_handler(CommandHandler('help',help_command))
app.add_handler(CommandHandler('mdmbypass',mdmbypass_command))
#Messages
app.add_handler(MessageHandler(filters.TEXT, handle_message))
    #error
app.add_error_handler(error)


print('polling...')
app.run_polling(poll_interval=3)

