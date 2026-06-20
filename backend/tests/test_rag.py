from app.services.rag import RAGService


def test_rag_initialization():

    rag = RAGService()

    assert rag is not None


def test_retrieve_returns_list():

    rag = RAGService()

    results = rag.retrieve(
        query="I am worried about exams",
        emotion_label="fear"
    )

    assert isinstance(results, list)


def test_retrieve_not_empty():

    rag = RAGService()

    results = rag.retrieve(
        query="I am worried about exams",
        emotion_label="fear"
    )

    assert len(results) > 0


def test_retrieve_returns_strings():

    rag = RAGService()

    results = rag.retrieve(
        query="I am worried about exams",
        emotion_label="fear"
    )

    assert isinstance(results[0], str)


def test_retrieve_multiple_documents():

    rag = RAGService()

    results = rag.retrieve(
        query="I am worried about exams",
        emotion_label="fear"
    )

    assert len(results) >= 3