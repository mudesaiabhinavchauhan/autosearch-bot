from browser_search import bing_search as google_search
from summarizer import summarize_results
def main():
    query = input("🔍 Enter your search query: ")
    print("\nSearching Google...\n")
    results = google_search(query)

    if not results:
        print("No results found.")
        return

    print("✅ Top Search Results:\n")
    for i, (title, url) in enumerate(results, 1):
        print(f"{i}. {title} ({url})")

    print("\nSummarizing using OpenAI...\n")
    summary = summarize_results(results)
    print("📄 Summary:\n")
    print(summary)

if __name__ == "__main__":
    main()