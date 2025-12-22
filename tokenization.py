from transformers import AutoTokenizer

model_name = "unsloth/Nemotron-3-Nano-30B-A3B-GGUF"
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "The quick brown fox jumps over the lazy dog!"

encoded_text = tokenizer(text)

print(tokenizer.decode(encoded_text["input_ids"]))

print(encoded_text["input_ids"])
print(", ".join([tokenizer.decode(t) for t in encoded_text[input_ids"]]))


