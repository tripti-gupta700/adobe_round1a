# Adobe Hackathon Round 1A – PDF Heading Detector

This is our repository for the submission of Round 1A's problem statement for the Adobe's Summer Internship Hackathon.

## Problem Statement
We were asked to extract the structured headings (like H1, H2, H3) from PDF documents and generate a .JSON output that displays the document's outlines and titles based on their font sizes.

## How this project helps out?
- It goes through each PDF in the `input` folder
- Extracts the text and font size using PyMuPDF
- Detects the top 3 largest font sizes and maps them to H1, H2, H3
- Generates a `.json` file for each PDF in the `output` folder

## Execution of our project (Using Docker)

Step 1: Build the Docker Image
    docker build -t mypdfapp .
Step 2: Run the Docker Container
    On Linux/macOS:
        docker run -it --rm -v $(pwd):/app mypdfapp
    On Windows (CMD):
        docker run --rm -v %cd%/input:/app/input -v %cd%/output:/app/output mypdfapp


## Folder Structure
├── main.py
├── requirements.txt
├── Dockerfile
├── input/               
├── output/             
├── README.md
└── approach_explanation.md

## Benefits { How does this project help Adobe? }
 -- Everything runs offline
 -- no APIs or online dependencies are used. 
 -- Once the image is built, Docker runs everything inside the container.

Acknowledgment
I would like to express my sincere gratitude to Adobe for organizing such a challenging and insightful hackathon. This problem statement gave me the opportunity to explore real-world applications of PDF parsing, document structure analysis, and offline-first engineering.

The experience not only sharpened my technical skills in Python and Docker but also deepened my understanding of how machines interpret documents — a problem we often overlook in day-to-day development. I'm truly thankful for the chance to work on this, and I look forward to building on what I've learned in future rounds and beyond.


