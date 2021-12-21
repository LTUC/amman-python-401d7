import React from 'react'

const QuestionsTable= (props)=> {
    return (
        <table className='w-1/2 mx-auto my-4'>
        <thead>
          <th className='border border-blue-600'>No</th>
          <th className='border border-blue-600'>Question</th>
          <th className='border border-blue-600'>Responoses</th>
        </thead>
        <tbody>
          {
            props.answersList.map(answer =>{
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
    )
}

export default QuestionsTable
