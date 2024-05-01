from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import load_dataset
from trl import SFTTrainer, DataCollatorForCompletionOnlyLM
from peft import LoraConfig


dataset = load_dataset("HuggingFaceH4/instruction-dataset", split="test")

model = AutoModelForCausalLM.from_pretrained("distilbert/distilgpt2")
tokenizer = AutoTokenizer.from_pretrained("distilbert/distilgpt2")

def formatting_prompts_func(example):
    output_texts = []
    for i in range(len(example['prompt'])):
        text = f"### Question: {example['prompt'][i]}\n ### Answer: {example['completion'][i]}"
        output_texts.append(text)
    return output_texts

response_template = " ### Answer:"
collator = DataCollatorForCompletionOnlyLM(response_template, tokenizer=tokenizer)

peft_config = LoraConfig(
    lora_alpha=16,
    lora_dropout=0.1,
    r=64,
    bias="none",
    task_type="CAUSAL_LM",
)

model.add_adapter(peft_config)

tokenizer.pad_token = tokenizer.eos_token

trainer = SFTTrainer(
    model,
    train_dataset=dataset,
    formatting_func=formatting_prompts_func,
    data_collator=collator,
)

trainer.train()

save_dir = "distilgpt2-instruct"

model.save_pretrained(save_dir)