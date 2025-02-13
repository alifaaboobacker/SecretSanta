from SecretSanta import SecretSanta
if __name__ == "__main__":
    file_path = "./assets/employees.csv"
    output_file_path = "./assets/secretsantas.csv"
    last_year_file = "./assets/last_year_santas.csv"

    secret_santa = SecretSanta(file_path, output_file_path, last_year_file)

    try:
        secret_santa.download_secret_santa_file()
        print("Secret Santa assignments created successfully!")
    except Exception as e:
        print(f"Error: {e}")
