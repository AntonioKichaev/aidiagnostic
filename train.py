import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torch.optim import Optimizer
import os


def train(model: nn.Module,
          loader: DataLoader,
          optimizer: Optimizer,
          loss_fn: torch.nn.Module,
          device: torch.device = "cpu"
          ) -> float:
    """
    train one epoch
    return train loss
    """
    model.train()
    model = model.to(device)
    train_loss = 0

    for x, y in loader:
        x, y = x.to(device), y.to(device)

        optimizer.zero_grad()
        output = model(x)

        loss = loss_fn(output, y)
        train_loss += loss.item()

        loss.backward()
        optimizer.step()

    return train_loss / len(loader)


@torch.inference_mode()
def evaluate(model: nn.Module,
             loss_fn: torch.nn.Module,
             loader: DataLoader,

             device: torch.device = "cpu"):
    model.eval()
    loss = 0
    for x, y in loader:
        x, y = x.to(device), y.to(device)
        output = model(x)
        loss = loss_fn(output, y)

    return loss / len(loader)


def whole_train_valid_cycle(model: nn.Module,
                            optimizer: Optimizer,
                            train_loader: DataLoader,
                            valid_loader: DataLoader,
                            loss_fn: nn.Module,
                            device: torch.device = "cpu",
                            verbose: int = 3,
                            epochs: int = 5):
    train_history_loss = []
    valid_history_loss = []

    best_loss = 1

    for i in range(1, epochs + 1):

        train_loss = train(model=model,
                           optimizer=optimizer,
                           loader=train_loader,
                           loss_fn=loss_fn,
                           device=device)

        valid_loss = evaluate(model=model,
                              loss_fn=loss_fn,
                              loader=valid_loader,
                              device=device)
        train_history_loss.append(train_loss)
        valid_history_loss.append(valid_loss)

        current_loss = valid_loss

        if current_loss < best_loss:
            best_loss = current_loss
            torch.save(model.state_dict(), os.path.join('output', f'best_model_{i}_{best_loss}'))

        if epochs % verbose == 0:
            print(f"epoch {i} loss {current_loss:.5f}")

    print(f"best loss {best_loss:.5f}")

