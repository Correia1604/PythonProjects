import pyttsx3
import PyPDF2

pdf_path = 'Currículo_2023.pdf'

pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
speaker = pyttsx3.init()

full_text = ""

for page_num in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    full_text += clean_text + '\n'

print(full_text)

# Save the full text to an MP3 file
speaker.save_to_file(full_text, 'currículo.mp3')
speaker.runAndWait()

speaker.stop()
