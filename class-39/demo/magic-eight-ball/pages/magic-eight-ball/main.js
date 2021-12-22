import React from 'react';
import { useState } from 'react';
import Head from 'next/head';
import Header from './header';
import QuestionsForm from './questionstForm';
import QuestionsTable from './questionsTable';
import EightBall from './eightBall';
import axios from 'axios';

const baseUrl ='http://127.0.0.1:8000/';
const responsesEndPoint = baseUrl+'api/v1/';
const answeredQuestionsEndPoint = baseUrl+'api/v1/answered-questions/';

const Main = (props) => {
    const responses =[]
    const [answeredQuesitons, setAnsweredQuesitons]=useState([]);

    const config={
        headers: {"Authorization" : `Bearer ${props.token}`}
    }
    axios.get(responsesEndPoint, config).then(res =>{
        responses = res.data;
    });

    const [latestAnswer, setLatestAnswer] = useState('No question yet, please ask a question!');
    const [counter, setCounter] = useState(0);

    const formHandler = async (e) => {

        e.preventDefault();
        // {id:1 text:"No"}
        const randomReply = responses[Math.floor(Math.random() * responses.length)];
        let answer = {
            question: e.target.question.value,
            id: answeredQuesitons.length,
            reply: randomReply.text
        };
        setLatestAnswer(answer.reply);
        setCounter(answer.id + 1);
        let answeredQuestions= await axios.get(answeredQuestionsEndPoint, config);
        setAnsweredQuesitons(answeredQuestions.data);
        // we need to create a POST request to store the questions and the random respone in the DB
        // update the answered questions state each time we ask a question
    }
    return (
        <>
            <Head>
                <title>Magic 8 Ball</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <Header counter={counter} title="Magic 8 ball" />
            <main className="">
                <QuestionsForm formHandler={formHandler} />
                <EightBall latestAnswer={latestAnswer} />
                <QuestionsTable answersList={answeredQuesitons} />
            </main>
        </>
    )
}

export default Main
