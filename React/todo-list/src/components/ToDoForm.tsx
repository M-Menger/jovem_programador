import { useEffect, useState } from 'react';

interface ToDo{
    text: string;
    description: string;
}

function ToDoForm{
    const[task, setTask] = useState<string>('');
    const[tasks,setTasks] = useState<Task[]>([]);

    const addTask = (): void => {
        if (task.trim()) {
            setTasks([...tasks, { text: task, completed: false }]);
            setTask(''); // Limpa o campo de input
        }
    };

    const removeTask = (index:number): void => {
        const newTasks = tasks.filter((_, i) => i !== index);
        setTasks(newTasks);
    };

    return (
        <div>
            <form>
                <input 
                    type="text" 
                    value={title}
                    onChange={(e) => setTask(e.target.value)}
                    placeholder='Titulo'
                />

                <input 
                    type="text" 
                    value={description}
                    onChange={(e) => setTask(e.target.value)}
                    placeholder='Decrição'
                />

                <button onClick={addTask}>Submit</button>

            </form>
        </div>
    )
};

