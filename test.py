from app.ai4bharat.transliteration import XlitEngine
# from ai4bharat.transliteration import XlitEngine

e = XlitEngine(src_script_type="indic", beam_width=10, rescore=False,
               models_path="./model")
out = e.translit_sentence("नमस्ते सचिन", lang_code="ne")
print(out)
t = "परशुराम"
out = e.translit_sentence(t, lang_code="ne")
print(out)

out = e.translit_sentence("12244 ae", lang_code="ne")
print(out)
