from google.adk.agents import LlmAgent
from sub_agents.conversation_data_retrieval_agent.prompts import CONVERSATION_DATA_RETRIEVAL_INSTRUCTION_STR
from tools.bigquery_tools import bigquery_execution_tool

# LLM Agent for retrieving conversation data with no-match events from BigQuery
conversation_data_retrieval_agent = LlmAgent(
    name="conversation_data_retrieval_agent",
    model="gemini-2.5-flash",
    description="Retrieves conversation data with no-match events from BigQuery for analysis",
    instruction=CONVERSATION_DATA_RETRIEVAL_INSTRUCTION_STR,
    tools=[bigquery_execution_tool],
    output_key="conversation_data_output"
) 