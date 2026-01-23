# Advanced OS

The program `main.py` performs basic analytics on a horse racing dataset. It generates summary statistics, plots, and a results report.

The dataset used is [Horse Racing results](https://www.kaggle.com/datasets/deltaromeo/horse-racing-results-ukireland-2015-2025).

To run it as a container 

docker build -t <name_of_your_image>:<tag> Dockerfile .

docker run --rm -v data_from_dataset:/os_project/outputs <name_of_your_image>:<tag>
