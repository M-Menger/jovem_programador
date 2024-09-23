import axios from 'axios';

const conectInstance = axios.create({
    baseURL: 'https://jsonplaceholder.typicode.com',
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json'
    }
});

const RandomToDoApi = {
    'getTasks': () => conectInstance.get('/posts'),
    'getTask': (id: number) => conectInstance.get(`/posts/${id}`),
    'createTask': (task: any) => conectInstance.post('/posts', task),
    'updateTask': (id: number, task: any) => conectInstance.put(`/posts/${id}`, task),
    'deleteTask': (id: number) => conectInstance.delete(`/todos/${id}`) 
}

export default RandomToDoApi