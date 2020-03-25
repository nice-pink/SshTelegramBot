import subprocess
import os
import telepot
import requests

class TeleCommander:

    def __init__(self):
        self.tunnel_process = None
        
    # unknown sender

    def handleUnknownIp(self, command: str):
        if command.casefold().startswith('/getip'):
            return '666.666.666.666', None
        if command.casefold().startswith('/opentunnel'):
            return 'No', None
        if command.casefold().startswith('/closetunnel'):
            return 'No', None
        if command.casefold().startswith('/hastunnel'):
            return 'No', None
        if command.casefold().startswith('/open'):
            return 'Come in...', None
        else:
            return 'I mean: no idea', None
    
    # handle commands

    def handleCommand(self, command: str):
        if command.casefold().startswith('/getip'):
            return self.handleGetIp(command)
        if command.casefold().startswith('/opentunnel'):
            return self.handleOpenTunnel(command)
        if command.casefold().startswith('/closetunnel'):
            return self.handleCloseTunnel(command)
        if command.casefold().startswith('/hastunnel'):
            return self.handleHasTunnel(command)
        if command.casefold().startswith('/open'):
            return self.handleOpen(command)
        else:
            return 'I mean: no idea', None
    
    def handleGetIp(self, command: str):
        response = requests.get("http://ifconfig.me")
        return response.content.decode('utf-8'), None
    
    def handleOpenTunnel(self, command: str):
        # /opentunnel/43022:localhost:22/dark@666.666.666.666
        # OR
        # /opentunnel/dark@666.666.666.666
        address = self.getParameter(command)
        port = self.getParameter(command, 2)
        
        if not address or not port:
            return 'Wrong format! (required: /opentunnel/43022:localhost:22/dark@666.666.666.666 OR /opentunnel/dark@666.666.666.666)', None

        # If no port specified set default port
        if address == port:
            port = 43022
        
        # Open tunnel
        # command = 'ssh -R ' + port + ' ' + address
        # os.system(command)
        commands = ['ssh', '-R', port, address]
        self.tunnel_process = subprocess.Popen(commands, shell=False)
        
        return 'Come in...', None

    def handleCloseTunnel(self, command: str):
        if not self.tunnel_process:
            return 'No tunnel open.', None
        
        self.tunnel_process.kill()
        self.tunnel_process = None

        return 'Tunnel closed.', None

    def handleHasTunnel(self, command: str):
        if not self.tunnel_process:
            return 'No tunnel open.', None
        
        return 'Yes.', None

    def handleOpen(self, command: str):
        return 'Come in...', None

    # helper

    def getParameter(self, command: str, index: int = -1):
        parts = command.split('/')
        if len(parts) <= index:
            return None

        return parts[index]
