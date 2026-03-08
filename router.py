from prompts import PROMPTS


def call_llm(system_prompt, user_message):
    """
    Replace with actual LLM call.
    """

    # Example placeholder response
    return f"Generated response for: {user_message}"


def route_and_respond(message: str, intent_data: dict):

    intent = intent_data["intent"]

    if intent == "unclear":

        return (
            "I'm not sure what you need help with. "
            "Are you asking about coding, data analysis, writing, "
            "or career advice?"
        )

    system_prompt = PROMPTS.get(intent)

    if not system_prompt:

        return "Sorry, I couldn't determine the correct expert to handle your request."

    response = call_llm(system_prompt, message)

    return response