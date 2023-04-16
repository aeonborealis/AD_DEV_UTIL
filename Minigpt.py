import torch
import torch.nn as nn
import torch.nn.functional as F

class MiniGPT(nn.Module):
    def __init__(self, vocab_size, emb_size, n_head, n_layer):
        super().__init__()
        self.emb_size = emb_size
        self.embed = nn.Embedding(vocab_size, emb_size)
        self.pos_encoder = PositionalEncoding(emb_size, dropout=0.1)
        self.layers = nn.ModuleList([TransformerBlock(emb_size, n_head) for _ in range(n_layer)])
        self.decoder = nn.Linear(emb_size, vocab_size)
        
    def forward(self, src):
        seq_len = src.size(1)
        position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(0).repeat(src.size(0), 1).to(src.device)
        src = self.embed(src) * torch.sqrt(self.emb_size)
        src = self.pos_encoder(src)
        for layer in self.layers:
            src = layer(src)
        src = self.decoder(src)
        return F.log_softmax(src, dim=-1)

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, dropout=0.1, max_len=5000):
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0).transpose(0, 1)
        self.register_buffer('pe', pe)

    def forward(self, x):
        x = x + self.pe[:x.size(0), :]
        return self.dropout(x)

class TransformerBlock(nn.Module):
    def __init__(self, emb_size, n_head):
        super().__init__()
        self.self_attn = nn.MultiheadAttention(emb_size, n_head)
        self.layer_norm1 = nn.LayerNorm(emb_size)
        self.dropout1 = nn.Dropout(0.1)
        self.ffn = nn.Sequential(
            nn.Linear(emb_size, 4 * emb_size),
            nn.ReLU(),
            nn.Linear(4 * emb_size, emb_size),
        )
        self.layer_norm2 = nn.LayerNorm(emb_size)
        self.dropout2 = nn.Dropout(0.1)
        
    def forward(self, src):
        src2, _ = self.self_attn(src, src, src)
        src = src + self.dropout1(self.layer_norm1(src2))
        src2 = self.ffn(src)
        src = src + self.dropout2(self.layer_norm2(src2))
        return src
