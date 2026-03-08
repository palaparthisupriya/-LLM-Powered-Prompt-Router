import json

CLASSIFIER_PROMPT = """
Your task is to classify the user's intent.

Choose ONE label from this list:
code, data, writing, career, unclear

Respond ONLY with a JSON object in this format:

{
  "intent": "label",
  "confidence": 0.0
}

Confidence must be a number between 0 and 1.

Do NOT include any explanation.
"""

def call_llm(prompt, message):

    message = message.lower()

    if "python" in message or "bug" in message or "function" in message or "code" in message:
        return '{"intent": "code", "confidence": 0.9}'

    elif "average" in message or "numbers" in message or "data" in message or "pivot" in message:
        return '{"intent": "data", "confidence": 0.85}'

    elif "paragraph" in message or "rewrite" in message or "writing" in message or "sentence" in message:
        return '{"intent": "writing", "confidence": 0.85}'

    elif "career" in message or "job" in message or "interview" in message or "resume" in message:
        return '{"intent": "career", "confidence": 0.9}'

    else:
        return '{"intent": "unclear", "confidence": 0.4}'


def classify_intent(message: str):

    try:

        response = call_llm(CLASSIFIER_PROMPT, message)

        parsed = json.loads(response)

        intent = parsed.get("intent", "unclear")
        confidence = float(parsed.get("confidence", 0.0))
        if confidence < 0.7:
            intent = "unclear"

        return {
            "intent": intent,
            "confidence": confidence
        }

    except Exception:
        # Graceful fallback
        return {
            "intent": "unclear",
            "confidence": 0.0
        }