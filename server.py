import socket
import threading

clientes = []

def enviar_mensagem_para_todos(mensagem, cliente_socket):
    for cliente in clientes:
        if cliente != cliente_socket:
            try:
                cliente.send(mensagem)
            except:
                clientes.remove(cliente)

def lidar_com_cliente(cliente_socket, endereco_cliente):
    nome_cliente = cliente_socket.recv(1024).decode()
    print(f"Novo cliente conectado: {nome_cliente} de {endereco_cliente}")
    
    while True:
        try:
            mensagem = cliente_socket.recv(1024).decode()
            
            if mensagem:
                mensagem_com_nome = f"{nome_cliente}: {mensagem}"
                print(f"Mensagem recebida: {mensagem_com_nome}")
                enviar_mensagem_para_todos(mensagem_com_nome.encode(), cliente_socket)
            else:
                break
        except:
            break

    clientes.remove(cliente_socket)
    cliente_socket.close()

def iniciar_servidor(): # CFG do servidor
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('127.0.0.1', 5555))
    servidor.listen(5)
    print("Servidor aguardando conexões...")

    while True:
        cliente_socket, endereco_cliente = servidor.accept()
        clientes.append(cliente_socket)
        threading.Thread(target=lidar_com_cliente, args=(cliente_socket, endereco_cliente)).start()

if __name__ == "__main__":
    iniciar_servidor()
