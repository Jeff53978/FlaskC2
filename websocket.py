from __main__ import app, sock, clients
import os, random, json, time

# Handshake + Ping for client
@sock.route('/auth')
def auth(ws):
    uuid = os.urandom(24).hex()
    clients.append(uuid)
    ws.send(json.dumps({'msg': 'Connected succesfully to C2 Server', 'uuid': uuid}))
    print(f'Client {uuid} connected')
    while not ws.closed:
        last_ping = time.time()
        ping = ws.receive()
        if ping is None:
            break
        
        if time.time() - last_ping > 10:
            clients.remove(uuid)
            print(f'Client {uuid} disconnected due to inactivity')
            ws.close()
            break
        
# Sends client list every second
@sock.route('/clients')
def clients(ws):
    while not ws.closed:
        ws.send(json.dumps({'clients': clients}))
        time.sleep(1)