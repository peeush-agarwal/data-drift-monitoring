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

### Real time ML monitoring with Evidently, Prometheus and Grafana

1. Change directory using `cd src/evidently_prometheus_grafana/`
1. Create a virtual env using `virtualenv .data-drift-e_p_g-env`
1. Activate the env using `source .data-drift-e_p_g-env/bin/activate`
1. Upgrade pip using `pip install --upgrade pip`
1. Install the dependencies using `pip install -r requirements.txt`
1. Run the `main.py` script using `python main.py`. This will generate the following dataset files inside `datasets/kdd_k_neighbors_classifier` folder:
   1. `reference.csv`: Reference or baseline data
   1. `production.csv`: Production data as for mimicking the real-world scenario
1. Launch the services to display dashboards, using `docker-compose up -d --build`
1. Browse [Grafana Dashboard](http://localhost:3000/) here. _Use admin/admin for uname and pwd._
1. Send HTTP POST request to evidently service using Postman as following:
   ```
   Method: POST
   URL: http://localhost:8085/iterate/kdd_k_neighbors_classifier
   Body: {"duration": {"0": 1, "1": 0, "2": 0, "3": 0, "4": 0}, "protocol_type": {"0": "tcp", "1": "tcp", "2": "icmp", "3": "icmp", "4": "tcp"}, "service": {"0": "smtp", "1": "http", "2": "ecr_i", "3": "ecr_i", "4": "private"}, "flag": {"0": "SF", "1": "SF", "2": "SF", "3": "SF", "4": "S0"}, "src_bytes": {"0": 1022, "1": 376, "2": 1032, "3": 1032, "4": 0}, "dst_bytes": {"0": 389, "1": 285, "2": 0, "3": 0, "4": 0}, "land": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0}, "wrong_fragment": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0}, "urgent": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0}, "hot": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0}, "num_failed_logins": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0}, "logged_in": {"0": 1, "1": 1, "2": 0, "3": 0, "4": 0}, "num_compromised": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0}, "root_shell": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0}, "su_attempted": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0}, "num_root": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0}, "num_file_creations": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0}, "num_shells": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0}, "num_access_files": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0}, "num_outbound_cmds": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0}, "is_host_login": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0}, "is_guest_login": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0}, "count": {"0": 1, "1": 2, "2": 511, "3": 511, "4": 252}, "srv_count": {"0": 1, "1": 2, "2": 511, "3": 511, "4": 1}, "serror_rate": {"0": 0.0, "1": 0.0, "2": 0.0, "3": 0.0, "4": 1.0}, "srv_serror_rate": {"0": 0.0, "1": 0.0, "2": 0.0, "3": 0.0, "4": 1.0}, "rerror_rate": {"0": 0.0, "1": 0.0, "2": 0.0, "3": 0.0, "4": 0.0}, "srv_rerror_rate": {"0": 0.0, "1": 0.0, "2": 0.0, "3": 0.0, "4": 0.0}, "same_srv_rate": {"0": 1.0, "1": 1.0, "2": 1.0, "3": 1.0, "4": 0.0}, "diff_srv_rate": {"0": 0.0, "1": 0.0, "2": 0.0, "3": 0.0, "4": 0.05}, "srv_diff_host_rate": {"0": 0.0, "1": 0.0, "2": 0.0, "3": 0.0, "4": 0.0}, "dst_host_count": {"0": 83, "1": 255, "2": 255, "3": 255, "4": 255}, "dst_host_srv_count": {"0": 175, "1": 255, "2": 255, "3": 255, "4": 1}, "dst_host_same_srv_rate": {"0": 0.64, "1": 1.0, "2": 1.0, "3": 1.0, "4": 0.0}, "dst_host_diff_srv_rate": {"0": 0.02, "1": 0.0, "2": 0.0, "3": 0.0, "4": 0.06}, "dst_host_same_src_port_rate": {"0": 0.01, "1": 0.0, "2": 1.0, "3": 1.0, "4": 0.0}, "dst_host_srv_diff_host_rate": {"0": 0.02, "1": 0.0, "2": 0.0, "3": 0.0, "4": 0.0}, "dst_host_serror_rate": {"0": 0.0, "1": 0.0, "2": 0.0, "3": 0.0, "4": 1.0}, "dst_host_srv_serror_rate": {"0": 0.0, "1": 0.0, "2": 0.0, "3": 0.0, "4": 1.0}, "dst_host_rerror_rate": {"0": 0.0, "1": 0.0, "2": 0.0, "3": 0.0, "4": 0.0}, "dst_host_srv_rerror_rate": {"0": 0.0, "1": 0.0, "2": 0.0, "3": 0.0, "4": 0.0}, "labels": {"0": "normal.", "1": "normal.", "2": "smurf.", "3": "smurf.", "4": "neptune."}, "prediction": {"0": "normal.", "1": "normal.", "2": "smurf.", "3": "smurf.", "4": "neptune."}}
   ```
   This should return "ok" in response.
1. Check the [Grafana Dashboard](http://localhost:3000/)