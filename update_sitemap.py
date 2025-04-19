import os
from datetime import datetime
import xml.etree.ElementTree as ET

def update_sitemap():
    # Base URL of your website
    base_url = "https://prahatishs.netlify.app/"
    
    # Create the root element
    urlset = ET.Element("urlset")
    urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
    
    # Priority mapping
    priority_map = {
        "Index.html": "1.0",
        "About.html": "0.8",
        "Blogs.html": "0.8",
        "Contact.html": "0.8"
    }
    
    # Get all HTML files
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    today = datetime.now().strftime("%Y-%m-%d")
    
    for html_file in html_files:
        url = ET.SubElement(urlset, "url")
        
        # Add location
        loc = ET.SubElement(url, "loc")
        loc.text = base_url + html_file
        
        # Add last modified date
        lastmod = ET.SubElement(url, "lastmod")
        lastmod.text = today
        
        # Add priority
        priority = ET.SubElement(url, "priority")
        if html_file in priority_map:
            priority.text = priority_map[html_file]
        elif html_file.startswith("blog"):
            priority.text = "0.7"
        else:
            priority.text = "0.5"
    
    # Create the XML tree
    tree = ET.ElementTree(urlset)
    
    # Write to sitemap.xml with proper XML declaration
    with open('sitemap.xml', 'wb') as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        tree.write(f, encoding='utf-8', xml_declaration=False)

if __name__ == "__main__":
    update_sitemap() 