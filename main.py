import tkinter as tk
from datetime import datetime
import datetime
import openai
import json
import os
import shutil
from tkinter import filedialog
from tkinter import messagebox, simpledialog

def create_conversation_file():
    try:
        with open("conversation.json", "r") as f:
            pass
    except FileNotFoundError:
        with open("conversation.json", "w") as f:
            json.dump([], f)

def get_api_response(prompt: str) -> str | None:
    text: str | None = None

    try:
        with open("settings.json", "r") as f:
            settings = json.load(f)

        response: dict = openai.Completion.create(
            model='text-davinci-003',
            prompt=prompt,
            temperature=settings["temperature"],
            max_tokens=settings["max_tokens"],
            top_p=settings["top_p"],
            frequency_penalty=settings["frequency_penalty"],
            presence_penalty=settings["presence_penalty"],
            stop=[' Human:', ' AI:']
        )

        choices: dict = response.get('choices')[0]
        text = choices.get('text')

    except Exception as e:
        print('ERROR:', e)

    return text
#👻 Just passing through.....
def create_settings_file():
    if not os.path.exists('settings.json'):
        default_settings = {"temperature": 0.9,"max_tokens": 150,"top_p": 1,"frequency_penalty": 0,"presence_penalty": 0.6}
        with open('settings.json', 'w') as f:
            json.dump(default_settings, f)

def create_color_settings_file():
    if not os.path.exists('colors_settings.json'):
        default_color_settings = {"user_color": "red","bot_color": "blue"}
        with open('colors_settings.json', 'w') as f:
            json.dump(default_color_settings, f)

def create_personality_file():
    if not os.path.exists('personality.json'):
        data = {'behavior': 'artificial intelligence'}
        with open('personality.json', 'w') as f:
            json.dump(data, f)

def update_list(message: str, pl: list[dict]):
    pl.append({'message': message,'timestamp': datetime.datetime.now().isoformat()})

def create_prompt(message: str, pl: list[dict]) -> str:
    p_message: str = f'\nHuman: {message}'
    update_list(p_message, pl)
    prompt_date = datetime.datetime.now().strftime('%d/%m/%Y')
    prompt: str = ''.join([f"\n{p['message']}\n" for p in pl]).replace('XX/XX/XXXX', prompt_date)
    return prompt

def get_bot_response(message, pl):
    prompt = create_prompt(message, pl)
    if message.strip().lower() == 'what is the date and time on the last message':
        if len(pl) > 1:
            last_message = sorted([p for p in pl if 'message' in p.keys()])[-2]
            last_message_dt = datetime.datetime.strptime(last_message['timestamp'], '%Y-%m-%dT%H:%M:%S.%f')
            last_message_date = last_message_dt.strftime('%d/%m/%Y')
            last_message_time = last_message_dt.strftime('%-I:%M %p')
            return f"On the last message, the date was {last_message_date} and the time was {last_message_time} (depending on your local time zone)."
        else:
            return "Sorry, there is no previous message to retrieve the date and time from."
    if message.strip().lower() == 'what day are we today' or message.strip().lower() == 'what day is it today' or message.strip().lower() == 'what day is it':
        current_day = datetime.datetime.now().strftime('%A')
        return f"The current day is {current_day}."
    bot_response = get_api_response(prompt)

    if bot_response:
        bot_response_lines = bot_response.splitlines()

        bot_response_lines = [line.replace("AI:", "").strip() for line in bot_response_lines]

        bot_response = "\n".join(bot_response_lines)

        update_list(bot_response, pl)
    else:
        bot_response = "Something went wrong..."
#🥕 CARROT RICKKKKK!!,I TURNED MYSELF INTO A CAROT MORTYY!, IM CARROT RICK BAbBYYYYY LOOK AT MEEE IM A CAROOTTTT!!
    current_time = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=3))).strftime('%-I:%M %p')
    current_date = datetime.datetime.now().strftime('%d/%m/%Y')
    return bot_response.replace('XX:XX', current_time).replace('XX/XX/XXXX', current_date)

