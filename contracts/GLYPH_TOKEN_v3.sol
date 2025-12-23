// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

/// @title GLYPH_TOKEN_v3
/// @notice Bu sezonun ana ekonomi token'ı (ψ-Glif ekosistemi için)
contract GLYPH_TOKEN_v3 is ERC20 {
    constructor() ERC20("GLYPH_TOKEN", "GLYPH") {
        // Toplam arz: 1,000,000 GLYPH (18 decimal)
        _mint(msg.sender, 1_000_000 * 10 ** decimals());
    }
}
