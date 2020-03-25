import time
import sys
from ip_bot.telepot_client import TelepotClient
from ip_bot.json_client import JsonClient
from ip_bot.tele_commander import TeleCommander


# Main

def main():
    if len(sys.argv) <= 1:
        print('Please parse config file path as argument.')
        sys.exit()

    args = sys.argv
    CONFIG_FILE_PATH = args[1]
    
    json_client = JsonClient(CONFIG_FILE_PATH)

    tele_commander = TeleCommander()

    telepot_client = TelepotClient(json_client, tele_commander)
    telepot_client.start_message_loop()

    while 1:
        time.sleep(10)

if __name__ == '__main__':
    main()