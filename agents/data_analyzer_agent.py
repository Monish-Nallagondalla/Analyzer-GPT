from autogen_agentchat.agents import AssistantAgent

from agents.prompts.data_analyzer_prompt import DATA_ANALYZER_PROMPT

def getDataAnalyzerAgent(model_client):
    data_analyzer_agent = AssistantAgent(
        name="DataAnalyzerAgent",
        description="A agent that analyzes data and provides insights.",
        model=model_client,
        prompt=DATA_ANALYZER_PROMPT,
    )
    return data_analyzer_agent