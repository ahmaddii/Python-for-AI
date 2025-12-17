from scraper import scrape_quotes
from ai_classifier import classify_text
from router import route_quote
from fileHandler import log_info


def run_automaton():
            
            quotes = scrape_quotes()

            for quote in quotes[:3]:
                    
                    category = classify_text(quote)
                    route_quote(quote,category)
                    log_info(f"Quote routed as {category}")

if __name__ == "__main__":
        run_automaton()