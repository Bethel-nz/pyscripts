import os
import requests
from bs4 import BeautifulSoup


def download_file(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)


def convert_css_to_inline(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    css_files = []
    for link in soup.find_all("link"):
        if "stylesheet" in link.get("rel", []):
            css_files.append(link.get("href"))
            link.extract()

    style_tag = soup.new_tag("style")
    for css_file in css_files:
        if css_file.startswith("http"):
            url = css_file
        else:
            url = base_url + css_file
        response = requests.get(url)
        css_text = response.text
        style_tag.string = css_text
    soup.head.append(style_tag)

    return str(soup)


def convert_js_to_inline(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    script_tags = soup.find_all("script")
    for script_tag in script_tags:
        if script_tag.has_attr("src"):
            url = script_tag["src"]
            if not url.startswith("http"):
                url = base_url + url
            response = requests.get(url)
            js_text = response.text
            script_tag.string = str(js_text)
            script_tag.attrs = {}
    return str(soup)


def convert_images_to_inline(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    img_tags = soup.find_all("img")
    for img_tag in img_tags:
        src = img_tag.get("src")
        if not src.startswith("http"):
            src = base_url + src
        response = requests.get(src)
        data_uri = f"data:{response.headers['Content-Type']};base64,{response.content.decode('base64').decode('utf-8')}"
        img_tag["src"] = data_uri
    return str(soup)


def convert_to_inline_elements(website_url):
    response = requests.get(website_url)
    base_url = website_url.rstrip("/") + "/"
    website_name = website_url.split("//")[1].split("/")[0]
    website_folder = f"{website_name}_cloned"
    os.makedirs(website_folder, exist_ok=True)
    html_file = os.path.join(website_folder, "index.html")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(convert_images_to_inline(response.text, base_url))
        f.write(convert_css_to_inline(response.text, base_url))
        f.write(convert_js_to_inline(response.text, base_url))
        print(f"Created {html_file}")


if __name__ == "__main__":
    # website_url = input(
    #     "Enter the URL of the website to convert to inline elements: ")
    convert_to_inline_elements('https://dreamlike.art/')

# Example usage
# extract_element_style("")
