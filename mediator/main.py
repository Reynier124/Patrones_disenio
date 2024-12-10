from chat_room import ChatRoom
from concrete_user import ConcreteUser

chat_room = ChatRoom()

lucho = ConcreteUser('Luciano', chat_room)
tincho = ConcreteUser('Martin', chat_room)
ian = ConcreteUser('Ian', chat_room)

chat_room.add_user(lucho)
chat_room.add_user(tincho)
chat_room.add_user(ian)

lucho.send('Me prestan plata?')
tincho.send('Mi pueblo no tiene agua, ayuda')
ian.send('Oh no')