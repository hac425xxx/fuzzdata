import socket

def target_alive():
    try:
        client = socket.socket(type=socket.SOCK_DGRAM)
        # send_data = "810a001301040005010c0c0203f7a2194c2900".decode("hex")
        send_data = "\x81\x04#\x00\x01\x13\n\x00\xe2\xf3\xef\xbb\xbf\xaf\x81\xa6\x05\x01\x0c)\x00\x02\x19\x03L\xa2"
        client.sendto(send_data,('192.168.46.128',47808))

        client.settimeout(10.0)
        re_Data,address = client.recvfrom(1024)
        client.settimeout(None)

        print(re_Data.encode('hex'))
        client.close()

        if len(re_Data) > 0:
            return True
        else:
            return False
    except:
        return False

print target_alive()