def save_conversation(pl: list[dict], filename: str):
    with open(filename, 'w') as f:
        json.dump(pl, f, indent=2)

def load_conversation(filename: str) -> list[dict]:
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def backup_conversation():
    backup_dir = filedialog.askdirectory(title="Select backup directory")
    if backup_dir:
        shutil.copyfile("conversation.json", os.path.join(backup_dir, "conversation.json"))
        messagebox.showinfo("Backup Successful", "Conversation backup was successful.")

def delete_chat(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        messagebox.showinfo("File Deleted", f"{file_name} deleted successfully")
    else:
        messagebox.showinfo("File Not Found", f"{file_name} does not exist")

def delete_chat_with_confirmation():
    user_input = simpledialog.askstring("Confirmation", "⚠️ Warning: This will delete the entire conversation you had with the bot. \n                                 Type 'delete' to confirm deletion:")
    if user_input == "delete":
        delete_chat('conversation.json')
    else:
        messagebox.showinfo("Deletion Cancelled", "File deletion cancelled")

def send_message(entry_field, chat_box, prompt_list):
    user_input = entry_field.get()

    bot_response = get_bot_response(user_input, prompt_list)

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"You: {user_input}\n", "user_message")
    chat_box.insert(tk.END, f"Bot: {bot_response}\n\n", "bot_message")
    chat_box.config(state=tk.DISABLED)

    save_conversation(prompt_list, "conversation.json")

    entry_field.delete(0, tk.END)

def exit():
    window.destroy()
    login.destroy()

def assign_personality(message: str, file_path: str):
    try:
        with open(file_path, 'r') as f:
            conversation = json.load(f)
    except FileNotFoundError:
        conversation = []
#It took me 2 hours to figure out how to give it a certain behavior properly.....End me 💀
    conversation.append({
        'message': message})

    with open(file_path, 'w') as f:
        json.dump(conversation, f)

def clear_p_entry():
    personality_entry.delete(0, tk.END)

def save_settings():
    temperature = float(temperature_entry.get())
    max_tokens = int(max_tokens_entry.get())
    top_p = float(top_p_entry.get())
    frequency_penalty = float(freq_penalty_entry.get())
    presence_penalty = float(presence_penalty_entry.get())

    settings = {"temperature": temperature,"max_tokens": max_tokens,"top_p": top_p,"frequency_penalty": frequency_penalty,"presence_penalty": presence_penalty}

    with open("settings.json", "w") as f:
        json.dump(settings, f)

    messagebox.showinfo("Settings Saved", "The settings were saved successfully!")

    temperature_entry.delete(0, tk.END)
    max_tokens_entry.delete(0, tk.END)
    top_p_entry.delete(0, tk.END)
    freq_penalty_entry.delete(0, tk.END)
    presence_penalty_entry.delete(0, tk.END)

def save_color():
    colors = {"user_color": user_color_entry.get(),"bot_color": bot_color_entry.get()}

    with open("colors_settings.json", "w") as f:
        json.dump(colors, f)

    messagebox.showinfo("Settings Saved", "The settings were saved successfully!")

    user_color_entry.delete(0, tk.END)
    bot_color_entry.delete(0, tk.END)

def save_personality():
    persona = {"behavior": personality_entry.get()}

    with open("personality.json", "w") as f:
        json.dump(persona, f)

    messagebox.showinfo("Settings Saved", "The personality behavior is saved successfully!")

    personality_entry.delete(0, tk.END)

# 👻 Nothing to see here keep scrolling...


