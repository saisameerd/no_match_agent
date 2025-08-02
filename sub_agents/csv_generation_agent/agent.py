from google.adk.agents import LlmAgent
from sub_agents.csv_generation_agent.prompts import CSV_GENERATION_INSTRUCTION_STR

# LLM Agent for generating CSV artifacts with training phrases for Dialogflow CX import
csv_generation_agent = LlmAgent(
    name="csv_generation_agent",
    model="gemini-2.5-flash",
    description="Generates CSV artifacts with training phrases that can be imported into Dialogflow CX to reduce no-match events",
    instruction=CSV_GENERATION_INSTRUCTION_STR,
    output_key="csv_generation_output"
) 