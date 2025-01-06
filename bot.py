import telebot
from gpt import GPT
bot = telebot.TeleBot('7806558234:AAGA-un5fwEIuOwTzClJqugk_1hwDPzVX1E')

@bot.message_handler(commands=['start'])
def gpt_dialog(message):
	sent_msg = bot.send_message(message.chat.id, 'Вы можете задать вопрос нейросети')
	bot.register_next_step_handler(sent_msg, checkgpt)

def checkgpt(message):
	gpt = GPT(system_content="")
	user_request = message.text
	gpt.clear_history()
	json = gpt.make_promt(user_request)
	resp = gpt.send_request(json)
	response = gpt.process_resp(resp)
	bot.send_message(message.chat.id, response[1])
	gpt_dialog(message)

bot.infinity_polling()