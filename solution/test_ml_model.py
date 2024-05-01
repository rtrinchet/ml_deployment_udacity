import pytest
from ml.model import compute_model_metrics
from train_model import main


@pytest.fixture
def create_model_and_data():
    model, X_train, y_train, X_test, y_test, _ = main()

    return model, X_train, y_train, X_test, y_test


@pytest.fixture
def evaluate_model(create_model_and_data):
    trained_model, X_train, y_train, X_test, y_test = create_model_and_data
    preds = trained_model.predict(X_test)
    precision, recall, fbeta = compute_model_metrics(y_test, preds)

    return precision, recall, fbeta


def test_train_model_not_none(create_model_and_data):
    trained_model, X_train, y_train, X_test, y_test = create_model_and_data

    # Check that the model is trained (i.e., not None)
    assert trained_model is not None


def test_precision(evaluate_model):
    precision, _, _ = evaluate_model

    assert precision > 0.2


def test_recall(evaluate_model):
    _, recall, _ = evaluate_model

    assert recall > 0.2
