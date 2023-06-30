<a href="https://www.buymeacoffee.com/metimol" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## Hello everyone!

I had several Telegram channels, but I didn't enjoy managing them. It was time-consuming, and I constantly had to search for new topics and information for the channels. That's when I decided to create this project. 
It's an **entirely free gpt-3.5-turbo that will manage your channel for you.** You just need to set up the virtual environment variables and run the bot with a single command. 

The bot remembers the last 10 messages it sent to your channel. And always write interesting posts.

Interested? Here's the complete guide:

## Run on the virtual machine:
- Clone this repository `git clone https://github.com/Metim0l/ChannelGPT.git`
- Open project directory `cd ChannelGPT`
- Install dependencies `pip install -r requirements.txt`
- Go to Telegram and create new bot with BotFather.
- Add this bot to your channel admins.
- Open file `setenv.sh` in project directory and change all variables to your values. For example, change variable `channel_id` to your channel username, you can get your channel username in channel url. For example url: `https://t.me/vladalek_channel`, username: `@vladalek_channel`.
- Run command `. setenv.sh`
- Run bot with command `python main.py`

After that, you can open url `http://127.0.0.1:5000` on your local machine and use this bot. When you click button `create post`, bot creating new post for your channel. When you click button `yes`, bot send this post to your channel.


**P.S.** I am a bad frontend developer, sorry) 
If you want, you can create new frontend for this bot and send to me, or to my Telegram: [Metimol](https://t.me/metimol).
