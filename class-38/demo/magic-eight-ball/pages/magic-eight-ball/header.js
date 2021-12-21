const Header = (props)=>{
    const {counter, title} = props;
    return(
        <header className='flex justify-between bg-teal-600 py-4 items-center'>
        <h1 className='text-4xl mx-1'>{title}</h1>
        <p className='m-1'>{counter} questions answered</p>
      </header>
    )
}
export default Header