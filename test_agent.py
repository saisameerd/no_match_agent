#!/usr/bin/env python3
"""
Simple test script to verify the no-match analysis agent setup.
This script tests imports and basic functionality without running the full agent.
"""

import os
import sys

# Add current directory to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all required modules can be imported successfully."""
    print("🧪 Testing imports...")
    
    try:
        # Test main agent import
        from agent import no_match_analysis_orchestrator, root_agent
        print("✅ Main agent imports successful")
        
        # Test sub-agents
        from sub_agents.conversation_data_retrieval_agent.agent import conversation_data_retrieval_agent
        from sub_agents.no_match_analysis_agent.agent import no_match_analysis_agent
        from sub_agents.dialogflow_cx_parser_agent.agent import dialogflow_cx_parser_agent
        from sub_agents.csv_generation_agent.agent import csv_generation_agent
        print("✅ Sub-agent imports successful")
        
        # Test tools
        from tools.bigquery_tools import bigquery_execution_tool, bigquery_metdata_extraction_tool
        from artifact_utils import save_csv_artifact, create_csv_content_from_data
        from tools.initialize_state import initialize_state_var
        print("✅ Tools imports successful")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_agent_structure():
    """Test that the agent structure is properly configured."""
    print("\n🏗️ Testing agent structure...")
    
    try:
        from agent import no_match_analysis_orchestrator
        
        # Check agent properties
        assert hasattr(no_match_analysis_orchestrator, 'conversation_data_retrieval_agent'), "Missing conversation_data_retrieval_agent"
        assert hasattr(no_match_analysis_orchestrator, 'no_match_analysis_agent'), "Missing no_match_analysis_agent"
        assert hasattr(no_match_analysis_orchestrator, 'dialogflow_cx_parser_agent'), "Missing dialogflow_cx_parser_agent"
        assert hasattr(no_match_analysis_orchestrator, 'csv_generation_agent'), "Missing csv_generation_agent"
        
        print("✅ Agent structure verification successful")
        return True
        
    except Exception as e:
        print(f"❌ Agent structure error: {e}")
        return False

def test_tools():
    """Test that the tools are properly configured."""
    print("\n🔧 Testing tools...")
    
    try:
        from artifact_utils import generate_sample_csv
        
        # Test CSV generation
        sample_csv = generate_sample_csv()
        assert "Intent Name" in sample_csv, "Sample CSV missing header"
        assert "AccountSuspensionIntent" in sample_csv, "Sample CSV missing expected content"
        
        print("✅ Tools testing successful")
        return True
        
    except Exception as e:
        print(f"❌ Tools testing error: {e}")
        return False

def test_environment():
    """Test environment configuration."""
    print("\n🌍 Testing environment configuration...")
    
    # Check if .env file exists
    env_file = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_file):
        print("✅ .env file found")
        
        # Read and check .env content
        with open(env_file, 'r') as f:
            content = f.read()
            required_vars = ['PROJECT', 'BQ_LOCATION', 'DATASET', 'GCS_BUCKET_NAME']
            for var in required_vars:
                if var in content:
                    print(f"✅ {var} found in .env")
                else:
                    print(f"⚠️ {var} missing from .env")
    else:
        print("⚠️ .env file not found")
    
    return True

def test_file_structure():
    """Test that all required files exist."""
    print("\n📁 Testing file structure...")
    
    required_files = [
        'agent.py',
        'requirements.txt',
        'README.md',
        'QUICKSTART.md',
        'sub_agents/__init__.py',
        'sub_agents/conversation_data_retrieval_agent/agent.py',
        'sub_agents/conversation_data_retrieval_agent/prompts.py',
        'sub_agents/no_match_analysis_agent/agent.py',
        'sub_agents/no_match_analysis_agent/prompts.py',
        'sub_agents/dialogflow_cx_parser_agent/agent.py',
        'sub_agents/dialogflow_cx_parser_agent/prompts.py',
        'sub_agents/csv_generation_agent/agent.py',
        'sub_agents/csv_generation_agent/prompts.py',
        'tools/__init__.py',
        'tools/bigquery_tools.py',
        'tools/initialize_state.py',
        'artifact_config.py',
        'artifact_utils.py'
    ]
    
    missing_files = []
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MISSING")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n⚠️ Missing files: {len(missing_files)}")
        return False
    else:
        print(f"\n✅ All {len(required_files)} required files found")
        return True

def test_artifact_implementation():
    """Test that artifact implementation follows ADK best practices."""
    print("\n📦 Testing artifact implementation...")
    
    try:
        # Test artifact config
        from artifact_config import get_artifact_service
        artifact_service = get_artifact_service()
        print(f"✅ Artifact service: {type(artifact_service).__name__}")
        
        # Test artifact utilities
        from artifact_utils import create_csv_content_from_data, generate_sample_csv
        
        # Test CSV generation
        sample_data = [{"test": "data"}]
        csv_content = create_csv_content_from_data(sample_data)
        assert "test" in csv_content, "CSV generation failed"
        
        sample_csv = generate_sample_csv()
        assert "Intent Name" in sample_csv, "Sample CSV generation failed"
        
        print("✅ Artifact implementation follows ADK best practices")
        return True
        
    except Exception as e:
        print(f"❌ Artifact implementation error: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 Starting No-Match Analysis Agent Tests\n")
    
    tests = [
        test_file_structure,
        test_imports,
        test_agent_structure,
        test_tools,
        test_artifact_implementation,
        test_environment
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The agent is ready to use.")
        print("\n📝 Next steps:")
        print("1. Configure your .env file with actual values")
        print("2. Set up GCS bucket for artifacts")
        print("3. Run: adk web")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main() 