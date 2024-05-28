import { Routes, Route } from 'react-router-dom';
import Layout from './components/Layout/Layout';
import Dashboard from './pages/Dashboard';
import Devices from './pages/Devices';
import Parameters from './pages/Parameters';

export default function App(){
  return (
    <>
      
        <Routes >
          <Route path="/" element={<Layout />}>
            <Route index element={<Dashboard/>} />
            <Route path="devices" element={<Devices/>} />
            <Route path="parameters" element={<Parameters/>} />
          </Route>
          
        </Routes>

    </>
  );
}

