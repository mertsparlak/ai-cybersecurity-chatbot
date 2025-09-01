from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from typing import List, Union, TypedDict, Annotated
from typing_extensions import TypedDict

class GraphState(TypedDict):
    messages: Annotated[List[Union[HumanMessage, AIMessage, SystemMessage]], "add"]
    intent: str

