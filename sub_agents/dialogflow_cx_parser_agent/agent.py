from google.adk.agents import LlmAgent
from sub_agents.dialogflow_cx_parser_agent.prompts import DIALOGFLOW_CX_PARSER_INSTRUCTION_STR

# LLM Agent for analyzing Dialogflow CX bot structure
dialogflow_cx_parser_agent = LlmAgent(
    name="dialogflow_cx_parser_agent",
    model="gemini-2.5-flash",
    description="Analyzes Dialogflow CX bot JSON structure and extracts intent information for optimization",
    instruction=DIALOGFLOW_CX_PARSER_INSTRUCTION_STR,
    output_key="dialogflow_analysis_output"
) 