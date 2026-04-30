import fitz

doc = fitz.open('/Users/ncai/dev/HechangPu/红河谷简谱.pdf')
for pageno, page in enumerate(doc):
    blocks = page.get_text("dict")["blocks"]
    print(f"--- PAGE {pageno} ---")
    for b in blocks:
        if "lines" in b:
            for l in b["lines"]:
                for s in l["spans"]:
                    # print some samples
                    text = s["text"]
                    if text.strip():
                        print(f"[{s['bbox'][0]:.1f}, {s['bbox'][1]:.1f}] Font:{s['font']} Size:{s['size']:.1f} Text: '{text}'")
