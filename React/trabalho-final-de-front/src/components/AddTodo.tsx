import {useState} from 'react';
import { serverApi } from '../services/serverApi';


interface IaddToDoProps {
    tasks: {title: string, description: string }[];
    setTasks: React.Dispatch<React.SetStateAction<{title: string, description: string}[]>>;
}

export const AddToDo: React.FC<IaddToDoProps> = ({ tasks, setTasks }) => {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');

    const handleAddTask = () => {
        if (title.trim() && description.trim()){
            setTasks([...tasks,{ title, description }]);

            setTitle('');
            setDescription('');
        }
    }

    return (

        <div>
            <h1>ToDo List JP</h1>
            <h3>Adicionar Tarefa</h3>
            <form>
                <input 
                    type="text"
                    placeholder='Titulo'
                    value={title}
                    onChange={e => setTitle(e.target.value)}
                />

                <input 
                    type="text"
                    placeholder='Descrição'
                    value={description}
                    onChange={e => setDescription(e.target.value)}
                />
                
                <button type='button' onClick={handleAddTask}>
                    Add Task
                </button>
            </form>
        </div>
    );
}

export default AddToDo