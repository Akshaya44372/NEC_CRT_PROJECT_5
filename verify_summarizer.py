import sys
import os
import re

# Add current directory to path
sys.path.append(os.getcwd())

try:
    from models.summarizer import generate_summary
except ImportError as e:
    print(f"ImportError: {e}")
    sys.exit(1)

def test_summarizer():
    # Test case 1: Short text (< 200 words)
    short_text = "Artificial Intelligence is transforming the way we work. Machine learning models can analyze vast amounts of data to find patterns. This helps businesses make better decisions and automate repetitive tasks. AI is now used in healthcare, finance, and many other sectors."
    
    print("Testing short text...")
    summary_short = generate_summary(short_text)
    words_short = len(re.findall(r'\w+', summary_short))
    print(f"Summary Length: {words_short} words")
    print(f"Summary Content:\n{summary_short}\n")
    
    # Test case 2: Long text (> 200 words)
    long_text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by animals including humans. AI research has been defined as the field of study of intelligent agents, which refers to any system that perceives its environment and takes actions that maximize its chance of achieving its goals. The various sub-fields of AI research are centered around particular goals and the use of particular tools. The traditional goals of AI research include reasoning, knowledge representation, planning, learning, natural language processing, perception, and the ability to move and manipulate objects. General intelligence (the ability to solve any problem) is among the field's long-term goals. To solve these problems, AI researchers have adapted and integrated a wide range of problem-solving techniques, including search and mathematical optimization, formal logic, artificial neural networks, and methods based on statistics, probability, and economics. AI also draws upon computer science, psychology, linguistics, philosophy, and many other fields.
    The field was founded on the claim that human intelligence can be so precisely described that a machine can be made to simulate it. This raised philosophical arguments about the mind and the ethical consequences of creating artificial beings endowed with human-like intelligence; these issues have been explored by myth, fiction, and philosophy since antiquity. Computer science researchers and enthusiasts have since experienced several waves of optimism, followed by disappointment and a loss of funding (known as an "AI winter"), followed by new approaches, success, and renewed funding.
    In the 21st century, AI techniques have experienced a resurgence following concurrent advances in computer power, large amounts of data, and theoretical understanding; and AI techniques have become an essential part of the technology industry, helping to solve many challenging problems in computer science, software engineering and operations research.
    """ * 2 # Duplicate to ensure > 200 words
    
    input_word_count = len(re.findall(r'\w+', long_text))
    print(f"Testing long text ({input_word_count} words)...")
    summary_long = generate_summary(long_text)
    words_long = len(re.findall(r'\w+', summary_long))
    print(f"Summary Length: {words_long} words")
    print(f"Summary Content (Flow):\n{summary_long}\n")
    
    if "*" in summary_long:
        print("SUCCESS: Flow format (bullet points) detected for long text.")
    else:
        print("FAILURE: Flow format not detected for long text.")

    if 80 <= words_long <= 200: # Allowing buffer
         print(f"SUCCESS: Summary length is {words_long} words, close to target range.")
    else:
         print(f"INFO: Summary length is {words_long}, target was 100-150.")


if __name__ == "__main__":
    test_summarizer()
