import Link from 'next/link';

function Footer() {
    return (
        <footer className="flex justify-between bg-teal-600 py-4 items-center">
            <Link href="components/career">
                <a className='m-4'>Career</a>
            </Link>
        </footer>
    )
}
export default Footer;