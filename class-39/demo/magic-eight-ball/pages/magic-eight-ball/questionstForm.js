import React from 'react'

const QuestionsForm = (props) => {
    const {formHandler} = props
    return (
        <form className='flex w-1/2 bg-gray-200 mx-auto my-5 p-2' onSubmit={formHandler}>
            <input name='question' className='flex-auto p-2' placeholder='ask a question...' />
            <button className='px-4 py-1 mx-2  bg-gray-500 rounded-full'>Ok</button>
        </form>
    )
}

export default QuestionsForm
