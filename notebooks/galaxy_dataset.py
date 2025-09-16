from torch.utils.data import Dataset
from sklearn.preprocessing import LabelEncoder
import os
import torchvision.io as tvio
import torch


class GalaxyDataset(Dataset):
    def __init__(self, df, image_dir, transform=None):
        self.df = df
        self.image_dir = image_dir
        self.transform = transform

        # Encode class labels to integers
        self.label_encoder = LabelEncoder()
        self.labels = self.label_encoder.fit_transform(self.df["class"])

    def __getitem__(self, idx):
        objid = self.df.iloc[idx]["objid"]
        image_path = os.path.join(self.image_dir, f"{objid}.jpeg")

        try:
            # Native torchvision loading
            encoded_image_bytes = tvio.read_file(image_path)
            image = tvio.decode_jpeg(encoded_image_bytes, mode=tvio.ImageReadMode.RGB)
            image = image.float() / 255.0  # Convert to [0,1] range
        except Exception as e:
            print(f"Error loading image {image_path}: {e}")
            # Return a black image as fallback
            image = torch.zeros(3, 224, 224, dtype=torch.float32)

        label = self.labels[idx]
        return image, label
