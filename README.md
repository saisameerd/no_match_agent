# 🤖 No-Match Analysis Agent

A dedicated Google ADK agent for analyzing no-match events in Dialogflow CX conversations and generating training phrases for bot optimization.

## 🎯 Overview

This agent specializes in:
- **Retrieving conversation data** with no-match events from BigQuery
- **Analyzing no-match patterns** to identify root causes
- **Providing actionable recommendations** for bot improvement
- **Generating CSV artifacts** with training phrases for Dialogflow CX import
- **Storing artifacts in Google Cloud Storage** using ADK's GcsArtifactService

## 🏗️ Architecture

```
User Query → Conversation Data Retrieval → No-Match Analysis → CSV Generation → GCS Artifact
```

### Components:
- **Conversation Data Retrieval Agent**: Extracts no-match conversation data from BigQuery
- **No-Match Analysis Agent**: Analyzes patterns and provides recommendations
- **Dialogflow CX Parser Agent**: Analyzes bot structure (optional)
- **CSV Generation Agent**: Creates training phrases CSV artifacts in GCS

## 🚀 Quick Start

### 1. Environment Setup
```bash
# Clone and setup
cd no_match_analysis_agent
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configuration
```bash
# Set environment variables
export PROJECT=gup-gpi-routing
export BQ_LOCATION=us-central1
export DATASET=gpi_routing
export GCS_BUCKET_NAME=your-no-match-analysis-artifacts
export GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account.json
```

### 3. Run the Agent
```bash
adk web
```

## 💬 Usage Examples

### Basic No-Match Analysis
```
User: "Analyze no_match events from last week"
```

### With Specific Date Range
```
User: "Find conversations with no_match events between 2024-01-01 and 2024-01-31"
```

### Generate Training Phrases CSV
```
User: "Generate training phrases CSV for Dialogflow CX import"
```

## 🎯 **Comprehensive Example Conversations**

### **Example 1: Complete No-Match Analysis Workflow**

**User Input:**
```
"Analyze no_match events from last week and generate training phrases CSV for Dialogflow CX import"
```

**Agent Response:**
```
🤖 Agent: I'll help you analyze no-match events from last week and generate training phrases. Let me start by retrieving conversation data with no-match events from BigQuery.

📊 Retrieving conversation data...
- Querying BigQuery for conversations with no_match events
- Date range: Last 7 days
- Filtering for intent detection confidence of 0.0 or NULL
- Focusing on conversations with highest no-match counts

✅ Found 15 conversations with no-match events
- Conversation ID: conv_001 - 8 no-match events
- Conversation ID: conv_002 - 5 no-match events  
- Conversation ID: conv_003 - 3 no-match events
- ... (12 more conversations)

🔍 Analyzing no-match patterns...

## No-Match Event Analysis Report

**Summary:**
- Total conversations analyzed: 15
- Conversations with no_match events: 15
- No-match rate: 12.3%

**Common No-Match Patterns:**

1. **Pattern 1: Account Suspension Queries**
   - Frequency: 23 occurrences
   - Example utterances: 
     * "Why is my account suspended?"
     * "My account got suspended"
     * "How do I unsuspend my account?"
   - Root cause: Missing intent for account suspension issues
   - Recommended solution: Create AccountSuspensionIntent

2. **Pattern 2: Payment Processing Issues**
   - Frequency: 18 occurrences
   - Example utterances:
     * "I can't make a payment"
     * "Payment failed"
     * "Why won't my payment go through?"
   - Root cause: Missing intent for payment problems
   - Recommended solution: Create PaymentIssueIntent

3. **Pattern 3: Order Status Inquiries**
   - Frequency: 12 occurrences
   - Example utterances:
     * "Where is my order?"
     * "Order tracking"
     * "When will I get my order?"
   - Root cause: Missing intent for order tracking
   - Recommended solution: Create OrderTrackingIntent

