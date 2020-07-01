for messages_count in range(0, 100):
    remainder = messages_count % 10
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        print('У вас ' + str(messages_count) + ' новое сообщение')
    elif messages_count >=2 and messages_count <= 4:
        print('У вас ' + str(messages_count) + ' новых сообщения')
    elif messages_count >=5 and messages_count <= 20:
        print('У вас ' + str(messages_count) + ' новых сообщений')
    elif messages_count > 20 and remainder == 0:
        print('У вас ' + str(messages_count) + ' новых сообщений')
    elif messages_count > 20 and remainder == 1:
        print('У вас ' + str(messages_count) + ' новое сообщение')
    elif messages_count > 20 and remainder >= 2 and remainder <= 4:
        print('У вас ' + str(messages_count) + ' новых сообщения')
    else:
        print('У вас ' + str(messages_count) + ' новых сообщений')