from flask import Flask, request, jsonify, render_template, send_from_directory, abort
from groq import Groq
from gtts import gTTS
from pypdf import PdfReader
import os
import uuid

app = Flask(__name__)

@app.route('/download/<path:filename>')
def download_file(filename):
    allowed_files = {
        'AI Legal Summarizer Report.pdf',
        'AI Legal Summarizer Ppt.pptx'
    }
    if filename not in allowed_files:
        abort(404)
    return send_from_directory('docs', filename, as_attachment=True)

# API KEY (store your key in .env)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# TEXT EXTRACTION (PDF + TXT FIXED)
def extract_text(file):
    try:
        if file.filename.lower().endswith(".pdf"):
            reader = PdfReader(file)
            text = ""

            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

            return text

        else:
            return file.read().decode("utf-8", errors="ignore")

    except Exception as e:
        print("PDF ERROR:", e)
        return ""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        print("--- NEW REQUEST ---")

        if "file" not in request.files:
            print("ERROR: No file in request")
            return jsonify({"error": "No file uploaded"})

        file = request.files["file"]
        print(f"File received: {file.filename}")
        
        text = extract_text(file)
        print(f"Extracted text length: {len(text)}")

        if not text.strip():
            print("ERROR: No text found")
            return jsonify({"error": "No text found in PDF / file"})

        # 🤖 AI CALL
        print("Calling Groq AI...")
        response = client.chat.completions.create(
            messages=[{
                "role": "system",
                "content": "You are a professional legal assistant. For the provided legal document, generate a Summary, Key Points, and 3 Multiple Choice Questions (MCQs) in both English and Urdu. Use the marker 'ENGLISH:' for the English section and 'URDU:' for the Urdu section. In each section, use sub-headers like 'Summary:', 'Key Points:', and 'MCQs:'."
            }, {
                "role": "user",
                "content": f"Document content:\n{text[:10000]}" # Limit text to avoid token limits
            }],
            model="llama-3.1-8b-instant"
        )
        print("AI Response received.")

        result = response.choices[0].message.content
        
        # Parse summaries
        en_summary = ""
        ur_summary = ""
        
        if "URDU:" in result:
            parts = result.split("URDU:")
            en_summary = parts[0].replace("ENGLISH:", "").strip()
            ur_summary = parts[1].strip()
        else:
            print("Warning: URDU: marker not found in AI response")
            en_summary = result
            ur_summary = "Urdu summary generation failed or marker missing."

        # 🔊 VOICE GENERATION
        print("Generating audio files...")
        en_audio_filename = f"en_{uuid.uuid4().hex}.mp3"
        ur_audio_filename = f"ur_{uuid.uuid4().hex}.mp3"
        
        en_audio_path = os.path.join("static", en_audio_filename)
        ur_audio_path = os.path.join("static", ur_audio_filename)

        try:
            # English TTS
            tts_en = gTTS(en_summary[:1000], lang="en") # Limit TTS length for speed
            tts_en.save(en_audio_path)
            print("English audio saved.")
            
            # Urdu TTS
            tts_ur = gTTS(ur_summary[:1000], lang="ur")
            tts_ur.save(ur_audio_path)
            print("Urdu audio saved.")
        except Exception as tts_e:
            print(f"TTS Error: {tts_e}")
            # Continue even if TTS fails
            en_audio_filename = ""
            ur_audio_filename = ""

        print("Request successful.")
        return jsonify({
            "en_summary": en_summary,
            "ur_summary": ur_summary,
            "en_audio": f"/static/{en_audio_filename}" if en_audio_filename else "",
            "ur_audio": f"/static/{ur_audio_filename}" if ur_audio_filename else ""
        })

    except Exception as e:
        print("CRITICAL ERROR:", e)
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)