import telegram as types
from telegram import Bot as bot
import random
import time
bot_name = "Oduraa"
# Conversation states
LEVEL, SEMESTER, COURSE, RESOURCE_TYPE, FEEDBACK = range(5)

# Dictionary to store user data
user_data = {}

# Custom "Back" button
back_button = types.KeyboardButton("Back🔙")

loading_messages = [
    "🚀Please wait while I prepare your resources",
    "🚀Working on it... Just a moment",
    "🚀Getting your resources ready",
] #Make the loading message be like a live typing letter by letter for once and clear it to make the resources come

# Courses for each level and semester, may change depending on the work order
level_courses = {
    "Level 100": {
        "First Semester": [
            "Algebra",
            "Applied Electricity",
            "Engineering Technology",
            "Basic Mechanics",
            "Environmental Studies",
            "Technical Drawing",
            "Communication Skills",
        ],
        "Second Semester": [
            "Basic Electronics",
            "Calculus With Analysis",
            "Engineering Research and Technical Report Writing",
            "Introduction to Phsychology",
            "Introduction to Communication Networks",
            "Introduction to Programming_I",
            "Electrical Measurement & Instrumentation",
            "Communication Skills_II",
            "Applied Thermodynamics",
            "Electrical Engineering Drawing",
            "Electrical Machines",
            "Introduction to IT(Matlab)",
        ],
    },
    "Level 200": {
        "First Semester": [
            "Differential Equation",
            "Introduction to Programmin_II",
            "Digital Systems",
            "Analog Communication Systems",
            "Circuit Theory",
            "Engineering In Society",
            "Analog Communication Lab",
            "Basic Accounting_I",
            "Basic Economics_I",
            "French_I",
            "Philosophy_I",
            "Semiconductor Devices",
            "C Programming",
           
        ],
        "Second Semester": [
            "Calculus With Several Variables",
            "Fundamentals of Data Science",
            "Electromagnetic Field Theory",
            "Communication Circuits",
            "Microprocessors",
            "Digital Electronics & Microprocessors Lab",
            "Basic Accounting_II",
            "Basic Economics_II",
            "French_II",
            "Philosophy_II",
            "Digital Systems",
            "Electrical Measurement & Instrumentation",
        ],
    },
    "Level 300": {
        "First Semester": [
            "Random Variables & Stochastic Processes",
            "Numerical Analysis",
            "Information Theory and Coding",
            "Microelectronic Devices & Circuits",
            "Optical Communication",
            "Signals & Systems",
            "Optical Communication Lab",
            "Microprocessors",
            "Statistics",
            "Linear Electronic Circuits",
            
        ],
        "Second Semester": [
            "Computer Networking",
            "Antenna Theory & Design",
            "Communication Systems Lab",
            "Engineering Project Design & Management",
            "Data Communication Principles",
            "Switching Engineering In Communication",
            "Digital Communication Systems",
            "Telecom Infrastructure",
            "Communication Circuits",
        ],
    },
    "Level 400": {
        "First Semester": [
            "Fundamentals of Network Security",
            "Emerging Trends In Communication",
            "Microwave Engineering",
            "Mobile & Wireless Communication",
            "Industrial Placement",
            "Project I",
            "Aviation Communication",
            "Digital Integrated Circuits",
            "VLSI",
            "Computer Application & Projects Design",
            "Electromagnetic Compatibility",
            "Wireless Data Communication Networks",
            "Engineering Economics & Management",
            "Computer Networking",
        ],
        "Second Semester": [
            "Digital Signal Processing",
            "Telecom Policy & Regulation",
            "Satelite Communication & Navigation Systems",
            "Radio Network Planning & Optimization",
            "Enterpreneurship Development",
            "Project II",
            "Radar Communications",
            "Millimeter Wave Technology",
            "Microwave Engineering",
            "Network Planning",
            "Introduction to VLSI"
        ],
    }
}


# Feedback Message
feedback_message = f"🌟 Thanks for using {bot_name} Bot! 🙌 I'm here to assist you, and your feedback is valuable to me. Please type your feedback or any suggestions you have below:Feel free to share your thoughts; I'm here to listen and make your experience even better! 📚🌟"