def reset_settings():
    with open('settings.json', 'r') as f:
        settings = json.load(f)

    settings['temperature'] = float(settings['temperature'])
    settings['max_tokens'] = int(settings['max_tokens'])
    settings['top_p'] = float(settings['top_p'])
    settings['frequency_penalty'] = float(settings['frequency_penalty'])
    settings['presence_penalty'] = float(settings['presence_penalty'])

    settings['temperature'] = 0.9
    settings['max_tokens'] = 150
    settings['top_p'] = 1
    settings['frequency_penalty'] = 0
    settings['presence_penalty'] = 0.6

    with open('settings.json', 'w') as f:
        json.dump(settings, f)

    messagebox.showinfo("Settings Saved", "The settings were Reset successfully!")

    temperature_entry.delete(0, tk.END)
    max_tokens_entry.delete(0, tk.END)
    top_p_entry.delete(0, tk.END)
    freq_penalty_entry.delete(0, tk.END)
    presence_penalty_entry.delete(0, tk.END)

def show_json_files():
    with open('personality.json') as f:
        personality = json.load(f)
    with open('settings.json') as f:
        settings = json.load(f)
    with open('colors_settings.json') as f:
        colors_setting = json.load(f)

    personality_str = "\n".join([f"{k}: {v}" for k, v in personality.items()])
    settings_str = "\n".join([f"{k}: {v}" for k, v in settings.items()])
    colors_setting_str = "\n".join([f"{k}: {v}" for k, v in colors_setting.items()])
    message = f"Personality:\n{personality_str}\n\nSettings:\n{settings_str}\n\nColor settings:\n{colors_setting_str}"

    messagebox.showinfo("JSON Files", message)