**Intent Gap Analysis:**
- **Missing Intents:**
  1. Intent Name: AccountSuspensionIntent
     - Purpose: Handle account suspension queries
     - Training phrases: 15 suggested phrases
     - Priority: High

  2. Intent Name: PaymentIssueIntent
     - Purpose: Handle payment-related problems
     - Training phrases: 12 suggested phrases
     - Priority: High

  3. Intent Name: OrderTrackingIntent
     - Purpose: Handle order status inquiries
     - Training phrases: 10 suggested phrases
     - Priority: Medium

📄 Generating training phrases CSV...

✅ CSV artifact created successfully!
- Filename: dialogflow_cx_training_phrases_2024_01_15_143022.csv
- Location: Google Cloud Storage
- Size: 2.3 KB
- MIME Type: text/csv

📋 CSV Content Preview:
Intent Name,Training Phrase,Priority,Category,Description
AccountSuspensionIntent,Why is my account suspended?,High,New Intent,Handles account suspension queries
AccountSuspensionIntent,My account got suspended,High,New Intent,Handles account suspension queries
AccountSuspensionIntent,How do I unsuspend my account?,High,New Intent,Handles account suspension queries
PaymentIssueIntent,I can't make a payment,High,New Intent,Handles payment-related issues
PaymentIssueIntent,Payment failed,High,New Intent,Handles payment-related issues
OrderTrackingIntent,Where is my order?,Medium,New Intent,Handles order status inquiries
OrderTrackingIntent,Order tracking,Medium,New Intent,Handles order status inquiries

🎯 **Implementation Recommendations:**

**Immediate Actions (High Priority):**
1. Create AccountSuspensionIntent with 15 training phrases
   - Expected impact: Reduce no-match events by 23%
2. Create PaymentIssueIntent with 12 training phrases
   - Expected impact: Reduce no-match events by 18%

**Expected Overall Impact:**
- Estimated no-match reduction: 53%
- Key metrics to monitor: No-match rate, user satisfaction
- Success criteria: No-match rate below 6%

📁 **CSV Artifact Details:**
- **Download URL**: gs://your-no-match-analysis-artifacts/dialogflow_cx_training_phrases_2024_01_15_143022.csv
- **Version**: 1
- **Created**: 2024-01-15 14:30:22 UTC
- **Total Training Phrases**: 37 phrases across 3 intents

You can now import this CSV file directly into Dialogflow CX to create the new intents and reduce no-match events!
```

### **Example 2: Specific Date Range Analysis**

**User Input:**
```
"Analyze no_match events between January 1st and January 31st, 2024"
```

**Agent Response:**
```
🤖 Agent: I'll analyze no-match events for the specified date range (2024-01-01 to 2024-01-31).

📊 Retrieving conversation data...
- Date range: 2024-01-01 to 2024-01-31
- Found 45 conversations with no-match events
- Total no-match events: 127

🔍 Analysis complete...

## No-Match Event Analysis Report

**Summary:**
- Total conversations analyzed: 45
- Conversations with no_match events: 45
- No-match rate: 8.7%

**Top Patterns Identified:**
1. **Technical Support Issues** (34 events)
2. **Billing Inquiries** (28 events)
3. **Feature Requests** (22 events)
4. **Account Management** (19 events)
5. **Order Issues** (24 events)

📄 Generating training phrases CSV...
✅ CSV artifact created: dialogflow_cx_training_phrases_2024_01_31_160045.csv
```

### **Example 3: With Bot Structure Analysis**

**User Input:**
```
"Analyze no_match events and include my current Dialogflow CX bot structure for better recommendations"
```

**Agent Response:**
```
🤖 Agent: I'll analyze no-match events and incorporate your current bot structure for more targeted recommendations.

📊 Retrieving conversation data...
✅ Found 22 conversations with no-match events

🤖️ Analyzing current bot structure...
- Bot Name: Customer Support Bot
- Current Intents: 15 intents
- Training Phrases: 127 phrases
- Flows: 3 main flows

🔍 Cross-referencing no-match patterns with existing bot structure...

