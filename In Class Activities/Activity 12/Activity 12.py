def Generate_Pages(base_url):
    # Total number of bugs and bugs per page
    BUGS = 420638
    BUGS_PER_PAGE = 75

    # Calculate the total number of pages
    total_pages = (BUGS + BUGS_PER_PAGE - 1) // BUGS_PER_PAGE

    # Loop through each page and generate the URL
    for page in range(total_pages):
        # Calculate the start value for the current page
        start_value = page * BUGS_PER_PAGE

        # Create the URL for the current page, including both &memo and &start
        page_url = f"{base_url}&memo={BUGS_PER_PAGE}&start={start_value}"

        # Print the generated page URL
        print(page_url)



base_url = "https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&orderby=-importance"
Generate_Pages(base_url)
