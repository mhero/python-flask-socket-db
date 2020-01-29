import React, {useState} from 'react';
import './App.css';
const io = require("socket.io-client");
const HOST = `http://${process.env.REACT_APP_HOST}:8000`;
const socket = io.connect(HOST);
const axios = require('axios').default;

const Card = ({value, onClick}) => {
  return (
    <button onClick={onClick} className="poker-card">{value}</button>
  );
}

function App() {

  const [step, setStep] = useState(1);
  const [userId, setUserId] = useState(null);
  const [gameId, setGameId] = useState(null);

  const [gameName, setGameName] = useState(null);
  const [userName, setUserName] = useState(null);
  const [taskName, setTaskName] = useState(null);

  const[poker, setPoker] = useState(null);

  socket.on("sendPokerData", (taskData) => {
    setPoker(taskData);
  });

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

  const createGame = () => {
    createUser();
    axios.post(
      `${HOST}/api/games`, { game_name: gameName, task_name: taskName }
    )
    .then((response) => {
      setGameId(response.data.game);
      setStep(2);
    })
    .catch((error) => {
      console.log(error);
    });
  }

  const gameData = (vote) => {
    socket.emit(
      "getPokerData", 
      { game_id: gameId, user_id: userId, vote: vote }
     );
  }

  const enterGame = () => {
    createUser();
    setStep(2);
    gameData(0);
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
        <div className="step-2"> 
          <div>User: {userName}</div>
          <div>Game {gameName} ID: {gameId}</div>
          <p>Choose one card from the left</p>
          
          <div className="game-container">
            <div className="cards-panel">
              <Card value={0} onClick={() => gameData(0)}/>
              <Card value={1} onClick={() => gameData(1)}/>
              <Card value={2} onClick={() => gameData(2)}/>
              <Card value={3} onClick={() => gameData(3)}/>
              <Card value={5} onClick={() => gameData(5)}/>
              <Card value={8} onClick={() => gameData(8)}/>
              <Card value={13} onClick={() => gameData(13)}/>
              <Card value={21} onClick={() => gameData(21)}/>
              <Card value={100} onClick={() => gameData(100)}/>
            </div>
            <div className="votes-panel">
              <ul>
                {
                  poker && poker.map((item) => 
                  <li className="card-vote">
                    <div className="vote-owner">{item[1]}</div>
                    <div className="vote-value">{item[2]}</div>
                  </li>)
                }
              </ul>
            </div>
          </div>
        </div>
      }
    </div>
  );
}

export default App;