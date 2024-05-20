import express from 'express';
import cors from 'cors';
import { config } from './config/index.js';
import userRouter from './routes/user.js';

const app = express();
app.use(cors());
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get("/", (req, res) => {
  res.send(`Hello World!`);
});

app.use('/api/user', userRouter);

app.listen(config.port, () => {
  console.log(`Example app listening on port ${config.port}!`);
});
