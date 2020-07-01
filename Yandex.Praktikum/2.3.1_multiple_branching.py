for messages_count in range(0, 21):
    if messages_count > 0:
        if messages_count == 1:
            print('У вас ' + str(messages_count) + ' новое сообщение')
        elif messages_count >=2 and messages_count <= 4:
            print('У вас ' + str(messages_count) + ' новых сообщения')
        elif messages_count >=5 and messages_count <= 20:
            print('У вас ' + str(messages_count) + ' новых сообщений')
    else:
        print('У вас нет новых сообщений')