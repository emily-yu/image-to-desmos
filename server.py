import socket_io as io

class Server(io.Server):
    def on_connect(self, client):
        # print client, 'connected'
        self.broadcast(str(client) + ' connected')
        # print 'there are now', len(self.clients), 'clients'
    
    def on_message(self, client, message):
        # print client, 'sent', message
        client.send(message)
    
    def on_disconnect(self, client):
        # print client, 'disconnected'
        self.broadcast(str(client) + ' disconnected')
        # print 'there are now', len(self.clients), 'clients'

Server().listen(5000)