def open_bot_config():
    config_window = tk.Toplevel()
    config_window.title("⚙️ Bot Configuration")

    choose_personality_label = tk.Label(config_window, text="🧠 Choose Bot Personality:")
    choose_personality_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

    global personality_entry
    personality_entry = tk.Entry(config_window)
    personality_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

    split_label = tk.Label(config_window, text="__________________________________________________________________")
    split_label.grid(row=2, column=0, padx=5, sticky=tk.W, columnspan=3)

    info_label = tk.Label(config_window, text="        🛠️ Output Settings")
    info_label.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W, columnspan=3)

    temperature_label = tk.Label(config_window, text="Temperature:")
    temperature_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

    temperature_d_label = tk.Label(config_window, text="default (0.9)")
    temperature_d_label.grid(row=4, column=2, padx=5, pady=5, sticky=tk.W)

    global temperature_entry
    temperature_entry = tk.Entry(config_window)
    temperature_entry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

    max_tokens_label = tk.Label(config_window, text=" Max Tokens:")
    max_tokens_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

    max_tokens_d_label = tk.Label(config_window, text="default (150)")
    max_tokens_d_label.grid(row=5, column=2, padx=5, pady=5, sticky=tk.W)

    global max_tokens_entry
    max_tokens_entry = tk.Entry(config_window)
    max_tokens_entry.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

    top_p_label = tk.Label(config_window, text="Top P:")
    top_p_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)

    top_p_label_d = tk.Label(config_window, text="default (1)")
    top_p_label_d.grid(row=6, column=2, padx=5, pady=5, sticky=tk.W)

    global top_p_entry
    top_p_entry = tk.Entry(config_window)
    top_p_entry.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

    freq_penalty_label = tk.Label(config_window, text="Frequency Penalty:")
    freq_penalty_label.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)

    freq_penalty_label_d = tk.Label(config_window, text="default (0)")
    freq_penalty_label_d.grid(row=7, column=2, padx=5, pady=5, sticky=tk.W)

    global freq_penalty_entry
    freq_penalty_entry = tk.Entry(config_window)
    freq_penalty_entry.grid(row=7, column=1, padx=5, pady=5, sticky=tk.W)

    presence_penalty_label = tk.Label(config_window, text="Presence Penalty:")
    presence_penalty_label.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)

    presence_penalty_label_d = tk.Label(config_window, text="default (0.6)")
    presence_penalty_label_d.grid(row=8, column=2, padx=5, pady=5, sticky=tk.W)

    global presence_penalty_entry
    presence_penalty_entry = tk.Entry(config_window)
    presence_penalty_entry.grid(row=8, column=1, padx=5, pady=5, sticky=tk.W)

    confirm_button = tk.Button(config_window, text="✅ Confirm", command=lambda: [(assign_personality(f'You are a {personality_entry.get()} and will answer as a {personality_entry.get()} would', "conversation.json"), save_personality(), clear_p_entry())])
    confirm_button.grid(row=1, column=1, pady=5)

    confirm_button2 = tk.Button(config_window, text="✅ Confirm", command=save_settings)
    confirm_button2.grid(row=9, column=1, padx=5)

    reset_button2 = tk.Button(config_window, text="💡 Reset To Default", command=reset_settings)
    reset_button2.grid(row=10, column=1, padx=5)

    split2_label = tk.Label(config_window, text="__________________________________________________________________")
    split2_label.grid(row=11, column=0, padx=5, sticky=tk.W, columnspan=3)

    info2_label = tk.Label(config_window, text="     🎨 Chat Color Settings")
    info2_label.grid(row=12, column=1, padx=5, pady=5, sticky=tk.W, columnspan=3)

    user_color_label = tk.Label(config_window, text="👥 User Messages Color:")
    user_color_label.grid(row=13, column=0, padx=5, pady=5, sticky=tk.W)

    global user_color_entry
    user_color_entry = tk.Entry(config_window)
    user_color_entry.grid(row=13, column=1, padx=5, pady=5, sticky=tk.W)

    bot_color_label = tk.Label(config_window, text="🤖 Bot Messages Color:")
    bot_color_label.grid(row=14, column=0, padx=5, pady=5, sticky=tk.W)

    global bot_color_entry
    bot_color_entry = tk.Entry(config_window)
    bot_color_entry.grid(row=14, column=1, padx=5, pady=5, sticky=tk.W)

    confirm_button3 = tk.Button(config_window, text="✅ Confirm", command=save_color)
    confirm_button3.grid(row=15, column=1, padx=5, pady=5)

    split3_label = tk.Label(config_window, text="__________________________________________________________________")
    split3_label.grid(row=16, column=0, padx=5, sticky=tk.W, columnspan=3)

    show_button = tk.Button(config_window, text="🧰 Show Current Settings", command=show_json_files)
    show_button.grid(row=17, column=1, pady=5)

    note_label = tk.Label(config_window, text="⚠️ Always fill all the Entries in a Section even if you are planning to change one Entry.")
    note_label.grid(row=18, column=0, padx=5, pady=5, columnspan=3)

    reload_label = tk.Label(config_window, text="⚠️ Exit the programe and run it again after Confirming anything for changes to work.")
    reload_label.grid(row=19, column=0, padx=5, pady=5, columnspan=3)

    config_window.mainloop()

#Random clown here 🤡 , wanna hear a joke ?...Take a selfie and youl figure out the rest :D


def signed_in():
    global api_key
    api_key = api_key_entry.get()
    if selected_value.get() == "selected":
        data = {"api_key": api_key}
        with open("remembered_keys.json", "w") as f:
            json.dump(data, f)
    login.withdraw()
    main()

def validate_api_key():
    openai.api_key = api_key_entry.get()
    try:
        openai.Completion.create(
            engine="davinci",
            prompt="Hello, world!",
            max_tokens=5
        )
        print("API key is valid.")
        signed_in()
    except Exception as e:
        print("API key is not valid.")
        invalid_key_label = tk.Label(login, text="Invalid API key")
        invalid_key_label.grid(row=2, column=1, padx=10, pady=10)
        invalid_key_label.config(text="⛔️ Invalid API key", fg="red")

