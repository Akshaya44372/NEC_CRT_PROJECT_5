from flask import Flask, render_template, request
from models.summarizer import generate_summary

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    text = ""
    summary = ""

    if request.method == "POST":
        try:
            text = request.form.get("paragraph", "")
            print(f"DEBUG: Processing text with {len(text.split())} words...")
            
            summary = generate_summary(text)
            print(f"DEBUG: Generated summary with {len(summary.split())} words.")
        except Exception as e:
            print(f"CRITICAL ERROR: {str(e)}")
            summary = f"An unexpected error occurred: {str(e)}"

    return render_template(
        "index.html",
        text=text,
        summary=summary
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)