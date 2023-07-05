import os, requests, sys
from gpt import GPT

class TelegramBot:
    def __init__(self, debug: bool = False):
        try:
            self.channel_url = os.environ.get('channel_url')
            self.bot_token = os.environ.get('bot_token')
            self.channel_name = os.environ.get('channel_name')
            self.channel_theme = os.environ.get('channel_theme')
            self.channel_language = os.environ.get('channel_language')
        except:
            print("\033[1;31mError. You don't create all environment variables.\033[0m")
            sys.exit()
        self.debug = debug

    def get_channel_username(self, channel_url) -> str:
        if "https://t.me/" in channel_url:
            response = requests.get(channel_url)
            if response.status_code == 200:
                url_list = channel_url.split("/")
                channel_username = f"@{url_list[-1]}"
                return channel_username
            else:
                print("\033[1;31mError. Invalid channel url.\033[0m")
                sys.exit()
        else:
            print("\033[1;31mError. Invalid channel url.\033[0m")
            sys.exit()

    def get_channel_messages(self, limit=20):
        with open("messages.txt", "r") as file:
            text = file.read()
            text_list = text.split("\end_of_post")
            if len(text_list) > limit:
                text_list = text_list[-20:]
            return text_list

    def create_post(self):
        model = GPT(debug=self.debug, channel_name=self.channel_name, channel_theme=self.channel_theme, channel_language=self.channel_language)
        chat_history = self.get_channel_messages()
        post = model.CreatePost(chat_history=chat_history)
        if len(post)>4096:
            post = post[:4096]
        return post

    def send_post(self, post):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        data = {
            'chat_id': self.get_channel_username(self.channel_url),
            'text': post
        }
        response = requests.post(url, data=data)
        if self.debug:
            if response.status_code == 200:
                print("Post sent successfully!")
            else:
                print("Failed to send post.")

        with open("messages.txt", "a") as file:
            file.write(post+"\end_of_post")

