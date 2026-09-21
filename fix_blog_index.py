#!/usr/bin/env python3
"""
Add Roman Urdu / Pakistani keyword sections to existing blog posts.
No new blog posts created. Only appends a section before </article>.
Updates FAQPage schema if present.
"""
from pathlib import Path
import re

ROOT = Path.cwd()
BLOG = ROOT / "blog"

# ============================================================
# Urdu sections per blog post
# ============================================================
URDU_SECTIONS = {
    "compress-image-for-whatsapp.html": {
        "title": "Roman Urdu Guide — Pakistani Users Ke Liye",
        "intro": "Pakistan mein WhatsApp sab se zyada use hota hai. Yeh guide Urdu mein samjhati hai ke image ka size kaise kam karein.",
        "faqs": [
            ("WhatsApp ke liye picture ka size kam kaise kare?",
             "ToolCrate ka Image Compressor kholo, apni picture drag karo, quality slider ko 70% pe rakho, aur download karo. Picture ka size 80% tak kam ho jayega without quality loss."),
            ("Photo chhoti kaise kare WhatsApp pe bhejne ke liye?",
             "WhatsApp 16MB se bade files accept nahi karta. Agar aapki photo 5MB ki hai to pehle compress karo — direct ToolCrate tool mein drag karo aur 500KB-1MB tak laao."),
            ("Kya image compress karne se quality kharab hoti hai?",
             "Nahi. Agar sahi tarike se karo (70-80% quality pe) to aapko farq nahi pata chalega. Bas original se ek hi baar compress karo, dobara nahi."),
            ("Kya ye tool mobile pe kaam karta hai?",
             "Bilkul. ToolCrate mobile aur desktop dono pe kaam karta hai. Sirf browser kholo aur tool use karo."),
        ],
    },

    "compress-jpg-to-100kb.html": {
        "title": "Roman Urdu Guide — Job Application Ke Liye Photo",
        "intro": "Pakistan mein har online job application ke liye 20KB-100KB ki photo chahiye hoti hai. Yeh guide batati hai kaise.",
        "faqs": [
            ("JPG ko 100KB mein kaise kare?",
             "ToolCrate Image Compressor kholo, JPG file drag karo, quality slider ko neeche karo jab tak size 100KB se kam ho jaye. Download karo aur apply karo."),
            ("Photo 100KB mein kaise karein bina quality kharab kiye?",
             "Quality 60-70% pe rakhо, size 100KB se kam ho jayega, aur photo saaf dikhegi. Zaroorat se zyada compress mat karo."),
            ("Job application ke liye photo ka size kya hona chahiye?",
             "Zyada tar Pakistani job portals (NJP, PPSC, FPSC) 20KB-100KB ki photo maangte hain. Signature 10KB-20KB. ToolCrate se exact size banao."),
            ("Kya ye tool free hai?",
             "Haan, 100% free. Koi signup nahi, koi limit nahi, koi ad nahi."),
        ],
    },

    "merge-pdf-free-online.html": {
        "title": "Roman Urdu Guide — PDF Merge Karne Ka Tarika",
        "intro": "Documents ko ek PDF mein jodna bahut asaan hai. Yeh guide Urdu mein samjhati hai.",
        "faqs": [
            ("PDF merge kaise karein?",
             "ToolCrate PDF Merger kholo, saari PDF files drag karo, agar order badalna ho to pages ko drag karke reorder karo, phir Merge PDFs button dabao. Download ho jayega."),
            ("Do PDF ko ek kaise banaye?",
             "PDF Merger tool mein dono files daalo, automatic merge ho jayengi. Agar reverse order chahiye to pages drag karke adjust karo."),
            ("PDF jodne ka tarika kya hai?",
             "Pakistan mein sab log Adobe ya online tools use karte hain. ToolCrate free hai, signup nahi chahiye, aur files browser se bahar nahi jaati — 100% private."),
            ("Kya PDF merge karne ke liye Adobe chahiye?",
             "Nahi. ToolCrate browser mein hi kaam karta hai. Na Adobe, na koi software install. Bas webpage kholo aur merge karo."),
        ],
    },

    "cgpa-calculator-pakistan.html": {
        "title": "Roman Urdu Guide — CGPA Kaise Nikale",
        "intro": "Pakistan ki har university mein 4.0 GPA scale hoti hai. Yeh guide Urdu mein samjhati hai CGPA aur GPA kaise nikalein.",
        "faqs": [
            ("CGPA kaise nikale?",
             "ToolCrate CGPA Calculator kholo, apne result card se grades aur credit hours daalo, aur semester GPA ya CGPA nikal lo. Bilkul free aur instant."),
            ("CGPA se percentage kaise nikale?",
             "Aam tor pe formula yeh hai: Percentage = (CGPA - 0.75) × 10. Lekin har university ka formula thoda different hota hai. ToolCrate ka tool university-specific calculation karta hai."),
            ("GPA kaise calculate karein?",
             "Har course ka grade point × credit hours = quality points. Sab quality points jama karo, total credit hours se divide karo — GPA mil jayega. ToolCrate yeh automatic karta hai."),
            ("Kya NUST/FAST/LUMS ka alag formula hai?",
             "Sab 4.0 scale follow karte hain, lekin aggregate formula (75% academics + 25% entry test) different ho sakta hai. CGPA calculation same hoti hai — ToolCrate sab ke liye kaam karta hai."),
        ],
    },

    "qr-code-wifi-password.html": {
        "title": "Roman Urdu Guide — WiFi Ka QR Code Kaise Banaye",
        "intro": "Mehmaan aate hain to WiFi password batana mushkil hota hai. Ek QR code banao, sab khud connect ho jayenge. Yeh guide Urdu mein.",
        "faqs": [
            ("WiFi ka QR code kaise banaye?",
             "ToolCrate QR Generator kholo, yeh format paste karo: WIFI:T:WPA;S:ApKaWiFiName;P:ApKaPassword;; — QR code turant ban jayega. Print karke fridge pe laga do."),
            ("QR code kaise scan karein?",
             "Phone ka camera kholo, QR code ki taraf point karo. 2-3 second mein connection ka option aayega. Android aur iPhone dono mein kaam karta hai."),
            ("Kya QR code expire ho jata hai?",
             "Nahi. Static QR code hai, kabhi expire nahi hoga. Aap WiFi password change karo to naya QR banao."),
            ("Kya mera WiFi password save hota hai kahin?",
             "Nahi. ToolCrate locally QR code banata hai. Kuch bhi upload nahi hota."),
        ],
    },
}

