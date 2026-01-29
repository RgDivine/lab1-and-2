import asyncio

# --- define the Agent class ---
class Agent:
    async def start(self):
        print("Agent started...")
        # simulate some ongoing work
        while True:
            await asyncio.sleep(1)  # pretend agent is doing something

    async def stop(self):
        print("Agent stopped.")

# create an instance of the agent
agent = Agent()  # pass any required arguments if needed

async def main():
    try:
        # start the agent
        await agent.start()
    except KeyboardInterrupt:
        # allow stopping with Ctrl+C
        pass
    finally:
        # stop the agent cleanly
        await agent.stop()

# run the main coroutine
if __name__ == "__main__":
    asyncio.run(main())