# Function to create and update the keyboard markup for each state
def update_keyboard_markup(chat_id, state):
    user_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    
    if state == LEVEL:
        user_markup.row("Level 100", "Level 200")
        user_markup.row("Level 300", "Level 400")
    elif state == SEMESTER:
        user_markup.row("First Semester", "Second Semester")
        user_markup.row(back_button)
    elif state == COURSE:
        selected_level = user_data.get(chat_id, {}).get("level", "")
        selected_semester = user_data.get(chat_id, {}).get("semester", "")
        courses = level_courses.get(selected_level, {}).get(selected_semester, [])
        for course in courses:
            user_markup.row(course)
        user_markup.row(back_button)
    elif state == RESOURCE_TYPE:
        user_markup.row("Past Questions", "Lecture Slides")
        user_markup.row("Recommended Books")
        user_markup.row("Feedback✉️") 
        user_markup.row("Back🔙")
    elif state == FEEDBACK:
        user_markup.row("Back🔙")  
    
    bot.send_message(chat_id, "🌟Choose an option:", reply_markup=user_markup)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    username = message.from_user.first_name

    # This Checks if this is the user's first interaction with the bot
    if chat_id not in user_data:

        welcome_message = f"🚀 Hello {username}! I am {bot_name} your personal Telecom academic resource assistant. Let's embark on an exciting academic journey.Choose your level below."
        channel_invite = "📢To stay connected for latest news and updates, Click the link below to join the channel and be part of the growing community of Telecom Engineers: https://t.me/learn_telesa 🚀📚"
        help_instruction = "Incase of any difficulties or problems encountered type /help."

        # Initialize user_data var for the current chat ID
        user_data[chat_id] = {}

        # Set the inital state to LEVEL
        user_data[chat_id]['state'] = LEVEL

        user_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        user_markup.row("Level 100", "Level 200")
        user_markup.row("Level 300", "Level 400")
        bot.send_message(chat_id, welcome_message, reply_markup=user_markup)
        bot.send_message(chat_id, channel_invite, reply_markup=user_markup)
        bot.send_message(chat_id, help_instruction, reply_markup=user_markup)
    else:
        # If the user has interacted with the bot before, proceed as usual
        user_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        user_markup.row("Level 100", "Level 200")
        user_markup.row("Level 300", "Level 400")
        bot.send_message(chat_id, f"📚Welcome back {username}! Choose your level below.", reply_markup=user_markup)

    
@bot.message_handler(commands=['help'])
def help(message):
    chat_id = message.chat.id
    help_message = """🤖 Welcome to my Help page 🤖

I'm here to make your academic journey easier. Whether you need course materials, lecture slides, past questions, or books, I've got you covered. No more searching; education is at your fingertips! Here's how I can assist:

1. Start by selecting your level (e.g., Level 100, Level 200) and semester.
2. Choose a course from the available options.
3. Let me know what you need (Past Questions, Lecture Slides, Recommended Books).
4. I'll provide you with the resources you're looking for.

If you have any feedback or questions, feel free to use the 'Feedback✉️' option to get in touch with me. Additionally, you can reach me in our Chatroom👥(t.me/telbotchat) for clarification, questions, or to report issues.

If you ever encounter any issues, simply type /start to begin a new conversation. Explore my features and access the resources you need for your studies. Enjoy learning! 📚✨
"""
    bot.send_message(chat_id, help_message)


@bot.message_handler(func=lambda message: message.text in ["Level 100", "Level 200", "Level 300", "Level 400"])
def level(message):
    chat_id = message.chat.id
    if chat_id in user_data:
        user_data[chat_id]['level'] = message.text
        user_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        user_markup.row("First Semester", "Second Semester")
        user_markup.row(back_button)
        bot.send_message(chat_id, f"You selected {message.text}. Choose a semester:", reply_markup=user_markup)
        user_data[chat_id]['state'] = SEMESTER
    else:
        bot.send_message(chat_id, "Please start the conversation.")
        start(message)

@bot.message_handler(func=lambda message: message.text in ["First Semester", "Second Semester"])
def semester(message):
    chat_id = message.chat.id
    if chat_id in user_data:
        user_data[chat_id]['semester'] = message.text
        user_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

        # Get the available courses based on the selected level and semester
        selected_level = user_data[chat_id]['level']
        selected_semester = user_data[chat_id]['semester']
        courses = level_courses.get(selected_level, {}).get(selected_semester, [])

        for course in courses:
            user_markup.row(course)

        user_markup.row(back_button)
        bot.send_message(chat_id, f"You selected {message.text}. Choose a course:", reply_markup=user_markup)
        user_data[chat_id]['state'] = COURSE
    else:
        bot.send_message(chat_id, "Please start the conversation.")
        start(message)

@bot.message_handler(func=lambda message: message.text in level_courses.get(user_data.get(message.chat.id, {}).get('level', ''), {}).get(user_data.get(message.chat.id, {}).get('semester', ''), []))
def course(message):
    chat_id = message.chat.id
    if chat_id in user_data:
        user_data[chat_id]['course'] = message.text
        user_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        user_markup.row("Past Questions", "Lecture Slides")
        user_markup.row("Recommended Books")
        user_markup.row("Feedback✉️")
        user_markup.row("Back🔙")
        bot.send_message(chat_id, f"You selected {message.text}. Choose a resource type:", reply_markup=user_markup)
        user_data[chat_id]['state'] = RESOURCE_TYPE
    else:
        bot.send_message(chat_id, "Please start the conversation.")
        start(message)

