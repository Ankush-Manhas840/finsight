"""Create the chat model used everywhere (Gemini by default, key from .env)."""


def get_llm():
    """Return a chat model. Nov 1: raw SDK call. Nov 8: switch to a LangChain chat model."""
    # TODO (Nov 1): load GOOGLE_API_KEY from .env and make one call.
    raise NotImplementedError
