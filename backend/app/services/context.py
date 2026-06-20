from pathlib import Path


class ContextBuilder:

    def __init__(self):

        self.system_prompt = Path(
            "backend/app/prompts/system.txt"
        ).read_text(
            encoding="utf-8"
        )

    def build(
        self,
        session,
        emotion_result,
        trajectory,
        rag_chunks
    ):

        messages = []

        messages.append(
            {
                "role": "system",
                "content": self.system_prompt
            }
        )

        emotion_context = f"""
Detected Emotion: {emotion_result.label.value}
Intensity: {emotion_result.intensity.value}
Trajectory: {trajectory}
"""

        messages.append(
            {
                "role": "system",
                "content": emotion_context
            }
        )

        rag_context = "\n\n".join(rag_chunks)

        messages.append(
            {
                "role": "system",
                "content": f"Relevant coping strategies:\n\n{rag_context}"
            }
        )

        messages.extend(
            session.get_history()
        )

        return messages