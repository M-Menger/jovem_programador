import { useState } from "react"
import editIcon from "./assets/icons/edit.png"
import trashIcon from "./assets/icons/trash.png"
import checkedIcon from "./assets/icons/checked.png"


function FormToDo(){
    return (
        <div className="container-form">
            <form className="formTodo">
                <input className="txtInp" type="text" placeholder="Tarefa" id="tarefa"/>
                <input className="btnInp" type="submit" value="Adicionar" />
                <a href="#"><img className="icons" src={checkedIcon} alt="Icone Checked" /></a>
                <a href="#"><img className="icons" src={editIcon} alt="Icone edição" /></a>
                <a href="#"><img className="icons" src={trashIcon} alt="Icone lixeira" /></a>
            </form>
        </div>
    )
}

export default FormToDo