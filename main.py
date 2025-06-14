from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

def main():
    model = ChatOpenAI(temperature=0)

    tools = []
    agent_executor = create_react_agent(model,tools)

    print("Hello and welcome to my AI Agent!!!")
    print("This agent will chat with you and also can perform calculations.")
    print("type - QUIT - to exit")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "QUIT":
            break

        print("\nAgent: ", end="")
        for chunk in agent_executor.stream(
                {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messaages" in chunk["agent"]:
                for message in chunk["agent"]["messgaes"]:
                    print(message.count, end="")

        print()

if __name__ == "__main__":
    main()