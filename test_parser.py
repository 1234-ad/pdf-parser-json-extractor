#!/usr/bin/env python3
"""
Test script for PDF Parser
Tests the parser with the assignment PDF
"""

from pdf_parser import PDFParser
import json

def test_parser():
    """Test the PDF parser with the provided URL"""
    parser = PDFParser()
    
    # Test URL from the assignment
    test_url = "https://client-uploads.nyc3.digitaloceanspaces.com/pdfs/288c7cb9-4eb0-4adc-9db7-e6b179389ef5/2025-09-17T07-27-39-833Z-5b0916cd.pdf"
    
    print("Testing PDF parser with assignment PDF...")
    print(f"URL: {test_url}")
    
    result = parser.parse_pdf(test_url)
    
    # Save test result
    with open('test_output.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    print("Test completed! Check test_output.json for results.")
    
    # Print summary
    if "pages" in result:
        print(f"\nSummary:")
        print(f"Pages processed: {len(result['pages'])}")
        for page in result["pages"]:
            content_count = len(page.get('content', []))
            print(f"  Page {page['page_number']}: {content_count} content items")
            
            # Show content types
            content_types = {}
            for item in page.get('content', []):
                item_type = item.get('type', 'unknown')
                content_types[item_type] = content_types.get(item_type, 0) + 1
            
            if content_types:
                type_summary = ", ".join([f"{count} {type_name}" for type_name, count in content_types.items()])
                print(f"    Types: {type_summary}")
    
    return result

if __name__ == "__main__":
    test_parser()