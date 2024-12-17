import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 1. Analyze HTTP Headers
def check_http_headers(url):
    required_headers = [
        "Content-Security-Policy",
        "X-Content-Type-Options",
        "Strict-Transport-Security",
        "X-Frame-Options"
    ]
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers
        missing_headers = [header for header in required_headers if header not in headers]
        return {
            "missing_headers": missing_headers,
            "present_headers": {h: headers[h] for h in headers if h in required_headers}
        }
    except Exception as e:
        print(f"Error checking HTTP headers for {url}: {e}")
        return None


# 2. Check for Open Redirects
def check_open_redirects(base_url):
    try:
        response = requests.get(base_url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        open_redirects = []

        for link in soup.find_all('a', href=True):
            href = link['href']
            if "://" in href and base_url not in href:
                open_redirects.append(href)

        return open_redirects
    except Exception as e:
        print(f"Error checking open redirects for {base_url}: {e}")
        return []


# 3. Assess XSS Vulnerabilities
def check_xss_vulnerabilities(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        forms = soup.find_all('form')
        vulnerable_forms = []

        for form in forms:
            if not form.get("action") or not form.get("method"):
                vulnerable_forms.append(str(form))

        return vulnerable_forms
    except Exception as e:
        print(f"Error checking XSS vulnerabilities for {url}: {e}")
        return []


# 4. Detect Mixed Content
def check_mixed_content(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        mixed_content = []

        for tag in soup.find_all(['img', 'script', 'link'], src=True):
            if tag['src'].startswith("http://"):
                mixed_content.append(tag['src'])

        return mixed_content
    except Exception as e:
        print(f"Error checking mixed content for {url}: {e}")
        return []


# 5. Identify Sensitive Data in URLs
def check_sensitive_data_in_url(url):
    sensitive_keywords = ["key", "token", "password", "auth"]
    return any(keyword in url.lower() for keyword in sensitive_keywords)


# 6. Examine Directory Traversal Risks //used chat gpt
def check_directory_traversal(url):
    traversal_patterns = ["../", "..\\", "%2e%2e%2f"]
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        traversal_links = []

        for link in soup.find_all('a', href=True):
            href = link['href']
            if any(pattern in href for pattern in traversal_patterns):
                traversal_links.append(href)

        return traversal_links
    except Exception as e:
        print(f"Error checking directory traversal risks for {url}: {e}")
        return []


# 7. Subdomain Takeover Risk Assessment //used chat gpt
def check_subdomain_takeover(base_domain):
    # Placeholder for a more robust subdomain checking logic
    subdomains = ["subdomain1.noaa.gov", "subdomain2.noaa.gov"]  # Example subdomains
    vulnerable_subdomains = []

    for subdomain in subdomains:
        try:
            response = requests.get(f"http://{subdomain}", timeout=10)
            if response.status_code == 404:  # Subdomain not properly managed
                vulnerable_subdomains.append(subdomain)
        except:
            pass  # Could not resolve subdomain

    return vulnerable_subdomains


# 8. Assess HTTP Methods
def check_http_methods(url):
    risky_methods = ["PUT", "DELETE"]
    try:
        for method in risky_methods:
            response = requests.request(method, url, timeout=10)
            if response.status_code < 400:
                return {method: "Allowed"}
    except:
        pass

    return {method: "Not Allowed"}


# 9. Password Policy Evaluation //used chat gpt here
def check_password_strength_policy(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        password_fields = soup.find_all("input", {"type": "password"})
        weak_password_fields = []

        for field in password_fields:
            if not field.get("minlength") or int(field.get("minlength", 0)) < 8:
                weak_password_fields.append(str(field))

        return weak_password_fields
    except Exception as e:
        print(f"Error checking password strength policy for {url}: {e}")
        return []


# Crawl and assess links
def crawl_and_assess(base_url, max_depth=2):
    visited = set()
    results = {}

    def crawl(url, depth):
        if depth > max_depth or url in visited:
            return
        visited.add(url)
        print(f"Processing: {url}")

        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.content, "html.parser")

            # Perform all checks for this URL
            results[url] = {
                "http_headers": check_http_headers(url),
                "open_redirects": check_open_redirects(url),
                "xss_vulnerabilities": check_xss_vulnerabilities(url),
                "mixed_content": check_mixed_content(url),
                "sensitive_data": check_sensitive_data_in_url(url),
                "directory_traversal": check_directory_traversal(url),
                "http_methods": check_http_methods(url),
                "password_policy": check_password_strength_policy(url),
            }

            # Extract and crawl linked pages
            for link in soup.find_all('a', href=True):
                href = link['href']
                # Ensure valid URL
                full_url = urljoin(url, href)
                if full_url.startswith(base_url):  # Stay within base domain
                    crawl(full_url, depth + 1)
        except Exception as e:
            print(f"Error processing {url}: {e}")

    crawl(base_url, 0)
    return results

# Main script
if __name__ == "__main__":
    base_url = "https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00821/html"
    max_depth = 2  # Limit crawl depth to avoid excessive runtime
    assessment_results = crawl_and_assess(base_url, max_depth)

    print("\nWeb Security Assessment Results:")
    for url, result in assessment_results.items():
        print(f"\nURL: {url}")
        for key, value in result.items():
            print(f"  {key}: {value}")