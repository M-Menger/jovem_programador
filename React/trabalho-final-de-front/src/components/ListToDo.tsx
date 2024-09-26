import { useState } from "react";

interface ITask {
    title: string;
    description: string;
}

interface IListToDoProps {
    tasks: ITask[];
}

const jsonToDo: ITask = {
    title: "",
    description: ""
};

export function Tasks() {
    const [t]
}


export const ListToDo: React.FC<IListToDoProps> = ({ tasks }) => {
    const [taskList, setTaskList] = useState<ITask[]>(tasks);
    const [editIndex, setEditIndex] = useState<number | null>(null);
    const [editTask, setEditTask] = useState<ITask>({ title: '', description:''});
    
    const handleDelete = (index: number) => {
        const newTaskList = taskList.filter((_, i) => i !== index);
        setTaskList(newTaskList);
    };

    const handleEdit = (index: number) => {
        setEditIndex(index);
        setEditTask(taskList[index]);
    };

    const handleSave = () => {
        if (editIndex !== null) {
            const updatedTasks = [...taskList];
            updatedTasks[editIndex] = editTask;
            setTaskList(updatedTasks);
            setEditIndex(null);
        }
    };


    return (
        <div className='Lista-ToDo'>
            <h1>ToDo List JP</h1>
            <h3>Tarefas</h3>
                <ul>
                    {taskList.map((task, index) => (
                        <li key={index}>
                            {editIndex === index ? (
                                <>
                                    <input 
                                        type="text" 
                                        value={editTask.title} 
                                        onChange={(e) => setEditTask({ ...editTask, title: e.target.value})} 
                                    />

                                    <input 
                                        type="text"
                                        value={editTask.description}
                                        onChange={(e) => setEditTask({ ...editTask, description: e.target.value})}
                                    />

                                    <button onClick={handleSave}>
                                        Save
                                    </button>
                                </>
                            ) : (
                                <>
                                    <strong>{task.title}:</strong> {task.description}
                                    <a href="#" onClick={() => handleEdit(index)}>
                                        <img className="icons" src="./src/assets/attention-icon.png" alt="Edit Icon" />
                                    </a>

                                    <a href="#" onClick={() => handleDelete(index)}>
                                        <img className="icons" src="./src/assets/delete-icon.png" alt="Delete Icon" />
                                    </a>

                                    <a href="#">
                                        <img className="icons" src="./src/assets/check-icon.png" alt="Check Icon" />
                                    </a>
                                </>
                            )}
                        </li>
                    ))}
                </ul>
        </div>
    );
};
export default ListToDo