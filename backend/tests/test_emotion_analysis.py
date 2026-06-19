from app.services.emotion import EmotionClassifier
from app.models.emotion import (
    EmotionLabel,
    IntensityLevel,
    EmotionResult
)


classifier = EmotionClassifier()


def test_returns_emotion_result():
    result = classifier.classify("I am very happy today")

    assert isinstance(result, EmotionResult)


def test_joy_label():
    result = classifier.classify("I had a wonderful day")

    assert result.label == EmotionLabel.JOY


def test_fear_label():
    result = classifier.classify("I am terrified of tomorrow's exam")

    assert result.label == EmotionLabel.FEAR


def test_intensity_high():
    result = classifier.classify("I am terrified of tomorrow's exam")

    assert result.intensity == IntensityLevel.HIGH


def test_concerning_emotion():
    result = classifier.classify("I am terrified of tomorrow's exam")

    assert result.is_concerning is True


def test_non_concerning_emotion():
    result = classifier.classify("I had a wonderful day")

    assert result.is_concerning is False


def test_empty_string():
    result = classifier.classify("")

    assert result.label == EmotionLabel.NEUTRAL


def test_score_range():
    result = classifier.classify("I am happy")

    assert 0.0 <= result.score <= 1.0


def test_timestamp_exists():
    result = classifier.classify("I am happy")

    assert result.timestamp is not None


def test_long_text():
    text = "I feel stressed " * 1000

    result = classifier.classify(text)

    assert result is not None