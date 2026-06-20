from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


DATA_DIR = Path("data/processed")

client = chromadb.PersistentClient(
    path="data/chroma_db"
)

collection = client.get_or_create_collection(
    name="empathetic_knowledge_base"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


for file_path in DATA_DIR.glob("*.txt"):

    text = file_path.read_text(
        encoding="utf-8"
    )

    embedding = model.encode(
        text
    ).tolist()

    collection.add(
        ids=[file_path.stem],
        documents=[text],
        embeddings=[embedding],
        metadatas=[
            {
                "source": file_path.name
            }
        ]
    )

    print(
        f"Added: {file_path.name}"
    )


print(
    "\nKnowledge base created successfully."
)