import path from 'path';
import { fileURLToPath } from 'url';
import sqlite3 from 'sqlite3';
sqlite3.verbose();

const currentModuleURL = import.meta.url;
const __filename = fileURLToPath(currentModuleURL);
const __dirname = path.dirname(__filename);

const dbPath = path.resolve(__dirname, 'app.db');
// Create a new database file or open an existing one
const db = new sqlite3.Database(dbPath, (err) => {
  if (err) {
    console.error('Error opening database:', err.message);
  } else {
    console.log('Connected to the SQLite database.');

    // Create table 1: lighthouse
    db.run(`
      CREATE TABLE IF NOT EXISTS lighthouse (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cid TEXT NOT NULL,
        cipherText TEXT NOT NULL,
        storage TEXT NOT NULL,
        fileName TEXT NOT NULL,
        uploadDate DATETIME DEFAULT CURRENT_TIMESTAMP
      )
    `, (err) => {
      if (err) {
        console.error('Error creating lighthouse table:', err.message);
      } else {
        console.log('Lighthouse table created or already exists.');
      }
    });

    // Create table 2: users
    db.run(`
      CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        createdAt DATETIME DEFAULT CURRENT_TIMESTAMP
      )
    `, (err) => {
      if (err) {
        console.error('Error creating users table:', err.message);
      } else {
        console.log('Users table created or already exists.');
      }
    });
  }
});

export default db;
