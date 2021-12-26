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
            props.answersList.map(item =>{
              return (
                <tr>
                  <td className='border border-blue-600'>{item.id}</td>
                  <td className='border border-blue-600'>{item.text}</td>
                  <td className='border border-blue-600'>{item.answer_text}</td>
                </tr>
              )
            })
          }

        </tbody>
      </table>
    )
}

export default QuestionsTable
