from dataclasses import dataclass
from enum import Enum
from datetime import datetime


class EmotionLabel(Enum):
    ANGER = "anger"
    FEAR = "fear"
    JOY = "joy"
    SADNESS = "sadness"
    SURPRISE = "surprise"
    NEUTRAL = "neutral"


class IntensityLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class EmotionResult:
    label: EmotionLabel
    score: float
    intensity: IntensityLevel
    is_concerning: bool
    timestamp: datetime