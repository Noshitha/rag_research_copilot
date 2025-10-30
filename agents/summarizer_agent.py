# agents/summarizer_agent.py
from transformers import pipeline

# Load a local summarization pipeline 
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str) -> str:
    """
    Summarizes a research abstract using a local Hugging Face model.
    """
    summary = summarizer(
        text,
        max_length=130,  
        min_length=30,
        do_sample=False
    )[0]["summary_text"]
    return summary

if __name__ == "__main__":
    sample_text = """
    Large language models (LLMs) like GPT-4 have revolutionized NLP,
    but deployment on resource-constrained devices remains challenging.
    This paper studies pruning, quantization, and distillation for efficient on-device models.
    """
    print(summarize_text(sample_text))
