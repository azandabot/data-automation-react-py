import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Offcanvas from 'react-bootstrap/Offcanvas';  
import { Link } from 'react-router-dom'
import { useState } from 'react';

function Navigation() {
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  
  return (
    <>
      {[false].map((expand) => (
        <Navbar key={expand} expand={expand} className="bg-dp-header">
          <Container fluid>
            <Link className="text-decoration-none text-body-tertiary" to="/">
              <Navbar.Brand>
              <img src="https://dataprophet.com/wp-content/uploads/2023/06/DataProphet-Logo-R-white.png" alt="DataProphet" id="logo" height="50px" />
              </Navbar.Brand>
            </Link>
            <button className='bg-transparent fs-4 border-0'><i className="bi bi-list text-lime bg-transparent" aria-controls={`offcanvasNavbar-expand-${expand}`} onClick={handleShow}/></button>

            <Navbar.Offcanvas show={show} onHide={handleClose}
                className="bg-dp-header text-white"
                id={`offcanvasNavbar-expand-${expand}`}
                aria-labelledby={`offcanvasNavbarLabel-expand-${expand}`}
                placement="end"
            >
                <Offcanvas.Header closeButton>
                <Offcanvas.Title id={`offcanvasNavbarLabel-expand-${expand}`}>
                    Timeseries
                </Offcanvas.Title>
                </Offcanvas.Header>
                <Offcanvas.Body>
                    <Nav className="justify-content-end flex-grow-1 pe-3">
                        <Link className="text-light text-decoration-none p-2" onClick={handleClose} to="/">
                            <i className='bi bi-grid-1x2-fill me-2 fs-6' />
                            Dashboard
                        </Link>
                        
                        <Link className="text-light text-decoration-none p-2" onClick={handleClose} to="/devices">
                            <i className='bi bi-hdd-rack-fill me-2 fs-6' />
                            Devices
                        </Link>

                        <Link className="text-light text-decoration-none p-2" onClick={handleClose} to="/parameters">
                            <i className='bi bi-braces-asterisk me-2 fs-6' />
                            Parameters
                        </Link>
                    </Nav>                
                </Offcanvas.Body>
            </Navbar.Offcanvas>
          </Container>
        </Navbar>
      ))}
    </>
  );
}

export default Navigation;