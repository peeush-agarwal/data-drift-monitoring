import os
import pandas as pd
import numpy as np

from sklearn.datasets import fetch_california_housing

from evidently.test_suite import TestSuite
from evidently.test_preset import DataStabilityTestPreset
from evidently.metric_preset import DataDriftPreset, TargetDriftPreset
from evidently.report import Report
from evidently.tests import (
    TestNumberOfColumnsWithMissingValues,
    TestNumberOfRowsWithMissingValues,
    TestNumberOfConstantColumns,
    TestNumberOfDuplicatedRows,
    TestNumberOfDuplicatedColumns,
    TestColumnsType,
    TestNumberOfDriftedColumns
)


def prepare_data():
    data = fetch_california_housing(as_frame=True)
    housing_data = data.frame

    housing_data.rename(columns={'MedHouseVal': 'target'}, inplace=True)
    housing_data['prediction'] = housing_data['target'].values + np.random.normal(0, 5, housing_data.shape[0])
    return housing_data


def split_data(df, n=5000):
    reference = df.sample(n, replace=False)
    current = df.sample(n, replace=False)
    return reference, current


def check_data_stability_and_save(reference, current, file_name):
    data_stability = TestSuite(tests=[
        DataStabilityTestPreset(),
    ])
    data_stability.run(reference_data=reference, current_data=current)
    data_stability.save_html(file_name)


def generate_drift_report(reference, current, file_name):
    drift_report = Report(metrics=[
        DataDriftPreset(),
        TargetDriftPreset(),
    ])
    drift_report.run(reference_data=reference, current_data=current)
    drift_report.save_html(file_name)


def run_custom_test_suite(reference, current, file_name):
    tests = TestSuite(tests=[
        TestNumberOfColumnsWithMissingValues(),
        TestNumberOfRowsWithMissingValues(),
        TestNumberOfConstantColumns(),
        TestNumberOfDuplicatedRows(),
        TestNumberOfDuplicatedColumns(),
        TestColumnsType(),
        TestNumberOfDriftedColumns(),
    ])
    tests.run(reference_data=reference, current_data=current)
    tests.save_html(file_name)


if __name__ == "__main__":
    housing_data = prepare_data()
    reference, current = split_data(housing_data)

    os.makedirs("evidently", exist_ok=True)
    check_data_stability_and_save(reference, current, "evidently/data_stability.html")
    generate_drift_report(reference, current, "evidently/drift_report.html")
    run_custom_test_suite(reference, current, "evidently/custom_test_suite.html")
