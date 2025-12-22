# ψ_GLYPH_TOKEN — tokenomics_v0.1
Status: draft · v0.1 · HYPERCORE series focus

---

## 1. Scope

Amaç: ψ_GLYPH ekosistemi için ilk nesil (v0.1) bir ekonomi iskeleti tanımlamak:

- Tekil glif NFT fiyatlama modeli
- ψ_POD soy hattı & çocuk üretim ekonomisi
- GLYPH_TOKEN (GT) kullanım alanı

---

## 2. Units

### GLYPH_TOKEN (GT)
- Birim fiyat standardı
- Ödül / ekosistem iç para
- NFT’lerin değer referansı

---

## 3. NFT Fiyat Modeli

### 3.1 Metrikler

1️⃣ Entropy bucket `E_b`
- α < 0.70  → 0
- 0.70–0.80 → 1
- 0.80–0.90 → 2
- ≥0.90 → 3

2️⃣ Visual Complexity `V_s`
1–5

3️⃣ Lineage potential `L_p`
0–3

4️⃣ Rarity `R_e`
- 1/1 → 3
- 1/3 → 2
- 1/10 → 1

---

### 3.2 Formül

Base_GT = 80

Price_GT =
 Base_GT
 + 10 * E_b
 + 5  * V_s
 + 15 * L_p
 + 5  * R_e

---

### 3.3 Örnek — HYPERCORE_009-A

α = 0.88 → Eb = 2  
V_s = 4  
L_p = 3  
R_e = 3  

Price =
80
+ 20
+ 20
+ 45
+ 15
= **180 GT**

Launch price = 130 GT

---

## 4. ψ_POD Ekonomisi

ψ_POD bir koloni / soy alanıdır.

Child Base =
 Parent_Price * 0.25

Child_GT =
 Child_Base * (1 + Δα)

Parent bonus =
 5% child

---

## 5. Supply Draft

Max = 1,000,000 GT
30% Artist
30% Liquidity
25% Ecosystem
15% Community

---

## 6. Metadata uyumu

NFT metadata JSON şu tip alanlar içerir:

- entropy_signature
- lineage_potential
- rarity
- model_price
- launch_price

---

v0.2:
- market feedback kalibrasyonu
- entropy_loss
- semantic_density
- on-chain price oracle
