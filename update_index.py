import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern: match each <a class="tool-row" ...>...</a> block
def simplify_card(m):
    full = m.group(0)
    
    # Extract the <a> opening tag attributes
    a_open = re.search(r'<a class="tool-row"(.*?)>', full, re.DOTALL).group(1)
    
    # Extract SVG from inside .icon
    svg_match = re.search(r'<div class="icon">(<svg.*?</svg>)</div>', full, re.DOTALL)
    svg = svg_match.group(1) if svg_match else ''
    
    # Extract tag text
    tag_match = re.search(r'<div class="tag">(.*?)</div>', full)
    tag = tag_match.group(1) if tag_match else ''
    
    # Extract title
    title_match = re.search(r'<h3 class="tool-title">(.*?)</h3>', full)
    title = title_match.group(1) if title_match else ''
    
    # Extract description
    desc_match = re.search(r'<p class="tool-desc">(.*?)</p>', full)
    desc = desc_match.group(1) if desc_match else ''
    
    return f'''<a class="tool-row"{a_open}>
          <div class="icon">{svg}</div>
          <div class="info">
            <h3>{title}</h3>
            <p>{desc}</p>
          </div>
        </a>'''

new_html = re.sub(r'<a class="tool-row"[^>]*>.*?</a>', simplify_card, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

# Count cards
count = len(re.findall(r'<a class="tool-row"', new_html))
print(f'Done. {count} tool cards simplified.')
