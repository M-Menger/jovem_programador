import axios from 'axios';

export const serverApi = axios.create({
    baseURL: 'https://localhost:3333/'

    }
)