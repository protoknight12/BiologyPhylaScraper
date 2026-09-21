from scraper_engine import run_app


def print_sink(user_input, taxonomy):
    print(f"\nGetting results for '{user_input}':")
    print("#" * 30)
    for rank, name in taxonomy:
        print(f"{rank}: {name}")


if __name__ == "__main__":
    run_app(print_sink)
