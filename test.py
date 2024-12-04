# from app.ai4bharat.transliteration import XlitEngine
from ai4bharat.transliteration import XlitEngine

e = XlitEngine(src_script_type="indic", beam_width=10, rescore=False)
out = e.translit_sentence("नमस्ते सचिन",lang_code="ne")
print(out)