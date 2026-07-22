import torch.nn as nn


class BlobsMLP(nn.Module):
    """Predict an x0 or score target from noisy blob coordinates."""

    def __init__(self, config):
        super().__init__()
        self.hidden_layers = nn.ModuleList()

        # First hidden block: dataset_features -> internal_neurons.
        self.hidden_layers.append(
            nn.Linear(config.dataset_features, config.internal_neurons)
        )

        # Subsequent hidden blocks: internal_neurons -> internal_neurons.
        for _ in range(config.mlp_blocks - 1):
            self.hidden_layers.append(
                nn.Linear(config.internal_neurons, config.internal_neurons)
            )

        self.activation = nn.ReLU()

        # Linear output preserves unrestricted regression values.
        self.output_layer = nn.Linear(
            config.internal_neurons, config.dataset_features
        )

    def forward(self, features):
        for layer in self.hidden_layers:
            features = layer(features)
            features = self.activation(features)

        features = self.output_layer(features)
        return features
