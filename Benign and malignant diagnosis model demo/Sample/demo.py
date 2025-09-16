from model import TumorTransformer3D
import torch
import torch.nn.functional as F
import os
import numpy as np
from model import TumorTransformer3D

# read npz dataset
def load_npz_data(npz_path):
    if not os.path.exists(npz_path):
        raise FileNotFoundError(f"The preprocessor file {npz_path} does not exist!")

    data = np.load(npz_path)
    img_combined = torch.tensor(data["img_combined"], dtype=torch.float32)

    return img_combined.unsqueeze(0)

# loead model
def load_model(model_path, device):
    model = TumorTransformer3D().to(device)  # use import model
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    return model

# predict
def predict(model, npz_path, device):
    img_combined = load_npz_data(npz_path)

    with torch.no_grad():
        outputs = model(img_combined.to(device))
        probabilities = F.softmax(outputs, dim=1)
        max_prob, predicted_class = torch.max(probabilities, 1)

    return predicted_class.item(), max_prob.item()

# main function
def main(model_path, data_dir):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = load_model(model_path, device)

    for npz_file in os.listdir(data_dir):
        if npz_file.endswith('.npz'):
            npz_path = os.path.join(data_dir, npz_file)
            predicted_class, confidence = predict(model, npz_path, device)
            print(f"Prediction for {npz_file}: {'Malignant' if predicted_class == 1 else 'Benign'} with confidence {confidence:.4f}")

# run predict
if __name__ == "__main__":
    model_path = "../model/modelfile.pth"
    data_dir = "../dataset"
    main(model_path, data_dir)

