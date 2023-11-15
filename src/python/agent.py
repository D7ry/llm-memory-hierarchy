import json
import os
import openai
from memory import Memory
# Assuming a placeholder for OpenAI's GPT API interaction
# from openai import GPT

class Agent:
    def __init__(self, agent_id: str=""):
        
        memory_dict: dict|None = None
        if agent_id != "":
            #TODO: Implement serialization and de-serialization
            # de-serialize agent memory from JSON
            raise NotImplementedError("De-serialization not implemented yet")

        # intiailize memory
        self.memory: Memory = Memory(memory_dict)

        # Initialize OpenAI
        openai_key: str|None = os.environ.get("OPENAI_API_KEY")
        if openai_key is None:
            raise Exception("OPENAI_API_KEY environment variable not set.")
        openai.api_key = openai_key

    def ask(self, question: str) -> str:
        # Recall relevant information from memory
        recalled_info = self.__recall(question)
        
        # Construct the context for GPT
        context = {
            "L1_memory": self.__L1_cache,
            "L2_memory": self.__L2_cache,
            "L3_memory": recalled_info  # Placeholder for L3 info
        }
        
        # Placeholder for querying OpenAI's GPT API
        response: str = self.__query_gpt_api(question, context)
        
        # Update memory after the conversation
        self.__memorize(question, response)
        
        return response

    def __recall(self, question):
        # Placeholder for logic to check L3 cache necessity and retrieval
        # For now, we return an empty object or relevant info if applicable
        return {}

    def __memorize(self, question, response):
        # Update L1 cache with the recent conversation
        self.__L1_cache.append({"question": question, "response": response})
        
        # Implement logic to condense L1 cache to L2, and manage overflow
        
        # Serialize the L1 and L2 cache state if needed
        # self.__serialize_memory()

    def __query_gpt_api(self, question, context) -> str:
        # Placeholder for querying OpenAI's GPT API
        # response = GPT.query(question, context)
        client = openai.OpenAI()
        messages: list = [
                ]
        # append everything from l1 cache
        
        completion = client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages = messages
                )

    def __serialize_memory(self):
        # Serialize the L1 and L2 caches to JSON
        # This is a placeholder for the actual serialization logic
        serialized_data = json.dumps({
            "L1_cache": self.__L1_cache,
            "L2_cache": self.__L2_cache
        })
        return serialized_data

# Example usage
agent = Agent()
response = agent.ask("What's the weather like today?")
print(response)
