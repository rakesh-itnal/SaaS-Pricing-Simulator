from src.load_data import load_data
from src.invoice import generate_invoices
from src.report import generate_report

def main():

    df = load_data("data/usage_data.csv")

    df = generate_invoices(df)

    print(df)

    generate_report(df)

if __name__ == "__main__":
    main()