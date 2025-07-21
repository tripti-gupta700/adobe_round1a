import fitz  # PyMuPDF
import json
import os

# Folder from which to read PDFs
input_dir = "/app/input"

# Folder where we'll save the JSON outputs
output_dir = "/app/output"

# Create the output directory if it doesn't already exist
os.makedirs(output_dir, exist_ok=True)

# Loop through all PDF files in the input folder
for filename in os.listdir(input_dir):
    if filename.endswith(".pdf"):
        # Full path to the input PDF file
        pdf_path = os.path.join(input_dir, filename)

        # Prepare corresponding output file path
        output_path = os.path.join(output_dir, filename.replace(".pdf", ".json"))

        # Open the PDF file using PyMuPDF
        doc = fitz.open(pdf_path)

        heading_candidates = []  # to store possible headings
        font_sizes = []          # to identify top 3 font sizes

        # Go through every page of the PDF
        for page_num, page in enumerate(doc, start=1):
            blocks = page.get_text("dict")["blocks"]
            for block in blocks:
                if "lines" in block:  # 🛡️ safeguard to avoid crashing if lines are missing
                    for line in block["lines"]:
                        for span in line["spans"]:
                            text = span["text"].strip()
                            size = span["size"]
                            if text:
                                # Save the text, font size, and page number
                                heading_candidates.append((text, size, page_num))
                                font_sizes.append(size)

        # Sort the font sizes in descending order
        unique_sizes = sorted(set(font_sizes), reverse=True)

        # In case we didn't find at least 3 font sizes, create fallback sizes
        if len(unique_sizes) < 3:
            print(f"Not enough distinct font sizes found in {filename} — using fallback")
            while len(unique_sizes) < 3:
                if unique_sizes:
                    unique_sizes.append(unique_sizes[-1])  # repeat last known size
                else:
                    # if absolutely no size found, use default guesses
                    unique_sizes = [12, 10, 8]
                    break

        # Assign top 3 font sizes to heading levels H1, H2, H3
        heading_map = {
            unique_sizes[0]: "H1",
            unique_sizes[1]: "H2",
            unique_sizes[2]: "H3"
        }

        outline = []  # to hold structured heading data

        # Loop through the candidates and map them to heading levels
        for text, size, page_num in heading_candidates:
            level = heading_map.get(size)
            if level:
                outline.append({
                    "level": level,
                    "text": text,
                    "page": page_num
                })

        # Choose first H1 as the document title, or fallback to default
        document_title = "Untitled Document"
        for item in outline:
            if item["level"] == "H1":
                document_title = item["text"]
                break

        # Structure the final output as required
        output = {
            "title": document_title,
            "outline": outline
        }

        # Write the JSON to the output folder
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        print(f" Processed: {filename} → {output_path}")
