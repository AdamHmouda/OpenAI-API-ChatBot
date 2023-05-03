# OpenAI Chatbot

This is a simple chatbot program that uses a graphical user interface (GUI) built with the tkinter library in Python and the OpenAI API. The chatbot allows users to input text and get responses based on pre-loaded conversation prompts. The program also includes features for backing up and deleting conversation history, changing the color scheme, and configuring the bot behavior.

## Getting Started

To use the chatbot program, simply run the `main()` function in your Python environment. This will open up a new window with the chatbot GUI. 

## Requirements

- Python 3.x 
- tkinter library 
- json library 
- datetime
- openai

`Any Issues`: Just navigate to the start of the code and make sure to download the required resources for all the imports that are used.

## Functionality

### Conversation Prompts

The chatbot's conversation prompts are loaded from a JSON file called `conversation.json`, which is created when the program is first run. If this file is not found then it will be created or if the file is empty, the chatbot will display a default message.

### Creating Your OpenAI API Key

To create your API key go to : https://platform.openai.com and create your free account then navigate to https://platform.openai.com/account/api-keys and create your API key by clicking on `+ Create new secret key`, name your key anything that you wish and click `create secret key`. `Note` that you can only view your secret key one time when you create it so make sure to copy and paste it somewhere safe. If you havent copied and pasted the key somewhere you can make another one using the same proccess.

### Key Test

I have included a keytest.py which tests if your key is valid before using it for the chatbot , using this py file is not necessary its just a way to check in case for errors that your key is actually working/copied fine.

To use this keytest , simply paste your API key into `openai.api_key = "YOUR KEY"`, replace `YOUR KEY` with your `OpenAI API key`.

### Login Screen
When you first run the program you will be presented with a login screen to enter your `OpenAI API Key`(If you dont have a key, check the section above on how to get one). If the key is valid you will be redirected to the main screen where you can chat with and modify the bot.

You can also choose to click on the `Remember key Button` inside the login screen so that you wont need to enter your API key each time you run the program ,this works by storing your api key inside a json file called `remembered_key.json`, beside that after pressing the `Remember Key Button` you will be presented with `Forget Key Button` , press this button if you wish to not save your key, by doing so you will be asked to enter your API Key each time you want to use the Chatbot.

Another usefull button is the `Reset Login Button`, this button will delete the json file that stores your API key when you saved it using the `Remember Key Button`. That way you can type and store other API keys , `Note that only one API key can be stored`.

### Chatting With The Bot

To chat with the bot simply navigate to the `Chatbot Screen` after login in, write your input and click `Send Button`and the conversation will appear inside the `Textbox`

![This is an image](./chat.png)

### Color Scheme

Users can customize the chatbox color scheme `by clicking on Bot Configuration Button` and `navigating to the Chat Color Settings` Section and Finally `typing what collor they need` for either the `User chat` or the `Bot chat`and `clicking` on the `Confirm Button`.

`Note that you need to rerun the program for the changes to work`.

![This is an image](./color1.png)
`Result`
![This is an image](./color2.png)

### Backup And Delete Conversation History

Users can backup their conversation history by clicking the `Backup Conversation` button. This will create a `JSON file` called `conversation_backup.json` that contains all the conversation prompts and their timestamps in the directory that they desire. Users can delete their conversation history by clicking the `Delete Conversation` button, which will display a confirmation message before deleting the file.

### Restoring Conversation

To restore a conversation that you have previously backed up , Simply drag and drop the `Conversation.json` file to the directory where main.py is located.

### Bot Personality Behavior

Users can configure the chatbot personality by clicking the `Bot Configuration` button, which will open up a new window with settings for the chatbot's personality called `Choose Bot Personality`, to set a specifiq personality for the bot `you simply type in the entry field` what personality you want the bot to respond with and click the `Confirm Button`. After changing the bot personality, the bot will start to respond as the chosen personality would, example in the picture below :

![This is an image](./b1.png)
`Result`
In the previous picture that is in the color Scheme section the bot responded as a general A.I would but after making the changes the bot responded as a potato :
![This is an image](./b2.png)

`Note that you need to rerun the program for the changes to work`.

### Bot Output Settings

Users can also change how the bot messages get outputed by clicking on the `Bot Configuration Button` and navigating into the `Output Settings` Section, from there users can type diffrent variables to change the bot chat output settings , here is a breakdown of what each setting does :

```
Temperature: This controls the randomness of the generated text. Higher values lead to more random and unpredictable outputs, while lower values lead to more conservative and predictable outputs.
```
```
Max Tokens: This controls the maximum length of the generated text, measured in the number of tokens (words or subwords). Setting this parameter to a lower value will generate shorter texts, while setting it to a higher value will generate longer texts.
```

