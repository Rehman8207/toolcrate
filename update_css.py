import re

with open('assets/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .tool-row styles with .tool-card styles
tool_card_css = """
/* ============ TOOL CARDS ============ */
.tool-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 24px;
  transition: all 0.2s ease;
  text-decoration: none;
  color: inherit;
  display: flex;
  align-items: flex-start;
  gap: 20px;
  animation: fadeUp 0.35s ease both;
  position: relative;
  overflow: hidden;
}

@keyframes fadeUp {
  from { opacity: 0.8; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

.tool-card:hover {
  border-color: var(--border-strong);
  background: var(--surface-2);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.tool-card .tool-icon {
  width: 56px;
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: 14px;
  color: var(--accent);
  flex-shrink: 0;
  transition: all 0.2s;
}

.tool-card:hover .tool-icon {
  background: var(--grad-primary);
  border-color: transparent;
  color: #fff;
  transform: scale(1.05);
}

.tool-card .tool-icon svg {
  width: 28px;
  height: 28px;
}

.tool-text {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 6px;
}

.tool-title {
  font-family: var(--font-display);
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--ink);
  line-height: 1.3;
  letter-spacing: -0.01em;
  margin: 0;
}

.tool-desc {
  font-size: 0.9rem;
  color: var(--ink-2);
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  margin: 0;
}

/* Mobile: Vertical Card Layout */
@media (max-width: 768px) {
  .tool-card {
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 24px 20px;
    gap: 16px;
  }
  
  .tool-text {
    align-items: center;
  }
  
  .tool-title {
    font-size: 1.25rem;
  }
}
"""

css = re.sub(r'/\* Tool Row / Card \*/.*?\.empty-note', tool_card_css + '\n.empty-note', css, flags=re.DOTALL)
# Make sure .tool-list uses grid properly
css = re.sub(r'\.tool-list \{\n  display: grid;\n  grid-template-columns: repeat\(auto-fill, minmax\(340px, 1fr\)\);\n  gap: 14px;\n  margin-top: 8px;\n\}',
             '.tool-list {\n  display: grid;\n  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));\n  gap: 20px;\n  margin-top: 8px;\n}', css)

with open('assets/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated style.css')
