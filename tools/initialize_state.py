from google.adk.agents.callback_context import CallbackContext
from google.adk.sessions.state import State
from google.adk.tools import ToolContext
import os
from tools.bigquery_tools import bigquery_metdata_extraction_tool

def initialize_state_var(callback_context: CallbackContext):
    """
    Initialize state variables for the no-match analysis agent.
    Sets up BigQuery configuration and initializes all workflow state variables.
    """
    # Initialize BigQuery configuration
    PROJECT = os.environ.get("PROJECT")
    BQ_LOCATION = os.environ.get("BQ_LOCATION")
    DATASET = os.environ.get("DATASET")
    GCS_BUCKET_NAME = os.environ.get("GCS_BUCKET_NAME")

    callback_context.state["PROJECT"] = PROJECT
    callback_context.state["BQ_LOCATION"] = BQ_LOCATION
    callback_context.state["DATASET"] = DATASET
    callback_context.state["GCS_BUCKET_NAME"] = GCS_BUCKET_NAME

    # Initialize BigQuery metadata for conversation data retrieval
    try:
        bigquery_metadata = bigquery_metdata_extraction_tool(
            PROJECT=PROJECT,
            BQ_LOCATION=BQ_LOCATION,
            DATASET=DATASET
        )
        callback_context.state["bigquery_metadata"] = bigquery_metadata
    except Exception as e:
        print(f"Warning: Could not initialize BigQuery metadata: {e}")
        callback_context.state["bigquery_metadata"] = []

    # Initialize no-match analysis flow state variables
    callback_context.state["conversation_data_output"] = ""
    callback_context.state["no_match_analysis_output"] = ""
    callback_context.state["dialogflow_bot_json"] = ""
    callback_context.state["dialogflow_analysis_output"] = ""
    callback_context.state["csv_generation_output"] = ""
    
    # Initialize user query for context
    callback_context.state["user_query"] = "" 