# Script to train machine learning model.
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle

# Add the necessary imports for the starter code.
from solution.ml.data import process_data
from solution.ml.model import train_model, compute_model_metrics
from solution.ml.performance import performance_on_slices

data_path = "solution/data/census_clean.csv"
cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]


def get_categorical_indices(df, categorical_columns):
    idx_list = [df.columns.get_loc(col) for col in categorical_columns]
    return {"column": df.columns, "idx": idx_list}


def get_train_test():
    import os
    # print('------->', os.chdir('solution'))
    print('------->', os.getcwd())

    print('------->', os.listdir())
    # Add code to load in the data.
    data = pd.read_csv(data_path)
    #
    # try:
    #     data = pd.read_csv("data/census_clean.csv")
    # except Exception as e:
    #     print(e)
    #     print('Github actions workflow!!')
    #     data = pd.read_csv("solution/data/census_clean.csv")

    # Optional enhancement, use K-fold cross validation instead of a train-test split.
    train, test = train_test_split(data, test_size=0.20)
    return train, test


def preprocess(train, test):
    X_train, y_train, encoder, lb = process_data(
        train, categorical_features=cat_features, label="salary", training=True
    )

    # Proces the test data with the process_data function.
    X_test, y_test, _, _ = process_data(
        test,
        categorical_features=cat_features,
        encoder=encoder,
        lb=lb,
        label="salary",
        training=False,
    )
    return X_train, y_train, X_test, y_test, encoder


def main():
    train, test = get_train_test()
    X_train, y_train, X_test, y_test, encoder = preprocess(train, test)

    # Train and save a model.
    model = train_model(X_train, y_train)

    with open("model.pkl", "wb") as output_file:
        pickle.dump(model, output_file)

    return model, X_train, y_train, X_test, y_test, encoder


if __name__ == "__main__":
    model, X_train, y_train, X_test, y_test, encoder = main()

    categorical_column_dict = get_categorical_indices(
        pd.read_csv(data_path), cat_features
    )

    y_pred = model.predict(X_test)
    precision, recall, fbeta = compute_model_metrics(y_test, y_pred)
    print(precision, recall, fbeta)
    categorical_column_indices = categorical_column_dict["idx"]
    performance_results = performance_on_slices(
        model, X_test, y_test, categorical_column_dict
    )  # , encoder)

    # performance_results = performance_on_slices(model,
    #                                             train, test,
    #                                             categorical_features)
