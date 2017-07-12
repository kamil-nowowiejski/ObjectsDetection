from Common.image_serialization import image_to_string
from Common.TCPConnections import TCPCommands


def send_image_to_remote_server(tcp_client, image):
    img_str = image_to_string(image)
    tcp_client.send(TCPCommands.IMAGE, img_str)


def take_picture(video_capture):
    _, image = video_capture.read()
    return image


def register(tcp_client):
    tcp_client.connect()
    tcp_client.send(TCPCommands.REGISTER, '')


def shutdown(main, tcp_server, tcp_client):
    if tcp_server is not None:
        tcp_server.disconnect()
    if tcp_client is not None:
        tcp_client.disconnect()
    main.exit = True