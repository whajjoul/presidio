from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def main():
    engine = AnonymizerEngine()

    text = "My name is Wissam, Wissam Hajjoul"

    result = engine.anonymize(
        text=text,
        analyzer_results=[
            # First name
            RecognizerResult(entity_type="PERSON", start=11, end=17, score=0.8),
            # Full name
            RecognizerResult(entity_type="PERSON", start=19, end=32, score=0.8),
        ],
        operators={
            "PERSON": OperatorConfig("replace", {"new_value": "whajjoul"})
        },
    )

    print(f"text: {result.text}")
    print(f"items: {result.items}")

if __name__ == "__main__":
    main()