```
Top P: This controls the diversity of the generated text by limiting the set of tokens the model is allowed to choose from. The model will only choose tokens whose cumulative probability mass is less than top_p. Setting this parameter to a lower value will result in more conservative and predictable outputs, while setting it to a higher value will result in more diverse and creative outputs.
```

```
Frequency Penalty: This parameter discourages the model from repeating the same words or phrases too frequently. Setting this parameter to a higher value will result in more diverse and varied outputs, while setting it to a lower value will result in more repetitive outputs.
```

```
Presence Penalty: This parameter discourages the model from including certain words or phrases in the generated text. Setting this parameter to a higher value will result in outputs that are less likely to contain specific words or phrases, while setting it to a lower value will result in outputs that are more likely to contain those words or phrases.
```
The user can also reset these paramaters to default settings by clicking on the `Reset To Default Button`.
`Note that you need to rerun the program for the changes to work`.

To view all current applied settings press the `Show Current Settings Button`. This will show a `Messagebox` containing all current applied data.

`NOTE` each time you want to change setting inside a particular section , `You need to modify all the settings in that section.` For Example you cant just change the `Temperature` that is part of the `Output settings Section`, you need to also change the `Max Tokens`, `Top P`, `Frequency Penalty` and `Presence Penalty` before clicking on `Confirm`.
### Exiting

It is preffered to exit the chatbot program by clicking on the `Exit Button` above the `Chatbox` this way the program can save the data correctly when it closes.
## Authors

This program was created by Adam Hmouda for learning purpose.

`Contact : adamhamouda24@gmail.com`

## License

You may edit this code as you see fit for your personal use but you may not sell it.

## Code Descriptions and usage
In this section i will provide what each Important function does:

```python
def create_conversation_file():
```
This Python function checks if a file named `conversation.json` exists in the current directory. If it does, it does nothing. If it does not exist, the function creates the file and initializes it with an empty JSON array. This file can later be used to store conversation data.

```python
def get_api_response(prompt: str) -> str | None:
```
This Python function takes a `prompt` string as input and returns a string or `None` object as output. The function uses the OpenAI API to generate a response to the given prompt.

Here's a step-by-step breakdown of what each line of the code does:

1. `def get_api_response(prompt: str) -> str | None:` defines a function named `get_api_response` that takes a string as input and returns a string or `None` object as output.
2. `text: str | None = None` initializes the variable `text` as a `str` or `None` object and sets its value to `None`.
3. `try:` starts a try-except block that attempts to open the file `settings.json` for reading.
4. `with open("settings.json", "r") as f:` opens the file named `settings.json` in read-only mode and assigns it to the variable `f`.
5. `settings = json.load(f)` reads the contents of the file as a JSON object and assigns it to the variable `settings`.
6. `response: dict = openai.Completion.create(...)` sends a request to the OpenAI API using the `openai.Completion.create()` method and assigns the resulting JSON response to the variable `response`. This method generates text based on the given `prompt` using the `text-davinci-003` model, which is a pre-trained language model that can generate human-like text.
7. The `response` object contains a list of `choices`. The code accesses the first `choice` object in the list and assigns it to the variable `choices`.
8. `text = choices.get('text')` extracts the generated text from the `choices` object and assigns it to the variable `text`.
9. `except Exception as e:` catches any exceptions that occur within the `try` block and assigns them to the variable `e`.
10. `print('ERROR:', e)` prints an error message if an exception occurs.
11. `return text` returns the generated text or `None` object to the caller of the function.

```python
def create_settings_file():
```
This Python function checks if a file named `settings.json` exists in the current working directory. If it does not exist, the function creates the file and initializes it with default settings for the OpenAI API. The default settings include values for parameters such as `temperature`, `max_tokens`, `top_p`, `frequency_penalty`, and `presence_penalty`.

```python
def create_color_settings_file():
```
This Python function checks if a file named `colors_settings.json` exists in the current working directory. If it does not exist, the function creates the file and initializes it with default color settings. The default color settings include values for the color of the user and bot messages.

```python
def create_prompt(message: str, pl: list[dict]) -> str:
```
This function creates a prompt for the OpenAI API based on the message provided by the user and the conversation history stored in a Json file called `Conversation.json` . Here's a step-by-step breakdown of what each line of the code does:

