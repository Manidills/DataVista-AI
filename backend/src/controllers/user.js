import fs from 'fs';
import lighthouse from '@lighthouse-web3/sdk';
import { config } from '../config/index.js';
import db from '../database/database.js';
import { encryptText, decryptText } from '../utils/lit.js';

export const uploadFile = async (req, res) => {
    try {
        const filePath = req.file.path;
        const fileName = req.body.fileName || req.file.originalname;
        const storage = req.body.storage || 'lighthouse';

        // Use Lighthouse SDK to upload the file
        const apiKey = config.lighthouse.apiKey;
        const rawFileResponse = await lighthouse.upload(filePath, apiKey);

        // Save the file metadata to the database
        const cidToEncrypt = rawFileResponse.data.Hash;
        
        const encryptedResponse = await encryptText(cidToEncrypt);

        const cid = encryptedResponse.dataToEncryptHash;
        const cipherText = encryptedResponse.ciphertext;

        const sql = `
        INSERT INTO lighthouse (cid, cipherText, fileName, storage)
        VALUES (?, ?, ?, ?)
        `;
        const values = [cid, cipherText, fileName, storage];
        
        db.run(sql, values, function(err) {
            if (err) {
            return console.error('Error inserting record:', err.message);
            }
            console.log(`A row has been inserted with rowid ${this.lastID}`);
        });
        
        // Delete the uploaded file
        fs.unlinkSync(filePath);

        return res.status(200).json('File successfully uploaded');
    } catch (error) {
        console.error('Error uploading file:', error);
        return res.status(400).send('Error uploading file');
    }
};

export const decryptFile = async (req, res) => {
    const { text } = req.params;
    try {
        const sql = `SELECT * FROM lighthouse WHERE cid = ?`;
        db.get(sql, [text], async function(err, row) {
            if (err) {
            console.error('Error fetching record:', err.message);
            return res.status(400).send('Error fetching record:');
            }
            else {
                const decryptedResponse = await decryptText(row.cipherText, row.cid);
                const lighthouseUrl = `https://gateway.lighthouse.storage/ipfs/${decryptedResponse.decryptedString}`;
                return res.status(200).json({ data: { lighthouseUrl, cid: decryptedResponse.decryptedString }});
            }
        });
    } catch (error) {
        console.error('Error decrypting file:', error);
        return res.status(400).send('Error decrypting file');
    }
};
