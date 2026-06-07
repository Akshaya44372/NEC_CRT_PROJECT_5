from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="t5-small"
)

import re

def generate_summary(text):
    if not text.strip():
        return ""

    # Count words
    words = re.findall(r'\w+', text)
    word_count = len(words)
    
    # Target values based on input size
    if word_count <= 50:
        # Too short to summarize meaningfully with T5-small without hallucination
        return text

    if word_count <= 200:
        # Short summary for medium text
        min_tokens = 30
        max_tokens = 80
    else:
        # 100-150 word summary for 200+ words
        # T5-small tokens are roughly 0.75 words, so 100 words ~ 130 tokens
        min_tokens = 130
        max_tokens = 200
    
    try:
        result = summarizer(
            text,
            max_length=max_tokens,
            min_length=min_tokens,
            do_sample=False,
            truncation=True
        )
        summary = result[0]["summary_text"]
        
        # Format as flow if it's a long summary
        if word_count > 200:
            sentences = summary.split('. ')
            if len(sentences) > 2:
                flow_summary = "\n* " + "\n* ".join([s.strip() + "." for s in sentences if s.strip() and not s.strip().endswith('.')])
                return flow_summary.replace("..", ".")
        
        return summary
    except Exception as e:
        return f"Error during summarization: {str(e)}"