def login_s():
    global login
    login = tk.Tk()
    login.title("Login")

    api_key_label = tk.Label(login, text="🔑 Enter your OpenAI API key:")
    api_key_label.grid(row=0, column=0, padx=10, pady=10)

    global api_key_entry
    api_key_entry = tk.Entry(login, show="*")
    api_key_entry.grid(row=0, column=1, padx=10, pady=10)

    if os.path.exists("remembered_keys.json"):
        with open("remembered_keys.json", "r") as f:
            remembered_keys = json.load(f)
            saved_api_key = remembered_keys.get("api_key")
            if saved_api_key:
                api_key_entry.insert(0, saved_api_key)

    def reset_login():
        if os.path.exists("remembered_keys.json"):
            os.remove("remembered_keys.json")
            clear_button.grid_forget()
            messagebox.showinfo("Login Reset", "The login has been reset.")
        else:
            messagebox.showwarning("File Not Found", "The login file was not found.")

    button_reset_login = tk.Button(login, text="🔄 Reset login", width=14, command=reset_login)
    button_reset_login.grid(row=1, column=0, padx=10, pady=10)

    button_login = tk.Button(login, text="🔐Login", command=validate_api_key)
    button_login.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

    global selected_value
    selected_value = tk.StringVar(value=None)
    radio_button = tk.Radiobutton(login, text="Remember Key", variable=selected_value, value="selected")
    radio_button.grid(row=2, column=0, pady=10)

    def update_clear_button_visibility():
        if selected_value.get() == "selected":
            clear_button.grid(row=2, column=0, pady=10)
        else:
            clear_button.grid_forget()

    clear_button = tk.Button(login, text="Forget Key", width=14, command=lambda: selected_value.set(None))
    update_clear_button_visibility()
    selected_value.trace_add("write", lambda *args: update_clear_button_visibility())

    login.mainloop()
#👀 watcha looking at ??
def main():
    global window
    window = tk.Toplevel()
    window.title("Chatbot")

    prompt_list = load_conversation("conversation.json")
    if not prompt_list:
        prompt_list = [{'message': 'You are a highly intelligent Artificial Intelligent and will answer as a Artificial Intelligent', 'timestamp': datetime.datetime.now().isoformat()}]

    with open('colors_settings.json', 'r') as f:
        color_settings = json.load(f)

    user_color = color_settings['user_color']
    bot_color = color_settings['bot_color']

    chat_box = tk.Text(window, width=110, height=20, state=tk.DISABLED)
    chat_box.tag_config("user_message", foreground=user_color)
    chat_box.tag_config("bot_message", foreground=bot_color)
    chat_box.grid(row=1, column=0, padx=10)

    scrollbar_x = tk.Scrollbar(window, orient=tk.HORIZONTAL)
    scrollbar_x.grid(row=2, column=0, sticky="ew")

    chat_box.configure(xscrollcommand=scrollbar_x.set)
    scrollbar_x.configure(command=chat_box.xview)

    entry_field = tk.Entry(window, width=60)
    entry_field.grid(row=3, column=0, padx=10, pady=10)
    entry_field.focus()

    label_text = tk.Label(window, text="📝 Enter Text:")
    label_text.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

    send_button = tk.Button(window, text="📩 Send", width=16, command=lambda: send_message(entry_field, chat_box, prompt_list))
    send_button.grid(row=4, column=0, padx=10, pady=10)

    backup_button = tk.Button(window, text="🔒 Backup Conversation", command=backup_conversation)
    backup_button.grid(row=1, column=1, padx=10, pady=10)

    delete_button = tk.Button(window, text="🗑️ Delete Conversation", command=delete_chat_with_confirmation)
    delete_button.grid(row=2, column=1)

    config_button = tk.Button(window, text="⚙️ Bot Configuration", command=open_bot_config)
    config_button.grid(row=0, column=1, padx=10, pady=10)

    exit_button = tk.Button(window, text="❌ Exit",width=10, command=exit)
    exit_button.grid(row=0, column=0, padx=10, pady=10)

    window.mainloop()

create_conversation_file()
create_settings_file()
create_color_settings_file()
create_personality_file()
login_s()