import { useEffect, useState } from 'react';
import styles from './TodoApp.module.css';
import TodoItem from '../to_do_item/ToDoItem';
import ToDoApi from '../../Api';

interface Task {
  text: string;
  completed: boolean;
}

function TodoApp() {
  const [task, setTask] = useState<string>(''); // Armazena o valor do input
  const [tasks, setTasks] = useState<Task[]>([]); // Armazena a lista de tarefas

  useEffect(() => {
    // Código do efeito aqui
    ToDoApi.getTask(5)
    .then((response:any) => {
      setTasks([...tasks,{text: response.data.title, completed: false}])
    })
    .catch((error:any) => console.log(error))
  }, []);

  const addTask = (): void => {
    if (task.trim()) {
      ToDoApi.createTask({
        title:task,
        completed: false
      }).then((response :any) => console.log(response)).catch((error :any) => console.log(error))
      setTasks([...tasks, { text: task, completed: false }]);
      setTask(''); // Limpa o campo de input
    }
    // CODIGO EXEMPLO
    // ToDoApi.createTask({
    //   text: task,
    //   completed: false
    // }).then((response) => console.log(response))
    // .catch((error) => console.log(error))
  };

  const removeTask = (index: number): void => {
    const newTasks = tasks.filter((_, i) => i !== index);
    setTasks(newTasks);
  };

  const toggleTask = (index: number): void => {
    const newTasks = tasks.map((task, i) =>
      i === index ? { ...task, completed: !task.completed } : task
    );
    setTasks(newTasks);
  };

  return (
    <div className={styles.container}>
      <h1>Lista de Tarefas</h1>
      <div className={styles.inputContainer}>
        <input
          type="text"
          value={task}
          onChange={(e) => setTask(e.target.value)}
          placeholder="Nova tarefa..."
        />
        <button onClick={addTask}>Adicionar</button>
      </div>
      <ul className={styles.taskList}>
        {tasks.map((task, index) => (
          <TodoItem
            key={index}
            task={task}
            index={index}
            removeTask={removeTask}
            toggleTask={toggleTask}
          >
            {task.text}
          </TodoItem>
        ))}
      </ul>
    </div>
  );
};

export default TodoApp;
