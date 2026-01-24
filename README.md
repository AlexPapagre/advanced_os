# Advanced OS

---

This project contains a Python program (`main.py`) that performs basic analytics on a horse racing dataset.

The program generates summary statistics, visual plots, and a results report.

The dataset used is [Horse Racing Results - UK/Ireland 2015 - 2025](https://www.kaggle.com/datasets/deltaromeo/horse-racing-results-ukireland-2015-2025)

---

## Project Structure

```bash
.
├── data
│   └── horse_racing.csv
├── docker-compose.yml
├── Dockerfile
├── main.py
├── README.md
└── requirements.txt
```

## Running the Project with Docker

### Using Docker Compose

**1.** Build and run:

```bash
docker compose up --build
```

**2.** The program will:

- Read the dataset from `data/`
- Automatically create the `outputs/` directory if it doesn't exist
- Generate plots and analytics results in `outputs/` directory

All generated outputs will be saved in the `outputs` directory.

**3.** Cleanup (Optional):

Stop and remove containers:

```bash
docker compose down
```

---

### Using Docker


**1.** Build the Docker Image:

```bash
docker build -t horse_analytics:latest .
```

**2.** Run the container (mounting the outputs directory):

```bash
docker run --rm -v ./outputs:/app/outputs -v ./data:/app/data horse_analytics:latest
```

All generated outputs will be saved in the `outputs` directory.

**3.** Cleanup (Optional):

Remove the Docker image you built:

```bash
docker rmi horse_analytics:latest
```

---

## Outputs

The program generates:

- Summary statistics
- Visual plots
- Results report
