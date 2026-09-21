from scraper_engine import run_app


def file_sink(name, taxonomy, image_url):
    print(f"\nSaving results for '{name}':")
    print("#" * 30)
    with open(f"D:/OTHER GAMES/Darwin's Vault/{name}.md", 'w') as file:
        file.write(f"# {name}\n\n")
        if image_url:
            file.write(f"![{name}]({image_url})\n\n")
        for rank, value in taxonomy:
            file.write(f"{rank}: [[{value}]]\n")


if __name__ == "__main__":
    run_app(file_sink)
