Here's how I solved the heading detection task:

## Understanding the Problem

The goal was to detect headings in a PDF based on font size and return them in a structured format. We were also told to run the solution fully offline using Docker.

## My Step-by-Step Approach

1. **Text Extraction**:  
   We have used `PyMuPDF` (also called `fitz`) to extract text, font sizes, and page numbers from each block of the PDF.

2. **Font Size Analysis**:  
   We have collected all font sizes used in the document and picked the top 3 largest ones — assuming the biggest text is H1, then H2, then H3.

3. **Heading Mapping**:  
   For every line of text, I checked its font size and matched it with H1, H2, or H3.

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
Headings are only differentiated by font size, not bold/italic/style.

The largest font in the PDF is considered H1, next two are H2 and H3.

If fewer than 3 sizes exist, fallback sizes are used to avoid errors.

## Dockerization
I added a Dockerfile so everything can run inside a container. No need to install anything except Docker.

## Command used to run:
docker run --rm -v %cd%/input:/app/input -v %cd%/output:/app/output mypdfapp

I’m still learning but tried to do this project on my own from scratch — if anything breaks, I’ll try to improve it. Thank you for reviewing!

