from scraper_engine import run_app


def print_sink(name, taxonomy, image_url):
    print(f"\nGetting results for '{name}':")
    print("#" * 30)
    for rank, value in taxonomy:
        print(f"{rank}: {value}")
    if image_url:
        print(f"Image: {image_url}")


if __name__ == "__main__":
    run_app(print_sink)
