import os

class Context:
    def __init__(self, l1_memory: 'list[tuple[str, str]]', l2_memory: 'list[str]', l3_memory: 'list[str]', summary: str):
        self.most_recent_conversations: list[tuple[str, str]] = l1_memory
        self.l2_memory: list[str] = l2_memory
        self.l3_memory: list[str] = l3_memory
        self.summary: str = summary


        
class Memory:
    def __init__(self, memory_dict: 'dict|None' = None, summary: str = ""):
        if memory_dict is not None:
            #TODO: implement de-serialziation
            raise NotImplementedError("De-serialization not implemented yet")
        
        self.__L1_cache: list = []  # List to store recent conversations
        self.__L2_cache: list = []  # List to store synopses of conversations
        self.__summary: str = summary


    def memorize(self, user_input: str, agent_input: str):
        self.__L1_cache.append(
                (user_input, agent_input)
                )
        

    def __check_cache_overflow(self):
        #TODO: implement cache overflow check, and flush cache
        raise NotImplementedError("Cache overflow check not implemented yet")

    def __get_relevant_l3_cache(self, user_input: str) -> 'list[str]':
        #TODO: implement L3 cache fetching
        raise NotImplementedError("L3 cache not implemented yet!")

    def get_memory(self, user_input: str) -> Context:
        #l3_memory: list[str] = self.__get_relevant_l3_cache(user_input)
        l3_memory = []
        ret = Context(self.__L1_cache, self.__L2_cache, l3_memory, self.__summary)
        return ret
