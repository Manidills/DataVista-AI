import express from 'express';
import multer  from 'multer';
import { 
    uploadFile,
    decryptFile,
} from '../controllers/user.js';

const upload = multer({ dest: 'backend/uploads/' });
const router = express.Router();

router.post(
    '/upload',
    upload.single('file'),
    uploadFile,
);
router.get(
    '/decryptFile/:text',
    decryptFile,
);
export default router;