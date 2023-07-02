import os, requests, sys
from gpt import GPT

class TelegramBot:
    def __init__(self, debug: bool = False):
        try:
            self.channel_id = os.environ.get('channel_id')
            self.bot_token = os.environ.get('bot_token')
            self.temperature = float(os.environ.get('temperature'))
            self.channel_name = os.environ.get('channel_name')
            self.channel_theme = os.environ.get('channel_theme')
            self.channel_language = os.environ.get('channel_language')
        except:
            print("\033[1;31mError. You don't create all environment variables.\033[0m")
            sys.exit()
        self.debug = debug

    def create_post(self):
        model = GPT(debug=self.debug, temperature=self.temperature, channel_name=self.channel_name, channel_theme=self.channel_theme, channel_language=self.channel_language)
        post = model.CreatePost()
        if len(post)>4096:
            post = post[:4096]
        return post

    def send_post(self, post):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        data = {
            'chat_id': self.channel_id,
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

