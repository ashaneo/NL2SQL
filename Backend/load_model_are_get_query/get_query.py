import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained('C:/Users/DELL/Desktop/Text2SQL/NL2SQL/Backend/model_and_tokenizer/tokenizer-final')
model = T5ForConditionalGeneration.from_pretrained('C:/Users/DELL/Desktop/Text2SQL/NL2SQL/Backend/model_and_tokenizer/model-final')
