import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";
import Todo from "./todo";
import CharacterList from "./CharacterList";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="" element={<Todo />} />
        <Route path="/smash_note" element={<CharacterList />} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;