1. `def create_prompt(message: str, pl: list[dict]) -> str:` defines a function named `create_prompt` that takes two parameters: `message` (a string representing the message entered by the user) and `pl` (a list of dictionaries representing the conversation history).
2. `p_message: str = f'\nHuman: {message}'` creates a string `p_message` that adds the prefix "Human: " to the user's message.
3. `update_list(p_message, pl)` calls a function named `update_list` with parameters `p_message` and `pl`. The purpose of this function is not provided in the code snippet, but it is likely that it updates the conversation history list with the user's message.
4. `prompt_date = datetime.datetime.now().strftime('%d/%m/%Y')` creates a string `prompt_date` that represents the current date in the format "dd/mm/yyyy".
5. `prompt: str = ''.join([f"\n{p['message']}\n" for p in pl]).replace('XX/XX/XXXX', prompt_date)` creates a string `prompt` that concatenates all the messages in the conversation history stored in `pl`, replacing any occurrences of "XX/XX/XXXX" with the current date. The `join()` method is used to concatenate the messages in the list of dictionaries `pl`.
6. `return prompt` returns the `prompt` string. The `prompt` string will be used as input for the OpenAI API to generate a response to the user's message.

```python
def get_bot_response(message, pl):
```
This is a function that generates a response from a chatbot to a given message. It takes two arguments: `message` and `pl`. `message` is the message sent by the user to the chatbot and `pl` is a list of dictionaries representing the conversation history.

The function starts by creating a prompt using the `create_prompt()` function and the given `message` and `pl` arguments. If the user's message is a request for the date and time of the last message or the current day, the function returns the appropriate response based on the `pl` history or the current system time, respectively.

If the user's message is not a request for the date or day, the function calls the `get_api_response()` function to generate a response from the chatbot using OpenAI's API. If the response is successfully obtained, it is cleaned up and added to the conversation history. If there is an error obtaining the response, the function returns an error message.

Finally, the function replaces the time and date placeholders in the response with the current system time and date and returns the updated response.

```python
def save_conversation(pl: list[dict], filename: str):
```

This function takes a list of dictionaries `pl` and a filename `filename`, and writes the contents of `pl` to a JSON file at the specified `filename`. The data is written with an indentation level of 2 spaces for readability.

```python
def load_conversation(filename: str) -> list[dict]:
```
This function takes  `conversation.json`, and attempts to open the file for reading. If the file exists, it reads the contents of the file as JSON and returns the resulting list of dictionaries. If the file does not exist, an empty list is returned.

```python
def backup_conversation():
```
This function prompts the user to select a directory for backing up the conversation. If a directory is selected, the function creates a backup of the conversation file (`conversation.json`) in the selected directory by copying the file to the backup directory. Finally, the function displays a message box to inform the user that the backup was successful.

```python
def delete_chat(file_name):
```
The `delete_chat` function takes a file name as input, checks if the file exists, and removes the file if it exists. If the file is removed, it shows a message box indicating that the file was deleted successfully. If the file does not exist, it shows a message box indicating that the file was not found.

```python
def send_message(entry_field, chat_box, prompt_list):
```
This function takes in the user's input from an entry field, the chat box widget, and the list of prompts and responses. It then calls the `get_bot_response` function to generate a response from the chatbot based on the input and prompts so far. The function then updates the chat box to display the user's input and the chatbot's response, and saves the conversation to a file.

Overall, this function handles sending the user's message to the chatbot, displaying the response, and saving the conversation history.

```python
def assign_personality(message: str, file_path: str):
```
The `assign_personality` logg a message to a file to assign a personality based on the conversation. Here is how it works:

1. It tries to open the file at `file_path` and read its contents into the `conversation` variable.
2. If the file is not found, it initializes `conversation` to an empty list.
3. It appends a dictionary to `conversation` containing the `'message'` key with the value of the `message` parameter.
4. It writes the updated `conversation` list to the file at `file_path`.

```python
def save_settings():
```
The `save_settings()` function saves the values entered in the GUI settings window to a JSON file named `settings.json`.

After the settings are saved, a message box is displayed to inform the user that the operation was successful. Finally, the function clears the entry fields in the settings window.

```python
def save_color():
```
The save_color function saves the user's color settings for the chat window to a `JSON file`called `colors_settings.json`

After the settings are saved, a message box is displayed to inform the user that the operation was successful. Finally, the function clears the entry fields in the settings window.

```python
def save_personality():
```
This code saves the personality behavior entered by the user in a JSON file called `personality.json`. The function first gets the personality behavior from a tkinter Entry widget called `personality_entry` and stores it in a dictionary called `persona` with the key "behavior". 

Finally, a message box is displayed indicating that the personality behavior was saved successfully, and the contents of the `personality_entry` widget are deleted.

