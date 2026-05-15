import os
import PyPDF2

files = [
    r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\Crickets Ain't Quiet.pdf",
    r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\3DO_boundary-madlibs-templates.txt",
    r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\stone-forgers-way-creative-context (1).pdf",
    r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\The Dynamics of Mathematics.pdf",
    r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\The Road to 3DO.pdf",
    r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\TSFW_Cohort.pdf",
    r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\Waterfalls and Breath.pdf",
    r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\You_Like_It_=_I_Love_It_The_Mathematics_of_Human_Connection.pdf"
]

output_path = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\extracted_contents.txt"

with open(output_path, 'w', encoding='utf-8') as out:
    for file in files:
        out.write(f"\n\n{'='*50}\nFILE: {os.path.basename(file)}\n{'='*50}\n")
        if file.endswith('.txt'):
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    out.write(f.read())
            except Exception as e:
                out.write(f"Error reading TXT: {e}")
        elif file.endswith('.pdf'):
            try:
                with open(file, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)
                    for i, page in enumerate(reader.pages):
                        text = page.extract_text()
                        if text:
                            out.write(text + "\n")
            except Exception as e:
                out.write(f"Error reading PDF: {e}")

print("Extraction complete. See extracted_contents.txt")
