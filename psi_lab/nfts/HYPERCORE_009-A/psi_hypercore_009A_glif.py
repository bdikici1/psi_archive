# psi_lab/nfts/HYPERCORE_009-A/psi_hypercore_009A_glif.py

ascii_art = r"""
          ╭────────────╮
          │ ψ HYPERCORE│
╭─────────┤   009-A    ├─────────╮
│                 │
│              │██│              │
│              │██│              │
│          ╭───┴──┴───╮          │
│          │◉  Ψ  ◉ │          │
│          ╰──────────╯          │
│     Recursive Energy Node      │
╰────────────────────────────────╯
"""

glif_metadata = {
    "id": "ψ_GLYPH_VIZ::HYPERCORE_009-A",
    "ascii": ascii_art,
    "type": "hypernode",
    "function": "Information relay core with recursive entropy shell",
    "encoding_level": 4,
    "entropy_signature": "α ≈ 0.88",
    "temporal_metric": "~1.12",
    "origin": "Generated via MetaRealistic Prompt v4.0",
    "linked_nodes": [
        "ψ_TRACE_LINE_001",
        "ψ_CORE_POD.ROOT"
    ],
    "glyph_token_price_gt": 130,
    "generation_time": "2025-07-23T23:15:00Z"
}


def print_glif(metadata: dict = glif_metadata) -> None:
    """Print the ASCII glyph and key metadata to terminal."""
    print(metadata["ascii"])
    print()
    print(f":: {metadata['id']} | Type: {metadata['type']}")
    print(f"↳ Function      : {metadata['function']}")
    print(f"↳ Entropy       : {metadata['entropy_signature']}")
    print(f"↳ Temporal metric: {metadata['temporal_metric']}")
    print(f"↳ Token (model) : {metadata['glyph_token_price_gt']} GT")
    print(f"↳ Origin        : {metadata['origin']}")
    print(f"↳ Linked Nodes  : {', '.join(metadata['linked_nodes'])}")


if __name__ == "__main__":
    print_glif()
