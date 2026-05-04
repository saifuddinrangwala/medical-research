"""Print Google Maps search URL for a college + city + state (India)."""
import sys
import urllib.parse


def map_url(name: str, city: str, state: str) -> str:
    q = f"{name}, {city}, {state}, India"
    return "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote(q)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: college_map_link.py \"College Name\" \"City\" \"State\"", file=sys.stderr)
        sys.exit(1)
    print(map_url(sys.argv[1], sys.argv[2], sys.argv[3]))
