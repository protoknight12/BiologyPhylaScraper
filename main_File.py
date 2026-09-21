from scraper_engine import run_app


def file_sink(user_input, taxonomy):
    print(f"\nSaving results for '{user_input}':")
    print("#" * 30)
    with open(f"D:/OTHER GAMES/Darwin's Vault/{user_input}.md", 'w') as file:
        for rank, name in taxonomy:
            file.write(f"{rank}: [[{name}]]\n")


if __name__ == "__main__":
    run_app(file_sink)
