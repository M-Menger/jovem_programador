import {useState} from 'react';
import { serverApi } from '../services/serverApi';

interface IaddToDoProps {
    tasks: {title: string, description: string }[];
    setTasks: React.Dispatch<React.SetStateAction<{title: string, description: string}[]>>;
}


export const AddToDo: React.FC<IaddToDoProps> = () => {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');

    const handleAddTask = () => {
        if (title.trim() && description.trim()){
            
            serverApi.post("/tasks", {
                title: title,
                description: description
            })
            .then((response) => console.log(response))
            .catch((error) => console.log(error));

            setTitle('');
            setDescription('');
        }
    };

    return (
        <div className='main-div'>
            <h2>Adicionar Tarefa</h2>
            <form className='ins-task'>
                <input
                    className='inp-title' 
                    type="text"
                    placeholder='Titulo'
                    value={title}
                    onChange={e => setTitle(e.target.value)}
                />

                <input 
                    className='inp-desc'
                    type="text"
                    placeholder='Descrição'
                    value={description}
                    onChange={e => setDescription(e.target.value)}
                />
                
                <button className='btn-add' type='button' onClick={handleAddTask}>
                    Add Task
                </button>
            </form>
        </div>
    );
}

export default AddToDo