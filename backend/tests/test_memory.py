from app.services.memory import (
    ConversationSession,
    SessionManager
)


def test_unique_session_ids():

    manager = SessionManager()

    session1 = manager.create_session()
    session2 = manager.create_session()

    assert session1.session_id != session2.session_id


def test_message_order_preserved():

    session = ConversationSession()

    session.add_message("user", "Hello")
    session.add_message("assistant", "Hi")

    history = session.get_history()

    assert history[0]["content"] == "Hello"
    assert history[1]["content"] == "Hi"


def test_history_limit():

    session = ConversationSession()

    for i in range(25):
        session.add_message("user", f"Message {i}")

    history = session.get_history(max_turns=20)

    assert len(history) == 20


def test_invalid_session():

    manager = SessionManager()

    try:
        manager.get_session("fake-id")
        assert False
    except ValueError:
        assert True