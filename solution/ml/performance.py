from sklearn.metrics import accuracy_score
import numpy as np


def performance_on_slices(
    model, X_test, y_test, categorical_column_dict
):  # , encoder):
    """
    Calculate the performance of a model on slices of the test data based on specified categorical column indices.

    Parameters:
        model: A trained machine learning model.
        X_test (array-like): Test input features without column names.
        y_test (array-like): Test true labels.
        categorical_column_indices (list): List of indices of the categorical columns.

    Returns:
        dict: A dictionary containing performance metrics for each slice.
    """
    performance_dict = {}
    categorical_column_indices = categorical_column_dict["idx"]
    categorical_column_names = categorical_column_dict["column"]
    for idx in categorical_column_indices:
        col_name = categorical_column_names[idx]
        unique_values = np.unique(X_test[:, idx])
        print(idx, col_name, unique_values)
        for value in unique_values:
            mask = X_test[:, idx] == value
            X_slice = X_test[mask]
            y_slice = y_test[mask]

            if (
                len(set(y_slice)) > 1
            ):  # Ensure there are samples from more than one class
                y_pred = model.predict(X_slice)
                slice_accuracy = accuracy_score(y_slice, y_pred)
                # value = encoder[idx].inverse_transform([[value]])[0][0]

                if col_name not in performance_dict:
                    performance_dict[col_name] = {}
                performance_dict[col_name][value] = slice_accuracy
    print(performance_dict)

    with open("slice_output.txt", "w") as f:
        print(performance_dict, file=f)

    return performance_dict


# Example usage:
# Assuming 'model' is a trained model, 'X_test' and 'y_test' are test data as arrays,
# and 'categorical_column_indices' is the list of indices of the categorical columns.
# performance_results = performance_on_slices(model, X_test, y_test, categorical_column_indices)
