import socket
import threading

def enviar_mensagem(cliente_socket):
    while True:
        mensagem = input()
        if mensagem:
            cliente_socket.send(mensagem.encode())

def receber_mensagem(cliente_socket):
    while True:
        try:
            mensagem = cliente_socket.recv(1024).decode()
            if mensagem:
                print(mensagem)
        except:
            print("Erro ao receber mensagem.")
            break


def iniciar_cliente():
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(('127.0.0.1', 5555))

    nome_cliente = input("Digite seu nome: ")
    cliente_socket.send(nome_cliente.encode())

    threading.Thread(target=enviar_mensagem, args=(cliente_socket,)).start()
    threading.Thread(target=receber_mensagem, args=(cliente_socket,)).start()

if __name__ == "__main__":
    iniciar_cliente()
