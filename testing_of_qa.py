from bs4 import BeautifulSoup

# Step 1: file read karo
with open("sample.xml", "r", encoding="utf-8") as f:
    xml_content = f.read()

# Step 2: XML parse karo
soup = BeautifulSoup(xml_content, "xml")

# Step 3: Title extract karo
title_tag = soup.find("title", {"type": "main"})
title = title_tag.text.strip() if title_tag else "No Title Found"


conclusions = []

# Find the div with type="conclusion"
conclusion_div = soup.find("div", {"type": "conclusion"})

if conclusion_div:
    # Loop through all <p> tags inside that div
    for p in conclusion_div.find_all("p"):
        conclusions.append(p.get_text(    strip=True))

print("Conclusion Paragraphs:", conclusions)

