import pdfplumber

def extract_text_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

if __name__ == "__main__":
    resume_text = extract_text_from_pdf("../data/resumes/sample.pdf")
    print(resume_text[:1000])
