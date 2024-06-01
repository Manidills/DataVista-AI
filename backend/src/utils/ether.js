import { ethers } from 'ethers';
import { config } from '../config/index.js';
import siwe from 'siwe';

const schema = "https";
const domain = "localhost";
const origin = "http://localhost/login";

export const generateAuthSig = async () => {
  // Replace with your wallet private key for testing purposes
  const privateKey = config.wallet.privateKey;
  const wallet = new ethers.Wallet(privateKey);

  const statement = 'Lit Protocol Authentication';

  const siweMessage = new siwe.SiweMessage({
    schema,
    domain,
    address: wallet.address,
    statement,
    uri: origin,
    version: '1',
    chainId: '1',
    expirationTime: new Date(Date.now() + 1000 * 60 * 60).toISOString(),
  });
  const messageToSign = siweMessage.prepareMessage();
  const signature = await wallet.signMessage(messageToSign);
  const recoveredAddress = ethers.verifyMessage(messageToSign, signature);
  
  // Generate authSig
  const authSig = {
    sig: signature,
    derivedVia: "web3.eth.personal.sign",
    signedMessage: messageToSign,
    address: recoveredAddress,
  };

  return authSig;
};

