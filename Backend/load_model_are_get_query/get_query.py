import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration


def load_model_and_tokenizer():
    tokenizer = T5Tokenizer.from_pretrained(
        './model_and_tokenizer/tokenizer-final')
    model = T5ForConditionalGeneration.from_pretrained(
        './model_and_tokenizer/model-final')
    return tokenizer, model


def model_in_evaluation_mode(model, device):
    model.to(device)
    model.eval()
    return model


def generate_sql(tokenizer, model, device, input_prompt):
    inputs = tokenizer(input_prompt, padding=True,
                       truncation=True, return_tensors="pt").to(device)

    # Forward pass
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=512)

    # Decode the output IDs to a string (SQL query in this case)
    generated_sql = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return generated_sql


def generate_query(prompt):
    tokenizer, model = load_model_and_tokenizer()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = model_in_evaluation_mode(model, device)

    generated_sql = generate_sql(tokenizer, model, device, prompt)

    return generated_sql


# This is only to test this script individually
if __name__ == '__main__':
    prompt = "tables:\ntable1: column1 TEXT, column2 TEXT, column3 TEXT\ntable2: column1 TEXT, column2 TEXT, column3 TEXT\nquery for: What is the name of the person with id 1?"
    query = generate_query(prompt)
    print(query)
