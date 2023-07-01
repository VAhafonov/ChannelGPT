<a href="https://www.buymeacoffee.com/metimol" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## Hello everyone!

I had several Telegram channels, but I didn't enjoy managing them. It was time-consuming, and I constantly had to search for new topics and information for the channels. That's when I decided to create this project. 
It's an **entirely free gpt-3.5-turbo that will manage your channel for you.** You just need to set up the virtual environment variables and run the bot with a single command. 

The bot remembers the last 10 messages it sent to your channel. And always write interesting posts.

Interested? Here's the complete guide:

## Run on Replit
- If you don't have account on [Replit](https://replit.com/), create it. It's Free.
- Click this button and deploy my repository to your Replit account.

[![Try on repl.it](https://img.shields.io/badge/Replit-DD1200?style=for-the-badge&logo=Replit&logoColor=white)](https://repl.it/github/metim0l/ChannelGPT)

- Configure `.replit` to run `python3 main.py`

![image](https://github.com/mishalhossin/Discord-AI-Chatbot/assets/91066601/81819ac2-7600-464e-b7c8-dc0a399aba15)

- Run command `pip install -r requirements.txt` in Replit Terminal. You can run Terminal in `Shell` from `Tools` tab in Replit.
- Go to Telegram and create new bot with BotFather.
- Add your new bot to your channel admins.
- Create Environment variables with your values, but with names from file `setenv.sh` in this repository. Environment variables set up in `secrets` from `Tools` tab in Replit.

![image](https://github.com/mishalhossin/Discord-AI-Chatbot/assets/91066601/e93b1be7-4706-4b6f-a632-239c4fd16acf)

- Click `Run` button.


## Run on local machine:
- Clone this repository `git clone https://github.com/Metim0l/ChannelGPT.git`
- Open project directory `cd ChannelGPT`
- Install dependencies `pip install -r requirements.txt`
- Go to Telegram and create new bot with BotFather.
- Add your new bot to your channel admins.
- Open file `setenv.sh` in project directory and change all variables to your values. For example, change variable `channel_id` to your channel username, you can get your channel username in channel url. For example url: `https://t.me/vladalek_channel`, username: `@vladalek_channel`.
- Run command `. setenv.sh`
- Run bot with command `python main.py`

After that, you can open url `http://127.0.0.1:8080` on your local machine and use this bot. When you click button `create post`, bot creating new post for your channel. When you click button `yes`, bot send this post to your channel.


**P.S.** I am a bad frontend developer, sorry) 
If you want, you can create new frontend for this bot and send to me, or to my Telegram: [Metimol](https://t.me/metimol).