```python
def reset_settings():
```
This code resets the values of various parameters in the `settings.json` file to a default setting. 

The function reads the existing settings from the file, updates the values of the parameters, and writes the updated settings back to the file.

The updated values of the parameters are:

- `temperature` = 0.9
- `max_tokens` = 150
- `top_p` = 1
- `frequency_penalty` = 0
- `presence_penalty` = 0.6

After the settings are reset, the function displays a message box to inform the user that the settings have been reset and clears the values in the entry fields for the parameters.

```python
def open_bot_config():
```
This function creates a graphical user interface for configuring the chatbot. When called, it creates a new window with various input fields, labels and buttons. The window has several sections - "Bot Personality", "Output Settings", "Chat Color Settings". In the "Bot Personality" section, there is a label asking the user to choose a bot personality, an input field for entering the name of the bot's personality and a confirmation button. In the "Output Settings" section, there are several labels and input fields for setting various parameters such as temperature, max tokens, top P, frequency penalty, and presence penalty, each with a default value. There are two confirmation buttons in this section, one for saving the settings and one for resetting the settings to default values. In the "Chat Color Settings" section, there are input fields for setting the colors of user and bot messages.

```python
def signed_in():
```
Here's a brief summary of what this code does:

1. It gets the value of a global variable `api_key` from an entry widget called `api_key_entry`.
2. If a radio button with the value of `"selected"` is selected, it saves the `api_key` in a JSON file called `"remembered_keys.json"`.
3. It hides the login window using the `withdraw()` method.
4. It calls another function called `main()`.

```python
def validate_api_key():
```
This function is used to validate the API key entered by the user. 

It first sets the API key using `openai.api_key = api_key_entry.get()`, where `api_key_entry` is a tkinter Entry widget that the user enters their API key into. 

It then tries to create a completion using `openai.Completion.create()`, which is a simple API call to OpenAI's API that doesn't require any specific input. If the API key is valid, the completion should be successful and the function will print "API key is valid" and call the `signed_in()` function to continue the program flow. 

If there is an error creating the completion, the function will print "API key is not valid" and display an "Invalid API key" label in the tkinter `login` window. The label is created using `tk.Label()` and added to the window using `grid()`. It also sets the text of the label to "Invalid API key" and sets the foreground color to red.

```python
def login_s():
```
The `login_s()` function sets up the login window using tkinter. The function includes a text label and an entry widget for the API key, buttons for logging in and resetting the login, and a radio button and forget button for remembering or forgetting the API key. If a remembered key is found in a saved file, it will automatically populate the API key entry.

The `reset_login()` function deletes the saved API key file if it exists and removes the forget button from the login window. The `update_clear_button_visibility()` function displays the forget button if the "Remember Key" radio button is selected, and hides it if not.

Finally, the `login.mainloop()` statement starts the main loop for the login window.

```python
def main():
```
This code defines a main function that creates a GUI chatbot interface using the tkinter module. 

Here is a breakdown of what the code does:

- Creates a new Toplevel window using the tkinter module.
- Sets the title of the window to "Chatbot".
- Loads the conversation history from a JSON file named "conversation.json" using the load_conversation function.
- If there is no conversation history, sets a default prompt message in the form of a dictionary.
- Loads user and bot colors from a JSON file named "colors_settings.json".
- Defines a Text widget named "chat_box" to display the conversation history. The widget is disabled to prevent user input.
- Configures two tag configurations for the chat_box widget for the user and bot messages, respectively, using the user_color and bot_color values.
- Defines a horizontal scrollbar named "scrollbar_x" for the chat_box widget.
- Configures the chat_box widget to use the scrollbar_x widget using the configure method.
- Configures the scrollbar_x widget to set the xview of the chat_box widget when scrolled.
- Defines an Entry widget named "entry_field" for the user to input text.
- Sets focus to the entry_field widget.
- Defines a Label widget named "label_text" to prompt the user to enter text.
- Defines a Button widget named "send_button" to submit the user's text input to the chatbot. The button calls the send_message function with the entry_field, chat_box, and prompt_list arguments using a lambda function.
- Defines a Button widget named "backup_button" to backup the conversation history to a file named "conversation_backup.json". The button calls the backup_conversation function.
- Defines a Button widget named "delete_button" to delete the conversation history. The button calls the delete_chat_with_confirmation function.
- Defines a Button widget named "config_button" to open the bot configuration settings. The button calls the open_bot_config function.
- Defines a Button widget named "exit_button" to exit the chatbot. The button calls the exit function.
- Calls the mainloop method to start the tkinter event loop.

## Full Code

```python
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
```