@bot.message_handler(func=lambda message: message.text in ["Past Questions", "Lecture Slides", "Recommended Books"])
def resource_type(message):
    chat_id = message.chat.id
    if chat_id in user_data:
        user_data[chat_id]['resource_type'] = message.text

        # Construct the path to the resource folder based on the user's choices
        selected_level = user_data[chat_id]['level']
        selected_semester = user_data[chat_id]['semester']
        selected_course = user_data[chat_id]['course']

        # constructed path
        s3_folder_path = f'assets/{selected_level}/{selected_semester}/{selected_course}/{message.text}'

        # Check if there are files in the S3 path
        objects = s3.list_objects_v2(Bucket=s3_bucket_name, Prefix=s3_folder_path)

        # Send loading indicator
        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        if 'Contents' in objects:
            # There are files in the S3 path, send them
            send_files_from_s3(chat_id, s3_folder_path)
        else:
            # No files found in the S3 path, inform the user
            bot.send_message(chat_id, "I'm sorry, but I couldn't find any files for the selected resource type. If you have any other questions or need assistance with something else, feel free to ask. I'm here to help!")

        # Update the keyboard markup to the RESOURCE_TYPE state
        update_keyboard_markup(chat_id, RESOURCE_TYPE)
    else:
        bot.send_message(chat_id, "Please start the conversation.")
        start(message)

# Function to send all files from a specified folder path to the bot chat
def send_files_from_s3(chat_id, folder_path):
    try:
      # Send a loading message
        loading_message = random.choice(loading_messages)
        message1 = bot.send_message(chat_id, loading_message)
        for _ in range(3):
                    loading_message += "."
                    bot.edit_message_text(loading_message, chat_id, message1.message_id)
                    time.sleep(1)
        # List objects in the S3 folder
        objects = s3.list_objects_v2(Bucket=s3_bucket_name, Prefix=folder_path)

        # Iterate over objects and send the files
        for obj in objects.get('Contents', []):
            file_key = obj['Key']
            
            # Get the file name from the file key
            file_name = os.path.basename(file_key)
            
            # Download the file from S3
            s3.download_file(Bucket=s3_bucket_name, Key=file_key, Filename=file_name)
            
            # Send the downloaded file to the user
            with open(file_name, 'rb') as file:
                bot.send_document(chat_id, file)
            
            # Delete the downloaded file
            os.remove(file_name)
        
    
    except Exception as e:
       
        print(f"Error occurred: {e}")




# Handler for the "Back" button
@bot.message_handler(func=lambda message: message.text == "Back🔙", content_types=['text'])
def back(message):
    chat_id = message.chat.id
    current_state = user_data.get(chat_id, {}).get('state', None)
    
    if current_state is not None:
        if current_state == RESOURCE_TYPE:
            # Go back to the course selection
            user_data[chat_id]['state'] = COURSE
            update_keyboard_markup(chat_id, COURSE)
        elif current_state == COURSE:
            # Go back to the semester selection
            user_data[chat_id]['state'] = SEMESTER
            update_keyboard_markup(chat_id, SEMESTER)
        elif current_state == SEMESTER:
            # Go back to the level selection
            user_data[chat_id]['state'] = LEVEL
            update_keyboard_markup(chat_id, LEVEL)
        elif current_state == FEEDBACK:
            # Go back to the RESOURCE_TYPE state
            user_data[chat_id]['state'] = RESOURCE_TYPE
            update_keyboard_markup(chat_id, RESOURCE_TYPE)
    else:
        bot.send_message(chat_id, "Please start the conversation.")
        start(message)


# Handler for the "Feedback" button
@bot.message_handler(func=lambda message: message.text == "Feedback✉️", content_types=['text'])
def feedback(message):
    chat_id = message.chat.id

    # Make sure the user's chat ID exists in user_data
    if chat_id in user_data:
        bot.send_message(chat_id, feedback_message)
        user_data[chat_id]['state'] = FEEDBACK
    else:
        bot.send_message(chat_id, "Please start the conversation.")
        start(message)


@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get('state') == FEEDBACK)
def process_feedback(message):
    chat_id = message.chat.id
    user_feedback = message.text
    
    username = message.from_user.username
    
    # Send user feedback to the feedback channel
    bot.send_message(personal_chat_id, f"Feedback from user @{username}:\n\n{user_feedback}")
    
    # Send a thank you message
    bot.send_message(chat_id, "🤖 I appreciate your feedback! 🙌\nI value your input; it helps me improve and serve you better. If you have more to share or any questions, don't hesitate to reach out anytime. Your experience matters to me! 📚✨")
    
    # move back to the RESOURCE_TYPE state
    user_data[chat_id]['state'] = RESOURCE_TYPE
    update_keyboard_markup(chat_id, RESOURCE_TYPE)
