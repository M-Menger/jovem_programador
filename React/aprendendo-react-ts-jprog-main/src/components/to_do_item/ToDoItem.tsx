import React from 'react';
import styles from './TodoItem.module.css';

interface TodoItemProps {
  task: {
    text: string;
    completed: boolean;
  };
  index: number;
  removeTask: (index: number) => void;
  toggleTask: (index: number) => void;
  children: React.ReactNode;
}

function TodoItem(props:TodoItemProps) {
  return (
    <li className={styles.taskItem}>
      <span
        onClick={() => props.toggleTask(props.index)}
        className={props.task.completed ? styles.completed : ''}
      >
        {props.children}
      </span>
      <button onClick={() => props.removeTask(props.index)} className={styles.removeBtn}>
        Remover
      </button>
    </li>
  );
};

export default TodoItem;
