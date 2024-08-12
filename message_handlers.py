import psycopg2
import uuid
import json
import time

def connect():
    conn = psycopg2.connect(database="postgres-chat",user="admin",password="admin",host="127.0.0.1",port="5433")
    return conn

conn = connect()
cursor = conn.cursor()

def handle_room_join(serialized_message):
    authorId = serialized_message["authorId"]
    roomId = serialized_message["roomId"]
    
    cursor.execute('UPDATE "User" SET "roomId" = %s WHERE "id" = %s;', (roomId, authorId))
    conn.commit()
    
def handle_text_message(serialized_message):
    authorId = serialized_message["authorId"]
    roomId = serialized_message["roomId"]
    content = serialized_message["content"]
    rndid = str(uuid.uuid4())
    createdAt = time.time()


    cursor.execute('INSERT INTO "Message" ("id", "authorId", "roomId", "content") VALUES (%s, %s, %s, %s);', (rndid, authorId, roomId, content))
    get_author = 'SELECT "name" FROM "User" WHERE "id" = %s;'
    cursor.execute(get_author, (authorId,))
    author = cursor.fetchone()
    conn.commit()
    message = json.dumps({"id": rndid, "authorId": authorId, "roomId": roomId, "content": content, "type": "message", "createdAt": createdAt,  "author": {
        "name": author[0]
    }}) 
    return message


def handle_client_leave(serialized_message):
    authorId = serialized_message["authorId"]
    roomId = serialized_message["roomId"]
    
    cursor.execute('UPDATE "User" SET "roomId" = NULL WHERE "id" = %s;', (authorId,))
    conn.commit()
