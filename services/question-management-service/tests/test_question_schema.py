import pytest
from pydantic import ValidationError

from src.models.question import OptionCreate, QuestionType
from src.schemas.question import QuestionCreate
from src.services.question_service import QuestionService


def test_mcq_question_requires_one_valid_correct_answer():
    question = QuestionCreate(
        type=QuestionType.MCQ,
        question_text="Which option is the correct answer?",
        options=[OptionCreate(text="First"), OptionCreate(text="Second")],
        correct_answers=[2],
    )

    assert question.correct_answers == [2]


def test_mcq_question_rejects_out_of_range_answer():
    with pytest.raises(ValidationError):
        QuestionCreate(
            type=QuestionType.MCQ,
            question_text="Which option is the correct answer?",
            options=[OptionCreate(text="First"), OptionCreate(text="Second")],
            correct_answers=[3],
        )


def test_options_are_assigned_one_indexed_ids():
    options = QuestionService.convert_options_to_stored_format(
        [OptionCreate(text=" Alpha "), OptionCreate(text="Beta")]
    )

    assert options is not None
    assert [option.option_id for option in options] == [1, 2]
    assert [option.text for option in options] == ["Alpha", "Beta"]
