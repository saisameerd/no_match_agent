# 🚀 Quick Start Guide - No-Match Analysis Agent

## Prerequisites

- Python 3.8+
- Google Cloud Project with BigQuery and Cloud Storage enabled
- Service account with BigQuery and Storage permissions

## 1. Environment Setup

### Install Dependencies
```bash
cd no_match_analysis_agent
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Configure Environment Variables
Edit the `.env` file with your actual values:
```bash
PROJECT=your-gcp-project-id
BQ_LOCATION=us-central1
DATASET=your_dataset_name
GCS_BUCKET_NAME=your-no-match-analysis-artifacts
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account.json
```

## 2. GCS Bucket Setup

### Create GCS Bucket
```bash
gsutil mb gs://your-no-match-analysis-artifacts
gsutil iam ch allUsers:objectViewer gs://your-no-match-analysis-artifacts
```

### Service Account Permissions
```bash
# Create service account (if needed)
gcloud iam service-accounts create no-match-analysis-agent \
    --display-name="No-Match Analysis Agent"

# Grant BigQuery permissions
gcloud projects add-iam-policy-binding your-gcp-project-id \
    --member="serviceAccount:no-match-analysis-agent@your-gcp-project-id.iam.gserviceaccount.com" \
    --role="roles/bigquery.dataViewer"

# Grant Storage permissions
gcloud projects add-iam-policy-binding your-gcp-project-id \
    --member="serviceAccount:no-match-analysis-agent@your-gcp-project-id.iam.gserviceaccount.com" \
    --role="roles/storage.objectAdmin"
```

## 3. Test the Setup

### Run Test Script
```bash
python test_agent.py
```

Expected output:
```
🚀 Starting No-Match Analysis Agent Tests

🧪 Testing imports...
✅ Main agent imports successful
✅ Sub-agent imports successful
✅ Tools imports successful

🏗️ Testing agent structure...
✅ Agent structure verification successful

🔧 Testing tools...
✅ Tools testing successful

🌍 Testing environment configuration...
✅ .env file found
✅ PROJECT found in .env
✅ BQ_LOCATION found in .env
✅ DATASET found in .env
✅ GCS_BUCKET_NAME found in .env

📊 Test Results: 4/4 tests passed
🎉 All tests passed! The agent is ready to use.
```

## 4. Run the Agent

### Start the Agent
```bash
adk web
```

### Test Queries

#### Basic No-Match Analysis
```
Analyze no_match events from last week
```

#### With Specific Date Range
```
Find conversations with no_match events between 2024-01-01 and 2024-01-31
```

#### Generate Training Phrases CSV
```
Generate training phrases CSV for Dialogflow CX import
```

## 5. Expected Output

The agent will provide:
1. **Conversation Data**: Retrieved from BigQuery with no-match events
2. **Analysis Report**: Detailed no-match pattern analysis
3. **Bot Structure Analysis**: (if bot JSON provided)
4. **CSV Artifact**: Stored in GCS with training phrases

### Sample CSV Output
```csv
Intent Name,Training Phrase,Priority,Category,Description
AccountSuspensionIntent,Why is my account suspended?,High,New Intent,Handles account suspension queries
AccountSuspensionIntent,My account got suspended,High,New Intent,Handles account suspension queries
PaymentIssueIntent,I can't make a payment,Medium,New Intent,Handles payment-related issues
```

## 6. Troubleshooting

### Common Issues

#### Import Errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.8+)

#### BigQuery Access Issues
- Verify service account has BigQuery permissions
- Check PROJECT, BQ_LOCATION, and DATASET in .env file
- Ensure BigQuery API is enabled in your GCP project

#### GCS Access Issues
- Verify service account has Storage permissions
- Check GCS_BUCKET_NAME in .env file
- Ensure Cloud Storage API is enabled in your GCP project

#### Missing .env File
- Copy the template and fill in your values
- Ensure file is in the root directory of the agent

### Getting Help

1. Check the logs for detailed error messages
2. Verify all environment variables are set correctly
3. Test individual components using the test script
4. Check GCP Console for API enablement and permissions

## 7. Next Steps

After successful setup:
1. **Customize Prompts**: Modify agent prompts for your specific use case
2. **Add Bot JSON**: Provide Dialogflow CX bot JSON for enhanced analysis
3. **Scale Up**: Deploy to production with proper monitoring
4. **Integrate**: Connect with your existing Dialogflow CX workflow

---

*For detailed documentation, see README.md* 