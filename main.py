import torch.cuda
from torch.optim.adam import Adam
from torch.utils.data import DataLoader

from model import BaseModel
from dataset import AiDiagnostic
from metrics_dice import DiceCoef
from train import whole_train_valid_cycle

if __name__ == "__main__":
    batch_size = 64
    epochs = 10

    model = BaseModel()
    optimizer = Adam(model.parameters(), lr=1e-3)
    loss_fn = DiceCoef()
    device = "cuda" if torch.cuda.is_available() else "cpu"

    dataset_train = AiDiagnostic(path_data='.', split='train')
    dataset_valid = AiDiagnostic(path_data='.', split='valid')

    train_loader = DataLoader(dataset=dataset_train, batch_size=batch_size)
    valid_loader = DataLoader(dataset=dataset_valid, batch_size=batch_size)

    whole_train_valid_cycle(model=model,
                            optimizer=optimizer,
                            train_loader=train_loader,
                            valid_loader=valid_loader,
                            loss_fn=loss_fn,
                            device=device,
                            verbose=1,
                            epochs=epochs
                            )
