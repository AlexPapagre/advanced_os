# Advanced OS

---

This project contains a Python program (`main.py`) that performs basic analytics on a horse racing dataset.

The program generates summary statistics, visual plots, and a results report.

The dataset used is [Horse Racing Results - UK/Ireland 2015 - 2025](https://www.kaggle.com/datasets/deltaromeo/horse-racing-results-ukireland-2015-2025)

---

## Project Structure

```bash
.
├── pandas
│   ├── build.sh
│   ├── data
│   │   └── horse_racing.csv
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   └── run.sh
├── README.md
└── spark
    ├── build.sh
    ├── config
    │   ├── spark-defaults.conf
    │   ├── spark-env.sh
    │   └── start-spark.sh
    ├── data
    │   └── horse_racing.csv
    ├── docker-compose.yml
    ├── Dockerfile
    ├── main.py
    ├── outputs
    │   └── analytics_results.txt
    ├── run.sh
    └── spark-rest-request.sh
```

---

## Running the Project with Docker

There are 2 sub projects:

- `pandas` uses the Pandas library to perform the analytics
- `spark` uses the Apache Spark library to perform the analytics

First of all go to one of the sub projects and follow the instructions below.

```bash
cd pandas
```

or

```bash
cd spark
```

---

### Using Docker Compose

**1.** Build and run:

```bash
docker compose up --build
```

**2.** Cleanup:

Stop and remove containers:

```bash
docker compose down
```

---

### Using Docker


**1.** Build the Docker Image:

```bash
./build.sh
```

**2.** Run the container:

```bash
./run.sh
```

**3.** Cleanup (Optional):

Remove the Docker Image you built:

```bash
docker rmi pandas-app
```

---

## Usage

The 2 sub projects analyse the same dataset but with different approaches.

---

### Pandas

After running the project, the program will:

- Read the dataset from `data/`
- Automatically create the `outputs/` directory if it doesn't exist
- Generate plots and analytics results in `outputs/` directory

After that the project will stop by itself.

---

### Spark

After running the project, the program will:

- Generate a hostname to use for the Spark master
- Wait for the user to send a REST request to the Spark master

Send a REST request to the Spark master:

```bash
./spark-rest-request.sh <HOSTNAME>
```

After the user sends the request, the program will:

- Read the dataset from `data/`
- Automatically create the `outputs/` directory if it doesn't exist
- Generate analytics results in `outputs/` directory and print them to `stdout`

The projet stays open and waits for the user to send another request.
