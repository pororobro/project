import React, {useState} from 'react'

const Todos = () => {
    const [item, setItem] = useState('')
    return(<>
    
    <h1>todos</h1>
    <input onchange = { e => setItem(e.target.value)}/><br/>
    <button onClick = { () => {setItem()}}>할일추가</button>
    <button onClick = { () => {setItem()}}>할일삭제</button>

    </>)    
}

export default Todos