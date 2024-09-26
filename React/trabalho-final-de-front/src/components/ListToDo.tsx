import { useState, useEffect } from "react";
import { serverApi } from "../services/serverApi";

interface ITask {
    id: number;
    title: string;
    description: string;
    solved: boolean;
}

interface IListToDoProps {
    tasks: ITask[];
}

export const ListToDo: React.FC<IListToDoProps> = ({ tasks }) => {
    const [taskList, setTaskList] = useState<ITask[]>(tasks);
    const [editIndex, setEditIndex] = useState<number | null>(null);
    const [editTask, setEditTask] = useState<ITask>({id:0 ,  title: "", description: "", solved: false});

    useEffect(() => {
        serverApi.get("/tasks").then((response) =>{
            console.log(response);
            setTaskList(response.data);
        });
    }, []);


    const handleComplete = (index: number) => {
        const taskToUpdate = taskList[index];
        const updatedTask = { ...taskToUpdate, solved: !taskToUpdate.solved }; 

        serverApi.put(`/tasks/${taskToUpdate.id}`, { 
            solved: updatedTask.solved,
            title: editTask.title,
            description: editTask.description,
         })
            .then(() => {
                
                const updatedTaskList = [...taskList];
                updatedTaskList[index] = updatedTask;
                setTaskList(updatedTaskList); 
            })
            .catch(error => console.log("Error Updating Task: ", error));
    };;

    const handleDelete = (index: number) => {
        const taskToDelete = taskList[index];

        serverApi.delete(`/tasks/${taskToDelete.id}`)
            .then(() => {
                const newTaskList = taskList.filter((_,i) => i !== index);
                setTaskList(newTaskList);
            })
            .catch(error => {
                console.error("Deu pau na deleção da tarefa! ", error);
            });
    };

    const handleEdit = (index: number) => {
        setEditIndex(index);
        setEditTask(taskList[index]);
    };

    const handleSave = () => {
        if (editIndex !== null) {
            const taskToUpdate = taskList[editIndex];

            serverApi.put(`/tasks/${taskToUpdate.id}`,{
                title: editTask.title,
                description: editTask.description,
            })
            .then(() => {
                const updatedTasks = [...taskList];
                updatedTasks[editIndex] = editTask;
                setTaskList(updatedTasks);

                setEditIndex(null);
            })
            .catch(error => console.log("Error Updating Task: ", error));
        }
    };

    return (
        <div className='Lista-ToDo'>
            <h2>Tarefas</h2>
                <div className="main-container">
                    <ul className="list-unorder">
                        {taskList?.map((task, index) => (
                            <li className="tasks" key={index}>
                                {editIndex === index ? (
                                    <>  
                                        <input 
                                            className="edt-title"
                                            type="text" 
                                            value={editTask.title} 
                                            onChange={(e) => setEditTask({ ...editTask, title: e.target.value})} 
                                        />

                                        <input  
                                            className="edt-desc"
                                            type="text"
                                            value={editTask.description}
                                            onChange={(e) => setEditTask({ ...editTask, description: e.target.value})}
                                        />

                                        <button className="btn-edt" onClick={handleSave}>
                                            <img className="icons" src="./src/assets/save-icon.png" alt="Save Icon" />
                                        </button>
                                    </>
                                ) : (
                                    <>
                                        <p className={`this-task ${task.solved ? 'completed' : ''}`}><strong>Titulo:</strong> {task.title} <strong>Descrição:</strong> {task.description}</p>

                                        <button className="btn-icon" onClick={() => handleEdit(index)}>
                                            <img className="icons" src="./src/assets/attention-icon.png" alt="Edit Icon" />
                                        </button>

                                        <button className="btn-icon" onClick={() => handleDelete(index)}>
                                            <img className="icons" src="./src/assets/delete-icon.png" alt="Delete Icon" />
                                        </button>

                                        <button className="btn-icon" onClick={() => handleComplete(index)} >
                                            <img className="icons" src="./src/assets/check-icon.png" alt="Check Icon" />
                                        </button>
                                    </>
                                )}
                            </li>
                        ))}
                    </ul>
                </div>
        </div>
    );
};
export default ListToDo