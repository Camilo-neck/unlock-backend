# Code based on: https://stackoverflow.com/questions/77696837/listening-to-database-changes-in-supabase-hosted-project-using-websocket-or-any

import asyncio
import websockets
import json
import os
from dotenv import load_dotenv


async def connect(anon_token, project_ref=None, channel_name=None):

    # To keep track of the id of each message sent to the server
    sent_ref = 1

    # WebSocket connection to Supabase
    uri = f"wss://{project_ref}.supabase.co/realtime/v1/websocket?apikey={anon_token}&vsn=1.0.0"
    async with websockets.connect(uri) as ws:
        print('Socket connection opened properly')

        # Send 1st message to server to subscribe to events of DB changes
        subscribe_msg = {
            "topic": f"realtime:{channel_name}",
            "event": "phx_join",
            "payload": {
                "config": {
                    "broadcast": {"ack": False, "self": False},
                    "presence": {"key": ""},
                    "postgres_changes": [
                        {"event": "*", "schema": "public", "table": "devices"}
                    ]
                },
                "access_token": f"{anon_token}"
            },
            "ref": str(sent_ref),
            "join_ref": "1"
        }
        await ws.send(json.dumps(subscribe_msg))
        sent_ref += 1

        # Send access token (anon key)
        access_token_msg = {
            "topic": f"realtime:{channel_name}",
            "event": "access_token",
            "payload": {"access_token": f"{anon_token}"},
            "ref": str(sent_ref),
            "join_ref": "1"
        }
        await ws.send(json.dumps(access_token_msg))
        sent_ref += 1

        # Start listening for incoming messages
        async def listen():
            while True:
                message = await ws.recv()
                print(f"Message received = {message}")

        # Keep the connection alive by sending a "heartbeat" every 30 seconds
        async def keep_alive():
            while True:
                heartbeat_msg = {
                    "topic": "phoenix",
                    "event": "heartbeat",
                    "payload": {},
                    "ref": str(sent_ref)
                }
                await ws.send(json.dumps(heartbeat_msg))
                await asyncio.sleep(30)

        # Run both tasks concurrently
        await asyncio.gather(listen(), keep_alive())

# Entry point for the async event loop
if __name__ == "__main__":

    ANON_TOKEN = os.getenv("SUPABASE_KEY")

    asyncio.run(connect(
        anon_token = ANON_TOKEN,
        project_ref = "vkduiueevhxmjujorjry",
        channel_name = "device"
    ))