# ============================================================
# Process each blog post
# ============================================================
print("=" * 70)
print("Adding Roman Urdu sections to blog posts")
print("=" * 70)
print()

updated = 0
skipped = 0

for fname, data in URDU_SECTIONS.items():
    fp = BLOG / fname
    if not fp.exists():
        print(f"   SKIP {fname} — not found")
        skipped += 1
        continue

    text = fp.read_text(encoding="utf-8")
    original = text

    # Skip if already has Roman Urdu section
    if "Roman Urdu Guide" in text:
        print(f"   SKIP {fname} — Roman Urdu section already exists")
        skipped += 1
        continue

    # Build FAQ HTML
    faq_html = "\n".join([
        f'<h3>{q}</h3>\n<p>{a}</p>'
        for q, a in data["faqs"]
    ])

    urdu_section = f'''
<h2>{data["title"]}</h2>
<p>{data["intro"]}</p>
{faq_html}
'''

    # Insert BEFORE the .related section (or before </article>)
    related_pos = text.find('<div class="related">')
    if related_pos == -1:
        related_pos = text.find('</article>')

    if related_pos == -1:
        print(f"   ERROR {fname} — could not find insertion point")
        skipped += 1
        continue

    text = text[:related_pos] + urdu_section + "\n" + text[related_pos:]

    # Also append these to schema (find FAQPage or Article schema)
    # We'll add FAQPage schema after the existing Article schema
    faq_schema_items = ",\n".join([
        f'''    {{
      "@type": "Question",
      "name": "{q.replace('"', '\\"')}",
      "acceptedAnswer": {{"@type": "Answer", "text": "{a.replace('"', '\\"')}"}}
    }}'''
        for q, a in data["faqs"]
    ])

    faq_schema = f'''
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
{faq_schema_items}
  ]
}}
</script>
'''

    # Insert schema before </head>
    if "</head>" in text and "FAQPage" not in text.split("</head>")[0][-2000:]:
        text = text.replace("</head>", faq_schema + "</head>", 1)

    if text != original:
        fp.write_text(text, encoding="utf-8")
        print(f"   OK   {fname}")
        print(f"        + Roman Urdu section ({len(data['faqs'])} FAQs)")
        print(f"        + FAQPage schema")
        updated += 1

print()
print("=" * 70)
print(f"DONE! {updated} updated, {skipped} skipped")
print("=" * 70)
print()
print("Verify:")
print("  python -m http.server 8000")
print("  Open: http://localhost:8000/blog/")
print("  Click any post → scroll down → Roman Urdu section should appear")
print()
print("Push after verifying:")
print("  git add .")
print("  git commit -m 'Add Roman Urdu keyword sections to blog posts'")
print("  git push")
print()
input("Press Enter to close...")