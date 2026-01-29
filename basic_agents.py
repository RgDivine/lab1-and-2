from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
import asyncio

class BasicAgent(Agent):
    class HelloBehaviour(CyclicBehaviour):
        async def run(self):
            print(f"{self.agent.jid} is running...")
            await asyncio.sleep(5)

    async def setup(self):
        print("BasicAgent starting...")
        self.add_behaviour(self.HelloBehaviour())

if __name__ == "__main__":
    agent = BasicAgent("basicagent@localhost", "password")
    agent.start()
    input("Press ENTER to stop the agent")
    agent.stop()
