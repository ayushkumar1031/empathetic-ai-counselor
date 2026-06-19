from datetime import datetime
import uuid
from enum import Enum


class ConversationSession:

    def __init__(self):

        self.session_id = str(uuid.uuid4())

        self.created_at = datetime.now()

        self.messages = []

        self.emotion_log = []

    def add_message(self, role, content):

        self.messages.append(
            {
                "role": role,
                "content": content
            }
        )

    def add_emotion(self, emotion_result):

        self.emotion_log.append(emotion_result)

    def get_history(self, max_turns=20):

        return self.messages[-max_turns:]

    def get_emotion_log(self):

        return self.emotion_log


class SessionManager:

    def __init__(self):

        self.sessions = {}

    def create_session(self):

        session = ConversationSession()

        self.sessions[session.session_id] = session

        return session

    def get_session(self, session_id):

        if session_id not in self.sessions:
            raise ValueError("Session not found")

        return self.sessions[session_id]


class TrajectoryLabel(Enum):
    IMPROVING = "improving"
    STABLE = "stable"
    WORSENING = "worsening"


class TrajectoryTracker:

    VALENCE_MAP = {
        "joy": 2,
        "neutral": 0,
        "anxiety": -1,
        "sadness": -1,
        "anger": -1,
        "fear": -2
    }

    def emotion_score(self, emotion_result):

        return self.VALENCE_MAP.get(
            emotion_result.label.value,
            0
        )

    def calculate_trajectory(self, emotion_log):

        if len(emotion_log) < 6:
            return TrajectoryLabel.STABLE

        recent = emotion_log[-3:]
        prior = emotion_log[-6:-3]

        recent_scores = [
            self.emotion_score(emotion)
            for emotion in recent
        ]

        prior_scores = [
            self.emotion_score(emotion)
            for emotion in prior
        ]

        mean_recent = sum(recent_scores) / len(recent_scores)
        mean_prior = sum(prior_scores) / len(prior_scores)

        if mean_recent > mean_prior + 0.3:
            return TrajectoryLabel.IMPROVING

        if mean_recent < mean_prior - 0.3:
            return TrajectoryLabel.WORSENING

        return TrajectoryLabel.STABLE