import fs from 'fs';
import lighthouse from '@lighthouse-web3/sdk';
import { config } from '../config/index.js';
import db from '../database/database.js';
// import { encryptFile, decryptFile } from '../utils/lit.js';

export const uploadFile = async (req, res) => {
    try {
        const filePath = req.file.path;
        const fileName = req.body.fileName || req.file.originalname;
        const storage = req.body.storage || 'lighthouse';

        // Use Lighthouse SDK to upload the file
        const apiKey = config.lighthouse.apiKey;
        const rawFileResponse = await lighthouse.upload(filePath, apiKey);

        // Save the file metadata to the database
        const cid = rawFileResponse.data.Hash;
        
        const sql = `
        INSERT INTO lighthouse (cid, fileName, storage)
        VALUES (?, ?, ?)
        `;
        const values = [cid, fileName, storage];
        
        db.run(sql, values, function(err) {
            if (err) {
            return console.error('Error inserting record:', err.message);
            }
            console.log(`A row has been inserted with rowid ${this.lastID}`);
        });
        
        // Delete the uploaded file
        fs.unlinkSync(filePath);

        return res.status(200).json(rawFileResponse);
    } catch (error) {
        console.error('Error uploading file:', error);
        return res.status(500).send('Internal Server Error');
    }
};
