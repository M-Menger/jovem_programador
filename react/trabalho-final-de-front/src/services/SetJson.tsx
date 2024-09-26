import axios from 'axios';

let ManageKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3V1aWQiOiJ5aUkxVHJqZlR6UTl5a0lmbVNQTm1OUjZMWUoyIiwiaXNzIjoiaHR0cHM6Ly9qc29uc2lsby5jb20iLCJleHAiOjE3Mjk3Mjc4OTJ9.VRM7ANA6mDkW9OXEu4INsyo_jVgNUSdpB7ipMe77Zbo"

const conectJsonSilo = axios.create({
    baseURL: 'https://api.jsonsilo.com/api/v1/manage/9856e4cb-2859-4cf2-83a1-26afff317cf5',
    headers: {
        'Content-Type': 'application/json',
        'ToDoJP': ManageKey
    }
});

const SetJson = {
    'getTasks': () => conectJsonSilo.get('/'),
    'getTask': (id: number) => conectJsonSilo.get(`/tasks/${id}`),
    'createTask': (task: { title: string, description: string }) => conectJsonSilo.post('', task),
    'updateTask': (id: number, task: any) => conectJsonSilo.put(`/tasks/${id}`, task),
    'deleteTask': (id: number) => conectJsonSilo.delete(`/tasks/${id}`)
}

export default SetJson;
