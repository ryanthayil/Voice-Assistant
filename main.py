import asyncio
from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent
from livekit.plugins import openai
from agent import MyAgent

load_dotenv()

async def entrypoint(ctx: agents.JobContext):
    await ctx.connect()

    session = AgentSession(
        llm=openai.realtime.RealtimeModel(
            voice="coral"
        )
    )

    await session.start(
        room=ctx.room,
        agent=MyAgent(
            instructions="You are a helpful voice AI assistant. Greet the user and offer assistance.Always greet in english first and then adjust to the user's preferred language."
        )
    )

    # Keep the session alive indefinitely
    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))

