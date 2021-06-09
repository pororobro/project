import React, { useState } from 'react'

const Todo = () =>{
    const [item, setItem] = useState('')
    return (<>
    <h1>할일 목록</h1>
    <h4>{item}</h4>
    <input onchage = { e => setItem(e.target.value)}/><br/>
    <button onclick = { () => {setItem('파이썬공부')}}>할일추가</button>
    <button onclick = { () => {setItem('')}}>할일삭제</button>

    </>)
    
}

export default Todo