# HealthCareAgent

# HealthCare Analytics Chatbot

A simple Streamlit chatbot UI that connects to Azure AI Foundry agents for healthcare analytics and non-clinical metrics.

## Features

- 🏥 Healthcare-focused UI design
- 🤖 Integration with Azure AI Foundry agents
- 📊 Hospital and Department filtering
- 💬 Interactive chat interface
- 🔄 Conversation reset functionality
- 📱 Responsive design

## Prerequisites

- Python 3.8+
- Azure AI Foundry project with an agent
- Azure subscription and appropriate credentials

## Installation

1. **Clone or create the project files**
   ```bash
   mkdir healthcare-chatbot
   cd healthcare-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Copy the `.env (example)` file to `.env`
   - Fill in your Azure AI Foundry credentials

## Configuration

### Required Environment Variables

Create a `.env` file with the following variables:

```bash
# Method 1: Using Connection String (Recommended)
AZURE_AI_PROJECT_CONNECTION_STRING=your_connection_string_here
AZURE_AI_AGENT_ID=your_agent_id_here

# Method 2: Using Individual Components (Alternative)
AZURE_AI_PROJECT_ID=your_project_id_here
AZURE_SUBSCRIPTION_ID=your_subscription_id_here
AZURE_RESOURCE_GROUP=your_resource_group_here
AZURE_AI_RESOURCE_NAME=your_ai_resource_name_here

# Azure Authentication (if needed)
AZURE_CLIENT_ID=your_client_id_here
AZURE_CLIENT_SECRET=your_client_secret_here
AZURE_TENANT_ID=your_tenant_id_here
```

### Getting Your Azure AI Foundry Agent ID

1. Go to your Azure AI Foundry project
2. Navigate to the Agent playground
3. Find your agent and copy its ID
4. The ID usually looks like: `asst_abc123xyz...`

### Getting Connection String

1. In Azure AI Foundry, go to your project
2. Go to "Settings" or "Overview"
3. Find the connection string in project details
4. It usually looks like: `DefaultEndpointsProtocol=https;AccountName=...`

## Usage

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the UI**
   - Open your browser to `http://localhost:8501`
   - Use the sidebar to select Hospital and Department filters
   - Start chatting with HealthBot Pro!

## File Structure

```
healthcare-chatbot/
├── app.py                 # Main Streamlit application
├── azure_agent_client.py  # Azure AI Foundry client wrapper
├── config.py             # Configuration management
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables (create this)
└── README.md           # This file
```

## Key Components

### `app.py`
- Main Streamlit application
- UI layout and chat interface
- Handles user interactions and message flow

### `azure_agent_client.py`
- Wrapper for Azure AI Projects SDK
- Handles authentication and agent communication
- Manages conversation threads

### `config.py`
- Configuration management
- Environment validation
- App constants and settings

## Customization

### Adding More Hospitals/Departments
Edit the lists in `config.py`:

```python
HOSPITALS = [
    "All Hospitals",
    "Your Hospital Name",
    # Add more hospitals
]

DEPARTMENTS = [
    "All Departments", 
    "Your Department Name",
    # Add more departments
]
```

### Styling
Modify the CSS in `app.py` to change colors, fonts, and layout.

### Agent Context
The application automatically adds filter context to messages sent to your agent:
```
[Context: Hospital: Central Medical Center | Department: Emergency Department] Your actual question
```

## Troubleshooting

### Common Issues

1. **"Failed to initialize Azure client"**
   - Check your `.env` file configuration
   - Verify your Azure credentials
   - Ensure your agent ID is correct

2. **"Agent not found"**
   - Verify the agent ID is correct
   - Check if the agent is deployed and active
   - Ensure you have access to the Azure AI project

3. **Authentication errors**
   - Try using Azure CLI: `az login`
   - Verify your Azure credentials
   - Check if service principal has proper permissions

### Debug Mode
Add this to see more detailed error messages:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Deployment

### Local Development
```bash
streamlit run app.py
```

### Azure Container Instances (Simple)
1. Create a Dockerfile
2. Build and push to Azure Container Registry
3. Deploy to Azure Container Instances

### Azure App Service
1. Use the Azure deployment template
2. Set environment variables in App Service configuration
3. Deploy your code

## License

This project is for educational and development purposes.

## Support

For issues with:
- **Azure AI Foundry**: Check Azure documentation
- **Streamlit**: Check Streamlit documentation  
- **This code**: Review the troubleshooting section above