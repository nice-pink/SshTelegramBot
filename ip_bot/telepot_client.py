import telepot
from telepot.loop import MessageLoop

class TelepotClient:

    def __init__(self, json_client, tele_commander):
        self.JSON_CLIENT = json_client
        self.BOT = None
        self.TOKEN = None
        self.CHAT_ID_WHITELIST = []
        self.TELE_COMMANDER = tele_commander
        
         # init with config
        self.IS_INITIALIZED = self.load_config(json_client)
        if not self.IS_INITIALIZED:
            print('Telepot client NOT initialized.')

        self.setup_telepot()

    def load_config(self, json_client):
        try:
            json_obj = json_client.load()
            config = json_client.get('telepot', json_obj)
            self.TOKEN = json_client.get('token', config)
            self.CHAT_ID_WHITELIST = []
            self.CHAT_ID_WHITELIST = json_client.get('user_id_whitelist', config)
        except Exception as exception:
            print('Json exception (telepot client)', str(exception))
            return False
        return True

    def setup_telepot(self):
        self.BOT = telepot.Bot(self.TOKEN)
        self.BOT.getMe()

    def start_message_loop(self):
        MessageLoop(self.BOT, {'chat': self.handle_chat_message,
                  'callback_query': self.handle_callback_query}).run_as_thread()
        print('Listening ...')

    # Chat message

    def handle_chat_message(self, message):
        content_type, chat_type, chat_id = telepot.glance(message)
        command = self.JSON_CLIENT.get('text', message)
        
        print('Message:', content_type, chat_type, chat_id)
        print(command)
        
        if chat_id in self.CHAT_ID_WHITELIST:
            self.handleCommand(command, chat_id)
        else:
            self.handleUnknownIp(command, chat_id)

    def handleUnknownIp(self, command, chat_id):
        self.BOT.sendMessage(chat_id, 'Alright')
        answer, keyboard = self.TELE_COMMANDER.handleUnknownIp(command)

        if keyboard:
            self.BOT.sendMessage(chat_id, answer, reply_markup=keyboard)
            return

        self.BOT.sendMessage(chat_id, answer)

    def handleCommand(self, command, chat_id):
        self.BOT.sendMessage(chat_id, 'Alright')
        answer, keyboard = self.TELE_COMMANDER.handleCommand(command)

        if keyboard:
            self.BOT.sendMessage(chat_id, answer, reply_markup=keyboard)
            return

        self.BOT.sendMessage(chat_id, answer)

    # Keyboard event

    def handle_callback_query(self, message):
        query_id, from_id, query_data = telepot.glance(message, flavor='callback_query')
        print('Callback Query:', query_id, from_id, query_data)

        self.BOT.answerCallbackQuery(query_id, text='Got it')
