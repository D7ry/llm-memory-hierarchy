import os


class Memory:
    def __init__(self, memory_dict: dict|None = None):
        if memory_dict is not None:
            #TODO: implement de-serialziation
            raise NotImplementedError("De-serialization not implemented yet")
        
        self.__L1_cache: list = []  # List to store recent conversations
        self.__L2_cache: list = []  # List to store synopses of conversations


    def memorize(self, user_input: str, agent_input: str):
        self.__L1_cache.append(
                {"user" : user_input, "agent" : agent_input}
                )

    def __check_cache_overflow(self):
        #TODO: implement cache overflow check, and flush cache
        raise NotImplementedError("Cache overflow check not implemented yet")

    def __get_relevant_l3_cache(self, user_input: str) -> list[str]:
        #TODO: implement L3 cache fetching
        raise NotImplementedError("L3 cache not implemented yet!")

    def get_memory(self, user_input: str) -> tuple[list[str], list[str], list[str]]:
        return (self.__L1_cache, self.__L2_cache, self.__get_relevant_l3_cache(user_input))
