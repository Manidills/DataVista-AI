import dotenv from 'dotenv';

dotenv.config();

export const config = {
    port: process.env.PORT || 5000,
    lighthouse: {
        apiKey: process.env.LIGHTHOUSE_API_KEY,
    },
};
