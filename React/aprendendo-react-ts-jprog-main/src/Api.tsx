import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: 'https://jsonplaceholder.typicode.com',
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json'
    }
});

const ToDoApi = {
    'getTasks': () => axiosInstance.get('/todos'),
    'getTask': (id: number) => axiosInstance.get(`/todos/${id}`),
    'createTask': (task: any) => axiosInstance.post('/todos', task),
    'updateTask': (id: number, task: any) => axiosInstance.put(`/todos/${id}`, task),
    'deleteTask': (id: number) => axiosInstance.delete(`/todos/${id}`)
}

export default ToDoApi