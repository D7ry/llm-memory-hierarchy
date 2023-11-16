import os
import threading
from typing import Optional
import openai
from memory import Memory, Context
# Assuming a placeholder for OpenAI's GPT API interaction
# from openai import GPT

class Agent:
    def __init__(self, agent_id: str="", agent_summary: str=""):
        
        memory_dict: dict|None = None
        if agent_id != "":
            #TODO: Implement serialization and de-serialization
            # de-serialize agent memory from JSON
            raise NotImplementedError("De-serialization not implemented yet")

        # intiailize memory
        self.memory: Memory = Memory(memory_dict, summary=agent_summary)

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
            threading.Thread(target=self.memory.memorize, args=[question, response]).start()
        return response



    def __query_gpt_api(self, question, context: Context) -> Optional[str]:
        # Placeholder for querying OpenAI's GPT API
        # response = GPT.query(question, context)
        client = openai.OpenAI()
        messages: list = [
                    {
                    "role" : "system",
                    "content" : context.summary
                    }
                ]
        # get things from l2 cache in
        
        # append everything from l1 cache
        for conversation in context.most_recent_conversations:
            messages.append({"role" : "user", "content":conversation[0]})
            messages.append({"role" : "assistant", "content": conversation[1]})

        # append question
        messages.append({"role": "user", "content" : question})
       
        
        completion = client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages = messages
                )
        print(messages)
        return completion.choices[0].message.content

# Example usage
agent = Agent(agent_summary="You're a very funny person who laughs and makes fun of everything I say")
response = agent.ask("Hello, my name is dtry")
print(response)
response = agent.ask("What is my name?")
print(response)
