# Data drift monitoring

This repo maintains the source code for monitoring the data drift in the given scenario.

## Tutorials

Install `virtualenv` if not already installed, using `pip install virtualenv`

### Evidently 101

1. Change directory using `cd src/evidently_101/`
1. Create a virtual env using `virtualenv .data-drift-101-env`
1. Activate the env using `source .data-drift-101-env/bin/activate`
1. Upgrade pip using `pip install --upgrade pip`
1. Install the dependencies using `pip install -r requirements.txt`
1. Run the `main.py` script using `python main.py`. This will generate the following reports as HTML files inside `evidently` folder:
   1. `data_stability.html`: This compares the baseline dataset with current dataset and runs several checks for data quality and integrity and help detect issues like feature values out of the expected range.
   1. `drift_report.html`: This compares the baseline dataset with current dataset input feature distributions, and the model outputs.
   1. `custom_test_suite.html`: This compares the baseline dataset with current dataset basic statistic tests.
