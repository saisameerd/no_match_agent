from google.adk.agents import BaseAgent, LlmAgent
from sub_agents.conversation_data_retrieval_agent.agent import conversation_data_retrieval_agent
from sub_agents.no_match_analysis_agent.agent import no_match_analysis_agent
from sub_agents.dialogflow_cx_parser_agent.agent import dialogflow_cx_parser_agent
from sub_agents.csv_generation_agent.agent import csv_generation_agent
from tools.initialize_state import initialize_state_var

from typing import Dict, Any, List
from typing import AsyncGenerator
from typing_extensions import override
from google.adk.events import Event, EventActions
from google.adk.agents.invocation_context import InvocationContext
from google.adk.tools import ToolContext
import logging

# --- Configure Logging ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NoMatchAnalysisAgent(BaseAgent):
    """
    Main orchestrator agent for no-match analysis workflow.
    Coordinates conversation data retrieval, analysis, and CSV generation.
    """
    conversation_data_retrieval_agent: LlmAgent
    no_match_analysis_agent: LlmAgent
    dialogflow_cx_parser_agent: LlmAgent
    csv_generation_agent: LlmAgent

    def __init__(self, name: str, **agents):
        super().__init__(
            name=name,
            before_agent_callback=initialize_state_var,
            description="Dedicated agent for no-match analysis and bot optimization with GCS artifact storage",
            **agents
        )

    @override
    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        """
        Execute the no-match analysis workflow:
        1. Retrieve conversation data with no-match events
        2. Analyze patterns and provide recommendations
        3. Parse Dialogflow CX bot structure (if provided)
        4. Generate CSV artifacts with training phrases
        """
        logger.info(f"[{self.name}] - Starting no-match analysis workflow.")
        
        # Step 1: Conversation data retrieval
        logger.info(f"[{self.name}] - Step 1: Retrieving conversation data with no-match events.")
        async for event in self.conversation_data_retrieval_agent.run_async(ctx):
            logger.info(f"[{self.name}] - Conversation data retrieval event: {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event
        
        conversation_data_output = ctx.session.state.get('conversation_data_output', '')
        logger.info(f"[{self.name}] - Conversation data retrieved: {len(conversation_data_output)} characters")

        if not conversation_data_output:
            logger.warning(f"[{self.name}] - No conversation data retrieved. Ending workflow.")
            return

        # Step 2: No-match analysis
        logger.info(f"[{self.name}] - Step 2: Analyzing no-match patterns and providing recommendations.")
        async for event in self.no_match_analysis_agent.run_async(ctx):
            logger.info(f"[{self.name}] - No-match analysis event: {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event
        
        no_match_analysis_output = ctx.session.state.get('no_match_analysis_output', '')
        logger.info(f"[{self.name}] - No-match analysis completed: {len(no_match_analysis_output)} characters")

        if not no_match_analysis_output:
            logger.warning(f"[{self.name}] - No no-match analysis results. Ending workflow.")
            return

        # Step 3: Dialogflow CX structure analysis (if bot JSON is provided)
        dialogflow_bot_json = ctx.session.state.get('dialogflow_bot_json', '')
        if dialogflow_bot_json:
            logger.info(f"[{self.name}] - Step 3: Analyzing Dialogflow CX bot structure.")
            async for event in self.dialogflow_cx_parser_agent.run_async(ctx):
                logger.info(f"[{self.name}] - Dialogflow CX analysis event: {event.model_dump_json(indent=2, exclude_none=True)}")
                yield event
            
            dialogflow_analysis_output = ctx.session.state.get('dialogflow_analysis_output', '')
            logger.info(f"[{self.name}] - Dialogflow CX analysis completed: {len(dialogflow_analysis_output)} characters")
        else:
            logger.info(f"[{self.name}] - Step 3: Skipping Dialogflow CX analysis (no bot JSON provided).")

        # Step 4: CSV generation (always generate for no-match analysis)
        logger.info(f"[{self.name}] - Step 4: Generating CSV artifacts with training phrases.")
        async for event in self.csv_generation_agent.run_async(ctx):
            logger.info(f"[{self.name}] - CSV generation event: {event.model_dump_json(indent=2, exclude_none=True)}")
            yield event
        
        csv_generation_output = ctx.session.state.get('csv_generation_output', '')
        logger.info(f"[{self.name}] - CSV generation completed: {len(csv_generation_output)} characters")

        if not csv_generation_output:
            logger.warning(f"[{self.name}] - No CSV generation results.")
            return

        logger.info(f"[{self.name}] - No-match analysis workflow completed successfully.")

# Initialize the main orchestrator agent
no_match_analysis_orchestrator = NoMatchAnalysisAgent(
    name="no_match_analysis_orchestrator",
    conversation_data_retrieval_agent=conversation_data_retrieval_agent,
    no_match_analysis_agent=no_match_analysis_agent,
    dialogflow_cx_parser_agent=dialogflow_cx_parser_agent,
    csv_generation_agent=csv_generation_agent
)

# Set as root agent for ADK
root_agent = no_match_analysis_orchestrator 