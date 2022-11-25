import argparse
import logging
import os
import shutil
import subprocess

from scripts import prepare_datasets


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler()]
    )


def check_dataset(
    force: bool,
    datasets_path: str,
    dataset_name: str,
) -> None:
    logging.info("Check dataset %s", dataset_name)
    dataset_path = os.path.join(datasets_path, dataset_name)

    if os.path.exists(dataset_path):
        if force:
            logging.info("Remove dataset directory %s", dataset_path)
            shutil.rmtree(dataset_path)
            os.makedirs(dataset_path)
        else:
            logging.info("Dataset %s already exists", dataset_name)
            return

    logging.info("Download dataset %s", dataset_name)
    prepare_datasets.prepare(dataset_name, dataset_path)


def download_test_datasets(force: bool):
    datasets_path = os.path.abspath("datasets")
    logging.info("Check datasets directory %s", datasets_path)

    if not os.path.exists(datasets_path):
        logging.info("Create datasets directory %s", datasets_path)
        os.makedirs(datasets_path)
    else:
        logging.info("Datasets directory already exists")

    for dataset_name in ["kdd_k_neighbors_classifier"]:
        check_dataset(force, datasets_path, dataset_name)


def run_script(cmd: list, wait: bool) -> None:
    logging.info("Run %s", " ".join(cmd))
    script_process = subprocess.Popen(
        " ".join(cmd),
        stdout=subprocess.PIPE,
        shell=True,
    )

    if wait:
        script_process.wait()

        if script_process.returncode != 0:
            exit(script_process.returncode)


def main(force: bool):
    setup_logger()
    download_test_datasets(force=force)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script for data and config generation for Evidently"
        " metrics integration with Prometheus and Grafana"
    )
    parser.add_argument(
        "-f", "--force",
        action="store_true",
        help="Remove and download again test datasets")
    parameters = parser.parse_args()
    main(force=parameters.force)
