from django.shortcuts import render
from googletrans import Translator

def home(request):
    translated_text = None
    original_text = None
    selected_language = None

    if request.method == "POST":
        original_text = request.POST.get("translate")
        selected_language = request.POST.get("language")

        try:
            translator = Translator()
            result = translator.translate(original_text, dest=selected_language)
            translated_text = result.text
        except Exception as e:
            translated_text = "Translation failed! Please try again."

    return render(request, "index.html", {
        "original_text": original_text,
        "translated_text": translated_text,
        "selected_language": selected_language,
    })
