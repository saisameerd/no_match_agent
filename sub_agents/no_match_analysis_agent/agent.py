from google.adk.agents import LlmAgent
from sub_agents.no_match_analysis_agent.prompts import NO_MATCH_ANALYSIS_INSTRUCTION_STR

# LLM Agent for analyzing no-match events and providing recommendations
no_match_analysis_agent = LlmAgent(
    name="no_match_analysis_agent",
    model="gemini-2.5-flash",
    description="Analyzes no-match events in conversation data and provides bot optimization recommendations",
    instruction=NO_MATCH_ANALYSIS_INSTRUCTION_STR,
    output_key="no_match_analysis_output"
) 