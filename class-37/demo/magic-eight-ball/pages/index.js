import Head from 'next/head'
import { useState } from 'react';


const App=()=> {

  const [answersList, setAnswersList] = useState([]);
  const [latestAnswer, setLatestAnswer] = useState('No question yet, please ask a question!');
  const [counter, setCounter] = useState(0)
  const formHandler = (e)=>{
      e.preventDefault();
      let replies = ['yes', 'no', 'not your business', 'HAHAHAHA!!', 'maybe another time!', 'ASK GOOGLE!'];
      const randomReply = replies[Math.floor(Math.random()* replies.length)];
      let answer ={
        question:e.target.question.value,
        id:answersList.length,
        reply :randomReply
      };
      setLatestAnswer(answer.reply)
      setAnswersList([...answersList, answer]);
      setCounter(answer.id+1);
  }
  return (
    <>
      <Head>
        <title>Magic 8 Ball</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <header className='flex justify-between bg-teal-600 py-4 items-center'>
        <h1 className='text-4xl mx-1'>Magic 8 Ball</h1>
        <p className='m-1'>{counter} questions answered</p>
      </header>
      <main className="">
        <form className='flex w-1/2 bg-gray-200 mx-auto my-5 p-2' onSubmit={formHandler}>
          <input name='question' className='flex-auto p-2' placeholder='ask a question...'/>
         <button className='px-4 py-1 mx-2  bg-gray-500 rounded-full'>Ok</button>
        </form>

        <div className='w-96 h-96 mx-auto bg-neutral-900 rounded-full'>
          <div className='relative flex items-center justify-center w-48 h-48 bg-neutral-100 rounded-full top-16 left-16'>
            <p className='text-x1 text-center'>{latestAnswer}</p>
          </div>
        </div>
        <table className='w-1/2 mx-auto my-4'>
          <thead>
            <th className='border border-blue-600'>No</th>
            <th className='border border-blue-600'>Question</th>
            <th className='border border-blue-600'>Responoses</th>
          </thead>
          <tbody>
            {
              answersList.map(answer =>{
                return (
                  <tr>
                  <td className='border border-blue-600'>{answer.id}</td>
                  <td className='border border-blue-600'>{answer.question}</td>
                  <td className='border border-blue-600'>{answer.reply}</td>
                </tr>
                )
              })
            }

          </tbody>
        </table>
      </main>

      <footer className="flex justify-between bg-teal-600 py-4 items-center">
        <a href="career" className='m-1'>Careers</a>
      </footer>
    </>
  )
}
export default App