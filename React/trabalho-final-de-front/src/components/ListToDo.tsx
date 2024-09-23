interface ITask {
    title: string;
    description: string;
}

interface IListToDoProps {
    tasks: ITask[];
}

export const ListToDo: React.FC<IListToDoProps> = ({ tasks }) => {
    return (
        <div className='Lista-ToDo'>
            <h1>ToDo List JP</h1>
            <h3>Tarefas</h3>
                <ul>
                    {tasks.map((task, index) => (
                        <li key={index}>
                            <strong>{task.title}:</strong> {task.description}
                            <a href="#">editar</a>
                            <a href="#">delete</a>
                        </li>
                    ))}
                </ul>
        </div>
    )
}
export default ListToDo