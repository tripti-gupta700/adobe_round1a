# Adobe Hackathon Round 1A – PDF Heading Detector

This is my submission for the Round 1A problem statement from Adobe's Summer Internship Hackathon.

## Problem Statement
We were asked to extract structured headings (like H1, H2, H3) from PDF documents and generate a JSON output that shows the document's outline based on font sizes.

## What this project does
- It goes through each PDF in the `input` folder
- Extracts the text and font size using PyMuPDF
- Detects the top 3 largest font sizes and maps them to H1, H2, H3
- Generates a `.json` file for each PDF in the `output` folder

## How to Run (Using Docker)

docker build -t mypdfapp .
docker run --rm -v %cd%/input:/app/input -v %cd%/output:/app/output mypdfapp
On Linux/Mac, use $(pwd) instead of %cd%.

## Folder Structure
├── main.py
├── requirements.txt
├── Dockerfile
├── input/               # Folder where I put sample PDF files
├── output/              # Final JSON output comes here
├── README.md
└── approach_explanation.md

No Internet Required
Everything runs offline — no APIs or online dependencies are used. Once the image is built, Docker runs everything inside the container.

Thanks to Adobe for giving such a unique and fun problem to solve! I really learned a lot from this round.


