import torch
from torch.autograd import Variable
import numpy as np
import os
import random
from PIL import Image
from torchvision.utils import save_image
from models import TransformerNet
from utils import test_transform, denormalize


def seed_everything(seed):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = True


seed_everything(42)  # for reproducibility
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def test_image(image_path, checkpoint_model, save_path):
    os.makedirs(os.path.join(save_path, "results"), exist_ok=True)
    transform = test_transform()

    # Define model and load model checkpoint
    transformer = TransformerNet().to(device)
    transformer.load_state_dict(torch.load(checkpoint_model, map_location=torch.device('cpu')))
    transformer.eval()

    # Prepare input
    image_tensor = Variable(transform(Image.open(image_path))).to(device)
    image_tensor = image_tensor.unsqueeze(0)

    # Stylize image
    with torch.no_grad():
        stylized_image = denormalize(transformer(image_tensor)).cpu()

    # Save image
    fn = os.path.splitext(os.path.basename(checkpoint_model))[0]
    output_image_path = os.path.join(save_path, f"results/{fn}-output.jpg")
    save_image(stylized_image, output_image_path)

    return output_image_path
