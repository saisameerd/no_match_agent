"""
ADK Artifact Service Configuration for No-Match Analysis Agent
This module configures the GCS artifact service for storing CSV files.
"""

import os
from google.adk.artifacts import GcsArtifactService, InMemoryArtifactService

def get_artifact_service():
    """
    Get the appropriate artifact service based on environment configuration.
    
    Returns:
        BaseArtifactService: Configured artifact service (GCS or InMemory)
    """
    bucket_name = os.environ.get("GCS_BUCKET_NAME")
    
    if bucket_name and bucket_name != "your-no-match-analysis-artifacts":
        try:
            # Use GCS Artifact Service for production
            print(f"🔧 Configuring GCS Artifact Service with bucket: {bucket_name}")
            return GcsArtifactService(bucket_name=bucket_name)
        except Exception as e:
            print(f"⚠️ Failed to initialize GCS Artifact Service: {e}")
            print("🔄 Falling back to InMemory Artifact Service")
            return InMemoryArtifactService()
    else:
        # Use InMemory Artifact Service for development/testing
        print("🔧 Configuring InMemory Artifact Service for development")
        return InMemoryArtifactService()

def configure_artifact_service_for_runner(runner):
    """
    Configure artifact service for an ADK runner.
    
    Args:
        runner: ADK Runner instance to configure
    """
    artifact_service = get_artifact_service()
    runner.artifact_service = artifact_service
    print(f"✅ Artifact service configured: {type(artifact_service).__name__}")
    return runner 