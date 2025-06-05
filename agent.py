

import yaml
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.agents.models import ListSortOrder


def get_agent_response(user_message: str) -> str:
    try:
        # Load agent config from YAML
        with open("Intent_Recognition_agent.yaml", "r") as f:
            config = yaml.safe_load(f)
        agent_id = config.get("id")
        # You may want to parameterize thread_id or manage threads dynamically
        thread_id = config.get("thread_id", "thread_3l7EQ5izM4chzV4OdYyb01xg")
        endpoint = config.get("endpoint", "https://agent-exp-shuchi.services.ai.azure.com/api/projects/code-generation")

        credential = DefaultAzureCredential()
        project = AIProjectClient(
            credential=credential,
            endpoint=endpoint)
        agent = project.agents.get_agent(agent_id)
        thread = project.agents.threads.get(thread_id)
        project.agents.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_message
        )
        run = project.agents.runs.create_and_process(
            thread_id=thread.id,
            agent_id=agent.id)
        if run.status == "failed":
            return f"Agent run failed: {run.last_error}"
        messages = project.agents.messages.list(thread_id=thread.id, order=ListSortOrder.ASCENDING)
        for message in reversed(list(messages)):
            if message.role == "assistant" and message.text_messages:
                return message.text_messages[-1].text.value
        return "No response from agent."
    except Exception as e:
        return f"Error communicating with agent: {e}"
