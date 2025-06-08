from livekit.agents import Agent

class MyAgent(Agent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_user_turn_completed(self, _turn_ctx, new_message):
        print(" User turn completed ", new_message)