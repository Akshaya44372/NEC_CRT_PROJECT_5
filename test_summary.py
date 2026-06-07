from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

text = """
Artificial Intelligence is transforming businesses worldwide.
Companies use machine learning to automate tasks and improve efficiency.
Healthcare, finance, and manufacturing sectors are rapidly adopting AI.
"""

result = summarizer(
    text,
    max_length=50,
    min_length=20,
    do_sample=False
)

print(result)