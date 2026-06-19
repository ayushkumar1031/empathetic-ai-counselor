from transformers import pipeline
from datetime import datetime

from app.models.emotion import (
    EmotionResult,
    EmotionLabel,
    IntensityLevel
)


class EmotionClassifier:

    def __init__(self):
        self.pipeline = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base"
        )

    def _get_intensity(self, score: float) -> IntensityLevel:
        if score >= 0.80:
            return IntensityLevel.HIGH
        elif score >= 0.50:
            return IntensityLevel.MEDIUM
        return IntensityLevel.LOW

    def _is_concerning(self, label: str, score: float) -> bool:
        concerning_emotions = {
            "fear",
            "sadness",
            "anger"
        }

        return label in concerning_emotions and score >= 0.70

    def classify(self, text: str) -> EmotionResult:

        if not isinstance(text, str):
            raise TypeError("Input must be a string")

        if not text.strip():
            return EmotionResult(
                label=EmotionLabel.NEUTRAL,
                score=0.0,
                intensity=IntensityLevel.LOW,
                is_concerning=False,
                timestamp=datetime.now()
            )

        result = self.pipeline(
            text,
            truncation=True,
            max_length=512
        )

        label = result[0]["label"]
        score = round(float(result[0]["score"]), 4)

        return EmotionResult(
            label=EmotionLabel(label),
            score=score,
            intensity=self._get_intensity(score),
            is_concerning=self._is_concerning(label, score),
            timestamp=datetime.now()
        )