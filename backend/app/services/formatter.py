from pathlib import Path


class ResponseFormatter:

    def __init__(self):
        prompt_dir = Path(__file__).parent.parent / "prompts"

        with open(prompt_dir / "system.txt", "r", encoding="utf-8") as f:
            self.system_prompt = f.read()

        with open(prompt_dir / "emotion_context.txt", "r", encoding="utf-8") as f:
            self.emotion_template = f.read()

    def build_messages(self, user_message, emotion_result):

        emotion_context = self.emotion_template.format(
            emotion=emotion_result.label.value,
            intensity=emotion_result.intensity.value,
            is_concerning=emotion_result.is_concerning
        )

        return [
            {
                "role": "system",
                "content": self.system_prompt
            },
            {
                "role": "system",
                "content": emotion_context
            },
            {
                "role": "user",
                "content": user_message
            }
        ]