import fs from 'fs';
import lighthouse from '@lighthouse-web3/sdk';
import { config } from '../config/index.js';

export const uploadFile = async (req, res) => {
    try {
        const filePath = req.file.path;
        const fileName = req.file.originalname;

        // Use Lighthouse SDK to upload the file
        const apiKey = config.lighthouse.apiKey;
        const response = await lighthouse.upload(filePath, apiKey);

        // Clean up the uploaded file from the server
        fs.unlinkSync(filePath);

        return res.status(200).json(response);
    } catch (error) {
        console.error('Error uploading file:', error);
        return res.status(500).send('Internal Server Error');
    }
};
