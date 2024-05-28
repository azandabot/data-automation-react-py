
import {Outlet} from 'react-router-dom'
import Navigation from "./Navigation";
import Footer from "./Footer";

export default function Layout(){
    return (
        <div >
            <Navigation />
            <main >
                <div className='p-5 py-3 et_pb_fullwidth_header et_pb_fullwidth_header_0'>
                    <Outlet />
                </div>
            </main>
            {/* <Footer /> */}
         </div> 
    )
}