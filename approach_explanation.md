This document outlines the thought process and implementation steps followed to solve the heading detection challenge from Adobe’s Summer Internship Hackathon Round 1A.

## Understanding the Problem

The goal was to detect headings in a PDF based on font size and return them in a structured format. We were also told to run the solution fully offline using Docker.

## My Step-by-Step Approach

1. **Text Extraction**:  
  We used PyMuPDF (also known as fitz) for parsing PDFs. It allowed us to extract:
   1.Text blocks
   2.Font sizes
   3.Page numbers


2. **Font Size Analysis**:  
  We analyzed all font sizes used across the document and identified the top 3 largest:
  The assumption: larger text generally indicates higher-level headings
  Mapped the sizes to:
  H1 → Largest font
  H2 → Second largest
  H3 → Third largest



3. **Heading Mapping**:  
   For each line of text:
   We matched its font size with the H1, H2, or H3 thresholds
   If a match was found, the line was tagged as a heading with its corresponding level and page number


4. **JSON Creation**:  
   saved the output in this format:

   {
     "title": "Main Heading (H1)",
     "outline": [
       {"level": "H1", "text": "...", "page": 1},
       {"level": "H2", "text": "...", "page": 2}
     ]
   }
Multi-PDF Support:
The script processes every PDF in the /input folder and generates one JSON file per document inside /output.

## Assumptions Made
Font size is the only determinant of heading level (no use of bold/italic/style for simplicity)

The largest font in the document is considered H1, followed by H2 and H3

If the document has fewer than 3 unique font sizes, fallback logic prevents errors and still assigns heading levels accordingly

## Dockerization
To ensure portability and compliance with the offline requirement, we containerized the solution using Docker. No additional installation is required beyond Docker itself.

## Command used to run:
docker run --rm -v %cd%/input:/app/input -v %cd%/output:/app/output mypdfapp

Final Thoughts
This project was a valuable learning experience — from working with document layouts to containerizing Python apps. While I'm still learning, I’ve built this from scratch and am excited to improve and extend it further.

Thank you for reviewing!


