import dotenv from 'dotenv';
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

dotenv.config();
// https://vitejs.dev/config/
export default defineConfig({
  envDir: './src/',
  plugins: [react()],
  define: {
    'process.env': process.env
  }
})
