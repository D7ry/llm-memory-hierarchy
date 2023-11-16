import os
import threading
import json
from typing import Optional
import openai
from memory import Memory, Context
# Assuming a placeholder for OpenAI's GPT API interaction
# from openai import GPT

class Agent:
    
    __AGENTS_DIR: str = "agents/"
    def __init__(self, agent_id: str, agent_summary: str=""):
        agent_data: dict = {}
        memory_data: dict = {}
        # Check if agent exists
        if os.path.exists(os.path.join(self.__AGENTS_DIR, f"{agent_id}.json")):
            # read agent from file
            print(f"Agent {agent_id} exists, de-serializing...")
            with open(os.path.join(self.__AGENTS_DIR, f"{agent_id}.json"), "r") as f:
                agent_data: dict = json.load(f) 
                memory_data = agent_data["memory"]

        self.__id: str = agent_id
        if memory_data != {}:
            if agent_summary != "":
                raise Exception("Agent already exists, cannot create new agent with summary")
        else:
            memory_data["summary"] = agent_summary
            memory_data["L1"] = []
            memory_data["L2"] = []
            memory_data["L3"] = []
            
        # intiailize memory
        self.memory: Memory = Memory(memory_data)

        # Initialize OpenAI
        openai_key: str|None = os.environ.get("OPENAI_API_KEY")
        if openai_key is None:
            raise Exception("OPENAI_API_KEY environment variable not set.")
        openai.api_key = openai_key

    def ask(self, question: str) -> Optional[str]:
        # Recall relevant information from memory
        
        context: Context = self.memory.get_memory(question)
        # Placeholder for querying OpenAI's GPT API
        response: str|None = self.__query_gpt_api(question, context)
        # Update memory after the conversation
        if response is not None: 
            # dispatch a thread to update memory
            t = threading.Thread(target=self.memorize_and_serialize, args=[question, response])
            t.start()
        return response

    def memorize_and_serialize(self, user_message: str, agent_message: str):
        self.memory.memorize(user_message, agent_message)
        self.serialize()
    
    def serialize(self):
        # serialize agent to .json file
        with open(os.path.join(self.__AGENTS_DIR, f"{self.__id}.json"), "w") as f:
            json.dump({
                "memory":self.memory.serialize()
                }, f)


    def __query_gpt_api(self, question, context: Context) -> Optional[str]:
        # Placeholder for querying OpenAI's GPT API
        # response = GPT.query(question, context)
        client = openai.OpenAI()
        system_prompt: str = context.summary


        print(system_prompt)
        messages: list = [
                    {
                    "role" : "system",
                    "content" : system_prompt
                    }
                ]
        # get things from l2 cache in
        
        for l2_summary in context.l2_memory:
            messages.append({"role" : "assistant", "content": l2_summary})
        # append everything from l1 cache
        for conversation in context.most_recent_conversations:
            messages.append({"role" : "user", "content":conversation[0]})
            messages.append({"role" : "assistant", "content": conversation[1]})

        # append question
        messages.append({"role": "user", "content" : question})
       
        print("querying openAI...")
        completion = client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages = messages
                )
        return completion.choices[0].message.content

if __name__ == "__main__": 
# Example usage
    agent = Agent(agent_id="Jarvis")
    while 1:
        question = input(":")
        response = agent.ask(question)
        print(response)
