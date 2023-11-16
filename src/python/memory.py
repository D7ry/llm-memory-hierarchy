import os

class Context:
    def __init__(self, l1_memory: 'list[tuple[str, str]]', l2_memory: 'list[str]', l3_memory: 'list[str]', summary: str):
        self.most_recent_conversations: list[tuple[str, str]] = l1_memory
        self.l2_memory: list[str] = l2_memory
        self.l3_memory: list[str] = l3_memory
        self.summary: str = summary


        
class Memory:
    def __init__(self, memory_dict: 'dict'):
        self.__L1_cache: list = memory_dict["L1"]  # List to store recent conversations
        self.__L2_cache: list = memory_dict["L2"]  # List to store synopses of conversations
        self.__summary: str = memory_dict["summary"]


    def memorize(self, user_input: str, agent_input: str):
        """
        Memorize a conversation between the user and agent.
        Internally, cache user and agent input into the L1 cache.
        Automatically flush L1 cache to L2 when L1 cache is full, and flush L2 cache to L3 when L2 cache is full. 
        """
        self.__L1_cache.append(
                (user_input, agent_input)
                )
        #self.__check_cache_overflow()
       
    def serialize(self):
        return {
                "L1": self.__L1_cache,
                "L2": self.__L2_cache,
                "summary": self.__summary
                }

    def __check_cache_overflow(self):
        """
        Checks if each level of the cache is full, and if is, flush to the next level.
        Currently we only use FIFO for eviction policy.
        """
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
