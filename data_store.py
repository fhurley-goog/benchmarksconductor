import csv

def create_data_store():
    """Creates the data.csv file with a header row."""
    header = ["Benchmark", "Gemini", "Model A", "Model B"]
    with open("data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)

if __name__ == "__main__":
    create_data_store()
