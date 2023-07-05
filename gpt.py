import requests, datetime, json, sys

class GPT():
    def __init__(self, channel_language: str, channel_name: str, channel_theme: str, debug: bool = False):
        self.channel_language = channel_language
        self.channel_name = channel_name
        self.channel_theme = channel_theme
        self.debug = debug
    
    url = "https://gpt4.gravityengine.cc"
    arguments = "/api/openai/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    messages = []
    system_prompt = "From now, you are a bot for writing posts to Telegram channel. The messages that are already in the channel are written by you, so write posts neatly and beautifully. The maximum post length is 4000 characters. If your previous posts were more than 4000 characters long, then your next posts should still be no longer 4000 characters. Come up with interesting post topics to make it interesting for users to read. Name of Telegram channel is {channel_name}. Channel theme is {channel_theme}. When you get message 'create' from user, you must to write a new post to channel. Always write posts on {channel_language} language."
    
    def process_text(self, text) -> str:
        data = text.text
        if self.debug:
            print(data)
        data_json = json.loads(data)
        if "choices" in data_json:
            choice = data_json["choices"][-1]
            if "message" in choice and "content" in choice["message"]:
                content = choice["message"]["content"]
                return content
            else:
                return "Error. GPT-3.5-Turbo don't work."
        else:
            return "Error. GPT-3.5-Turbo don't work."
    
    def call(self, messages) -> str:
        data = {
            "model": "gpt-3.5-turbo",
            "temperature": 0.7,
            "messages": messages
        }

        endpoint = self.url + self.arguments
        with requests.post(url=endpoint, headers=self.headers, json=data) as response:
            msg = self.process_text(response)
            return msg

    def CreatePost(self, chat_history):
        current_datetime = datetime.datetime.now()
        system_message = {"role": "system", "content": self.system_prompt.format(channel_language=self.channel_language, channel_name=self.channel_name, channel_theme=self.channel_theme)+f"Current datetime: {current_datetime}"}
        self.messages=[system_message, {"role": "user", "content": "create"}]
        if chat_history:
            for message in chat_history:
                self.messages.append({"role": "system", "content": message})
                self.messages.append({"role": "user", "content": "create"})

        r = self.call(messages=self.messages)
        if self.debug:
            print(r)
        return r


