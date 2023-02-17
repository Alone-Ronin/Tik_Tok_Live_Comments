from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent

# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="@hyperkgz") # Вместо @hyperkgz вставляем ник нейм пользователя Тик Ток, который ведёт прямой эфир
count = 0
# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)
# Notice no decorator?
@client.on("comment")
async def on_comment(event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment}")
    if("hi" in event.comment) : # Если в комментарии присутсвует слово "hi" то он это засчитывает за голос
        print(f"---------------------------------------------\n 1 голос от {event.user.nickname} -- {event.comment}")
        voice = inc() # После каждого голоса добавляем +1 к счётчику общего кол-во голосов, 
        print(f"Общее количесвто голосов: {voice}\n---------------------------------------------")
        
def inc() :
    global count
    count += 1
    return count

# Define handling an event via "callback"
client.add_listener("comment", on_comment)

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()