**Enhanced Analysis:**
- 3 patterns can be handled by existing intents (adding training phrases)
- 2 patterns require new intents
- 1 pattern suggests intent consolidation

📄 Generating optimized CSV...
✅ CSV artifact created with both new intents and enhanced existing intents
```

### **Example 4: Quick Analysis**

**User Input:**
```
"Quick no-match analysis for today"
```

**Agent Response:**
```
🤖 Agent: I'll perform a quick analysis of today's no-match events.

📊 Quick retrieval...
- Date: Today (2024-01-15)
- Found 8 conversations with no-match events
- Total no-match events: 12

🔍 Quick analysis...
**Top Patterns:**
1. Account issues (5 events)
2. Payment problems (4 events)
3. Order inquiries (3 events)

📄 Generating focused CSV...
✅ CSV artifact created with top priority items only
```

## 📊 Output

The agent provides:
1. **Conversation Data**: Retrieved from BigQuery with no-match events
2. **Analysis Report**: Detailed no-match pattern analysis
3. **Bot Structure Analysis**: (if bot JSON provided)
4. **CSV Artifact**: Stored in GCS with training phrases

## 🔧 Configuration

### Environment Variables
- `PROJECT`: GCP Project ID
- `BQ_LOCATION`: BigQuery location
- `DATASET`: BigQuery dataset name
- `GCS_BUCKET_NAME`: GCS bucket for artifacts
- `GOOGLE_APPLICATION_CREDENTIALS`: Service account key path

### BigQuery Table
The agent works with:
```sql
`gup-gpi-routing.gpi_routing.dialogflow_bigquery_export_data`
```

## 📁 Project Structure

```
no_match_analysis_agent/
├── agent.py                          # Main orchestrator agent
├── run_agent.py                      # Runner with artifact service
├── artifact_config.py                # Artifact service configuration
├── artifact_utils.py                 # ADK context-based utilities
├── verify_implementation.py          # Comprehensive verification
├── test_agent.py                     # Basic tests
├── test_integration.py               # Integration tests
├── requirements.txt                   # Dependencies
├── .env                              # Environment variables
├── README.md                         # This file
├── QUICKSTART.md                     # Quick start guide
├── FINAL_SETUP.md                    # Complete setup guide
├── IMPLEMENTATION_SUMMARY.md         # Implementation summary
├── sub_agents/
│   ├── conversation_data_retrieval_agent/
│   ├── no_match_analysis_agent/
│   ├── dialogflow_cx_parser_agent/
│   └── csv_generation_agent/
└── tools/
    ├── bigquery_tools.py             # BigQuery execution tools
    └── initialize_state.py           # State initialization
```

## 🔍 Key Features

- **☁️ Cloud Storage**: Uses GCS artifacts instead of local files
- **🎯 Focused Purpose**: Dedicated to no-match analysis only
- **📊 Comprehensive Analysis**: Pattern detection and recommendations
- **🔄 Versioned Artifacts**: Automatic versioning of CSV files
- **🚀 Production Ready**: Proper error handling and logging
- **🤖 Natural Language**: Understands various ways to request analysis
- **📅 Date Flexibility**: Handles relative and specific date ranges
- **📋 Actionable Output**: Ready-to-import CSV files for Dialogflow CX

## 📈 Benefits

- **Faster Insights**: Get no-match analysis in seconds
- **Actionable Recommendations**: Specific training phrase suggestions
- **Cloud Integration**: Seamless GCS artifact storage
- **Scalable**: Handles large conversation datasets
- **Maintainable**: Clean, modular architecture
- **User-Friendly**: Natural language interaction
- **Production-Ready**: Comprehensive error handling and logging

## 🔮 Future Enhancements

- Real-time no-match monitoring
- Advanced pattern recognition with ML
- Direct Dialogflow CX API integration
- Automated intent creation
- Performance dashboards
- Multi-language support
- Advanced analytics and reporting

---

*Built with Google ADK for enterprise-grade AI agent development.* 