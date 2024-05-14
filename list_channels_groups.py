from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest            

api_id = '26931421'
api_hash = 'd16501751e313ecf52fed51ab74fe26f'

def main():

    with TelegramClient('session_name', api_id, api_hash) as client:
    
        client.connect()
            
        dialogs = client.get_dialogs()

        for dialog in dialogs:

            if (dialog.is_group or dialog.is_channel):
                #chatid = str(dialog.id)[4:]
                #print(f"https://t.me/c/{chatid}/-1")
                print(f"ID: {dialog.id},CHAT: {dialog.name}")
                #print(f"USERNAME: {entidad.username},CHAT: {dialog.name}")

if __name__ == '__main__':
    main()