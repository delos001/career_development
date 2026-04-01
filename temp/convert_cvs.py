import os
from docx import Document

input_dir = r'C:\Users\delos\code\career_development\temp'
output_dir = r'C:\Users\delos\code\career_development\temp\converted'
os.makedirs(output_dir, exist_ok=True)

def docx_to_markdown(path):
    doc = Document(path)
    lines = []
    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            lines.append('')
            continue
        style = para.style.name.lower()
        if 'heading 1' in style:
            lines.append(f'# {text}')
        elif 'heading 2' in style:
            lines.append(f'## {text}')
        elif 'heading 3' in style:
            lines.append(f'### {text}')
        else:
            lines.append(text)
    return '\n'.join(lines)

files = [f for f in os.listdir(input_dir) if f.endswith('.docx')]
print(f'Found {len(files)} files')
errors = []
for f in sorted(files):
    try:
        md = docx_to_markdown(os.path.join(input_dir, f))
        out_name = os.path.splitext(f)[0] + '.md'
        with open(os.path.join(output_dir, out_name), 'w', encoding='utf-8') as fh:
            fh.write(md)
        print(f'  OK: {f}')
    except Exception as e:
        errors.append((f, str(e)))
        print(f'  FAIL: {f} — {e}')

print(f'Done. {len(files)-len(errors)} converted, {len(errors)} failed.')
