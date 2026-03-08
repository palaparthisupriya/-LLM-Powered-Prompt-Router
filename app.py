from classifier import classify_intent
from router import route_and_respond
from logger import log_route


def main():

    print("AI Intent Router Started")
    print("Type 'exit' to stop\n")

    while True:

        message = input("User: ")

        if message.lower() == "exit":
            break

        intent_data = classify_intent(message)

        intent = intent_data["intent"]
        confidence = intent_data["confidence"]

        response = route_and_respond(message, intent_data)

        print("\nDetected Intent:", intent)
        print("Confidence:", confidence)
        print("\nResponse:", response)
        print()

        log_route(intent, confidence, message, response)


if __name__ == "__main__":
    main()