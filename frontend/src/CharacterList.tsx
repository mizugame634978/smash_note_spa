import axios from "axios";
import { useState, useEffect } from "react";
import "./App.css";


type CharacterListType = {
  // id: number;
  characterName: string;
  imageUrl: string;
};




function CharacterList() {
  const [character, setCharacter] = useState<CharacterListType[]>([]);
  // const [inserTodoData, setInsertTodoData] = useState<string>("");

  // :todoを格納している変化があったときに再描画
  useEffect(() => {//Todo: delete時に再描画されないので修正
    axios.get<CharacterListType[]>("//localhost:8000/smash_note/api/")//語尾にはスラッシュが必要（ DEFAULT_ROUTER や APIViewを使っているため）
      .then(res => {
        setCharacter(res.data)
        console.log(res.data)
      })
      .catch((err) => {
        console.error('APIエラー:', err);
      });
  }, []);




  return (
    <>
      <div>
        <h1>TODOアプリ</h1>
        <ul>
          {character.map((todo) => (
            <li>

              <img src={`http://localhost:8000${todo.image_url}`} />
            </li>
          ))}
        </ul>

      </div>
    </>
  );
}

export default CharacterList;
