from langchain_ollama import ChatOllama

chat = CharOllama(
    mode="deepseek-r1:1.5b",
    tempature=0,
)

messages = [
    (
        "system",
        "You are a helpful assistant. ",
    ),
    ("human", "What makes LangChain great for working with LLMs?"),
]
ai_msg = chat.invoke(messages)
print(ai_msg.content)
