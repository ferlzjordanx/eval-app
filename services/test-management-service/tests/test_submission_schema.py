from datetime import datetime, timezone

from src.schemas.test_submission_schema import TestSubmissionCreate as SubmissionCreate


def test_submission_create_strips_timezone_from_due_date():
    due_date = datetime(2026, 6, 1, 12, 30, tzinfo=timezone.utc)

    submission = SubmissionCreate(test_id=1, user_id=2, due_date=due_date)

    assert submission.due_date is not None
    assert submission.due_date.tzinfo is None
    assert submission.due_date.hour == 12
