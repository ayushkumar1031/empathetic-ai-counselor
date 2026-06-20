from app.services.rag import RAGService
from app.services.context import ContextBuilder
from app.services.llm import LLMService

from app.services.memory import ConversationSession

from app.models.emotion import (
    EmotionResult,
    EmotionLabel,
    IntensityLevel
)

from datetime import datetime


session = ConversationSession()

session.add_message(
    "user",
    "I am extremely worried about tomorrow's exam. Give me specific coping strategies."
)

emotion_result = EmotionResult(
    label=EmotionLabel.FEAR,
    score=0.95,
    intensity=IntensityLevel.HIGH,
    is_concerning=True,
    timestamp=datetime.now()
)

rag = RAGService()

rag_chunks = rag.retrieve(
    query="I am extremely worried about tomorrow's exam. Give me specific coping strategies.",
    emotion_label="fear"
)

print("\nRAG DOCUMENTS RETRIEVED:\n")
print("=" * 60)

for i, chunk in enumerate(rag_chunks, start=1):
    print(f"\nDOCUMENT {i}")
    print("-" * 60)
    print(chunk[:500])

builder = ContextBuilder()

messages = builder.build(
    session=session,
    emotion_result=emotion_result,
    trajectory="stable",
    rag_chunks=rag_chunks
)

print("\n\nPROMPT SENT TO LLM:\n")
print("=" * 60)

for message in messages:
    print(f"\nROLE: {message['role']}")
    print(message["content"][:500])

llm = LLMService()

response = llm.generate(messages)

print("\n\nFINAL RESPONSE:\n")
print("=" * 60)
print(response)