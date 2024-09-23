import editIcon from '../assets/icons/edit.png'
import trashIcon from '../assets/icons/trash.png'
import checkedIcon from '../assets/icons/checked.png'


function ListToDo(){
    return (
        <div className="container-form">
            <form className="list-ToDo">
                <input className="titleToDo" type="text" placeholder="Titulo" id="tarefa"/>
                <input className="taskToDo" type="text" placeholder="Tarefa" id="tarefa"/>
                <a href="#"><img className="icons" src={checkedIcon} alt="Icone Checked" /></a>
                <a href="#"><img className="icons" src={editIcon} alt="Icone edição" /></a>
                <a href="#"><img className="icons" src={trashIcon} alt="Icone lixeira" /></a>
            </form>
        </div>
    )
}

export default ListToDo