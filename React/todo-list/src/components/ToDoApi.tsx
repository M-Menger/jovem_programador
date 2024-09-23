import axios from "axios";

const conectInstance = axios.create({
    baseURL:'',
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json'
    }
});

const ToDoApi = {
    'getTasks': () => conectInstance.get('/Todos'),
    'getTask': (id: number) => conectInstance.get(`/todos${id}`),
    'createTask': (task: any) => conectInstance.post('/todos',task),
    'updateTask': (id: number, task:any) => conectInstance.put(`/todos/${id}`, task),
    'deleteTask': (id:number) => conectInstance.delete(`/todos/${id}`)
}

export default ToDoApi