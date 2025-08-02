#!/usr/bin/env python3
"""
Runner Configuration Script for No-Match Analysis Agent
This script configures and runs the agent with proper artifact service setup.
"""

import os
import sys
from google.adk import Runner
from agent import no_match_analysis_orchestrator
from artifact_config import configure_artifact_service_for_runner

def main():
    """Configure and run the no-match analysis agent."""
    print("🚀 Starting No-Match Analysis Agent with ADK Artifact Integration")
    
    try:
        # Create the runner
        runner = Runner(agent=no_match_analysis_orchestrator)
        
        # Configure artifact service
        runner = configure_artifact_service_for_runner(runner)
        
        print("✅ Agent configured successfully")
        print("🌐 Starting web interface...")
        print("📝 Use Ctrl+C to stop the agent")
        
        # Start the web interface
        runner.web()
        
    except KeyboardInterrupt:
        print("\n🛑 Agent stopped by user")
    except Exception as e:
        print(f"❌ Error starting agent: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 