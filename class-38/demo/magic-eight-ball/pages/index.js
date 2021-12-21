import Head from 'next/head'
import { useState } from 'react';
import Header from './magic-eight-ball/header';
import QuestionsForm from './magic-eight-ball/questionstForm';
import QuestionsTable from './magic-eight-ball/questionsTable';
import EightBall from './magic-eight-ball/eightBall';
import responses from '../data';

const Home = () => {

  const [answersList, setAnswersList] = useState([]);
  const [latestAnswer, setLatestAnswer] = useState('No question yet, please ask a question!');
  const [counter, setCounter] = useState(0);

  const formHandler = (e) => {
    e.preventDefault();
    const randomReply = responses[Math.floor(Math.random() * responses.length)];
    let answer = {
      question: e.target.question.value,
      id: answersList.length,
      reply: randomReply
    };
    setLatestAnswer(answer.reply)
    setAnswersList([...answersList, answer]);
    setCounter(answer.id + 1);
  }
  return (
    <>
      <Head>
        <title>Magic 8 Ball</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header counter={counter} title="Magic 8 ball" />
      <main className="">
        {/* {
            counter <= 5 &&<QuestionsForm formHandler={formHandler}/>
          } */}

        {
          counter <= 5 ? <QuestionsForm formHandler={formHandler} /> : <></>
        }
        <EightBall latestAnswer={latestAnswer} />
        <QuestionsTable answersList={answersList} />
      </main>
    </>

  )
}
export default Home;