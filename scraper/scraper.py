import requests
from bs4 import BeautifulSoup

def scrape_brainlox():
    url = "https://brainlox.com/courses/category/technical"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"❌ Failed to fetch website data (Status Code: {response.status_code})")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # ✅ Debug: Print first 1000 characters of the fetched HTML
    print("🔍 Website HTML Preview (First 1000 characters):")
    print(soup.prettify()[:1000])

    # ✅ Find courses (Updated Selectors)
    courses = []
    for course_div in soup.find_all("div", class_="courses-content"):  # Updated class name
        title_tag = course_div.find("h3").find("a")  # Extract title from <h3><a>
        price_tag = course_div.find_next("span", class_="price-per-session")  # Find closest price
        
        title = title_tag.text.strip() if title_tag else "Unknown Title"
        price = price_tag.text.strip() if price_tag else "No Price Available"

        courses.append(f"{title}: {price}")

    if not courses:
        print("⚠️ No courses found! The HTML structure might have changed.")
    else:
        print("\n✅ Scraped Courses:\n", "\n".join(courses))

    return "\n".join(courses)

if __name__ == "__main__":
    try:
        scrape_brainlox()
    except Exception as e:
        print(f"❌ An error occurred: {e}")