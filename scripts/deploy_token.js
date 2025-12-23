import hardhat from "hardhat";
const { ethers } = hardhat;

async function main() {
  const [deployer] = await ethers.getSigners();
  console.log("Deploying from:", deployer.address);

  const Token = await ethers.getContractFactory("GLYPH_TOKEN_v2");
  const token = await Token.deploy();

  await token.waitForDeployment();

  const addr = await token.getAddress();
  console.log("GLYPH_TOKEN deployed to:", addr);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
