from models.gpt3 import GPT3

def test_generate_text():
    gpt3 = GPT3()
    prompt = "Once upon a time"
    text = gpt3.generate_text(prompt)
    assert text is not None
