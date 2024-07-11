import os
import random
import torch
import numpy as np
from torch.autograd import Variable
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


seed_everything(42)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def test_image(image_path, checkpoint_model, save_path):
    os.makedirs(os.path.join(save_path, "results"), exist_ok=True)
    transform = test_transform()

    transformer = TransformerNet().to(device)
    transformer.load_state_dict(torch.load(checkpoint_model))
    transformer.eval()

    image_tensor = Variable(transform(Image.open(image_path))).to(device)
    image_tensor = image_tensor.unsqueeze(0)

    with torch.no_grad():
        stylized_image = denormalize(transformer(image_tensor)).cpu()

    fn = checkpoint_model.split('/')[-1].split('.')[0]
    output_image_path = os.path.join(save_path, f"results/{fn}-output.jpg")
    save_image(stylized_image, output_image_path)
    return output_image_path
