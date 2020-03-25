# About

This is a python implementation of a Telegram bot (using Telepot framework) for opening a reverse ssh tunnel to a client.

The script should run on the remote machine, that should be able to open the reverse ssh tunnel to the client machine. If your work computer e.g. is not accessible via ssh directly, but you need to work remotely, you can establish a reverse ssh tunnel from your work computer to the client machine you wish to work on (if the client is accessible via ssh and this bot script is already running). Just by telling your Telegram bot to do so.

# Run

## Install required python libraries

Go to base folder of this project (SshTelegramBot).

```
pip3 install requirements.txt
```

## Execute

Run script as module from the base path of this project. Before you need to add a config.json (see Telegram section).

```
python3 -m ip_bot ./config.json
```

# Usage

Send `/opentunnel/LOCALHOST_PORT:localhost:CLIENT_SSH_PORT/CLIENT_USER@CLIENT_IP`

The Telegram bot will open a reverse ssh tunnel from your remote machine to your client machine. On the client you can establish a ssh connection to your localhost with the given LOCALHOST_PORT. 

Hooray. You are connected to your work machine! Congrats. 🎉

# Telegram

* Register a Telegram account. (https://telegram.org)
* Create a TelegramBot. (https://core.telegram.org/bots)

After creating a bot, you will receive a token. This token must be placed in the config json file. (Best copy the **config_example.json** into a new file named **config.json**, which is already added to .gitignore.) After successfully running the bot script send some stuff to the Telegram bot to find out your **chat_id**. Add your chat_id to the **chat_id_whitelist** array in the config json file. Otherwise your requests will not be handled.

## Example

### Prerequisites

**Remote machine:**
* User: remote
* Run SshTelegramBot python script. And let it run forever...
* Remote machine contains ssh public key (e.g. id_rsa.pub) from client machine in **~/.ssh/authorized_keys**.

**Client machine:**
* User: client
* Server with fixed IP: 123.123.123.123
* OR
* Router: Set portforwarding - port 22 -> your client machine in local network.
* Client machine contains ssh public key (e.g. id_rsa.pub) from remote machine in **~/.ssh/authorized_keys**.
* Client machine contains own ssh public key (e.g. id_rsa.pub) in **~/.ssh/authorized_keys**.

### Establish reverse ssh tunnel

**Steps:**
* Send to your Telegram bot `/opentunnel/33333:localhost:22/client@123.123.123.123` (via Telegram messenger).
* Client: `ssh remote@localhost -p 33333`

# Tips

Run SshTelegramBot as service or start as crontab or put into login item or anything else to start SshTelegramBot everytime you boot your computer. This way it will always be accessible.

Check wether the right ssh keys are added to the authorized_keys file und used when executing SshTelegramBot e.g. as a service (might be root instead of user).