
import { useState } from 'react';
import Main from './magic-eight-ball/main';
import LoginForm from './magic-eight-ball/loginForm';
import axios from 'axios';

const baseUrl ='http://127.0.0.1:8000/';
const tokenUrl = baseUrl+'api/token/';

const Home = () => {
// if user is logged in show main component
// else show login form component
const [token, setToken] = useState('');

const submitHandler = async (e, credintials)=>{
  e.preventDefault();
  axios.post(tokenUrl,credintials).then(data=>{
    setToken(data.data.access)
  });
  console.log(token)
}

  if (!token) return <LoginForm submitHandler={submitHandler}/>
  return (<Main token={token}/>)
}
export default Home;