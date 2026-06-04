from transformers import pipeline


class EmotionClassifier:

    def __init__(self):
        self.pipeline = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base"
        )

    def classify(self, text: str) -> dict:

        if not isinstance(text, str):
            raise TypeError("Input must be a string")

        if not text.strip():
            return {
                "label": "neutral",
                "score": 0.0
            }

        result = self.pipeline(
            text,
            truncation=True,
            max_length=512
        )

        return {
            "label": result[0]["label"],
            "score": round(float(result[0]["score"]), 4)
        }