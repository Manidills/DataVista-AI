import express from 'express';
import multer  from 'multer';
import { uploadFile } from '../controllers/user.js';

const upload = multer({ dest: 'backend/uploads/' });
const router = express.Router();

router.post(
    '/upload',
    upload.single('file'),
    uploadFile,
);

export default router;