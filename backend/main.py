from fastapi import FastAPI, File, UploadFile
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch

app = FastAPI()

# Load ViT model
processor = AutoImageProcessor.from_pretrained("google/vit-base-patch16-224")
model = AutoModelForImageClassification.from_pretrained("google/vit-base-patch16-224")

@app.get("/")
def root():
    return {"message": "Backend with ViT ready!"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_idx = logits.argmax(-1).item()
        label = model.config.id2label[predicted_class_idx]
    return {"prediction": label}
