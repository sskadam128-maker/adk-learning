from google.adk.agents import Agent

root_agent = Agent(
    name="bigquery_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are a helpful AI assistant.

    Answer the user's questions politely.

    If you don't know the answer, say you don't know.
    """
)
