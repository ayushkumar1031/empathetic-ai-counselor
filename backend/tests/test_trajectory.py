from datetime import datetime

from app.models.emotion import (
    EmotionResult,
    EmotionLabel,
    IntensityLevel
)

from app.services.memory import (
    TrajectoryTracker,
    TrajectoryLabel
)


def make_emotion(label):

    return EmotionResult(
        label=label,
        score=0.9,
        intensity=IntensityLevel.HIGH,
        is_concerning=False,
        timestamp=datetime.now()
    )


def test_improving_trajectory():

    tracker = TrajectoryTracker()

    emotion_log = [
        make_emotion(EmotionLabel.FEAR),
        make_emotion(EmotionLabel.FEAR),
        make_emotion(EmotionLabel.SADNESS),
        make_emotion(EmotionLabel.NEUTRAL),
        make_emotion(EmotionLabel.JOY),
        make_emotion(EmotionLabel.JOY)
    ]

    result = tracker.calculate_trajectory(emotion_log)

    assert result == TrajectoryLabel.IMPROVING


def test_worsening_trajectory():

    tracker = TrajectoryTracker()

    emotion_log = [
        make_emotion(EmotionLabel.JOY),
        make_emotion(EmotionLabel.JOY),
        make_emotion(EmotionLabel.NEUTRAL),
        make_emotion(EmotionLabel.SADNESS),
        make_emotion(EmotionLabel.FEAR),
        make_emotion(EmotionLabel.FEAR)
    ]

    result = tracker.calculate_trajectory(emotion_log)

    assert result == TrajectoryLabel.WORSENING


def test_stable_trajectory():

    tracker = TrajectoryTracker()

    emotion_log = [
        make_emotion(EmotionLabel.NEUTRAL),
        make_emotion(EmotionLabel.NEUTRAL),
        make_emotion(EmotionLabel.NEUTRAL),
        make_emotion(EmotionLabel.NEUTRAL),
        make_emotion(EmotionLabel.NEUTRAL),
        make_emotion(EmotionLabel.NEUTRAL)
    ]

    result = tracker.calculate_trajectory(emotion_log)

    assert result == TrajectoryLabel.STABLE


def test_short_history_returns_stable():

    tracker = TrajectoryTracker()

    emotion_log = [
        make_emotion(EmotionLabel.FEAR),
        make_emotion(EmotionLabel.SADNESS),
        make_emotion(EmotionLabel.JOY)
    ]

    result = tracker.calculate_trajectory(emotion_log)

    assert result == TrajectoryLabel.STABLE