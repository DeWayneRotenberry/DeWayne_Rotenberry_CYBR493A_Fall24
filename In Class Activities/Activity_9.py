import Web_Scraping_beautiful_soup as ws


# Main function to initialize and run the scraper
def main():
    # Initialize the scraper with the base URL
    scraper = ws.WVUScraper("https://www.wvu.edu")

    # Scrape the main page and follow links
    data = scraper.follow_links(scraper.base_url, max_pages=3, delay=1)

    # # Print data for each page
    # for page in data:
    #     print("Page URL:", page['url'])
    #     print("Headings:", page['headings'])
    #     print("Links:", page['links'])

    # Example of grabbing a specific item using a CSS selector
    html = scraper.get_html(scraper.base_url)
    soup = scraper.parse_html(html)

    # Attempt to retrieve the main heading using an alternative selector
    main_heading = scraper.grab_specific_item(soup, "h1, .wvu-masthead__logo, .hero-title")
    print("Main Heading:", main_heading)

    main_heading = scraper.grab_specific_item(soup, ".wvu-nav-wrapper")
    for something in main_heading:
        print( something,'\t')

    # Attempt to retrieve paragraphs within the about section using an alternative selector
    about_paragraphs = scraper.grab_specific_item(soup, ".about-section p, .about-content p, #about p")
    print("About Section Paragraphs:")
    for para in about_paragraphs:
        print(para)

    # Extract a section title (e.g., a subheading or section header)
    section_title = scraper.grab_specific_item(soup, "h2, .section-title, .content-heading")
    print("\nSection Titles:")
    for title in section_title:
        print(title)

   # Extract specific text from a feature section or banner
    feature_text = scraper.grab_specific_item(soup, ".feature-text, .banner-content, .highlight")
    print("\nFeature Section Content:")
    for feature in feature_text:
        print(feature)

    # Extract text from the footer or specific information in a footer section
    footer_info = scraper.grab_specific_item(soup, "footer p, .footer-content")
    print("\nFooter Information:")
    for footer in footer_info:
        print(footer)

if __name__ == "__main__":
    main()
