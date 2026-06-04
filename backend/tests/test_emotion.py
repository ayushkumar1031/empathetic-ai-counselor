from app.services.emotion import EmotionClassifier
import pytest

classifier = EmotionClassifier()


def test_empty_string():
    result = classifier.classify("")
    assert result["label"] == "neutral"


def test_whitespace_string():
    result = classifier.classify("   ")
    assert result["label"] == "neutral"


def test_happy_text():
    result = classifier.classify("I had a wonderful day today")
    assert "label" in result
    assert "score" in result


def test_sad_text():
    result = classifier.classify("I feel very sad and lonely")
    assert "label" in result
    assert "score" in result


def test_anger_text():
    result = classifier.classify("I am extremely angry")
    assert "label" in result
    assert "score" in result


def test_fear_text():
    result = classifier.classify("I am terrified of tomorrow's exam")
    assert "label" in result
    assert "score" in result


def test_neutral_text():
    result = classifier.classify("The book is on the table")
    assert "label" in result
    assert "score" in result


def test_short_text():
    result = classifier.classify("Hi")
    assert "label" in result
    assert "score" in result


def test_long_text():
    text = "I feel stressed " * 1000
    result = classifier.classify(text)
    assert "label" in result
    assert "score" in result


def test_type_error_int():
    with pytest.raises(TypeError):
        classifier.classify(123)


def test_type_error_list():
    with pytest.raises(TypeError):
        classifier.classify(["hello"])


def test_type_error_dict():
    with pytest.raises(TypeError):
        classifier.classify({"text": "hello"})


def test_score_type():
    result = classifier.classify("I am happy")
    assert isinstance(result["score"], float)


def test_label_type():
    result = classifier.classify("I am happy")
    assert isinstance(result["label"], str)


def test_return_type():
    result = classifier.classify("I am happy")
    assert isinstance(result, dict)