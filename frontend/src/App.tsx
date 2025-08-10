import axios from 'axios';
import { useState, useEffect } from 'react'
import './App.css'

type Todo = {
  id: number;
  title: string;
  completed: boolean;
};
type insertTodo={
title:string;
completed:boolean;
};
function App() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [inserTodoData, setInsertTodoData] = useState<string>("");
  const [deleteTodoData, setDeleteTodoData] = useState<number>(-1);
  const [updateTodoText, setUpdateTodoText] = useState<string>("");
  const [updateId,setUpdateId]=useState<number>(-1);//エラーを消すために使用しないIDの-1を入れている
  // :todoを格納している変化があったときに再描画
  useEffect(() => {//Todo: delete時に再描画されないので修正
    axios.get<Todo[]>("//localhost:8000/api/todo/")//語尾にはスラッシュが必要（ DEFAULT_ROUTER や APIViewを使っているため）
      .then(res => {
        setTodos(res.data)
        console.log(res.data)
      })
      .catch((err) => {
        console.error('APIエラー:', err);
      });
  }, []);
  // console.log(todos);

  const addTodo = (data: insertTodo) => {

    axios.post<Todo>("//localhost:8000/api/todo/", data)
      .then((res) => {
        console.log("post success");
        setTodos([...todos,res.data])
      })
      .catch(err => {
        console.log("error", err);
      })
  };

  const deleteTodo = (id: number) => {
    axios.delete<Todo[]>(`//localhost:8000/api/todo/${id}/`)
      .then(() => {
        console.log("delete success");
        setTodos(todos.filter(todo => todo.id !== id));
      })
      .catch(err => {
        console.log("error", err);
        console.log(id);
        
      })
  };
  /**todoの内容自体を変更する */
  const putTodo = (id: number,title:string) => {
    axios.put<Todo>(`//localhost:8000/api/todo/${id}/`, ({ "title": title }))
      .then((res) => {
        console.log("put success");
         setTodos(todos.map(t => (t.id === id ? res.data : t)));//idと一致したら更新データを返し、そうでないなら本のデータを返すmap
      })
      .catch(err => {
        console.log("error", err);
      })
  };

  /**チェックをする、外す */
  const checkTodo =(id:number)=>{
    const nowTodo =todos.filter(todo=>todo.id===id);
    const nowCompleted = nowTodo[0].completed;
    console.log(id,nowCompleted,!nowCompleted);
    const nowTitle = nowTodo[0].title;
    
    //  setTodos(todos.filter(todo => todo.id !== id));
    axios.put<Todo>(`//localhost:8000/api/todo/${id}/`, ({ "completed": !nowCompleted,"title":nowTitle }))
      .then((res) => {
        console.log("put success");
         setTodos(todos.map(t => (t.id === id ? res.data : t)));//idと一致したら更新データを返し、そうでないなら本のデータを返すmap
        //  res.dataで更新したデータが返ってきている
      })
      .catch(err => {
        console.log("error", err);
      })
  }
  //  


  return (
    <>
      <div>
        <h1>TODOアプリ</h1>
        <ul>
          {todos.map(todo => (
            // todo.id
            <li key={todo.id}>
              [{todo.completed ? '✅' : '➖️'}]{todo.title}🐱{todo.id}
            </li>
          ))}
        </ul>
        <div>
          <input type="text" onChange={(event)=>setInsertTodoData(event.target.value)}/>
          <button onClick={() => addTodo({ "title": inserTodoData, "completed": false })}>
            insert
          </button><br />

          <input type="number"  onChange={(event) => setDeleteTodoData(Number(event.target.value))}/>
          <button onClick={() => deleteTodo(deleteTodoData)}>
            delete
          </button><br />
          {/* 更新 */}
          <input type="number" onChange={(event)=>setUpdateId(Number(event.target.value))}/>
          <input type="text" onChange={(event)=>setUpdateTodoText(event.target.value)}/>
          <button onClick={() => putTodo(updateId,updateTodoText)}>
            put
          </button><br />
          {/* チェックのトグル */}
          <input type="number" onChange={(event)=>setUpdateId(Number(event.target.value))}/>
          <button onClick={() => checkTodo(updateId)}>
            check toggle
          </button>
        </div>
      </div>
    </>
  )
}

export default App
