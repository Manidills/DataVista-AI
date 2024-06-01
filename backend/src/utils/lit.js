import * as LitJsSdk from "@lit-protocol/lit-node-client";
import { generateAuthSig } from "./ether.js";

const accessControlConditions = [
  {
    contractAddress: "",
    standardContractType: "",
    chain: "ethereum",
    method: "eth_getBalance",
    parameters: [":userAddress", "latest"],
    returnValueTest: {
      comparator: ">=",
      value: "0",
    },
  },
];

class Lit {
  litNodeClient;
  chain;

  constructor(chain) {
    this.chain = chain;
  }

  async connect() {
    this.litNodeClient = new LitJsSdk.LitNodeClientNodeJs({
      alertWhenUnauthorized: false,
      litNetwork: 'cayenne',
      debug: true,
    });

    await this.litNodeClient.connect();
  }

  async encryptMessage(message) {
    const authSig = await generateAuthSig();
    try {
      // Encrypt the message
      const { ciphertext, dataToEncryptHash } = await LitJsSdk.encryptString(
        {
          accessControlConditions: accessControlConditions,
          dataToEncrypt: message,
          chain: this.chain,
          authSig: authSig,
        },
        this.litNodeClient,
      );

      // Return the ciphertext and dataToEncryptHash
      return { ciphertext, dataToEncryptHash };
    } catch (error) {
        console.error(error);
    }
  }

  async decryptMessage(message, hash) {
    try {
      const authSig = await generateAuthSig();
      // Decrypt the message
      const decryptedString = await LitJsSdk.decryptToString(
        {
          accessControlConditions,
          chain: this.chain,
          ciphertext: message,
          dataToEncryptHash: hash,
          authSig: authSig,
        },
        this.litNodeClient,
      );
      // Return the decrypted string
      return { decryptedString };
    } catch (error) {
        console.error(error);
    }
  }
}

const chain = "etherum";
let myLit = new Lit(chain);

export const encryptText = async (message) => {
    try {
        await myLit.connect();
        const encryptResponse = await myLit.encryptMessage(message);
        return encryptResponse;
    } catch (error) {
        console.error('Error encrypting text', error);
        return null;
    }
};

export const decryptText = async (message, hash) => {
    try {
        await myLit.connect();
        const decryptedResponse = await myLit.decryptMessage(message, hash);
        return decryptedResponse;
    } catch (error) {
        console.error('Error decrypting file:', error);
        return null;
    }
};
