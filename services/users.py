from typing import Dict, Any

_FAKE_DATABASE = Dict[int, Dict[str, Any]]
_counter = 0
async def create_user(email: str, full_name: str)-> Dict[str, Any]:

        global _counter

        _counter+=1

        data = {id : _counter, full_name : full_name, email: email}

        _FAKE_DATABASE[_counter] = data

        return data