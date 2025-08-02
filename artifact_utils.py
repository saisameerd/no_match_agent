"""
Artifact Utilities for No-Match Analysis Agent
Provides helper functions for accessing and managing CSV artifacts using ADK context.
"""

import os
from datetime import datetime
from typing import List, Dict, Any, Optional
from google.adk.agents.invocation_context import InvocationContext

def list_available_artifacts(ctx: InvocationContext) -> List[str]:
    """
    List all available artifacts in the current session.
    
    Args:
        ctx: Invocation context
        
    Returns:
        List[str]: List of artifact filenames
    """
    try:
        artifacts = ctx.list_artifacts()
        return artifacts
    except Exception as e:
        print(f"⚠️ Error listing artifacts: {e}")
        return []

def get_latest_csv_artifact(ctx: InvocationContext, filename_pattern: str = "dialogflow_cx_training_phrases") -> Optional[Dict[str, Any]]:
    """
    Get the latest CSV artifact matching the filename pattern.
    
    Args:
        ctx: Invocation context
        filename_pattern: Pattern to match in filename
        
    Returns:
        Optional[Dict[str, Any]]: Artifact data if found, None otherwise
    """
    try:
        artifacts = ctx.list_artifacts()
        
        # Filter CSV artifacts matching the pattern
        csv_artifacts = [art for art in artifacts if filename_pattern in art and art.endswith('.csv')]
        
        if not csv_artifacts:
            print(f"📭 No CSV artifacts found matching pattern: {filename_pattern}")
            return None
        
        # Get the latest artifact (assuming versioning)
        latest_artifact = csv_artifacts[-1]
        artifact_data = ctx.load_artifact(latest_artifact)
        
        print(f"📄 Loaded artifact: {latest_artifact}")
        return {
            "filename": latest_artifact,
            "data": artifact_data,
            "loaded_at": datetime.now().isoformat()
        }
        
    except Exception as e:
        print(f"⚠️ Error loading CSV artifact: {e}")
        return None

def get_csv_artifact_by_version(ctx: InvocationContext, filename: str, version: int) -> Optional[Dict[str, Any]]:
    """
    Get a specific version of a CSV artifact.
    
    Args:
        ctx: Invocation context
        filename: Name of the artifact file
        version: Version number to load
        
    Returns:
        Optional[Dict[str, Any]]: Artifact data if found, None otherwise
    """
    try:
        artifact_data = ctx.load_artifact(filename, version=version)
        
        print(f"📄 Loaded artifact: {filename} (version {version})")
        return {
            "filename": filename,
            "version": version,
            "data": artifact_data,
            "loaded_at": datetime.now().isoformat()
        }
        
    except Exception as e:
        print(f"⚠️ Error loading artifact {filename} version {version}: {e}")
        return None

def save_csv_artifact(ctx: InvocationContext, csv_content: str, filename: str = None) -> Dict[str, Any]:
    """
    Save CSV content as an artifact using ADK context.
    
    Args:
        ctx: Invocation context
        csv_content: CSV content to save
        filename: Optional filename, will generate one if not provided
        
    Returns:
        Dict[str, Any]: Result of the save operation
    """
    try:
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"dialogflow_cx_training_phrases_{timestamp}.csv"
        
        # Save the artifact using ADK context
        ctx.save_artifact(filename, csv_content.encode('utf-8'), mime_type="text/csv")
        
        print(f"💾 Saved CSV artifact: {filename}")
        return {
            "status": "success",
            "filename": filename,
            "saved_at": datetime.now().isoformat(),
            "size": len(csv_content.encode('utf-8')),
            "mime_type": "text/csv"
        }
        
    except Exception as e:
        print(f"⚠️ Error saving CSV artifact: {e}")
        return {
            "status": "error",
            "error": str(e),
            "saved_at": datetime.now().isoformat()
        }

def get_artifact_metadata(ctx: InvocationContext, filename: str) -> Dict[str, Any]:
    """
    Get metadata about a specific artifact.
    
    Args:
        ctx: Invocation context
        filename: Name of the artifact file
        
    Returns:
        Dict[str, Any]: Metadata about the artifact
    """
    try:
        artifacts = ctx.list_artifacts()
        
        if filename not in artifacts:
            return {
                "status": "not_found",
                "filename": filename,
                "message": "Artifact not found"
            }
        
        # Try to load the artifact to get its size
        try:
            artifact_data = ctx.load_artifact(filename)
            size = len(artifact_data) if artifact_data else 0
        except:
            size = 0
        
        return {
            "status": "found",
            "filename": filename,
            "size": size,
            "type": "csv" if filename.endswith('.csv') else "unknown",
            "checked_at": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "status": "error",
            "filename": filename,
            "error": str(e),
            "checked_at": datetime.now().isoformat()
        }

def create_csv_content_from_data(data: List[Dict[str, Any]]) -> str:
    """
    Helper function to create CSV content from structured data.
    
    Args:
        data: List of dictionaries containing the data to convert to CSV
    
    Returns:
        str: CSV content as a string
    """
    if not data:
        return ""
    
    import csv
    import io
    
    # Get fieldnames from the first item
    fieldnames = list(data[0].keys())
    
    # Create CSV content
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    
    # Write header
    writer.writeheader()
    
    # Write data rows
    writer.writerows(data)
    
    return output.getvalue()

def generate_sample_csv() -> str:
    """
    Generate a sample CSV content for testing.
    
    Returns:
        str: Sample CSV content
    """
    sample_data = [
        {
            "Intent Name": "AccountSuspensionIntent",
            "Training Phrase": "Why is my account suspended?",
            "Priority": "High",
            "Category": "New Intent",
            "Description": "Handles account suspension queries"
        },
        {
            "Intent Name": "AccountSuspensionIntent",
            "Training Phrase": "My account got suspended",
            "Priority": "High",
            "Category": "New Intent",
            "Description": "Handles account suspension queries"
        },
        {
            "Intent Name": "PaymentIssueIntent",
            "Training Phrase": "I can't make a payment",
            "Priority": "Medium",
            "Category": "New Intent",
            "Description": "Handles payment-related issues"
        }
    ]
    
    return create_csv_content_from_data(sample_data) 