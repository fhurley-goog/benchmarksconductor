import pandas as pd
from jinja2 import Environment, FileSystemLoader

def generate_html(csv_path):
    """
    Generates an HTML file from a CSV file using a Jinja2 template.

    Args:
        csv_path (str): The path to the input CSV file.
    """
    # Load the data from the CSV file
    df = pd.read_csv(csv_path)

    # Set up the Jinja2 environment
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    # Prepare the data for the template
    headers = df.columns.tolist()
    data = df.values.tolist()

    # Render the template with the data
    html_content = template.render(headers=headers, data=data)

    # Write the rendered HTML to a file
    with open("index.html", "w") as f:
        f.write(html_content)

if __name__ == "__main__":
    generate_html("data.csv")
