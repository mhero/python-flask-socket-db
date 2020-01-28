import React, {useState} from 'react';
import './App.css';
const io = require("socket.io-client");
const HOST = "http://localhost:8000";
const socket = io.connect(HOST);
const axios = require('axios').default;

const Card = ({value, onClick}) => {
  return (
    <button onClick={onClick} className="poker-card">{value}</button>
  );
}

function App() {

  const [step, setStep] = useState(1);
  const [vote, setVote] = useState(-1);

  const [userId, setUserId] = useState(null);
  const [gameId, setGameId] = useState(null);
  const [taskId, setTaskId] = useState(null);

  const [gameName, setGameName] = useState(null);
  const [userName, setUserName] = useState(null);
  const [taskName, setTaskName] = useState(null);

  const post = (url, object, callback) => {
    axios.post(
      url, object
    )
    .then((response) => {
      callback(response.data.id);
    })
    .catch((error) => {
      console.log(error);
    });
  }

  const createUser = () => {
    post(`${HOST}/api/users`, { name: userName }, setUserId);
  }

  const createTask = (game) => {
    post(`${HOST}/api/tasks`, { name: taskName, game_id: game }, setTaskId);
  }

  const getGameData = () => {
    setStep(2);
    socket.on("sendPokerData", (taskData) => {
      console.log(taskData);
    });
  }

  const askGameData = () =>{
    socket.emit("getPokerData", 
                { task_id: userId,  user_id: gameId, vote: vote }
                );
  }

  const createGame = () => {
    createUser();
    axios.post(
      `${HOST}/api/games`, { name: gameName }
    )
    .then((response) => {
      setGameId(response.data.id);
      createTask(response.data.id);
      getGameData();
    })
    .catch((error) => {
      console.log(error);
    });
  }

  const enterGame = () => {
    createUser();
    getGameData();
  }
 
  return (
    <div className="App">
      <h1>Poker Planning!</h1>
      { step === 1 && 
        <div className="main-panel">
          <div className="panel create-game-panel">
            <h2>Create a game</h2>
            <input type="text" id="game" name="game" 
                placeholder="Enter game name"
                onChange={(event) => setGameName(event.target.value) }/>
            <input type="text" id="user" name="user" 
                placeholder="Enter your name"
                onChange={(event) => setUserName(event.target.value) }/>
            <input type="text" id="user" name="user" 
                placeholder="Enter your first task"
                onChange={(event) => setTaskName(event.target.value) }/>
            <button type="button" onClick={createGame}>Create game!</button>
          </div>
          <div className="panel join-game-panel">
            <h2>Join a game</h2>
            <input type="text" id="game" name="game" 
                  placeholder="Enter game id"
                  onChange={(event) => setGameId(event.target.value) }/>
            <input type="text" id="user" name="user" 
                placeholder="Enter your name"
                onChange={(event) => setUserName(event.target.value) }/>
            <button type="button" onClick={enterGame}>Join game!</button>
          </div>
        </div>
      }
      { step === 2 && 
        <div>
          <div>User ID: {userId}</div>
          <div>Game ID: {gameId}</div>
          <div>Task ID: {taskId}</div>

          <div className="cards-panel">
            <Card value={0} onClick={() => setVote(0)}/>
            <Card value={1} onClick={() => setVote(1)}/>
            <Card value={2} onClick={() => setVote(2)}/>
            <Card value={3} onClick={() => setVote(3)}/>
            <Card value={5} onClick={() => setVote(5)}/>
            <Card value={8} onClick={() => setVote(8)}/>
            <Card value={13} onClick={() => setVote(13)}/>
            <Card value={21} onClick={() => setVote(21)}/>
            <Card value={100} onClick={() => setVote(100)}/>
          </div>

          <input type="text" id="vote" name="vote" 
                  placeholder="Enter vote"
                  onChange={(event) => setVote(event.target.value) }/>
          <button type="button">Next Task</button>
        </div>
      }
    </div>
  );
}

export default App;